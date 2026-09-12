from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Головна",
        page="home",
    )


@app.route("/about")
def about():
    return render_template(
        "index.html",
        title="Про мене",
        page="about",
    )


@app.route("/skills")
def skills():
    return render_template(
        "index.html",
        title="Навички",
        page="skills",
    )


if __name__ == "__main__":
    app.run(debug=True)