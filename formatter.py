def format_signal(signal_data):
    return (
        f"✅ New Trading Signal\n"
        f"📌 Action: {signal_data['action']}\n"
        f"🧠 Structure: {signal_data['structure']}\n"
        f"🎯 Take Profit: {signal_data['tp']}%\n"
        f"🛑 Stop Loss: {signal_data['sl']}%"
    )
