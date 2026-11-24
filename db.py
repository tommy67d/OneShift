import click
from flask_sqlalchemy import SQLAlchemy
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///oneshift.sqlite'

db = SQLAlchemy()
db.init_app(app)

# Modelle kommen hier rein (jeder in seinem eigenen Branch)


@click.command('init-db')
def init_db():
    """Löscht alle Tabellen und legt sie neu an."""
    with app.app_context():
        db.drop_all()
        db.create_all()
    print('Datenbank angelegt.')


app.cli.add_command(init_db)