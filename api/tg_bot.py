from aiogram import Bot, Dispatcher, types
import asyncio


TOKEN = '5678145201:AAE-Imh05lTw89pcT9WK9TAAH3pJDr9yUj8'


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def send_message_to_bot(chat_id, text):
    await bot.send_message(chat_id, text)

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


# print("============================ ok ko ko k ok ok o ko ko ko k ===========================")
