class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    SECRET_KEY = 'a secret'
    JWT_SECRET_KEY = 'super-secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../test.db'


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
