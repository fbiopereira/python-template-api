import os


class Config:
    DEPENDENCY_API_B_URL = os.environ.get('DEPENDENCY_API_B_URL')
    DEPENDENCY_API_A_URL = os.environ.get('DEPENDENCY_API_A_URL')
    SERVICE_NAME = os.environ.get('SERVICE_NAME')
    GIT_TAG = os.environ.get('GIT_TAG')
    ENVIRONMENT = os.environ.get('ENVIRONMENT')
    LOG_PATH = os.environ.get('LOG_PATH')
    REDIS_URL = os.environ.get('REDIS_URL')
    REDIS_PORT = os.environ.get('REDIS_PORT')
    REDIS_ERROR_INTERVAL = os.environ.get('REDIS_ERROR_INTERVAL')
    SWAGGER_UI_DOC_EXPANSION = os.environ.get('SWAGGER_UI_DOC_EXPANSION')
    RESTPLUS_VALIDATE = os.environ.get('RESTPLUS_VALIDATE')
    RESTPLUS_MASK_SWAGGER = os.environ.get('RESTPLUS_MASK_SWAGGER')
    ERROR_404_HELP = os.environ.get('ERROR_404_HELP')


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'pre-production': ProductionConfig,
    'default': DevelopmentConfig
}
