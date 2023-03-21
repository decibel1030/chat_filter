import conf
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import filters
import time
from main import Controller

class MyBot:
    def __init__(self, token):
        bot = Bot(token)
        dp = Dispatcher(bot)
        cont = Controller()
        @dp.message_handler(commands=["start"])
        async def start(msg: types.Message):
            text = "<b>Бот созданный для того чтобы люди в чате не грешили как минимум своими пальцами</b>"
            await msg.reply(
                text=text,
                parse_mode="HTML")
            bot_msg = await bot.send_photo(chat_id=msg.chat.id, photo="https://i.pinimg.com/564x/05/a1/64/05a1643b14d1d176bc64df19a2851753.jpg")
            time.sleep(4)
            await bot.delete_message(message_id=bot_msg.message_id, chat_id=msg.chat.id)

        @dp.message_handler(commands="stop")
        async def stop(msg: types.Message):
            if msg.from_user.id == "5434606232":
                await msg.reply("Ты не тот кто мне нужен.")
            else:
                await msg.answer("Хорошо хозяюшка")

        @dp.message_handler(commands="target")
        async def save_word(message: types.Message):
            if message.reply_to_message is not None:
                bad_word = message.reply_to_message.text
                cont.push_word(bad_word.lower())
                text = f"""
                Слово <b>{bad_word}</b> под запретом
                """
                await message.answer(
                    text=text,
                    parse_mode="HTML")

        @dp.message_handler()
        async def check_word(message: types.Message):
            if cont.check_word(message.text.lower()):
                await message.reply("За базаром следи чепушила")

        executor.start_polling(dp)


if __name__ == '__main__':
    MyBot(token=conf.token)

