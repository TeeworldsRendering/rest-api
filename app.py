from flask import Flask

app: object = Flask(__name__)

from routes.index import *
from routes.sql import *

# gunicorn -b localhost:1234 app
from app import app as application
app = application
