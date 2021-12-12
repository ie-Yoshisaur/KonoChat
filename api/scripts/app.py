from flask import Flask, jsonify
from flask import request

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/test', methods=['POST'])
def test():
    message = request.json['message']
    return jsonify({'message': message})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
