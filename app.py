from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World! <a href='/sida2'>sida2</a><a href='/sida3'>sida3</a>"

@app.route("/sida2")
def sida2():
    return "thetta er sida 2"

@app.route("/sida3")
def sida3():
    return render_template("http.html")
    
if __name__ == "__main__":
    app.run(debug=True) 
