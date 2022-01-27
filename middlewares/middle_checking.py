from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from data.config import kanallar
from utils.misc import checkk
from loader import bot




class Asosiy_checking(BaseMiddleware):
    async def on_pre_process_update(self,xabar:types.Update,data:dict):
        if xabar.message:
            user_id = xabar.message.from_user.id
        elif xabar.callback_query:
            user_id = xabar.callback_query.from_user.id
        else:
            return
        matn = 'Quyidagi kanalga azo boling\n'

        holati = True
        for kanal in kanallar:
            daslabki_holati = await checkk.tekshirish(user_id=user_id,kanal=kanal)
            holati*=daslabki_holati

            kanal = await bot.get_chat(kanal)
            if not daslabki_holati:
                link = await kanal.export_invite_link()
                matn+=(f"👉 <a href='{link}'>{kanal.title}</a>\n")
        if not holati:
            await xabar.message.answer(matn,disable_web_page_preview=True)
            raise CancelHandler()