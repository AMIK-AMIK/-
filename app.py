from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/location', methods=['POST'])
def get_location():
    data = request.json
    latitude = data.get('latitude')
    longitude = data.get('longitude')

    print(f"User Location: Latitude={latitude}, Longitude={longitude}")
    return {"status": "success"}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
