# ╔═════════════════════════════════════════════════╗
# ║           OpenGiftsBuyer for Telegram.          ║
# ║             Developed by: @whicencer            ║
# ║              Not for commercial use             ║
# ╚═════════════════════════════════════════════════╝

import config
from pyrogram.types import Gift

def validate_gift(gift: Gift):
  if not isinstance(gift, Gift):
    return False
  
  if not gift.is_limited:
    return False
  
  if not config.MIN_GIFT_PRICE <= gift.price <= config.MAX_GIFT_PRICE:
    return False
  
  if not config.MIN_GIFT_SUPPLY <= gift.total_amount <= config.MAX_GIFT_SUPPLY:
    return False
  
  if config.ONLY_PREMIUM and not gift.require_premium:
    return False

  if not config.BUY_RELEASED and gift.released_by is not None:
    return False
  
  return True