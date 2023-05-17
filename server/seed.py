#!/usr/bin/env python3

from random import randint, choice as rc

# Local imports
from app import app
from models import db, User, Product, Topping, ProductWithTopping, Order, OrderItem, Payment

if __name__ == '__main__':
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

def make_this():
    User.query.delete()
    Product.query.delete()
    Topping.query.delete()
    ProductWithTopping.query.delete()
    Order.query.delete()
    OrderItem.query.delete()
    Payment.query.delete()

    u1= User(username= 'katelynnmorris', password_hash= 'steve123')
    u2= User(username= 'kaydenravia', password_hash= '123steve')

    u= [u1,u2]

    db.session.add_all(u)
    db.session.commit()

    p1= Product(name= 'Onion Ring Burger', price= 14.99)
    p2= Product(name= 'T-Bone Steak', price= 28.99)
    p3= Product(name= 'Boneless Wings', price= 12.99)
    p4= Product(name= 'Fajita Plate', price= 17.99)
    p5= Product(name= 'Spaghetti and Meatballs', price= 13.99)
    p6= Product(name= 'Seafood Pasta', price= 22.99)
    p7= Product(name= 'Chicken Caesar Salad', price= 11.99)
    
    p= [p1, p2, p3, p4, p5, p6, p7]

    db.session.add_all(p)
    db.session.commit()

    t1= Topping(name= 'Ketchup')
    t2= Topping(name= 'Mustard')
    t3= Topping(name= 'Mayonnaise')
    t4= Topping(name= 'Pickles')
    t5= Topping(name= 'Lettuce')
    t6= Topping(name= 'Onions')
    t7= Topping(name= 'Ranch Dressing')
    t8= Topping(name= 'Italian Dressing')
    t9= Topping(name= 'Honey Mustard')
    t10= Topping(name= 'Buffalo Sauce')
    t11= Topping(name= 'Garlic Butter')
    t12= Topping(name= 'Tortillas')
    t13= Topping(name= 'Garlic Toast')
    t14= Topping(name= 'Salsa')
    t15= Topping(name= 'Guacamole')

    t=[t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14, t15]

    db.session.add_all(t)
    db.session.commit()

    pwt1= ProductWithTopping(product_id= p1.id, topping_id= t1.id)
    pwt2= ProductWithTopping(product_id= p1.id, topping_id= t2.id)
    pwt3= ProductWithTopping(product_id= p1.id, topping_id= t3.id)
    pwt4= ProductWithTopping(product_id= p1.id, topping_id= t4.id)
    pwt5= ProductWithTopping(product_id= p1.id, topping_id= t5.id)
    pwt6= ProductWithTopping(product_id= p2.id, topping_id= t11.id)
    pwt7= ProductWithTopping(product_id= p3.id, topping_id= t7.id)
    pwt8= ProductWithTopping(product_id= p4.id, topping_id= t6.id)
    pwt9= ProductWithTopping(product_id= p4.id, topping_id= t12.id)
    pwt10= ProductWithTopping(product_id= p4.id, topping_id= t14.id)
    pwt11= ProductWithTopping(product_id= p4.id, topping_id= t15.id)
    pwt12= ProductWithTopping(product_id= p5.id, topping_id= t13.id)
    pwt13= ProductWithTopping(product_id= p6.id, topping_id= t13.id)
    pwt14= ProductWithTopping(product_id= p7.id, topping_id= t7.id)
    
    pwt=[pwt1, pwt2, pwt3, pwt4, pwt5, pwt6, pwt7, pwt8, pwt9, pwt10, pwt11, pwt12, pwt13, pwt14]

    db.session.add_all(pwt)
    db.session.commit()

    o1 = Order(total_amount= 20, user_id= u1.id, status= True)
    o2 = Order(total_amount= 40, user_id= u2.id, status= False)
    o3 = Order(total_amount= 60, user_id= u1.id, status= True)
    o4 = Order(total_amount= 120, user_id= u2.id, status= False)
    o5 = Order(total_amount= 50, user_id= u2.id, status= False)
    o6 = Order(total_amount= 60, user_id= u2.id, status= False)
    o7 = Order(total_amount= 20, user_id= u1.id, status= False)
    o8 = Order(total_amount= 20, user_id= u1.id, status= True)

    o=[o1, o2, o3, o4, o5, o6, o7, o8]

    db.session.add_all(o)
    db.session.commit()

    oi1= OrderItem(order_id= o1.id, productwithtopping_id= pwt1.id, quantity= 1)
    oi2= OrderItem(order_id= o2.id, productwithtopping_id= pwt2.id, quantity= 2)
    oi3= OrderItem(order_id= o2.id, productwithtopping_id= pwt1.id, quantity= 3)
    oi4= OrderItem(order_id= o3.id, productwithtopping_id= pwt3.id, quantity= 2)
    oi5= OrderItem(order_id= o3.id, productwithtopping_id= pwt7.id, quantity= 1)
    oi6= OrderItem(order_id= o3.id, productwithtopping_id= pwt8.id, quantity= 1)
    oi7= OrderItem(order_id= o4.id, productwithtopping_id= pwt4.id, quantity= 1)
    oi8= OrderItem(order_id= o4.id, productwithtopping_id= pwt8.id, quantity= 1)
    oi9= OrderItem(order_id= o4.id, productwithtopping_id= pwt9.id, quantity= 2)
    oi10= OrderItem(order_id= o4.id, productwithtopping_id= pwt12.id, quantity= 1)
    oi11= OrderItem(order_id= o4.id, productwithtopping_id= pwt1.id, quantity= 2)
    oi12= OrderItem(order_id= o5.id, productwithtopping_id= pwt7.id, quantity= 1)
    oi13= OrderItem(order_id= o5.id, productwithtopping_id= pwt8.id, quantity= 1)
    oi14= OrderItem(order_id= o5.id, productwithtopping_id= pwt9.id, quantity= 1)
    oi15= OrderItem(order_id= o6.id, productwithtopping_id= pwt11.id, quantity= 1)
    oi16= OrderItem(order_id= o7.id, productwithtopping_id= pwt13.id, quantity= 2)
    oi17= OrderItem(order_id= o8.id, productwithtopping_id= pwt14.id, quantity= 4)

    oi= [oi1, oi2, oi3, oi4, oi5, oi6, oi7, oi8, oi9, oi10, oi11, oi12, oi13, oi14, oi15, oi16, oi17]

    db.session.add_all(oi)
    db.session.commit()
    
    
    
    
    


if __name__ == '__main__':
    with app.app_context():
        make_this()  
