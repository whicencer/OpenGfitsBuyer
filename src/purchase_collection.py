# ╔═════════════════════════════════════════════════╗
# ║           OpenGiftsBuyer for Telegram.          ║
# ║             Developed by: @whicencer            ║
# ║              Not for commercial use             ║
# ╚═════════════════════════════════════════════════╝

import config
from pyrogram.client import Client
from pyrogram.types import Gift
from utils.gift_validator import validate_gift
from utils.purchase_gift import purchase_gift
from utils import logger

async def purchase_collection(client: Client, gift: Gift):
  gift_valid = validate_gift(gift)
  if gift_valid:
    try:
      await client.send_message(
        chat_id=config.CHANNEL_ID,
        text=f"🎁 Gift fits to the user's requirements.\nPurchasing gift `[{gift.id}]` {config.NUM_GIFTS} times..."
      )
      
      for _ in range(config.NUM_GIFTS):
        gift_purchased = await purchase_gift(client, gift_id=gift.id)
        if not gift_purchased: break
    except Exception as e:
      await client.send_message(
        chat_id=config.CHANNEL_ID,
        text=f"❌ Failed to purchase gifts: {str(e)}"
      )
      logger.log(f"❌ Failed to purchase gifts: {e}")
  else:
    await client.send_message(
      chat_id=config.CHANNEL_ID,
      text=f"❌ Gift `[{gift.id}]` does not fit to the user's requirements."
    )