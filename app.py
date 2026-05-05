from flask import Flask, render_template, request, redirect, url_for
from expense import Expense
from storage import load_data, save_data
from analytics import total_spending, category_summary
from utils import export_to_csv

app = Flask(__name__)


@app.route("/")
def index():
    data = load_data()
    total = total_spending(data)
    summary = category_summary(data)
    return render_template("index.html", data=data, total=total, summary=summary)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        amount = float(request.form["amount"])
        category = request.form["category"]
        note = request.form["note"]

        expense = Expense(amount, category, note)
        data = load_data()
        data.append(expense.to_dict())
        save_data(data)

        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:index>")
def delete(index):
    data = load_data()
    if 0 <= index < len(data):
        data.pop(index)
        save_data(data)
    return redirect(url_for("index"))


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    data = load_data()

    if request.method == "POST":
        data[index]["amount"] = float(request.form["amount"])
        data[index]["category"] = request.form["category"]
        data[index]["note"] = request.form["note"]

        save_data(data)
        return redirect(url_for("index"))

    return render_template("edit.html", exp=data[index], index=index)


@app.route("/export")
def export():
    export_to_csv(load_data())
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)