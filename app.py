from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def handle_post():
    # Get the request data
    data = request.get_json()
    # Print the data to console
    print("Received POST data:", data)
    return {"message": "Data received successfully"}, 200

if __name__ == '__main__':
    # Only use this for local development
    app.run(debug=True, host='0.0.0.0', port=10000) 