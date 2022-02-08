from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import gpt2_model

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

device = gpt2_model.load_device()
tokenizer = gpt2_model.generate_tokenizer()
pretrained_model_path = 'Yoshisaur/kono-chat'
model = gpt2_model.generate_model(pretrained_model_path, device)


@app.route('/reply', methods=['POST'])
def reply():
    message = request.json['message']
    reply = gpt2_model.generate_reply(message, device, tokenizer, model)
    return jsonify({'message': reply})
