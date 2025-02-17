from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time_and_ip():
    # Get current timestamp
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    # Get visitor's IP address
    ip = request.remote_addr
    
    # Return JSON response
    return jsonify({
        "timestamp": timestamp,
        "ip": ip
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
