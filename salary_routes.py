from flask import Blueprint, jsonify

salary_bp = Blueprint("salary", __name__)


@salary_bp.route("/salary/test", methods=["GET"])
def salary_test():

    return jsonify({
        "message": "Salary API is working"
    })