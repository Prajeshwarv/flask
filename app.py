from flask import Flask, Blueprint, jsonify
from flask_cors import CORS

from books.bookRoutes import book_routes 
from DBconnection import connection



# APP setup

def create_app():
    web_app = Flask(__name__)  # Initialize Flask App
    CORS(web_app)

    api_blueprint = Blueprint('api_blueprint', __name__)
    api_blueprint = book_routes(api_blueprint)

    web_app.register_blueprint(api_blueprint, url_prefix='/book')

    return web_app


app = create_app()






if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
