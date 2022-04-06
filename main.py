import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5265838947:AAHb8UVGVHcU6dx4B-sOTm_rp57s4MwcdyE'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Botiga Xush Kelibsiz!\nIltimos shu tartibda ro`yxatdan o`ting:\nIsm: name\nFamilya: surname\nTel: number")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)