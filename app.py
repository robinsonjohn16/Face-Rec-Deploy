from flask import Flask
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)   
app.secret_key = os.getenv("secret_key")

from myRoutes import *  