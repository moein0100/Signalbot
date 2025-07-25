import telegram
from config import TELEGRAM_TOKEN, CHAT_ID

def send_signal(signal_data):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    message = f"Signal: {signal_data['signal']}\nTP: {signal_data['TP']}\nSL: {signal_data['SL']}"
    bot.send_message(chat_id=CHAT_ID, text=message)
