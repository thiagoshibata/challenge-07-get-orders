from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

from src.main.composer.login_create_composer import login_create_composer
from src.main.composer.create_orders_composer import create_orders_composer

from src.main.middlewares.auth_jwt import auth_jwt_verify

orders_routes_bp = Blueprint("orders_routes", __name__)

@orders_routes_bp.route("/orders/login", methods=["POST"])
def create_login():
    http_request = HttpRequest(body=request.json)
    http_response = login_create_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@orders_routes_bp.route("/orders", methods=["POST"])
def create_order():
    token_information = auth_jwt_verify()
    http_request = HttpRequest(body=request.json, headers=request.headers, token_infos=token_information)
    http_response = create_orders_composer().handle(http_request)
    return jsonify(http_response.body), http_response.status_code
