from flask import Blueprint

access = Blueprint('access', __name__)


@access.route('/test')
def test():

    return {'status': 'access successful'}