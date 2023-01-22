from flask import Flask, render_template, url_for, redirect

from cupcake import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("cupcakes.html", cupcakes= get_cupcakes("cupcakes.csv"))

@app.route("/cupcake_individual")
def individual_cupcake():
    return render_template("individual-cupcakes.html", cupcakes= get_cupcakes("cupcakes.csv"))

@app.route("/order")
def order():
    return render_template("order.html", cupcakes= get_cupcakes("orders.csv"))

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv",name)

    if cupcake:
        print(cupcake)
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")