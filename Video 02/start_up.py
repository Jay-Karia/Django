import flask

app = flask.Flask(__name__)
@app.route('/')
def hello():
    return 'Hello World'

@app.route('/jay')
def jay():
    return 'Hello Jay Programmer'

app.run(debug=True)