# ╔═════════════════════════════════════════════════╗
# ║           OpenGiftsBuyer for Telegram.          ║
# ║             Developed by: @whicencer            ║
# ║              Not for commercial use             ║
# ╚═════════════════════════════════════════════════╝

import json

def save_data(data, filename="data/gifts.json"): 
  with open(filename, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

def load_data(filename="data/gifts.json"):
  try:
    with open(filename, "r", encoding="utf-8") as f:
      return json.load(f)
  except FileNotFoundError:
    return None