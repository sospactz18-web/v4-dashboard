from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "V4 Engine API is running live!"})

@app.route('/api/data', methods=['GET'])
def get_data():
    # Hapa V4 Algorithm yako inatoa Signal iliyo na usahihi mkubwa
    return jsonify({
        "pair": "EUR/USD OTC",
        "direction": "BUY",          # BUY, SELL, au WAIT
        "timeframe": "M1 (1 MIN)",
        "accuracy": "95%",
        "quality": "STRONG V4",
        "action": "ENTER NOW",
        "time": datetime.now().strftime("%H:%M:%S")
    })

if __name__ == '__main__':
    app.run()
