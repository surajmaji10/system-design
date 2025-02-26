
"""
@author: Akash Maji
@email: akashmaji@iisc.ac.in
"""

from flask import Flask, request, jsonify  
import redis  
import time  

app = Flask(__name__)  
redis_db = redis.StrictRedis(host='localhost', port=6379, db=0)  

# Rate limiter configuration  
RATE_LIMIT = 3  # Max requests  
TIME_WINDOW = 10  # Time window in seconds  

def is_rate_limited(ip):  
    """Check if the IP has exceeded the rate limit."""  
    current_time = int(time.time())  
    key = f"rate_limit:{ip}"  
    request_count = redis_db.incr(key)  

    # Set expiration if this is the first request  
    if request_count == 1:  
        redis_db.expire(key, TIME_WINDOW)  

    # Check if the request count exceeds the limit  
    if request_count > RATE_LIMIT:  
        return True  
    return False  

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the page"

@app.route('/load', methods = ['GET'])
def load():
    a = 1
    n = 100
    for i in range(1, n+1):
        a = a * i
    return "The fact is:" + str(a)


@app.route('/users', methods=['GET'])  
def users():  
    ip = request.remote_addr  
    if is_rate_limited(ip):  
        return jsonify({"error": "Rate limit exceeded. Try again later."}), 429  
    return jsonify({"message": "Welcome to the /users endpoint!"})  

if __name__ == '__main__':  
    app.run(host="localhost", port = 9090, debug=True)