from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time_and_ip():
    # Get the current timestamp
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    # Get the visitor's IP address
    ip_address = request.remote_addr
    
    # Return the JSON response
    return jsonify({
        "timestamp": timestamp,
        "ip": ip_address
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
