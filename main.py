from telegram_bot import send_signal
from signal_generator import generate_signal
from logger import log

if __name__ == "__main__":
    signal = generate_signal()
    if signal:
        send_signal(signal)
        log(f"Signal sent: {signal}")
    else:
        log("No signal generated.")
