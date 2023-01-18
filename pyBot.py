import logging
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)

bot = Bot(token="5989340565:AAGclP_1Fr4IiIXRK7kdnCBoLTnHcks-D9Q")
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def echo(message: types.CallbackQuery):
	photo = open('test.png', 'rb')
	await message.answer_photo(photo, caption="caption")

if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
