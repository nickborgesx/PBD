import flask
from iponto.modules.roles.dao import DAORoles

roles_controller = flask.Blueprint('role_controller', __name__)
dao_roles = DAORoles()
module_name = 'roles'