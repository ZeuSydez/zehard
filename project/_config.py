# project/_config.py


import os


# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = "noname.db"
CSRF_ENABLED = True
SECRET_KEY = "my_precious"
DEBUG = True

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# the database uri
SQLALCHEMY_DATABASE_URI = "sqlite:///" + DATABASE_PATH

# mail configs
MAIL_SERVER = "smtp.office365.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = "zehard@outlook.com"
MAIL_PASSWORD = "hardhus123123"