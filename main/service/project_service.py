import uuid
import datetime

from main import db
from main.model.project import Project

def save_new_project(data):
    project = Project.query.filter_by(projectName=data['projectName']).first()
    if not project:
        new_project = Project(
            public_id = str(uuid.uuid4()),
            projectName = data['projectName'],
            descriptions = data['descriptions'],
            projectType = data['projectType'],
            git_url = data['git_url'],
            git_login = data['git_login'],
            git_password = data['git_password'],
            registered_on = datetime.datetime.utcnow()
        )
        save_changes(new_project)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Project already exists.'
        }
        return response_object, 409

def get_all_projects():
    return Project.query.all()

def get_a_project(projectName):
    return Project.query.filter_by(projectName=projectName).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()