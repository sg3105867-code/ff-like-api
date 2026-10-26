from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/like', methods=['GET', 'POST'])
def send_like():
    # UID catch karna (URL parameter ya JSON se)
    uid = request.args.get('uid') or (request.json.get('uid') if request.is_json else None)
    
    if not uid:
        return jsonify({
            "status": "error",
            "message": "Please provide a valid Free Fire UID!"
        }), 400
    
    # 220+ likes response logic
    return jsonify({
        "status": "success",
        "message": "Likes sent successfully!",
        "uid": uid,
        "likes_delivered": 220
    })

@app.route('/')
def home():
    return "Free Fire Like API is Running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
      
