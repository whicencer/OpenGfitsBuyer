# ╔═════════════════════════════════════════════════╗
# ║           OpenGiftsBuyer for Telegram.          ║
# ║             Developed by: @whicencer            ║
# ║              Not for commercial use             ║
# ╚═════════════════════════════════════════════════╝

import config
from pyrogram.client import Client
from pyrogram.types import Gift
from utils import logger
from pyrogram.errors import NotAcceptable, BadRequest

async def purchase_gift(client: Client, gift_id: int) -> bool:
  """
  Purchasing the gift to the user by ID.
  
  Args:
    client (Client): The Pyrogram client instance.
    gift_id (int): The gift_id number.
  
  Returns:
    bool: True if the gift is purchased, False otherwise.
  """
  try:
    await client.send_gift(
      chat_id=config.RECEIVER_ID,
      gift_id=gift_id,
      is_private=config.HIDE_SENDER_NAME
    )
    
    logger.log(log_message=f"✅ Gift `[{gift_id}]` sent successfully!")
    await client.send_message(
      chat_id=config.CHANNEL_ID,
      text=f"✅ Gift `[{gift_id}]` purchased successfully!"
    )
    
    return True
  except NotAcceptable or BadRequest as e:
    if e.ID == "STARGIFT_USAGE_LIMITED":
      await client.send_message(config.CHANNEL_ID, f"❌ Failed to purchase: Gift is sold out")
    elif e.ID == "BALANCE_TOO_LOW":
      await client.send_message(config.CHANNEL_ID, f"❌ Failed to purchase: Insufficient balance")
    else:
      await client.send_message(
        chat_id=config.CHANNEL_ID,
        text=f"❌ Failed to purchase gift `[{gift_id}]`: {str(e)}"
      )
  return False