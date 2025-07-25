import requests
from config import TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from formatter import format_signal

def send_signal(signal_data):
    message = format_signal(signal_data)
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)
