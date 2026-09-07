import yfinance as yf
import time
import sys
from datetime import datetime

def get_signal(symbol="EURUSD=X"):
    try:
        data = yf.download(symbol, period="1d", interval="1m", progress=False)
        if len(data) < 2:
            return "WAIT"
        
        last = data.iloc[-1]
        prev = data.iloc[-2]

        # Real logic
        if last['Close'] > last['Open']:
            return "CALL 🔼"
        else:
            return "PUT 🔽"
    except:
        return "WAIT"

def start_bot():
    symbol = "EURUSD=X"
    print(f"BOT STARTED: {symbol}")
    print("Candle close ka wait kar raha hun...")
    
    while True:
        now = datetime.now()
        sec_left = 60 - now.second

        if sec_left <= 5 and sec_left >= 1:
            sys.stdout.write(f"\r⏳ {sec_left}   ")
            sys.stdout.flush()
            time.sleep(1)

            if sec_left == 1:
                sig = get_signal(symbol)
                entry_time = now.strftime("%H:%M:%S")
                sys.stdout.write(f"\r✅ SIGNAL: {sig} | TIME: {entry_time} | NEXT CANDLE      \n")
                time.sleep(1.5)
        
        time.sleep(0.1)

if __name__ == "__main__":
    start_bot()
