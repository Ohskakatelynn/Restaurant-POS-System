#!/usr/bin/env python3
from flask import request, make_response
from flask_restful import Resource
from config import app, db, api
from models import User, Product, Topping, ProductWithTopping, Order, OrderItem, Payment


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
            password_hash = data["password_hash"],
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
















if __name__ == '__main__':
    app.run(port=5555, debug=True)


