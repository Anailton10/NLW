from src.views.tag_creator_view import TagCreatorView
from src.views.htpp_types.http_request import HttRequest
from flask import Blueprint, request, jsonify


tags_routes_bp = Blueprint('tag_routes', __name__)


@tags_routes_bp.route('/create_tag', methods=["POST"])
def create_tags():
    tag_creator_view = TagCreatorView()

    http_request = HttRequest(body=request.json)
    response = tag_creator_view.validade_and_create(http_request)
    return jsonify(response.body), response.status_code
