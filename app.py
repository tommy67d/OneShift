from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='nur-fuer-die-entwicklung',
)

bootstrap = Bootstrap5(app)


from db import db


@app.route('/')
def index():
    return render_template('index.html')