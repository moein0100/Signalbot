def calculate_tp_sl(signal):
    if signal["action"] == "Buy":
        return 1.5, 0.5  # TP = 1.5%, SL = 0.5%
    elif signal["action"] == "Sell":
        return 0.5, 1.5  # TP = 0.5%, SL = 1.5%
