from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from models import db
from resources.books import BookList, BookDetail
from resources.review import ReviewList, ReviewDetail
from resources.user import UserList, UserDetail
from resources.favorites import AddFavorite, RemoveFavorite

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db.init_app(app)

CORS(app, supports_credentials=True)
cors = CORS(app, resources={
    r"/api/*": {"origins": "http://localhost:3000"},
    r"/users/*": {"origins": "http://localhost:3000"},
    r"/users/<int:user_id>/favorites/<int:book_id>": {"origins": "http://localhost:3000"},
    r"/users/<int:user_id>/favorites/<int:book_id>": {"origins": "http://localhost:3000"}
})


migrate = Migrate(app, db)

api = Api(app)




@app.route('/')
def home():
    return "<h1>Library API</h1>"

api.add_resource(BookList, '/books')
api.add_resource(BookDetail, '/books/<int:book_id>')

api.add_resource(ReviewList, '/reviews')
api.add_resource(ReviewDetail, '/reviews/<int:review_id>')

api.add_resource(UserList, '/users')
api.add_resource(UserDetail, '/users/<int:user_id>')

api.add_resource(AddFavorite, '/user/<int:user_id>/favorites/<int:book_id>')
api.add_resource(RemoveFavorite, '/users/<int:user_id>/favorites/<int:book_id>')




if __name__ == "__main__":
    app.run(debug=True)
