import flask
app=flask.Flask("__main__")

@app.route("/")
def my_index():
    return "Hello world"

app.run(debug=True)