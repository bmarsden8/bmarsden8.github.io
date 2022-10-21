from property import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    address = db.Column(db.String(length=150), nullable=False, unique=True)
    email_address = db.Column(db.String(length=60), nullable=False)
