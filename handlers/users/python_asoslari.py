from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from keyboards.default.darsliklar import darslar_button
from keyboards.inline.inline_buttons import inline_tugmalar
from loader import dp

@dp.message_handler(text='Python asoslari')
async def bot_darslar(dars: types.Message):
    await dars.answer(text='Python asoslari darsliklari', reply_markup=inline_tugmalar)