from core.market_structure import analyze_market
from core.risk_manager import calculate_tp_sl

def generate_signal():
    market_data = analyze_market()
    tp, sl = calculate_tp_sl(market_data)
    return {"signal": market_data["action"], "TP": tp, "SL": sl}
