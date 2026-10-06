from flask import Blueprint, jsonify

attendance_bp = Blueprint("attendance", __name__)


@attendance_bp.route("/attendance/test", methods=["GET"])
def attendance_test():

    return jsonify({
        "message": "Attendance API is working"
    })
    