from flask_restplus import Namespace, fields, Resource

api = Namespace('projects', description='project operations')

project_create_requests = api.model('ProjectCreateRequests', {
    'id':           fields.Integer(readOnly=True, description='The project unique identifier'),
    'login':        fields.String(required=True, description='The login\'s User, it should be email'),
    'firstname':    fields.String(required=True, description='First Name User'),
    'lastname':     fields.String(required=True, description='Last Name User'),
    'git_url':      fields.String(required=True, description='Repository of Project'),
    'git_login':    fields.String(required=True, description='Github account\'s name'),
    'git_password': fields.String(required=True, description='Github password')
})


class ProjectCreate(object):
    def __init__(self):
        self.counter = 0
        self.projects = []

    def get(self, id):
        for project in self.projects:
            if project['id'] == id:
                return project
        api.abort(404, "project {} doesn't exist".format(id))

    def create(self, data):
        project = data
        project['id'] = self.counter = self.counter + 1
        self.projects.append(project)
        return project

    def update(self, id, data):
        project = self.get(id)
        project.update(data)
        return project

    def delete(self, id):
        project = self.get(id)
        self.projects.remove(project)


DAO = ProjectCreate()
DAO.create({'task': 'Build an API'})
DAO.create({'task': '?????'})
DAO.create({'task': 'profit!'})


@api.route('/')
class TodoList(Resource):
    '''Shows a list of all projects, and lets you POST to add new tasks'''
    @api.doc('list_todos')
    @api.marshal_list_with(project)
    def get(self):
        '''List all tasks'''
        return DAO.projects

    @api.doc('create_todo')
    @api.expect(project)
    @api.marshal_with(project, code=201)
    def post(self):
        '''Create a new task'''
        return DAO.create(api.payload), 201


@api.route('/<int:id>')
@api.response(404, 'project not found')
@api.param('id', 'The task identifier')
class project(Resource):
    '''Show a single project item and lets you delete them'''
    @api.doc('get_todo')
    @api.marshal_with(project)
    def get(self, id):
        '''Fetch a given resource'''
        return DAO.get(id)

    @api.doc('delete_todo')
    @api.response(204, 'project deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        DAO.delete(id)
        return '', 204

    @api.expect(project)
    @api.marshal_with(project)
    def put(self, id):
        '''Update a task given its identifier'''
        return DAO.update(id, api.payload)

