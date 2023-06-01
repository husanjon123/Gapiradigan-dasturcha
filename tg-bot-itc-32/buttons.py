from aiogram.types import KeyboardButton

from commands import COMMANDS

ADD_MUSIC_BUTTON = KeyboardButton(COMMANDS["add_music"])
ADD_AUTHOR_BUTTON = KeyboardButton(COMMANDS["add_author"])
ADD_GENRE_BUTTON = KeyboardButton(COMMANDS["add_genre"])
AUTHORS_LIST_BUTTON = KeyboardButton(COMMANDS["authors_list"])
DELETE_AUTHOR_BUTTON = KeyboardButton(COMMANDS["delete_author"])
GENRES_LIST_BUTTON = KeyboardButton(COMMANDS["genres_list"])
SEARCH_MUSIC_BUTTON = KeyboardButton(COMMANDS["search_music"])
