import time
import logging

from aiogram import Bot, Dispatcher, executor, types

TOKEN = "5860437716:AAEqNEuYAGYpoboTO-dhfZNeJqz_wgBQU1E"
MSG = "Программировал ли ты сегодня, {}?"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handlef(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.INFO(f'{user_id=} {user_full_name=} {time.asctime()}')

    await message.re(f"Привет детка, {user_full_name}!")

    for i in range(10):
        time.sleep(2)

        await bot.send_message(user_id,  MSG.format(user_name))


if __name___ == "__main__":
    executor.start_polling(dr)


