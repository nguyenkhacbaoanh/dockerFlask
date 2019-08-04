from main import flask_bcrypt, db

class Project(db.Model):
    """User Model for storing project related details"""
    __tablename__ = "project"

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # login = db.Column(db.String(255), unique=True, nullable=False)
    # registered_on = db.Column(db.DateTime(255), nullable=False)
    # firstname = db.Column(db.String(255), nullable=False)
    # lastname = db.Column(db.String(255), nullable=False)
    # git_url = db.Column(db.String(255), nullable=False)
    # git_login = db.Column(db.String(255), nullable=False)
    # git_password = db.Column(db.String(255), nullable=False)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    projectName = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime(255), nullable=False)
    descriptions = db.Column(db.String(255), nullable=False)
    projectType = db.Column(db.String(255), nullable=False)
    git_url = db.Column(db.String(255), nullable=False)
    git_login = db.Column(db.String(255), nullable=False)
    git_password = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')
    
    @password.setter
    def password(self, password):
        self.git_password = flask_bcrypt.generate_password_hash(password).decode('utf-8')
    
    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.git_password, password)
    
    def __repr__(self):
        return "<Project '{}'".format(self.projectName)