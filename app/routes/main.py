from flask import Blueprint, jsonify

main_bp = Blueprint("main", __name__)


@main_bp.route("/healthz", methods=["GET"])
def home():
    print("Application is healthy")
    return jsonify({"message": "Application is healthy"})
