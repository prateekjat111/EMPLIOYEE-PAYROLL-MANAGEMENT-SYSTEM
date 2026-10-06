from flask import Flask, jsonify
from flask_cors import CORS

from routes.employee_routes import employee_bp
from routes.salary_routes import salary_bp
from routes.attendance_routes import attendance_bp


app = Flask(__name__)

CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Employee Payroll Management System Backend is Running"
    })


# Register routes
app.register_blueprint(employee_bp)
app.register_blueprint(salary_bp)
app.register_blueprint(attendance_bp)


if __name__ == "__main__":
    app.run(debug=True)
