from flask_restful import Resource
from flask import request 
from models import User,db

class UserList(Resource):
    def get(self):
        users = User.query.all()
        return [user.to_dict() for user in users]
    
    def post(self):
        data = request.get_json()
        if not data.get('username'):
            return {'message': 'Please provide a username'}, 400
        
        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user:
            return {'message': 'Username already exists'}, 400
        new_user = User(username=data['username'])
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict(), 201
    
class UserDetail(Resource):
        def get(self, user_id):
            user = User.query.get(user_id)
            if not user:
                return {'message': 'User not found'}, 404
            return user.to_dict()
        
        def put(self, user_id):
            user = User.query.get(user_id)
            if not user:
                return {'message': 'User not found'}, 404
            
            data = request.get_json()
            if 'username' in data:
                existing_user = User.query.filter_by(username=data['username']).first()
                if existing_user and existing_user.id != user.id:
                    return {'message': 'Username already exists'}, 400
                user.username = data['username']
            db.session.commit()
            return user.to_dict(), 200
        
        def delete(self, user_id):
            user = User.query.get(user_id)
            if not user:
                return {'message': 'User not found'}, 404
            db.session.delete(user)
            db.session.commit()
            return {'message': 'User has been deleted successfully!'}, 200
    
