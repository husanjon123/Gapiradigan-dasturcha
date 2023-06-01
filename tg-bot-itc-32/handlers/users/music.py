from aiogram.dispatcher import FSMContext
from aiogram.types import Message, InputFile

from commands import COMMANDS
from config import Session
from loader import dp
from models import Music
from state import SearchMusicState


@dp.message_handler(text=COMMANDS["search_music"])
async def search_music(message: Message):
    await SearchMusicState.search.set()
    await message.answer("Отлично! Отправьте имя трека")


@dp.message_handler(state=SearchMusicState.search)
async def search_result(message: Message, state: FSMContext):
    await state.finish()
    with Session() as session:
        musics = session.query(Music).filter(Music.name.contains(message.text)).all()
    for music in musics:
        await message.bot.send_audio(
            message.from_user.id,
            audio=InputFile(music.mp3_file_path),
            caption=f"Автор: {music.author}\nЖанр: {music.genre}\n"
                    f"Длительность: {music.duration}"
        )
