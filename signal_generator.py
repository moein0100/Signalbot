from market_structure import analyze_market
from risk_manager import calculate_tp_sl
from trend_analyzer import is_trend_valid

def generate_signal():
    structure = analyze_market()
    if structure["action"] and is_trend_valid():
        tp, sl = calculate_tp_sl(structure)
        return {
            "action": structure["action"],
            "structure": structure["structure"],
            "tp": tp,
            "sl": sl
        }
    return None
