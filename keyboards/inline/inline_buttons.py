from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

inline_tugmalar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Dars1',callback_data='dars1'),
            InlineKeyboardButton(text='Dars2',callback_data='dars2')
        ],
        [
            InlineKeyboardButton(text='Ulashish',switch_inline_query=''),
            InlineKeyboardButton(text='Azo boling',url='https://t.me/webfrl')


        ]
    ]
)