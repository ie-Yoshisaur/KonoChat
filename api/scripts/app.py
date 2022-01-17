from flask import Flask, jsonify
from flask import request
import gpt2_model

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/reply', methods=['POST'])
def reply():
    message = request.json['message']
    return jsonify({'message': message})
