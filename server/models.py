from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from config import db
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

class User(SerializerMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Product(SerializerMixin, db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    custom = db.Column(db.String)
    
    toppings = db.relationship('Topping', backref='product')
    order_items = db.relationship('OrderItem', backref='product')




class Topping(SerializerMixin, db.Model):
    __tablename__ = 'toppings'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)




class Order(SerializerMixin, db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Numeric, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    order_items = db.relationship('OrderItem', backref='order')
    user = db.relationship('User')




class OrderItem(SerializerMixin, db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric, nullable=False)




class Payment(SerializerMixin, db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
