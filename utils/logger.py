# ╔═════════════════════════════════════════════════╗
# ║           OpenGiftsBuyer for Telegram.          ║
# ║             Developed by: @whicencer            ║
# ║              Not for commercial use             ║
# ╚═════════════════════════════════════════════════╝

import logging

file_handler = logging.FileHandler('bot.log')
console_handler = logging.StreamHandler()

logging.basicConfig(
  level=logging.INFO,
  handlers=[file_handler, console_handler],
  format='%(asctime)s - %(levelname)s - %(message)s'
)

def log(log_message: str):
  logging.info(log_message)