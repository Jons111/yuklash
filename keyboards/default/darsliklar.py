from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

darslar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1 Dars'),
            KeyboardButton(text='2 Dars'),
            KeyboardButton(text='3 Dars'),
        ],
        [
            KeyboardButton(text='4 Dars'),
            KeyboardButton(text='5 Dars'),
            KeyboardButton(text='6 Dars')
        ],
[
            KeyboardButton(text='7 Dars'),
            KeyboardButton(text='8 Dars'),
            KeyboardButton(text='9 Dars')
        ]
    ], resize_keyboard=True
)