import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
# gives access to the project frmo any operatins system
# we find ourselves in
# alllow outside file/folders to be added to the project
# from the base directory

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set config variables for the flask app.
    Using environment variables where available
    Otherwise creat the config variable if not done already
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Nana nana boo boo you will never guess'
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turns off changes from sql alchemy

