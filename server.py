from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def checkerboard():
    return render_template("index.html", y = 8, x = 8)

@app.route('/<int:y>')
def checkerboard_rows(y):
    return render_template("index.html", y = y, x = 8)

@app.route('/<int:y>/<int:x>')
def checkerboard_custom(y,x):
    return render_template("index.html", y = y, x = x)





if __name__ == "__main__":
    app.run(debug=True)  