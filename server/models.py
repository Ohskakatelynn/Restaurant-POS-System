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
    serialize_rules = ('-toppings',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    set_toppings= db.Column(db.String)
    custom = db.Column(db.String)

    toppings = db.relationship('ProductWithTopping', back_populates='product')


class Topping(SerializerMixin, db.Model):
    __tablename__ = 'toppings'
    serialize_rules = ('-products',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    products = db.relationship('ProductWithTopping', back_populates='topping')

class ProductWithTopping(SerializerMixin, db.Model):
    __tablename__ = 'productwithtoppings'

    id= db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    topping_id= db.Column(db.Integer, db.ForeignKey('toppings.id'), nullable=False)

    product = db.relationship('Product', back_populates='toppings')
    topping = db.relationship('Topping', back_populates='products')

class Order(SerializerMixin, db.Model):
    __tablename__ = 'orders'
    serialize_rules = ('-order_items',)
    id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Numeric, nullable=False)
    #created_at = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    
    order_items = db.relationship('OrderItem', backref='order')
    user = db.relationship('User')



class OrderItem(SerializerMixin, db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    productwithtopping_id = db.Column(db.Integer, db.ForeignKey('productwithtoppings.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    # unit_price = db.Column(db.Numeric, nullable=False)



class Payment(SerializerMixin, db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
    longcardnumber= db.Column(db.Numeric, nullable=False)
    cardnumber= db.Column(db.Numeric, nullable=False)
    full_name= db.Column(db.String, nullable=False)

    @validates('longcardnumber')
    def validates_pay(self, key, longcardnumber):
        longcardnumber_str = str(longcardnumber)
        if len(longcardnumber_str) != 16:
            raise ValueError('Card number must be 16 digits')
        return longcardnumber
    
    @validates('cardnumber')
    def validates_pay(self, key, cardnumber):
        cardnumber_str = str(cardnumber)
        if len(cardnumber_str) != 3:
            raise ValueError('Number must be 3 digits')
        return cardnumber