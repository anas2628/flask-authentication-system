from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# Secret key is required for session management
app.secret_key = "secret123"


# Home route
@app.route("/")
def home():
    # If user already logged in, go to dashboard
    if "username" in session:
        return redirect(url_for("dashboard"))
    return "Go to /admin to login"


# Login page
@app.route("/admin")
def admin():
    return render_template("login.html")


# Login processing (form submission)
@app.route("/login", methods=["POST"])
def login():
    # Get data from login form
    username = request.form["username"]
    password = request.form["password"]

    # Simple authentication logic
    if username == "admin" and password == "1234":
        # Store username in session (login success)
        session["username"] = username
        return redirect(url_for("dashboard"))

    # Login failed
    return "Invalid username or password"


# Protected dashboard
@app.route("/dashboard")
def dashboard():
    # Allow access only if logged in
    if "username" in session:
        return render_template(
            "dashboard.html",
            user=session["username"]
        )
    return redirect(url_for("admin"))


# Logout route
@app.route("/logout")
def logout():
    # Remove user session
    session.pop("username", None)
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)
