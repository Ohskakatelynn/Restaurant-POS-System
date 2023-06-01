#!/usr/bin/env python3
from flask import request, make_response
from flask_restful import Resource
from config import app, db, api
from models import User, Product, Topping, ProductWithTopping, Order, OrderItem, Payment, Drink, Side, SideWithTopping, TicketNumber


class Users(Resource):
    def get(self):
        u_list = [u.to_dict() for u in User.query.all()]
        if len(u_list) == 0:
            return make_response({'error': 'no users'}, 404)
        return make_response(u_list, 200)
    
    def post (self):
        data = request.get_json()
        newUser = User(
            username= data["username"],
            password= data["password"],
            )
        try:
            db.session.add(newUser)
            db.session.commit()
            return make_response (newUser.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            u = User.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(u, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no user'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(u)
            db.session.commit()
        
        return make_response(u.to_dict(), 200)
    
    def delete(self, id):
        u = User.query.filter_by(id = id).first()
        db.session.delete(u)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "User deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(Users, '/users')


class Products(Resource):
    def get(self):
        p_list = [p.to_dict() for p in Product.query.all()]
        if len(p_list) == 0:
            return make_response({'error': 'no products'}, 404)
        return make_response(p_list, 200)
    
    def post (self):
        data = request.get_json()
        newProduct = Product(
            name= data["name"],
            price = data["price"],
            )
        try:
            db.session.add(newProduct)
            db.session.commit()
            return make_response (newProduct.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            p = Product.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(p, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no product'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(p)
            db.session.commit()
        
        return make_response(p.to_dict(), 200)
    
    def delete(self, id):
        p = Product.query.filter_by(id = id).first()
        db.session.delete(p)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Product deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(Products, '/products')


class ProductsById(Resource):
    def get(self, id):
        p = Product.query.filter_by(id = id).first()
        if p == None:
            return make_response({'error': 'no Products'}, 404)
        return make_response(p.to_dict(), 200)
    def delete(self, id):
        p = Product.query.filter_by(id = id).first()
        db.session.delete(p)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Product deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
    def patch(self, id):
        try:
            p = Product.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(p, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no product'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(p)
            db.session.commit()
        
        return make_response(o.to_dict(), 200)
    
api.add_resource(ProductsById, '/products/<int:id>')


class Toppings(Resource):
    def get(self):
        t_list = [t.to_dict() for t in Topping.query.all()]
        if len(t_list) == 0:
            return make_response({'error': 'no toppings'}, 404)
        return make_response(t_list, 200)
    
    def post (self):
        data = request.get_json()
        newTopping = Topping(
            name= data["name"],
            )
        try:
            db.session.add(newTopping)
            db.session.commit()
            return make_response (newTopping.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            t = Topping.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(t, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no topping'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(t)
            db.session.commit()
        
        return make_response(t.to_dict(), 200)
    
    def delete(self, id):
        t = Topping.query.filter_by(id = id).first()
        db.session.delete(t)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Topping deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(Toppings, '/toppings')


class ToppingsById(Resource):
    def get(self, id):
        t = Topping.query.filter_by(id = id).first()
        if t == None:
            return make_response({'error': 'no Toppings'}, 404)
        return make_response(t.to_dict(), 200)
    def delete(self, id):
        t = Topping.query.filter_by(id = id).first()
        db.session.delete(t)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Topping deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
    def patch(self, id):
        try:
            t = Topping.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(t, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no topping'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(t)
            db.session.commit()
        
        return make_response(t.to_dict(), 200)
    
api.add_resource(ToppingsById, '/toppings/<int:id>')


class ProductWithToppings(Resource):
    def get(self):
        pwt_list = [pwt.to_dict() for pwt in ProductWithTopping.query.all()]
        if len(pwt_list) == 0:
            return make_response({'error': 'no products with toppings'}, 404)
        return make_response(pwt_list, 200)
    
    def post (self):
        data = request.get_json()
        newProductWithToppings = ProductWithTopping(
            product_id= data["product.id"],
            topping_id = data["topping.id"],
            )
        try:
            db.session.add(newProductWithToppings)
            db.session.commit()
            return make_response (newProductWithToppings.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            pwt = ProductWithTopping.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(pwt, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no product with toppings'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(pwt)
            db.session.commit()
        
        return make_response(pwt.to_dict(), 200)
    
    def delete(self, id):
        pwt = ProductWithTopping.query.filter_by(id = id).first()
        db.session.delete(pwt)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Product with topping deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(ProductWithToppings, '/productwithtoppings')


class ProductsWithToppingsById(Resource):
    def get(self, id):
        pwt = ProductWithTopping.query.filter_by(id = id).first()
        if pwt == None:
            return make_response({'error': 'no Products With Toppings'}, 404)
        return make_response(pwt.to_dict(), 200)
    def delete(self, id):
        pwt = ProductWithTopping.query.filter_by(id = id).first()
        db.session.delete(pwt)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Product With Topping deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
    def patch(self, id):
        try:
            pwt = ProductWithTopping.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(pwt, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no product with toppings'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(pwt)
            db.session.commit()
        
        return make_response(pwt.to_dict(), 200)
    
api.add_resource(ProductsWithToppingsById, '/productwithtoppings/<int:id>')


class OrderItems(Resource):
    def get(self):
        oi_list = [oi.to_dict() for oi in OrderItem.query.all()]
        if len(oi_list) == 0:
            return make_response({'error': 'no orderitems'}, 404)
        return make_response(oi_list, 200)
    
    def post (self):
        data = request.get_json()
        newOrderItems = OrderItem(
            order_id= data["orders.id"],
            productwithtopping_id = data["productwithtoppings.id"],
            sidewithtopping_id = data["sidewithtoppings.id"],
            quantity= data["quantity"]
            )
        try:
            db.session.add(newOrderItems)
            db.session.commit()
            return make_response (newOrderItems.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            oi = OrderItem.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(oi, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no orderitems'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(oi)
            db.session.commit()
        
        return make_response(oi.to_dict(), 200)
    
    def delete(self, id):
        oi = OrderItem.query.filter_by(id = id).first()
        db.session.delete(oi)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "OrderItem deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(OrderItems, '/orderitems')


class OrderItemsById(Resource):
    def get(self, id):
        o = OrderItem.query.filter_by(id = id).first()
        if o == None:
            return make_response({'error': 'no Orderitems'}, 404)
        return make_response(t.to_dict(), 200)
    def delete(self, id):
        o = OrderItem.query.filter_by(id = id).first()
        db.session.delete(o)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Orderitem deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
    def patch(self, id):
        try:
            o = OrderItem.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(o, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no orderitem'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(o)
            db.session.commit()
        
        return make_response(t.to_dict(), 200)
    
api.add_resource(OrderItemsById, '/orders/<int:id>')


class Orders(Resource):
    def get(self):
        o_list = [o.to_dict() for o in Order.query.all()]
        if len(o_list) == 0:
            return make_response({'error': 'no orders'}, 404)
        return make_response(o_list, 200)
    
    def post (self):
        data = request.get_json()
        newOrders = Order(
            total_amount= data["total_amount"],
            users_id = data["users.id"],
            status= data["status"]
            )
        try:
            db.session.add(newOrders)
            db.session.commit()
            return make_response (newOrders.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            o = Order.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(o, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no orders'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(o)
            db.session.commit()
        
        return make_response(o.to_dict(), 200)
    
    def delete(self, id):
        o = Order.query.filter_by(id = id).first()
        db.session.delete(o)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Order deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(Orders, '/orders')


class OrdersById(Resource):
    def get(self, id):
        o = Order.query.filter_by(id = id).first()
        if o == None:
            return make_response({'error': 'no Orders'}, 404)
        return make_response(o.to_dict(), 200)
    def delete(self, id):
        o = Order.query.filter_by(id = id).first()
        db.session.delete(o)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Order deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
    def patch(self, id):
        try:
            o = Order.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(o, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no order'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(o)
            db.session.commit()
        
        return make_response(o.to_dict(), 200)
    
api.add_resource(OrdersById, '/orders/<int:id>')


class Sides(Resource):
    def get(self):
        s_list = [s.to_dict() for s in Side.query.all()]
        if len(s_list) == 0:
            return make_response({'error': 'no sides'}, 404)
        return make_response(s_list, 200)
    
    def post (self):
        data = request.get_json()
        newSide = Side(
            name= data["name"],
            price= data["price"],
            )
        try:
            db.session.add(newSide)
            db.session.commit()
            return make_response (newSide.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            s = Side.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(s, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no side'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(s)
            db.session.commit()
        
        return make_response(s.to_dict(), 200)
    
    def delete(self, id):
        s = Side.query.filter_by(id = id).first()
        db.session.delete(s)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Side deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(Sides, '/sides')


class SidesById(Resource):
    def get(self, id):
        s = Side.query.filter_by(id = id).first()
        if s == None:
            return make_response({'error': 'no Sides'}, 404)
        return make_response(t.to_dict(), 200)
    def delete(self, id):
        s = Side.query.filter_by(id = id).first()
        db.session.delete(s)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Side deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
    def patch(self, id):
        try:
            s = Side.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(s, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no side'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(s)
            db.session.commit()
        
        return make_response(s.to_dict(), 200)
    
api.add_resource(SidesById, '/sides/<int:id>')


class SideWithToppings(Resource):
    def get(self):
        swt_list = [swt.to_dict() for swt in SideWithTopping.query.all()]
        if len(swt_list) == 0:
            return make_response({'error': 'no sides with toppings'}, 404)
        return make_response(swt_list, 200)
    
    def post (self):
        data = request.get_json()
        newSideWithToppings = SideWithTopping(
            side_id= data["side.id"],
            topping_id = data["topping.id"],
            )
        try:
            db.session.add(newSideWithToppings)
            db.session.commit()
            return make_response (newSideWithToppings.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            swt = SideWithTopping.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(swt, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no side with toppings'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(swt)
            db.session.commit()
        
        return make_response(swt.to_dict(), 200)
    
    def delete(self, id):
        swt = SideWithTopping.query.filter_by(id = id).first()
        db.session.delete(swt)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Side with topping deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(SideWithToppings, '/sidewithtoppings')


class SidesWithToppingsById(Resource):
    def get(self, id):
        swt = SideWithTopping.query.filter_by(id = id).first()
        if swt == None:
            return make_response({'error': 'no Sides With Toppings'}, 404)
        return make_response(swt.to_dict(), 200)
    def delete(self, id):
        swt = SideWithTopping.query.filter_by(id = id).first()
        db.session.delete(swt)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Side With Topping deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
    def patch(self, id):
        try:
            swt = SideWithTopping.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(swt, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no side with toppings'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(swt)
            db.session.commit()
        
        return make_response(swt.to_dict(), 200)
    
api.add_resource(SidesWithToppingsById, '/sidewithtoppings/<int:id>')


class Drinks(Resource):
    def get(self):
        d_list = [d.to_dict() for d in Drink.query.all()]
        if len(d_list) == 0:
            return make_response({'error': 'no drinks'}, 404)
        return make_response(d_list, 200)
    
    def post (self):
        data = request.get_json()
        newDrink = Drink(
            name= data["name"],
            price = data["price"],
            alcoholic = data["alcoholic"]
            )
        try:
            db.session.add(newDrink)
            db.session.commit()
            return make_response (newDrink.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            d = Drink.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(d, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no drink'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(d)
            db.session.commit()
        
        return make_response(d.to_dict(), 200)
    
    def delete(self, id):
        d = Drink.query.filter_by(id = id).first()
        db.session.delete(d)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Drink deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(Drinks, '/drinks')


class DrinksById(Resource):
    def get(self, id):
        d = Drink.query.filter_by(id = id).first()
        if d == None:
            return make_response({'error': 'no Drinks'}, 404)
        return make_response(d.to_dict(), 200)
    def delete(self, id):
        d = Drink.query.filter_by(id = id).first()
        db.session.delete(d)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Drink deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
    def patch(self, id):
        try:
            d = Drink.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(d, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no drink'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(d)
            db.session.commit()
        
        return make_response(d.to_dict(), 200)
    
api.add_resource(DrinksById, '/drinks/<int:id>')


class TicketNumbers(Resource):
    def get(self):
        t_list = [t.to_dict() for t in TicketNumber.query.all()]
        if len(t_list) == 0:
            return make_response({'error': 'no tickets'}, 404)
        return make_response(t_list, 200)
    
    def post (self):
        data = request.get_json()
        newTicketNumber = TicketNumber(
            name= data["name"],
            )
        try:
            db.session.add(newTicketNumber)
            db.session.commit()
            return make_response (newTicketNumber.to_dict(), 200)
        except Exception as e:
            db.session.rollback()
            return make_response({'error': f'{repr(e)}'}, 422)
        
    def patch(self, id):
        try:
            t = TicketNumber.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(t, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no ticketnumber'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(t)
            db.session.commit()
        
        return make_response(t.to_dict(), 200)
    
    def delete(self, id):
        t = TicketNumber.query.filter_by(id = id).first()
        db.session.delete(t)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "TicketNumber deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
        
api.add_resource(TicketNumbers, '/ticketnumbers')


class TicketNumbersById(Resource):
    def get(self, id):
        t = TicketNumbers.query.filter_by(id = id).first()
        if t == None:
            return make_response({'error': 'no ticket numbers'}, 404)
        return make_response(t.to_dict(), 200)
    def delete(self, id):
        t = TicketNumber.query.filter_by(id = id).first()
        db.session.delete(t)
        db.session.commit()
        response_body = {
            "deleted successfully": True,
            "message": "Ticket number deleted successfully"
        }
        response = make_response(
            response_body,
            202
        )
        return response
    def patch(self, id):
        try:
            t = TicketNumber.query.filter_by(id = id).first()

            for attr in request.get_json():
                setattr(t, attr, request.get_json()[attr])
        except:
            response_body = {
                'error': 'no ticket number'
            }
            return make_response( response_body, 404 )
        else:
            db.session.add(t)
            db.session.commit()
        
        return make_response(t.to_dict(), 200)
    
api.add_resource(TicketNumbersById, '/ticketnumbers/<int:id>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)