# Create a internal respresentation for item
from db import db

class StoreModel(db.Model):

    # SQLAlchemy
    __tablename__ = 'stores'
    # items' Columns info
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy = 'dynamic') # many items to store -> many to one

    def __init__(self, name):
        self.name = name        

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
        # list of items since one sotre will have multiple items

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        # Equal to -> SELECT * FROM store WHERE name = name LIMIT 1
        # Also return as ItemModel object

    def save_to_db(self):
        db.session.add(self) # session allow multiple insert
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
