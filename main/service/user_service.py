from main import db
import uuid
import datetime

from main.model.user import User

def save_new_user(data):
    user = User.query.filter_by(login=data['login']).first()
    if not user:
        new_user = User(
            public_id = str(uuid.uuid4()),
            login = data['login'],
            password = data['password'],
            firstname = data['firstname'],
            lastname = data['lastname'],
            git_login = data['git_login'],
            git_password = data['git_password'],
            registered_on = datetime.datetime.utcnow()
        )
        save_changes(new_user)
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

def get_all_users():
    return User.query.all()

def get_a_user(login):
    return User.query.filter_by(login=login).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()