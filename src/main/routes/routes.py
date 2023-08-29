from flask import Blueprint, request, jsonify
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer


user_route_bp = Blueprint("user_routes", __name__)


@user_route_bp.route("/users/find/", methods=["GET"])
def find_user():
    http_response = request_adapter(request, user_finder_composer())
    return jsonify(http_response.body), http_response.status_code


@user_route_bp.route("/users/", methods=["POST"])
def register_user():
    http_response = request_adapter(request, user_register_composer())
    return jsonify(http_response.body), http_response.status_code
