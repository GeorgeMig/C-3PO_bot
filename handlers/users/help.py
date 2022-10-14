from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Сэр, это список моих команд: ",
            "/start - запускает меня",
            "/help - предоставляет информацию о моих командах",
            "/audio - скачивает аудио из вашего любимого видео на Youtube")

    await message.answer("\n".join(text))