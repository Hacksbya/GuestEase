from flask import Flask, request, jsonify
import csv
import os
from flask_cors import CORS



app = Flask(__name__)
CORS(app)
# CSV file path
CSV_FILE = "submissions.csv"

# Ensure the CSV file exists and has a header
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Index", "Selected Plan", "Name", "Organization Name", "Contact No", "Email"])

@app.route("/save-data", methods=["POST"])
def save_data():
    data = request.json

    # Read current index
    with open(CSV_FILE, mode="r") as file:
        lines = list(csv.reader(file))
        index = len(lines)  # Next index starts after the last line

    # Save the data
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([index, data["selectedPlan"], data["name"], data["organization"], data["contact"], data["email"]])

    return jsonify({"message": "Data saved successfully!"}), 200

if __name__ == "__main__":
    app.run(debug=True)
