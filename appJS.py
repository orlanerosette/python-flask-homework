from flask import Flask, Response, request, url_for

# instantiating the flask application object
app = Flask(__name__)

# the route variable is a string by default
# equivalent to @app.route('/dynamic/string<string:word>')
@app.route('/dynamic/<word>')
def home(word):
    return word


# this route variable is an int type called number
@app.route('/square/<int:number>')
def square(number):
    squared = number ** 2
    line = 'Your number squared is' + " " + str(squared)
    return line


@app.route('/name/<name>')
def say_hello_page(name):
    return """
<html>
<head>
    <title>Sample - Flask routes</title>
</head>
<body>
    <h1>Name Page</h1>
    <p>Hello {}!</p>
</body>
</html>  
""".format(name)
# tripe quotes means the code can print on multiple lines. the {} is a formated string so what I type in for name, that will appear where the empty {} is.


@app.route('/get/text')
def get_text():
    return Response("Hello from Flask using an explicit Response object", mimetype='text/plain')


@app.route("/index/<name>/<int:age>")
def index(name, age):
    url = url_for('get_text')
    return """
<html>
<head>
    <title>Sample - Flask routes</title>
</head>
<body>
    <h1>Name Page</h1>
    <p>Hello {}!</p>
    <p>You are {} year(s) old.</p>
    <hr>
    <a href="{}">Welcome</a>
</body>
</html>
""".format(name, age, url)


@app.route('/about')
def about():
    url = url_for('index')
    return """
<html>
<head>
    <title>Sample - Flask routes About</title>
</head>
<body>
    <h1>About</h1>
    <p>Hello!</p>
    <p>Learn about this project.</p>
    <hr>
    <a href="{}">Welcome</a>
</body>
</html>
""".format(url)


if __name__ == "__main__":
    app.run(debug=True, port=4001)