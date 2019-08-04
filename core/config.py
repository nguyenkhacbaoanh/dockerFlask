import os
from configparser import ConfigParser

# DATABASE_URL = "postgresql://user:password@postgresserver/db"

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class Config:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    def __init__(self, filename='database.ini', section='postgresql'):
        self.filename = filename
        self.section = section

    @property
    def setConfig(self):
        # create a parser
        parser = ConfigParser()
        # read config file
        parser.read(self.filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(self.section):
            params = parser.items(self.section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(self.section, self.filename))
        self.SQLALCHEMY_DATABASE_URI = "postgresql://{user}:{password}@{host}/{database}".format(**db)

class  DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'development'
    def __init__(self, filename=basedir+'/database.ini', section='postgresql_dev'):
        self.filename = filename
        self.section = section
        super().setConfig

class  TestConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    def __init__(self, filename=basedir+'/database.ini', section='postgresql_test'):
        # self.filename = filename
        # self.section = section
        super().__init__(filename=basedir+'/database.ini', section='postgresql_test')
        super().setConfig

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    def __init__(self, filename=basedir+'/database.ini', section='postgresql_prod'):
        # self.filename = filename
        # self.section = section
        super().__init__(filename=basedir+'/database.ini', section='postgresql_prod')
        super().setConfig

# conf = Config()

config_by_name = dict(
    dev=DevConfig(),
    test=TestConfig(),
    prod=ProdConfig()
)
