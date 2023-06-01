from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from commands import COMMANDS
from config import Session
from filters import IsAdmin
from loader import dp
from models import Genre
from state import CreateGenreState


@dp.message_handler(Text(COMMANDS["add_genre"]), IsAdmin())
async def add_genre(message: Message):
    await message.answer("Круто! Отправь мне название жанра")
    await CreateGenreState.name.set()


@dp.message_handler(IsAdmin(), state=CreateGenreState.name)
async def add_genre(message: Message, state: FSMContext):
    await state.finish()
    with Session() as session:
        genre = session.query(Genre).filter(Genre.name == message.text).first()
        if genre:
            await message.answer("Такой жанр уже существует!")
            return
        genre = Genre(name=message.text)
        session.add(genre)
        session.commit()
    await message.answer("Отлично! Успешно создал жанр!")


@dp.message_handler(IsAdmin(), text=COMMANDS["genres_list"])
async def genres_list(message: Message):
    with Session() as session:
        genres = session.query(Genre).all()
    if not genres:
        await message.answer("Жанров нет!")
        return
    await message.answer("\n\n".join(map(
        lambda model: f"🆔: {model.id}\n💾: {model.name}\n",
        genres
    )))
