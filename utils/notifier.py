# ╔═════════════════════════════════════════════════╗
# ║           OpenGiftsBuyer for Telegram.          ║
# ║             Developed by: @whicencer            ║
# ║              Not for commercial use             ║
# ╚═════════════════════════════════════════════════╝

import os
from pyrogram.client import Client
from pyrogram.types import Gift

async def notify_changes(client: Client, chat_id, new_gift: Gift):
  sticker_filename = f"Sticker_{new_gift.id}.tgs"
  await client.download_media(new_gift.sticker.file_id, file_name=sticker_filename)
  
  file_path = os.path.abspath(f"downloads/{sticker_filename}")
  sticker_message = await client.send_document(
    chat_id=chat_id,
    document=file_path,
  )
  
  if (sticker_message is not None):
    await sticker_message.reply_text(
      text=f"🆕 **New gift available! `[{new_gift.id}]`**\n\nPrice: ⭐️ **{new_gift.price}**\nQuantity: **{new_gift.total_amount}**\n{f"Relased by: **@{new_gift.released_by.username}**" if new_gift.released_by is not None else ""}",
      quote=True
    )
  
  os.remove(file_path)