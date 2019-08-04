from flask import request
from flask_restplus import Resource

from main.utils.dto import ProjectDto
from main.service.project_service import (save_new_project, 
                                            get_all_projects, 
                                            get_a_project)

api = ProjectDto.api
project = ProjectDto.project 

@api.route('/')
class ProjectList(Resource):
    """Show list of project and method POST to add new project"""
    @api.doc('get_list_project')
    @api.marshal_list_with(project, envelope='projects')
    def get(self):
        """Fetch project source"""
        return get_all_projects()

    @api.doc('create_project')
    @api.expect(project, validate=True)
    @api.marshal_with(project, code=201)
    @api.response(201, 'Project successfully created')
    def post(self):
        """Create a new project"""
        data = request.json
        save_new_project(data)
        return data, 201
    
@api.route('/<projectName>')
@api.param('projectName', 'The project identifier')
@api.response(404, 'Project not found')
class Project(Resource):
    @api.doc('get a project')
    @api.marshal_with(project, code=200, envelope='project')
    def get(self, projectName):
        """Get a project given its identifier"""
        _project = get_a_project(projectName)
        if not _project:
            api.abort(404)
        else:
            return _project, 200