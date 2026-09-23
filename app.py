from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello TCS Folks welcome to ACR v4.0,integrated with github</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)