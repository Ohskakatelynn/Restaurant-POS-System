from random import randint, choice as rc

# Local imports
from app import app
from models import db, User, Product, Topping, ProductWithTopping, SideWithTopping, TicketNumber, Order, OrderItem, Payment, Side, Drink

def make_this():
    User.query.delete()
    Product.query.delete()
    Topping.query.delete()
    ProductWithTopping.query.delete()
    Order.query.delete()
    OrderItem.query.delete()
    Payment.query.delete()
    Side.query.delete()
    db.create_all()

    u1 = User(username='katelynnmorris', password='steve123')
    u2 = User(username='kaydenravia', password='123steve')

    u = [u1, u2]
    db.session.add_all(u)
    db.session.commit()

    p1 = Product(name='Onion Ring Burger', price=14.99)
    p2 = Product(name='T-Bone Steak', price=28.99)
    p3 = Product(name='Boneless Wings', price=12.99)
    p4 = Product(name='Fajita Plate', price=17.99)
    p5 = Product(name='Spaghetti and Meatballs', price=13.99)
    p6 = Product(name='Seafood Pasta', price=22.99)
    p7 = Product(name='Chicken Caesar Salad', price=11.99)

    p = [p1, p2, p3, p4, p5, p6, p7]
    db.session.add_all(p)
    db.session.commit()

    s1 = Side(name='Baked Potato', price='4.99')
    s2 = Side(name='French Fries', price='2.99')
    s3 = Side(name='Onion Rings', price='4.99')
    s4 = Side(name='Spanish Rice', price='2.99')
    s5 = Side(name='Garlic Toast', price='1.99')
    s6 = Side(name='Mashed Potatoes', price='1.99')
    s7 = Side(name='Corn', price='1.99')
    s8 = Side(name='Green Beans', price='1.99')
    s9 = Side(name='Chili', price='2.99')
    s10 = Side(name='Broccoli', price='2.99')
    s11 = Side(name='Asparagus', price='4.99')
    s12 = Side(name='Mac and Cheese', price='2.99')
    s13 = Side(name='Yams', price='1.99')
    s14 = Side(name='Cornbread', price='1.99')

    s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14]
    db.session.add_all(s)
    db.session.commit()

    t1 = Topping(name='Cheese', price='1.00')
    t2 = Topping(name='Bacon', price='1.50')
    t3 = Topping(name='Mushrooms', price='0.75')
    t4 = Topping(name='Onions', price='0.50')
    t5 = Topping(name='Lettuce', price='0.25')
    t6 = Topping(name='Tomatoes', price='0.50')
    t7 = Topping(name='Pickles', price='0.25')

    t = [t1, t2, t3, t4, t5, t6, t7]
    db.session.add_all(t)
    db.session.commit()

    pt1 = ProductWithTopping(product_id=p1.id, topping_id=t1.id)
    pt2 = ProductWithTopping(product_id=p1.id, topping_id=t2.id)
    pt3 = ProductWithTopping(product_id=p1.id, topping_id=t4.id)
    pt4 = ProductWithTopping(product_id=p1.id, topping_id=t5.id)
    pt5 = ProductWithTopping(product_id=p1.id, topping_id=t6.id)
    pt6 = ProductWithTopping(product_id=p2.id, topping_id=t3.id)
    pt7 = ProductWithTopping(product_id=p3.id, topping_id=t4.id)
    pt8 = ProductWithTopping(product_id=p3.id, topping_id=t6.id)
    pt9 = ProductWithTopping(product_id=p4.id, topping_id=t2.id)
    pt10 = ProductWithTopping(product_id=p4.id, topping_id=t3.id)

    pt = [pt1, pt2, pt3, pt4, pt5, pt6, pt7, pt8, pt9, pt10]
    db.session.add_all(pt)
    db.session.commit()

    sn1 = SideWithTopping(side_id=s1.id, topping_id=t1.id)
    sn2 = SideWithTopping(side_id=s1.id, topping_id=t2.id)
    sn3 = SideWithTopping(side_id=s2.id, topping_id=t4.id)
    sn4 = SideWithTopping(side_id=s3.id, topping_id=t5.id)
    sn5 = SideWithTopping(side_id=s4.id, topping_id=t6.id)

    sn = [sn1, sn2, sn3, sn4, sn5]
    db.session.add_all(sn)
    db.session.commit()

    o1 = Order(user_id=u1.id, ticket_number_id=1, payment_id=1, total_price= 50)
    o2 = Order(user_id=u2.id, ticket_number_id=2, payment_id=2, total_price= 60)

    o = [o1, o2]
    db.session.add_all(o)
    db.session.commit()

    order_items = []

    order1 = OrderItem(order_id=o1.id, product_with_topping_id=p1.id, side_with_topping_id=sn1.id)
    order_items.append(order1)

    order2 = OrderItem(order_id=o1.id, product_with_topping_id=p3.id, side_with_topping_id=sn3.id)
    order_items.append(order2)

    order3 = OrderItem(order_id=o2.id, product_with_topping_id=p2.id, side_with_topping_id=sn2.id)
    order_items.append(order3)

    order4 = OrderItem(order_id=o2.id, product_with_topping_id=p4.id, side_with_topping_id=sn4.id)
    order_items.append(order4)

    for order_item in order_items:
        db.session.add(order_item)

    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        make_this()  