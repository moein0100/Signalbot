from datetime import datetime

def get_current_time():
    return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
