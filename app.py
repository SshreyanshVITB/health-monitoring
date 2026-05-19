from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this in production

# Dummy user data
USER_DATA = {
    "admin": "password123"
}

# -------------------- Routes -------------------- #
@app.route("/")
def home():
    if "user" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in USER_DATA and USER_DATA[username] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))

    # Generate simulated readings
    heart_rate = random.randint(60, 100)   # bpm
    spo2 = random.randint(92, 100)         # %

    # Suggestions
    suggestions = [
        "Exercise regularly (at least 30 mins/day).",
        "Eat more fruits and vegetables.",
        "Avoid smoking and excessive alcohol.",
        "Manage stress through yoga or meditation.",
        "Get regular health checkups.",
        "Maintain a healthy weight."
    ]

    return render_template("dashboard.html", heart_rate=heart_rate, spo2=spo2, suggestions=suggestions)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))


# -------------------- Run -------------------- #
if __name__ == "__main__":
    app.run(debug=True)
