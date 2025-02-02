from flask import request
from flask_restful import Resource
from models import db, User, Book

class AddFavorite(Resource):
      def post(self, user_id, book_id):
        user = User.query.get(user_id)
        book = Book.query.get(book_id)
        if not user or not book:
            return {'error': 'User or Book not found'}, 404
        user.favorites.append(book)
        db.session.commit()
        return {'message': 'Book added to favorites'}, 200

class RemoveFavorite(Resource):
    def delete(self, user_id, book_id):
        user = User.query.get(user_id)
        book = Book.query.get(book_id)
        if not user or not book:
            return {'message': 'User or Book not found'}, 404
        if book not in user.favorites:
            return {'message': 'Book not in favorites'}, 400
        user.favorites.remove(book)
        db.session.commit()
        return {'message': 'Book removed from favorites'}, 200

