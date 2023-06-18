from aiogram import Bot, Dispatcher, types
import asyncio
import logging

TOKEN = '6233717340:AAFU_2wbRrP-2frjSR2t6c_gD90y5rSvScY'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_message_to_bot(chat_id, text):
    await bot.send_message(chat_id, text)

@dp.message_handler(commands='star')
async def add_to_db(message: types.Message):
    await bot.send_message(message.chat.id, 'Сейчас добавлю')
    await bot.send_message(message.chat.id, message.text)
 

async def main():
    # dp.run_until_disconnected()
    with open('api/data.txt', 'r') as file:
        data = str(file.read().strip())
  
    chat_id = 973108256  # O'zingizning chat ID raqamingizni qo'ying
   
    await send_message_to_bot(chat_id, data)
    await bot.close()

def run_bot():
    # main()    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    dp.run_polling()
# print("============================ ok ko ko k ok ok o ko ko ko k ===========================")
