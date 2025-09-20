from flask import Flask
from flask import render_template, Blueprint


comment = Blueprint('commnet', __name__, url_prefix='/commnet')