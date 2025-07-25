def calculate_tp_sl(data):
    entry = data.get("entry_price", 100)
    tp = entry * 1.03
    sl = entry * 0.97
    return tp, sl
