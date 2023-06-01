from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from buttons import ADD_MUSIC_BUTTON, ADD_AUTHOR_BUTTON, ADD_GENRE_BUTTON, AUTHORS_LIST_BUTTON, DELETE_AUTHOR_BUTTON, \
    GENRES_LIST_BUTTON, SEARCH_MUSIC_BUTTON

admin_commands_list_keyboard = ReplyKeyboardMarkup([
    [ADD_MUSIC_BUTTON, ADD_AUTHOR_BUTTON],
    [ADD_GENRE_BUTTON, AUTHORS_LIST_BUTTON],
    [DELETE_AUTHOR_BUTTON, GENRES_LIST_BUTTON],
    [SEARCH_MUSIC_BUTTON]
], resize_keyboard=True)


moderator_commands_list_keyboard = ReplyKeyboardMarkup([
    [ADD_MUSIC_BUTTON, ADD_AUTHOR_BUTTON],
    [ADD_GENRE_BUTTON, AUTHORS_LIST_BUTTON],
    [DELETE_AUTHOR_BUTTON, GENRES_LIST_BUTTON],
    [SEARCH_MUSIC_BUTTON]
], resize_keyboard=True)


users_keyboard = ReplyKeyboardMarkup([
    [SEARCH_MUSIC_BUTTON],
])
