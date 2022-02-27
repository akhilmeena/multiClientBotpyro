# (c) HeimanPictures
import logging
import os
import pyrogram
from config import Config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


START = """
Hi {}!

This Is Multi-Client"""

@Client.on_message(filters.command('start') & filters.private)
async def start(bot, message):
  await message.reply_chat_action("typing")
  await message.reply_text(
    text=START.format(message.from_user.mention),
    disable_web_page_preview=True,
    )

