from main import db, flask_bcrypt

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    login = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime(255), nullable=False)
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    git_login = db.Column(db.String(255), nullable=False)
    git_password = db.Column(db.String(255), nullable=False)
    public_id = db.Column(db.String(500), nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')
    
    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return "<User '{}'".format(self.login)