from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='public')
CORS(app)  # Enable CORS for all routes

data = {}  # Initialize data storage

@app.route('/api', methods=['POST'])
def handle_post():
    global data
    data = request.json
    return jsonify({'message': 'Dados salvos com sucesso'}), 200

@app.route('/api', methods=['GET'])
def handle_get():
    print("Dados enviados para a requisição GET:", data)
    return jsonify(data), 200

@app.route('/', methods=['GET'])
def root():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True, port=3333)
