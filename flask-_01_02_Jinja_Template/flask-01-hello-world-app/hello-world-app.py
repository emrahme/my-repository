from flask import Flask 
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello WOrld"

@app.route("/bye")
def bye():
    return "bye"

@app.route("/third")
def third():
    return "Hello From My Third Path"

@app.route("/third/subthird")
def subthird():
    return "This is a double path"

@app.route("/fourth/<string:id>")
def fourth(id):
    output = f"Your id is: {id}"
    return output







if __name__ == '__main__':

    app.run(debug=True, port=5000)
    # app.run(host= '0.0.0.0', port=8081)