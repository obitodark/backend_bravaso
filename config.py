from os import getenv
from datetime import timedelta


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = getenv('JWT_SECRET')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(hours=3)

    MAIL_SERVER = getenv('MAIL_SERVER')
    MAIL_PORT = getenv('MAIL_PORT')
    MAIL_USE_TLS = bool(getenv('MAIL_USE_TLS'))
    MAIL_USERNAME = getenv('MAIL_USERNAME')
    MAIL_PASSWORD = getenv('MAIL_PASSWORD')
    MAIL_DEBUG = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
    # SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL').replace(
    #     'postgres', 'postgresql', 1
    # )
    SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
  
# SQLALCHEMY_DATABASE_URI=f"postgresql://{getenv('PGUSER')}:{getenv('PGPASSWORD')}@{getenv('PGHOST')}:{getenv('PGPORT')}/{getenv('PGDATABASE')}"
config_env = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
# postgresql://${{ PGUSER }}:${{ PGPASSWORD }}@${{ PGHOST }}:${{ PGPORT }}/${{ PGDATABASE }}