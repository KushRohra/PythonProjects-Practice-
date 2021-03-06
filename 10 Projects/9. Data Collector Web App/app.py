from flask import Flask, render_template, request
import json
from send_email import send_email

app = Flask(__name__)


def get_statistics():
    with open('data.json', 'r') as f:
        data = json.load(f)
    count = 0
    total_height = 0
    for entry in data:
        count += 1
        total_height += data[entry]
    return (total_height / count), count


def enter_data(email, height):
    value = 1
    with open('data.json', 'r') as f:
        data = json.load(f)
    if email in list(data.keys()):
        if height == data[email]:
            value = 2
        else:
            value = 3
    data.update({email: height})
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=2)
    return value


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        email = request.form["email_name"]
        height = int(request.form["height_name"])
        res = enter_data(email, height)
        if res == 1:
            avg_height, count = get_statistics()
            send_email(email, height, avg_height, count)
            return render_template("success.html")
        if res == 2:
            return render_template("index.html", error_mssg="Data with same email address and height already exists")
        if res == 3:
            return render_template("index.html", error_mssg="Height for the email address is updated")
    return render_template("index.html", error_mssg="")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
