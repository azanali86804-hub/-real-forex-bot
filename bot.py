from flask import Flask
import threading
import os

# --- Ye Web Server Render ko khush rakhne ke liye hai ---
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is LIVE - Forex Bot Running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

# --- Tumhara Asal Bot ka Code Yahan Se Shuru Hoga ---
# Neeche apna purana bot ka code paste karo
# Agar tumhara purana code is tarah hai to waisa hi rehne do

# Example ke liye me tumhara purana code yahan import kar raha hun
# Tum bas iske neeche apna pura purana code copy kar dena

# --- BOT START ---
import time
# Yahan se tumhara original bot.py ka code shuru karo...
# [TUMHARA PURANA CODE YAHAN PASTE KARO]

# Agar tumhare bot me last me bot.infinity_polling() ya app.run() jaisa kuch hai to wo sab se neeche hona chahiye

# --- END ---

if __name__ == "__main__":
    # Web server alag thread me chalao
    threading.Thread(target=run_web, daemon=True).start()
    
    # Yahan apne bot ko start karne wala function call karo
    # Jaise: main() ya bot.polling()
    print("Bot starting...")
    # TUMHARA BOT START CODE YAHAN LIKHO
    # For example agar tumhare pas bot.polling() hai to:
    # bot.infinity_polling()
