from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit-enquiry", methods=["POST"])
def submit_enquiry():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    service = request.form.get("service", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        return render_template(
            "index.html",
            success="Please fill in all required fields."
        )

    enquiry = f"""
----------------------------------------
NEXORA PROJECT ENQUIRY
----------------------------------------
Date: {datetime.now().strftime("%d-%m-%Y %H:%M:%S")}

Name: {name}
Email: {email}
Phone: {phone}
Service: {service}

Message:
{message}

----------------------------------------
"""

    with open("enquiries.txt", "a", encoding="utf-8") as file:
        file.write(enquiry)

    return render_template(
        "index.html",
        success="Thank you! Your enquiry has been received."
    )


if __name__ == "__main__":
    app.run(debug=True)