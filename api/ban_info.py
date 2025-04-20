import json
import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/ban_info", methods=["GET"])
def ban_info():
    uid = request.args.get("uid")
    key = request.args.get("key")

    if key != "akiru_3K9xgH7sZrLpQt92":
        return jsonify({"error": "Invalid API key"}), 403

    if not uid:
        return jsonify({"error": "UID parameter is required"}), 400

    try:
        json_data = {
            'app_id': 100067,
            'login_id': uid,
            'app_server_id': 0,
        }

        res = requests.post(
            'https://shop2game.com/api/auth/player_id_login',
            headers={'Content-Type': 'application/json'},
            json=json_data
        )

        if res.status_code != 200 or not res.json().get("nickname"):
            return jsonify({"error": "ID NOT FOUND"}), 404

        nickname = res.json().get("nickname")
        region = res.json().get("region")

        return jsonify({
            "nickname": nickname,
            "region": region,
            "ban_status": "Mock OK"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Lấy giá trị cổng từ biến môi trường PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
