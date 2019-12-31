from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy = 'dynamic') 
    # one store can relate to many items. so it's a list of ItemModel -> need a json
      # until we call json() method, WE are not look into the item table,
      # so create store will be simple

    def __init__(self, name):
        self.name = name

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}
      

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first() #select * from... where name = ?
        # sqlalchmy will auto return a ItemModel object

        #if row:
           # return cls(*row) # perfect example to use unpacking
             # return an object instead of a dictionalry 
            #return cls(row[0], row[1])

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()