from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Muhimu sana kuzuia Error kwenye Telegram

@app.route('/')
def home():
    return jsonify({"status": "V4 Engine API is running live!"})

# Weka au rekebisha endpoint hii:
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify({
        "pair": "EUR/USD OTC",
        "direction": "BUY"  # au "SELL" / "WAIT"
    })

if __name__ == '__main__':
    app.run()
