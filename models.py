# models.py


from project import db

class User(db.Model):
    
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return f"User {self.username}"