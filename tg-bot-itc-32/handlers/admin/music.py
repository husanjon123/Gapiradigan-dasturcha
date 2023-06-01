import asyncio
import os

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, ContentType, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import Session, MUSICS_DIR
from formats import HUMAN_READABLE_DURATION_FORMAT, validate_duration
from loader import dp
from commands import COMMANDS
from filters import IsAdmin
from models import Genre, Author, Music
from state import CreateMusicState


@dp.message_handler(Text(COMMANDS["add_music"]), IsAdmin())
async def add_music(message: Message):
    await message.reply("Отлично! Отправь название музыки")
    await CreateMusicState.name.set()


@dp.message_handler(IsAdmin(), state=CreateMusicState.name)
async def music_genre(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    # await state.set_data({"music_name": message.text})
    keyboard = InlineKeyboardMarkup()
    with Session() as session:
        genres = session.query(Genre).all()
    if not genres:
        await message.answer("Жанров нет!")
        await state.finish()
        return
    for genre in genres:
        keyboard.add(InlineKeyboardButton(genre.name, callback_data=genre.id))
    await CreateMusicState.genre.set()
    await message.reply("Отлично! Выбери жанр музыки", reply_markup=keyboard)


@dp.callback_query_handler(state=CreateMusicState.genre)
async def music_duration(callback: CallbackQuery, state: FSMContext):
    await state.update_data(genre=int(callback.data))
    await CreateMusicState.duration.set()
    await callback.bot.delete_message(
        callback.from_user.id,
        callback.message.message_id
    )
    await callback.bot.send_message(
        callback.from_user.id,
        f"Отлично! Отправь мне длительность музыки в формате "
        f"{HUMAN_READABLE_DURATION_FORMAT}"
    )


@dp.message_handler(IsAdmin(), state=CreateMusicState.duration)
async def music_author(message: Message, state: FSMContext):
    if not validate_duration(message.text):
        await message.answer("Неправильный формат! Попробуйте ещё раз!")
        return
    await state.update_data(duration=message.text)
    keyboard = InlineKeyboardMarkup()
    await CreateMusicState.author.set()
    with Session() as session:
        authors = session.query(Author).all()
    if not authors:
        await message.answer("Авторов нет!")
        return
    for author in authors:
        keyboard.add(InlineKeyboardButton(author.full_name, callback_data=author.id))
    await message.answer("Выберите автора трека", reply_markup=keyboard)


@dp.callback_query_handler(state=CreateMusicState.author)
async def music_raw(callback: CallbackQuery, state: FSMContext):
    await state.update_data(author=int(callback.data))
    await CreateMusicState.music_raw.set()
    await callback.bot.delete_message(
        callback.from_user.id,
        callback.message.message_id
    )
    await callback.bot.send_message(
        callback.from_user.id,
        "Отлично! Отправьте сам трек"
    )


@dp.message_handler(IsAdmin(), state=CreateMusicState.music_raw, content_types=[ContentType.AUDIO])
async def get_music(message: Message, state: FSMContext):
    file_path = await asyncio.wait_for(message.bot.download_file_by_id(
        message.audio.file_id, destination_dir=MUSICS_DIR
    ), None)
    filename = file_path.name
    file_path.close()
    async with state.proxy() as data:
        music_data = data.as_dict()
    music_raw_name = f'{MUSICS_DIR}/{music_data["name"]}_' \
                     f'{music_data["author"]}.{filename.split(".")[-1]}'
    os.rename(
        filename,
        music_raw_name
    )
    music_data["mp3_file_path"] = music_raw_name
    with Session() as session:
        session.add(Music(**music_data))
        session.commit()
    await state.finish()
    await message.answer("Успешно создал!")
