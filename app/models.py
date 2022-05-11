from app import db

class User(db.Model):
#inherits from db.Model - base class in Flask-SQLAlchemy defines fields as class vars
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.string(128))

    #formats data for more helpful debugging
    def __repr__(self):
        return '<User {}>'.format(self.username)