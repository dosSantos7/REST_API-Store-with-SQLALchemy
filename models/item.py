from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'     # defining the table name used in this resource

    # which attribute of the table is to be used, must be same as the instance variables
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    # return the item object in JSON format
    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    # gets the row from the DB and returns it in ItemModel object format
    @classmethod
    def get_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    # adds itself to the DB
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Deletes itself from the DB
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()