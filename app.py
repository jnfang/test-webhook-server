from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store raw events in memory
events = []

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Get and store the complete event data
        event_data = request.get_json()
        events.append(event_data)
        
        # Print to console for logging
        print(f"Received event: {event_data['data']['id']}")
        
        return {"message": "Event received successfully"}, 200
    else:  # GET request
        return {
            "events": events,
            "total_events": len(events)
        }, 200

if __name__ == '__main__':
    # Only use this for local development
    app.run(debug=True, host='0.0.0.0', port=10000) 