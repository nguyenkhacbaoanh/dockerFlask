from flask_restplus import fields, Namespace

class ProjectDto:
    api = Namespace('project', description='operations project')

    project = api.model('Project', {
        'projectName': fields.String(required=True, description='Name Project'),
        'descriptions': fields.String(required=False, description='Project\'s descriptions'),
        'projectType': fields.String(required=True, enum=['A','B'], description='Project type'),
        'git_url': fields.String(required=True, description='Git URL project'),
        'git_login': fields.String(required=True, description='Git login'),
        'git_password': fields.String(required=True, description='Git password')
    })

class UserDto:
    api = Namespace('user', description='user operations')

    user = api.model('User', {
        'login':        fields.String(required=True, description='The login\'s User, it should be email'),
        'password':     fields.String(required=True, description='Password to log in'),
        'firstname':    fields.String(required=True, description='First Name User'),
        'lastname':     fields.String(required=True, description='Last Name User'),
        'git_login':    fields.String(required=True, description='Github account\'s name'),
        'git_password': fields.String(required=True, description='Github password')
    })
# class ProjectModel(object):
#     def __init__(self):
#         self.counter = 0
#         self.projects = []

#     def get(self, id):
#         for project in self.projects:
#             if project['id'] == id:
#                 return project
#         api.abort(404, "Project {} doesn't exist".format(id))
    
#     def create(self, data):
#         project = data
#         project['id'] = self.counter = self.counter + 1
#         self.projects.append(project)
#         return project
    
#     def update(self, id, data):
#         project = self.get(id)
#         project.update(data)
#         return project
    
#     def delete(self, id):
#         project = self.get(id)
#         self.projects.remove(project)

# PROJECT = ProjectModel()
