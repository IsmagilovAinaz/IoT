import subprocess
import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)

bot = Bot(token="Your token")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def echo(message: types.CallbackQuery):
	ret = subprocess.call("python3 raspoznavalka.py", shell=True)
	if ret == 0:
		answertext = ""
		with open("listOfObjects.txt", "r") as listfile:
			for line in listfile:
				answertext = answertext + line
		photo = open('test.png', 'rb')
		await message.answer_photo(photo, caption=answertext)
	else: 
		await message.answer("Ошибка модуля распознавания объектов")
		
if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
