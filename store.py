from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/hello')
def hello():
    return 'hello world'


@app.route('/hello/<username>')
def hello_user(username):
    return 'hello %s' % username


if __name__ == "__main__":
    app.run()
