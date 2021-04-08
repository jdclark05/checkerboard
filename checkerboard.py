from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/<int:x>/<int:y>")
def index(x, y):
    return render_template("index.html", num1=x, num2=y)

if __name__=="__main__":
    app.run(debug=True)