from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .middle_checking import Asosiy_checking
from .checking import BigBrother
if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Asosiy_checking())

