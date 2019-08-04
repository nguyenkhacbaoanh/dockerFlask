from main import db
from main.model.blacklist import BlackListToken

def save_token(token):
    blacklist_token = BlackListToken(token=token)
    try:
        # insert token
        db.session.add(blacklist_token)
        db.session.commit()
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out'
        }
        return response_object, 200
    
    except Exception as e:
        response_object = {
            'status': 'fail',
            'message': e
        }
        return response_object, 400