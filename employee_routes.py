from flask import Blueprint, jsonify, request
from database import get_db_connection

employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/employees", methods=["GET"])
def get_employees():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(employees)


@employee_bp.route("/employees", methods=["POST"])
def add_employee():

    data = request.json

    connection = get_db_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO employees
        (employee_name, email, phone, department,
         designation, joining_date, basic_salary)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["employee_name"],
        data["email"],
        data["phone"],
        data["department"],
        data["designation"],
        data["joining_date"],
        data["basic_salary"]
    )

    cursor.execute(query, values)
    connection.commit()

    cursor.close()
    connection.close()

    return jsonify({
        "message": "Employee added successfully"
    }), 201