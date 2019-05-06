"""picoCTF API v1 app."""

from flask import Blueprint, jsonify
from flask_restplus import Api

from api.common import PicoException

from .achievements import ns as achievements_ns
from .problems import ns as problems_ns
from .shell_servers import ns as shell_servers_ns
from .exceptions import ns as exceptions_ns
from .settings import ns as settings_ns
from .bundles import ns as bundles_ns
from .submissions import ns as submissions_ns
from .feedback import ns as feedback_ns
from .users import ns as users_ns
from .user import ns as user_ns

blueprint = Blueprint('v1_api', __name__)
api = Api(
    app=blueprint,
    title='picoCTF API',
    version='1.0',
)

api.add_namespace(achievements_ns)
api.add_namespace(problems_ns)
api.add_namespace(shell_servers_ns)
api.add_namespace(exceptions_ns)
api.add_namespace(settings_ns)
api.add_namespace(bundles_ns)
api.add_namespace(submissions_ns)
api.add_namespace(feedback_ns)
api.add_namespace(users_ns)
api.add_namespace(user_ns)


@api.errorhandler(PicoException)
def handle_pico_exception(e):
    """Handle exceptions."""
    response = jsonify(e.to_dict())
    response.status_code = e.status_code
    return response
