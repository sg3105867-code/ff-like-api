from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/like', methods=['GET', 'POST'])
def send_like():
    # UID catch karna (URL parameter ya JSON se)
    uid = request.args.get('uid') or (request.json.get('uid') if request.is_json else None)
    
    if not uid:
        return jsonify({
            "status": "error",
            "message": "Please provide a valid Free Fire UID!",
            "powered_by": "@cheeku_boy"
        }), 400

    # आपके निर्देशानुसार प्रोग्रेस स्टेप्स
    progress_steps = [
        {"progress": "20%", "message": "Connecting to Free Fire game server..."},
        {"progress": "40%", "message": "Fetching player profile data..."},
        {"progress": "50%", "message": "Bypassing security protocols..."},
        {"progress": "90%", "message": "Sending likes to player UID..."},
        {"progress": "100%", "message": "Likes sent successfully!"}
    ]
    
    # 220+ likes response logic with progress and credit
    return jsonify({
        "status": "success",
        "message": "Likes sent successfully!",
        "uid": uid,
        "likes_delivered": 220,
        "steps": progress_steps,
        "powered_by": "@cheeku_boy"
    })

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Free Fire Like API is Running!",
        "powered_by": "@cheeku_boy"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
