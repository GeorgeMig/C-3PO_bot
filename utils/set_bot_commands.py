from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить меня"),
            types.BotCommand("help", "Справка обо мне"),
            types.BotCommand("audio", "Получить аудио из вашего любимого видео")
        ]
    )
