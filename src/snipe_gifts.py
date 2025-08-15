# ╔═════════════════════════════════════════════════╗
# ║           OpenGiftsBuyer for Telegram.          ║
# ║             Developed by: @whicencer            ║
# ║              Not for commercial use             ║
# ╚═════════════════════════════════════════════════╝

import asyncio
import config
from utils import file_manager, notifier, logger, gift_validator
from pyrogram.client import Client
from pyrogram.types import Gift
from src.purchase_collection import purchase_collection

async def start(client: Client):
  logger.log(log_message="🔍 Sniping for new gifts...")
  await client.send_message(config.CHANNEL_ID, "🔍 **New gifts sniping started!**")
  while True:
    latest_gifts = file_manager.load_data()
    current_gifts = await client.get_available_gifts()
    current_serialized = [serialize_gift(gift) for gift in current_gifts]
  
    if latest_gifts is None:
      file_manager.save_data(current_serialized)
      continue
    
    new_gifts = sorted(
      [g for g in current_gifts if g.id not in {lg["id"] for lg in latest_gifts}],
      key=lambda g: g.price,
      reverse=True
    )
    
    if new_gifts:
      logger.log(log_message=f"🔔 New gifts detected: {len(new_gifts)}")
      await client.send_message(
        config.CHANNEL_ID,
        f"🔔 **New gifts detected:** {len(new_gifts)}\n"
      )
      file_manager.save_data(current_serialized)
      
      for gift in new_gifts:
        if gift:
          await notifier.notify_changes(client, config.CHANNEL_ID, gift)
          await purchase_collection(client, gift)
    await asyncio.sleep(config.INTERVAL)


def serialize_gift(gift: Gift) -> dict:
  return {
    "id": gift.id,
    "price": gift.price,
    "require_premium": gift.require_premium,
    "limit_per_user": gift.limited_per_user,
    "per_user_total": gift.per_user_total,
    "total_supply": gift.total_amount,
    "is_limited": gift.is_limited,
    "released_by": f"@{gift.released_by.username}" if gift.released_by else None
  }
