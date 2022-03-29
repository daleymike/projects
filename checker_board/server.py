from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def checkerboard():
    return render_template("index.html", y = 8, x = 8, color1 = "red", color2 = "black")

@app.route('/<int:y>')
def checkerboard_rows(y):
    return render_template("index.html", y = y, x = 8, color1 = "red", color2 = "black")

@app.route('/<int:y>/<int:x>')
def checkerboard_custom(y,x):
    return render_template("index.html", y = y, x = x, color1 = "red", color2 = "black")

@app.route('/<int:y>/<int:x>/<color1>/<color2>')
def checkerboard_custom_colors(y,x,color1,color2):
    return render_template("index.html", y = y, x = x, color1 = color1, color2 = color2) 



if __name__ == "__main__":
    app.run(debug=True)  