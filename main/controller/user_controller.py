from flask_restplus import Resource
from flask import request

from main.utils.dto import UserDto
from main.service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
user = UserDto.user

@api.route('/')
class UserList(Resource):
    '''Shows a list of all users, and lets you POST to add new user'''
    @api.doc('list_users')
    @api.marshal_list_with(user, envelope='users')
    def get(self):
        '''List all user'''
        users = get_all_users()
        return users, 200

    @api.doc('create_user')
    @api.expect(user)
    @api.marshal_with(user, code=201, envelope='user')
    def post(self):
        '''Create a new task'''
        data = request.json
        save_new_user(data)
        return data, 201


@api.route('/<string:login>')
@api.response(404, 'project not found')
@api.param('login', 'The user identifier')
class User(Resource):
    '''Show a single user and lets you delete them'''
    @api.doc('get_user')
    @api.marshal_with(user, envelope='user')
    def get(self, login):
        '''Fetch a given resource'''
        _user = get_a_user(login)
        return _user, 200

    # @api.doc('delete_todo')
    # @api.response(204, 'project deleted')
    # def delete(self, id):
    #     '''Delete a task given its identifier'''
    #     DAO.delete(id)
    #     return '', 204

    # @api.expect(project)
    # @api.marshal_with(project)
    # def put(self, id):
    #     '''Update a task given its identifier'''
    #     return DAO.update(id, api.payload)

