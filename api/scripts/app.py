from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def home():
    message = "HOME"
    return jsonify({'message': message})

@app.route('/Hello-World')
def hello_world():
    message = "Hello, World!"
    return jsonify({'message': message})

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
