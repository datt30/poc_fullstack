from app import db


class ExternalProvider(db.Model):
    external_provider_id = db.Column(db.Integer, primary_key=True)
    external_provider_name = db.Column(db.String(25))
    phone = db.Column(db.Integer)
    detail = db.Column(db.String(255))

    def __init__(self, external_provider_name, phone, detail):
        self.external_provider_name = external_provider_name
        self.phone = phone
        self.detail = detail
