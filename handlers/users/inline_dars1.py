from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from keyboards.default.darsliklar import darslar_button
from keyboards.default.yonalishlar import yonalish_button

from loader import dp

@dp.callback_query_handler(text ='dars1')
async def darslar(sorov :CallbackQuery):
    await sorov.message.answer(text='dars1 ga hush kelibsiz',reply_markup=darslar_button)
