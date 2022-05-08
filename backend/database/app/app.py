from logging import exception
from database.auth.auth import AuthError, requires_auth
from database.model.model import Seller, Buyer, setup_db
import os
from flask import Flask, request, jsonify, abort
from flask_cors import CORS

app = Flask(__name__)
def format(getting_seller_info):
    sellers = [seller.format_seller() for seller in getting_seller_info]
    return sellers

def format_seller(seller):
        return seller.format_seller()


def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def index():
        return "hello"
    @app.route('/home')
    def get_sellers_info():
        all_sellers = Seller.query.order_by(Seller.id).all()
        sellers = format(all_sellers)
        return jsonify({
            'sellers': sellers
        }), 200


    @app.route('/home/<id>')
    @requires_auth('get:product')
    def get_seller_info(token,id):
        seller = Seller.query.filter(Seller.id == id).one_or_none()
        if seller is None:
            abort(404)
        seller_info = format_seller(seller)
        return jsonify({
            'sellers': seller_info
        }), 200


    @app.route('/create', methods=['POST'])
    @requires_auth('post:product')
    def create_seller(token):
        data = request.form
        try:
            seller_data = Seller(name=data['name'],product=data['product'],product_type=data['type'],product_description=data['description'],product_image=data['image'],phone_number=data['phone'])
            seller_data.insert()
            return jsonify({
            "success": "true"
            })
        except:
            abort(422)
        
    @app.route('/delete/<id>', methods=['DELETE'])
    @requires_auth('delete:product')
    def delete_product(token,id):
            try:
                product = Seller.query.filter(Seller.id== id).one_or_none()
                if product is None:
                    abort(404)
                product.delete()
                return jsonify({
                "success": True 
                })

            except:
                abort(400)


    
    @app.route('/edit/<id>', methods=["PATCH"])
    @requires_auth('patch:product')
    def edit_product(token,id):
        data = request.form
        try:
            seller = Seller.query.filter(Seller.id == id).one_or_none()
            if seller is None:
                abort(404)
            seller.name = data['name']
            seller.product = data['product']
            seller.product_type = data['type']
            seller.product_description = data['description']
            seller.product_image = data['image']
            seller.phone_number = data['phone']
            seller.update()
            return jsonify({
                "success": True 
                })

        except:
            abort(400)

    @app.errorhandler(AuthError)
    def auth_error(e):
        return jsonify(e.error), e.status_code

    app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422


    @app.errorhandler(404)  
    def not_found(error):
            return (
                jsonify({"success": False, "error": 404, "message": "resource not found"}),
                404,
            )



    @app.errorhandler(400)  
    def Bad_Request(error):
            return (
                jsonify({"success": False, "error": 400, "message": "Bad Request"}),
                400,
            )


    if __name__ == '__main__':
        app.run()
    return app