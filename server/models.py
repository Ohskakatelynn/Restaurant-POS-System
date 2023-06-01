from sqlalchemy_serializer import SerializerMixin
from config import db
from sqlalchemy.orm import validates


class User(SerializerMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


class Product(SerializerMixin, db.Model):
    __tablename__ = 'products'
    serialize_rules = ('-toppings',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    set_toppings = db.Column(db.String)
    custom = db.Column(db.String)

    toppings = db.relationship('ProductWithTopping', back_populates='product')


class Topping(SerializerMixin, db.Model):
    __tablename__ = 'toppings'
    serialize_rules = ('-products', '-sides')
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    sides = db.relationship('SideWithTopping', back_populates='topping')
    products = db.relationship('ProductWithTopping', back_populates='topping')


class ProductWithTopping(SerializerMixin, db.Model):
    __tablename__ = 'productwithtoppings'
    serialize_rules = ('-products', '-toppings')
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    topping_id = db.Column(db.Integer, db.ForeignKey('toppings.id'), nullable=False)

    product = db.relationship('Product', back_populates='toppings')
    topping = db.relationship('Topping', back_populates='products')


class Side(SerializerMixin, db.Model):
    __tablename__ = 'sides'
    serialize_rules = ('-side_with_toppings',)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    set_toppings = db.Column(db.String)
    custom = db.Column(db.String)

    side_with_toppings = db.relationship('SideWithTopping', back_populates='side')


class SideWithTopping(SerializerMixin, db.Model):
    __tablename__ = 'sidewithtoppings'
    id = db.Column(db.Integer, primary_key=True)
    side_id = db.Column(db.Integer, db.ForeignKey('sides.id'), nullable=False)
    topping_id = db.Column(db.Integer, db.ForeignKey('toppings.id'), nullable=False)

    side = db.relationship('Side', back_populates='side_with_toppings')
    topping = db.relationship('Topping', back_populates='sides')



class OrderItem(SerializerMixin, db.Model):
    __tablename__ = 'order_items'
    serialize_rules = ('-side_with_toppings','-product_with_toppings', '-orders')
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_with_topping_id = db.Column(db.Integer, db.ForeignKey('productwithtoppings.id'), nullable=False)
    side_with_topping_id = db.Column(db.Integer, db.ForeignKey('sidewithtoppings.id'), nullable=False)
    mealprice = db.Column(db.Integer)
    status = db.Column(db.Boolean)

    product_with_topping = db.relationship('ProductWithTopping')
    side_with_topping = db.relationship('SideWithTopping')



class TicketNumber(SerializerMixin, db.Model):
    __tablename__ = 'ticketnumbers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Order(SerializerMixin, db.Model):
    __tablename__ = 'orders'
    serialize_rules = ('-order_item',)
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    ticket_number_id = db.Column(db.Integer, db.ForeignKey('ticketnumbers.id'), nullable=False)
    total_price = db.Column(db.Numeric, nullable=False)
    order_item = db.relationship('OrderItem', backref='order', lazy='dynamic')
    payment_id = db.Column(db.Integer, db.ForeignKey('payments.id'))
    payment = db.relationship('Payment', backref='order', foreign_keys=[payment_id])


class Payment(SerializerMixin, db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    amount = db.Column(db.Numeric, nullable=False)
    long_card_number = db.Column(db.String, nullable=False)
    card_number = db.Column(db.String, nullable=False)
    full_name = db.Column(db.String, nullable=False)

    @validates('long_card_number')
    def validate_long_card_number(self, key, long_card_number):
        long_card_number_str = str(long_card_number)
        if len(long_card_number_str) != 16:
            raise ValueError('Card number must be 16 digits')
        return long_card_number

    @validates('card_number')
    def validate_card_number(self, key, card_number):
        card_number_str = str(card_number)
        if len(card_number_str) != 3:
            raise ValueError('Number must be 3 digits')
        return card_number


class Drink(SerializerMixin, db.Model):
    __tablename__ = 'drinks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Numeric, nullable=False)
    alcoholic = db.Column(db.Boolean, nullable=False)