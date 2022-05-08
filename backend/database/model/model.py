import os
from flask_moment import Moment
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json
from flask_migrate import Migrate


DB_PATH = 'postgresql://postgres:123@localhost:5432/shop'
db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = DB_PATH
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    moment = Moment(app)
    db.app = app
    migrate = Migrate(app,db)
    db.init_app(app)

class Seller(db.Model):
    id = Column(Integer, primary_key=True)
    name =  Column(String)
    product = Column(String)
    product_type = Column(String)
    product_description = Column(String)
    product_image = Column(String(500))
    phone_number = Column(Integer)
    buyer_id = Column(Integer, db.ForeignKey('buyer.id'), nullable=True)

    def format_seller(self):
        return {
            'id': self.id,
            'name': self.name,
            'product': self.product,
            'type': self.product_type,
            'description': self.product_description,
            'image': self.product_image,
            'number': self.phone_number
        }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

class Buyer(db.Model):
    id = Column(Integer, primary_key=True)
    name =  Column(String)
    sellers = db.relationship('Seller')
    def insert(self):
        db.session.add(self)
        db.session.commit()




