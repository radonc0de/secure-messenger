from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
messages = [
    {
        'from': 'Me',
        'body': 'Hey there!'
    },
    {
        'from': 'Them',
        'body': 'Sup dude'
    }
]

# GET endpoint
@app.route('/getdata', methods=['GET'])
def get_data():
    # Example data
    return jsonify(messages)

# POST endpoint
@app.route('/postdata', methods=['POST'])
def post_data():
    # Receiving JSON data
    received_data = request.json
    messages.push(received_data)

    return jsonify({"received": received_data}), 201

if __name__ == '__main__':
    app.run(debug=True)

