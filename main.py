from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    total = None
    average = None

    if request.method == "POST":
        tamil = int(request.form["tamil"])
        english = int(request.form["english"])
        maths = int(request.form["maths"])
        chemistry = int(request.form["chemistry"])
        physics = int(request.form["physics"])
        cs = int(request.form["cs"])

        total = tamil + english + maths + chemistry + physics + cs
        average = total / 6

    return render_template("index.html", total=total, average=average)

if __name__ == "__main__":
    app.run(debug=True)
