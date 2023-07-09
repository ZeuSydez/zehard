# models.py


from project import db

class User(db.Model):
    
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    coord = db.relationship("MCCoord", backref="user")
    
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password
    
    def __repr__(self):
        return f"User {self.username}"

class MCCoord(db.Model):
    
    __tablename__ = "mccoord"

    coord_id = db.Column(db.Integer, primary_key=True)
    coord_name = db.Column(db.String(100), nullable=False)
    coord_x = db.Column(db.Integer, nullable=False)
    coord_y = db.Column(db.Integer, nullable=False)
    coord_z = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    
    def __init__(self, coord_name=None, coord_x=None, coord_y=None, coord_z=None, user_id=None):
        self.coord_name = coord_name
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.coord_z = coord_z
        self.user_id = user_id
    
    def __repr__(self):
        return f"name {self.coord_name}"
