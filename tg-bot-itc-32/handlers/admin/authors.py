import datetime

from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from commands import COMMANDS
from config import Session
from filters import IsAdmin
from formats import HUMAN_READABLE_DATE_FORMAT, DATE_FORMAT
from loader import dp
from models import Author
from state import CreateAuthorState, DeleteAuthorState


@dp.message_handler(IsAdmin(), text=COMMANDS["add_author"])
async def add_author(message: Message):
    await message.answer("Отлично! Отправь имя автора")
    await CreateAuthorState.full_name.set()


@dp.message_handler(IsAdmin(), state=CreateAuthorState.full_name)
async def author_full_name(message: Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await CreateAuthorState.birth_date.set()
    # await CreateAuthorState.next()
    await message.answer(f"Отправь дата рождения автора в формате: {HUMAN_READABLE_DATE_FORMAT}")


@dp.message_handler(IsAdmin(), state=CreateAuthorState.birth_date)
async def author_b_date(message: Message, state: FSMContext):
    try:
        date_ = datetime.datetime.strptime(message.text, DATE_FORMAT).date()
        async with state.proxy() as data:
            full_name = data["full_name"]
        await state.finish()
        with Session() as session:
            author = Author(full_name=full_name, birth_date=date_)
            session.add(author)
            session.commit()
        await message.answer("Успешно создал автора!")
    except ValueError:
        await message.answer(f"Неверный формат даты! Формат должен быть: {HUMAN_READABLE_DATE_FORMAT}")


@dp.message_handler(IsAdmin(), text=COMMANDS["authors_list"])
async def authors_list(message: Message):
    with Session() as session:
        authors = session.query(Author).all()
    if not authors:
        await message.answer("Авторов нет!")
        return
    await message.answer("\n\n".join(map(
        lambda model: f"🆔: {model.id}\n👤: {model.full_name}\n📅: {model.birth_date}",
        authors
    )))


@dp.message_handler(IsAdmin(), text=COMMANDS["delete_author"])
async def delete_author(message: Message):
    with Session() as session:
        authors = session.query(Author).all()
    if not authors:
        await message.answer("Авторов нет!")
        return
    keyboard = InlineKeyboardMarkup()
    for author in authors:
        keyboard.add(InlineKeyboardButton(
            author.full_name,
            callback_data=author.id
        ))
    await DeleteAuthorState.callback_query.set()
    await message.answer("Ща будет прикольно", reply_markup=keyboard)


@dp.callback_query_handler(state=DeleteAuthorState.callback_query)
async def delete_author_callback(callback: CallbackQuery):
    with Session() as session:
        author = session.query(Author).filter(Author.id == int(callback.data)).first()
        session.delete(author)
        session.commit()
    await callback.bot.send_message(
        callback.from_user.id,
        "Успешно удалил!"
    )
    await callback.bot.delete_message(
        callback.from_user.id,
        callback.message.message_id
    )
