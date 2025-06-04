from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store messages in memory
message_history = []

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Get the request data
        data = request.get_json()
        # Add timestamp to the data
        message_entry = {
            'timestamp': datetime.now().isoformat(),
            'data': data
        }
        # Store in memory
        message_history.append(message_entry)
        # Print the data to console
        print("Received POST data:", data)
        return {"message": "Data received successfully"}, 200
    else:  # GET request
        return {"messages": message_history}, 200

if __name__ == '__main__':
    # Only use this for local development
    app.run(debug=True, host='0.0.0.0', port=10000) 