# ╔═════════════════════════════════════════════════╗
# ║           OpenGiftsBuyer for Telegram.          ║
# ║             Developed by: @whicencer            ║
# ║              Not for commercial use             ║
# ╚═════════════════════════════════════════════════╝

import asyncio
import config
from pyrogram import types, filters
from pyrogram.client import Client
from utils import logger
from src import snipe_gifts
from textwrap import dedent
import os

is_test_env = os.getenv("TEST_ENV").lower() == "true"
app = Client(
  "my_account_test" if is_test_env else "my_account",
  api_id=config.API_ID,
  api_hash=config.API_HASH,
  test_mode=is_test_env
)

@app.on_message(filters.private)
async def status_message(client: Client, message: types.Message):
  if (message.text == "/status"):
    await message.reply("**Status**: 🟢 Online")

async def main():
  await app.start()
  logger.log(log_message="✅ User bot started successfully!")
  star_balance = await app.get_stars_balance()
  account_me = await app.get_me()
  await app.send_message(
    config.CHANNEL_ID,
    dedent(f"""\
    ✅ **User bot started!**\n
    
    🆔 **Authorized account ID**: `[{account_me.id}]`
    ⭐ **Account balance**: {star_balance} stars
    
    Developer: @whicencer
    GitHub: https://github.com/whicencer/OpenGiftsBuyer
    """),
    link_preview_options=types.LinkPreviewOptions(is_disabled=True)
  )
  await snipe_gifts.start(client=app)
  await app.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())