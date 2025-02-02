from flask_restful import Resource
from flask import request
from models import db, Book

class BookList(Resource):
    def get(self):
        books = Book.query.all()
        return [book.to_dict() for book in books]
    
    def post(self):
        data = request.get_json()
        if not data or not all(key in data for key in ('title', 'rarity', 'spell_type', 'author', 'hogwarts_class')):
            return {'error': 'Missing required fields'}, 422
        new_book = Book(
            title=data['title'], 
            rarity=data['rarity'], 
            spell_type=data['spell_type'], 
            author=data['author'], 
            hogwarts_class=data['hogwarts_class']
        )
        db.session.add(new_book)
        db.session.commit()
        return new_book.to_dict()
    
class BookDetail(Resource):
    def get(self, book_id):
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book not found'}, 404
        return book.to_dict()
    
    def put(self, book_id):
        data = request.get_json()
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book not found'}, 404
        if 'title' in data:
            book.title = data['title']
        if 'rarity' in data:
            book.rarity = data['rarity']
        if 'spell_type' in data:
            book.spell_type = data['spell_type']
        if 'author' in data:
            book.author = data['author']
        if 'hogwarts_class' in data:
            book.hogwarts_class = data['hogwarts_class']
        db.session.commit()
        return book.to_dict(), 200
      
    def delete(self, book_id):
        book = Book.query.get(book_id)
        if not book:
            return {'message': 'Book not found'}, 404
        db.session.delete(book)
        db.session.commit()
        return {'message':'The magic book has been deleted successfully!'}
        