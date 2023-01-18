import subprocess
import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)

bot = Bot(token="5989340565:AAGclP_1Fr4IiIXRK7kdnCBoLTnHcks-D9Q")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def echo(message: types.CallbackQuery):
	ret = subprocess.call("python3 raspoznavalka.py", shell=True)
	if ret == 0:
		photo = open('test.png', 'rb')
		await message.answer_photo(photo, caption="caption")
	else: 
		await message.answer("Ошибка модуля распознавания объектов")
		
if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
