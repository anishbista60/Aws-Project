from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world! and Congrats you are sucessfully done with this  '

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
