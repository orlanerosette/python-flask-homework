from flask import Flask, Response, request, url_for

app = Flask(__name__)


@app.route('/')
def welcome_to_flask():
    return "Welcome to Flask"


@app.route('/hello')
def hello_from_flask():
    return "Hello from Flask"


@app.route('/hello/<name>')
def hello(name):
    return "Hello " + name


@app.route('/name/<name>')
def say_hello_page(name):
    return """
    <html>
    <head>
        <title>Sample - Flask Routes</title>
    </head>
    <body>
        <h1>Name page </h1>
        <p>Hello {}!</p>
    </body>
    </html>
    """.format(name)


@app.route('/dynamic/<word>')
def home(word):
    return word


@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    return "Your number squared is: " + str(squared)


@app.route('/bye')
def bye_from_flask():
    return "Goodbye from Flask"


@app.route('/get/text')
def get_text():
    return Response("Hello from using an explicit RESPONSE object", mimetype='text/plain')


@app.route('/post/text', methods=['post'])
def post_text():
    data_sent = request.data.decode('utf-8')
    return Response("You posted this data: " + data_sent, mimetype='text/plain')


@app.route('/index/<name>/<int:age>')
def index(name, age):
    url = url_for('get_text')
    return """
    <html>
    <head>
    <title>Sample - Flask Routes</title>
    </head>
    <body>
        <h1>Name page</h1>
        <p>Hello {}!</p>
        <p>You are {} year(s) old.</p>
        <hr>
        <a href="{}">Welcome</a>
    </body>
    </html>
    """.format(name, age, url)


@app.route('/About/')
def about():
    url = url_for('bye_from_flask')
    return """
    <html>
    <head>
    <title>Sample - Flask Routes</title>
    </head>
    <body>
        <h1>About page</h1>
        <p>Hello!</p>
        <p>This is an about us page.</p>
        <hr>
        <a href="{}">Name page</a>
    </body>
    </html>
    """.format(url)


if __name__ == "__main__":
    app.run(debug=True, port=4000)
