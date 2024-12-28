from flask import Blueprint, jsonify

orders_routes_bp = Blueprint("orders_routes", __name__)

@orders_routes_bp.route("/orders", methods=["GET"])
def hello_world():
    return jsonify({"message": "Hello, World!"})