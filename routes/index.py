from flask import Blueprint
from controller import IndexController


index_route = Blueprint('index', __name__, url_prefix='/index')

@index_route.route('/read', methods=['GET'])
def read():
    return IndexController.read()
