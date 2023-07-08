# db_create.py


from project import db, app
from models import User

with app.app_context():
    db.create_all()