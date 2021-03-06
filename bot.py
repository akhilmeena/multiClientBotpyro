import os
import logging
from config import Config
import pyrogram

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

plugins = dict(root="plugins")

app = pyrogram.Client(
  "Multi-ClientBot",
  bot_token=Config.BOT_TOKEN,
  api_id=Config.API_ID,
  api_hash=Config.API_HASH,
  plugins=plugins
  )

app2 = pyrogram.Client(
  "Multi-ClientBot2",
  bot_token=Config.BOT_TOKEN2,
  api_id=Config.API_ID,
  api_hash=Config.API_HASH,
  plugins=plugins
  )

  
if __name__ == "__main__" :
  #loop.run_until_complete(start_services())
  app.start()
  app2.start()
