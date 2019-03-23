from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'index page'


@app.route('/hello')
def hello_world():
    return 'hello world!'


@app.route('/fib/<int:n>', methods=['GET'])
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b

    response_data = {'data': result}
    return render_template('fibo.html', response=response_data)
