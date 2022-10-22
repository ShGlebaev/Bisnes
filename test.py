from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import main as m

dp = Dispatcher(m)


@dp.message_handler()
async def bot_message(message: types.Message):
        if message.text == "Проката автомобилей":
            await message.reply("1.Высокая температура.")