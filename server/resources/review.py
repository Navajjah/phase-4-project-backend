from flask_restful import Resource
from flask import request
from models import db, Review


class ReviewList(Resource):
    def get(self):
        reviews = Review.query.all()
        return [review.to_dict() for review in reviews]
    
    def post(self):
        data = request.get_json()

        if not all(key in data for key in ['content', 'rating', 'book_id', 'user_id']):
            return {'message': 'Missing required fields'}, 422
        
        
        if not isinstance(data['rating'], (int, float)) or not (1 <= data['rating'] <= 5):
            return {'message': 'Rating must be a number between 1 and 5'}, 400

        new_review = Review(
            content=data['content'],
            rating=data['rating'],
            book_id=data['book_id'],
            user_id=data['user_id']  
        )
        db.session.add(new_review)
        db.session.commit()
        return new_review.to_dict(), 201  

class ReviewDetail(Resource):
    def get(self, review_id):
        review = Review.query.get(review_id)
        if not review:
            return {'message': 'Review not found'}, 404
        return review.to_dict(), 200

    def patch(self, review_id):
        data = request.get_json()
        review = Review.query.get(review_id)
        if not review:
            return {'message': 'Review not found'}, 404

        if 'content' in data:
            review.content = data['content']
        if 'rating' in data:
            review.rating = data['rating']
        if 'book_id' in data:
            review.book_id = data['book_id']
        db.session.commit()
        return review.to_dict(), 200  
    
    def delete(self, review_id):
        review = Review.query.get(review_id)
        if not review:
            return {'message': 'Review not found'}, 404
        db.session.delete(review)
        db.session.commit()
        return {'message': 'Review deleted'}, 200
