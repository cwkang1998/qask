from flask import Blueprint
from flask import jsonify, request

api_bp = Blueprint('api', __name__, url_prefix='/')


@api_bp.route('/')
def index():
    return "Qask running successfully"


@api_bp.route('/api/v1.0/ping', methods=['GET'])
def dummy_endpoint():
    return jsonify({'data': 'Server running'}), 200
