# Simple Flask API

A simple Flask API that accepts POST requests and prints the request body to console.

## API Endpoint

POST `/api`

### Request
- Method: POST
- Content-Type: application/json
- Body: Any valid JSON

### Response
```json
{
    "message": "Data received successfully"
}
```

## Local Development
1. Create virtual environment: `python -m venv venv`
2. Activate virtual environment: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `python app.py`

## Deployment
This application is configured for deployment on Render.com 