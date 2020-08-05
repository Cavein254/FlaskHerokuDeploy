from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    return "<h1>You are home</h1>"

if __name__ == '__main__':
    app.run(debug=True)