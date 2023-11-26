import os

class BaseConfig:
    
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    TESTING = False


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    pass
