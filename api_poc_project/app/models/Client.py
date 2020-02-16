from app.init import db


class Client(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)
    identity_number = db.Column(db.Integer)
    age = db.Column(db.Integer)
    client_name = db.Column(db.String(25))
    client_surname = db.Column(db.String(25))

    def __init__(self, identity_number, age, client_name, client_surname):
        self.identity_number = identity_number
        self.age = age
        self.client_name = client_name
        self.client_surname = client_surname
