from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

yonalish_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Python asoslari')
        ],
        [
            KeyboardButton(text='Telegram bot'),
            KeyboardButton(text='Django')
        ]
    ], resize_keyboard=True
)