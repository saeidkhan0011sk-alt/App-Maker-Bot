import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# নিচের কোডটিতে আপনার টেলিগ্রাম বটের এপিআই টোকেন বসাবেন
TOKEN = "8925561070:AAFJmkim5kA6N_h9HVsxk06JaI4sau7T2Es"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("স্বাগতম! এটি আপনার ক্রিয়েট করা অ্যাপ মেকার বট। খুব শীঘ্রই এখানে অ্যাপ তৈরির ফিচার যুক্ত করা হবে।")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
