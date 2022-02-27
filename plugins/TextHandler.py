import os
import requests
import logging
from config import Config
import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


@Client.on_message(filters.regex('http') & filters.private)
async def remote_upload(bot, message):
  await message.reply_chat_action("typing")
  link = message.text
  await message.reply_text("This is a link{}".format(link))
