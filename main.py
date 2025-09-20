from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name="world"):
    return f'Hello, {name}!'


@app.route('/datetime')
def datetime():
    import datetime
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

