from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def get_time_and_ip():
    timestamp = datetime.utcnow().isoformat() + "Z"
    ip = request.remote_addr
    return jsonify({
        "timestamp": timestamp,
        "ip": ip
    })

# No need for __main__ block when using Gunicorn
~
