from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Store workflow events in memory
workflow_events = []

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'POST':
        # Get the request data
        event_data = request.get_json()
        
        try:
            # Extract relevant information
            workflow_event = {
                'event_id': event_data['data']['id'],
                'event_type': event_data['data']['attributes']['name'],
                'event_timestamp': event_data['data']['attributes']['created-at'],
                'workflow': {
                    'id': event_data['data']['attributes']['payload']['included'][0]['id'],
                    'name': event_data['data']['attributes']['payload']['included'][0]['attributes']['name'],
                    'status': event_data['data']['attributes']['payload']['included'][0]['attributes']['status'],
                    'created_at': event_data['data']['attributes']['payload']['included'][0]['attributes']['created-at']
                },
                'workflow_version': {
                    'id': event_data['data']['attributes']['payload']['data']['id'],
                    'status': event_data['data']['attributes']['payload']['data']['attributes']['status'],
                    'created_at': event_data['data']['attributes']['payload']['data']['attributes']['created-at']
                }
            }
            
            # Store the processed event
            workflow_events.append(workflow_event)
            
            # Print to console for logging
            print(f"Received workflow event: {workflow_event['event_type']} for workflow: {workflow_event['workflow']['name']}")
            
            return {"message": "Event received successfully", "event_id": workflow_event['event_id']}, 200
            
        except KeyError as e:
            return {"error": f"Invalid event format: missing {str(e)}"}, 400
        except Exception as e:
            return {"error": f"Error processing event: {str(e)}"}, 500
            
    else:  # GET request
        return {
            "events": workflow_events,
            "total_events": len(workflow_events)
        }, 200

if __name__ == '__main__':
    # Only use this for local development
    app.run(debug=True, host='0.0.0.0', port=10000) 