from flask_restplus import Api
from flask import Blueprint

from main.controller.project_controller import api as project_ns
from main.controller.user_controller import api as user_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
    version='1.0', 
    title='TodoMVC API',
    description='A simple TodoMVC API',
)

api.add_namespace(project_ns, path='/project')
api.add_namespace(user_ns, path='/user')