# Signalbotfrom core.signal_generator import generate_signal
from services.telegram_bot import send_signal

if __name__ == "__main__":
    signal = generate_signal()
    send_signal(signal)
