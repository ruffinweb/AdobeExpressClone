
import os
import ast


class ProductionConfig:
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SECURE = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_BINDS = ast.literal_eval(os.environ.get("SQLALCHEMY_BINDS", "{}"))
    static_folder = "static"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    DEBUG = False
    TESTING = False
    MAIL_SUPPRESS_SEND = False


class DevelopmentConfig:
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SECURE = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_BINDS = ast.literal_eval(os.environ.get("SQLALCHEMY_BINDS", "{}"))
    static_folder = "static"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    DEBUG = True
    TESTING = False
    MAIL_SUPPRESS_SEND = False


class TestingConfig:
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SECURE = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_BINDS = ast.literal_eval(os.environ.get("SQLALCHEMY_BINDS", "{}"))
    static_folder = "static"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    DEBUG = False
    TESTING = True
    MAIL_SUPPRESS_SEND = False


# print(ProductionConfig.SECRET_KEY)
# print(ProductionConfig.SQLALCHEMY_DATABASE_URI)
# print(ProductionConfig.SQLALCHEMY_BINDS)
# print(ProductionConfig.MAIL_USERNAME)
# print(ProductionConfig.MAIL_PASSWORD)
# print()
# print(DevelopmentConfig.SECRET_KEY)
# print(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
# print(DevelopmentConfig.SQLALCHEMY_BINDS)
# print(DevelopmentConfig.MAIL_USERNAME)
# print(DevelopmentConfig.MAIL_PASSWORD)
# print()
# print(TestingConfig.SECRET_KEY)
# print(TestingConfig.SQLALCHEMY_DATABASE_URI)
# print(TestingConfig.SQLALCHEMY_BINDS)
# print(TestingConfig.MAIL_USERNAME)
# print(TestingConfig.MAIL_PASSWORD)


