from flask import Flask, jsonify
from flask import request
import gpt2_model

device = gpt2_model.load_device()
tokenizer = gpt2_model.generate_tokenizer()
pretrained_model_path = 'Yoshisaur/kono-chat'
model = gpt2_model.generate_model(pretrained_model_path, device)

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/reply', methods=['POST'])
def reply():
    message = request.json['message']
    reply = gpt2_model.generate_reply(message, device, tokenizer, model)
    return jsonify({'message': reply})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
