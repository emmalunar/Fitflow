from flask import Flask, request, jsonify
from flask_cors import  CORS
import requests

app = Flask(__name__)

@app.route('/api/vitals', methods=['POST'])
def post_vitals():
    vitals = {
        'heartRate': 72,
        'spo2': 98
    }

    try:
        # POST the vitals data to the specified URL
        response = requests.post('http://192.168.137.1:5173/api/vitals', json=vitals)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Return the response from the external server
        return jsonify({'status': 'Data posted successfully', 'response': response.json()})
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    
    app.run(debug=True)  # Customize port if needed