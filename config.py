# ╔═════════════════════════════════════════════════╗
# ║           OpenGiftsBuyer for Telegram.          ║
# ║             Developed by: @whicencer            ║
# ║              Not for commercial use             ║
# ╚═════════════════════════════════════════════════╝

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

API_ID: int = int(os.getenv("API_ID"))
API_HASH: str = os.getenv("API_HASH")

INTERVAL: int = int(os.getenv("INTERVAL"))
CHANNEL_ID: int = int(os.getenv("CHANNEL_ID"))

MIN_GIFT_PRICE: int = int(os.getenv("MIN_GIFT_PRICE"))
MAX_GIFT_PRICE: int = int(os.getenv("MAX_GIFT_PRICE"))
NUM_GIFTS: int = int(os.getenv("NUM_GIFTS"))
ONLY_PREMIUM: bool = os.getenv("ONLY_PREMIUM").lower() == "true"
BUY_RELEASED: bool = os.getenv("BUY_RELEASED").lower() == "true"
MIN_GIFT_SUPPLY: int = int(os.getenv("MIN_GIFT_SUPPLY"))
MAX_GIFT_SUPPLY: int = int(os.getenv("MAX_GIFT_SUPPLY"))

RECEIVER_ID: int = int(os.getenv("RECEIVER_ID"))
HIDE_SENDER_NAME: bool = os.getenv("HIDE_SENDER_NAME").lower() == "true"