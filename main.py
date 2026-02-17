from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import Message
import keeboards
from work_db import  show_all
import config
# import buttons
# from costom_filters import button_filter
bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name=""
)

@bot.on_message(filters=filters.command("start"))
async def start(client: Client, message: Message):
    await message.reply(f'Привет, {message.from_user.first_name}')


@bot.on_message(filters=filters.command("input"))
async def start(client: Client, message: Message):
    await message.reply(f"статистика - ")


if __name__ == '__main__':
    bot.run()

