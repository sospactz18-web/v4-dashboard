import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"status": "V4 Engine API is running live!"})

@app.route('/api/latest-signal', methods=['GET'])
def get_signal():
    signal_data = {
        "pair": "EUR/USD OTC",
        "direction": "BUY",
        "timeframe": "5M",
        "confidence": 88,
        "action": "EXECUTE BUY NOW",
        "reason": "V4 Engine Signal Verified"
    }
    return jsonify(signal_data)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
