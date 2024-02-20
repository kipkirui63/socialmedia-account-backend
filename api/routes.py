from flask import request, jsonify
from flask_restx import Resource, Namespace
from api import app, api
from .api_models import *
from .models import *


ns_user = Namespace('users')
ns_friendship = Namespace('frienships')
ns_follow = Namespace('follows')


api.add_namespace(ns_user)
api.add_namespace(ns_friendship)
api.add_namespace(ns_follow)


@ns_user.route('/')
class UserList(Resource):
    @ns_user.marshal_list_with(user_schema)
    def get(self):
        users = User.query.all()
        return users

    @ns_user.expect(user_schema)
    @ns_user.marshal_with(user_schema, code=201)
    def post(self):
        """Create a new user"""
        data = request.json
        new_user = User(**data)
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201


@ns_user.route('/<int:id>')
@ns_user.response(404, 'User not found')
class UserResource(Resource):
    @ns_user.marshal_with(user_schema)
    def get(self, id):
        """Get a user by ID"""
        user = User.query.get(id)
        if not user:
            ns_user.abort(404, message="User {} doesn't exist".format(id))
        return user

    @ns_user.expect(user_schema)
    @ns_user.marshal_with(user_schema)
    def put(self, id):
        """Update a user by ID"""
        user = User.query.get(id)
        if not user:
            ns_user.abort(404, message="User {} doesn't exist".format(id))
        data = request.json
        user.username = data['username']
        db.session.commit()
        return user

    @ns_user.response(204, 'User deleted')
    def delete(self, id):
        """Delete a user by ID"""
        user = User.query.get(id)
        if not user:
            ns_user.abort(404, message="User {} doesn't exist".format(id))
        db.session.delete(user)
        db.session.commit()
        return '', 204


# Friendship routes
@ns_friendship.route('/')
class FriendshipList(Resource):
    @ns_friendship.marshal_list_with(friendship_schema)
    def get(self):
        """List all friendships"""
        friendships = Friendship.query.all()
        return friendships

    @ns_friendship.expect(friendship_schema)
    @ns_friendship.marshal_with(friendship_schema, code=201)
    def post(self):
        """Create a new friendship"""
        data = request.json
        new_friendship = Friendship(**data)
        db.session.add(new_friendship)
        db.session.commit()
        return new_friendship, 201


@ns_friendship.route('/<int:id>')
@ns_friendship.response(404, 'Friendship not found')
class FriendshipResource(Resource):
    @ns_friendship.marshal_with(friendship_schema)
    def get(self, id):
        """Get a friendship by ID"""
        friendship = Friendship.query.get(id)
        if not friendship:
            ns_friendship.abort(404, message="Friendship {} doesn't exist".format(id))
        return friendship

    @ns_friendship.expect(friendship_schema)
    @ns_friendship.marshal_with(friendship_schema)
    def put(self, id):
        """Update a friendship by ID"""
        friendship = Friendship.query.get(id)
        if not friendship:
            ns_friendship.abort(404, message="Friendship {} doesn't exist".format(id))
        data = request.json
        friendship.user_id = data['user_id']
        friendship.friend_id = data['friend_id']
        db.session.commit()
        return friendship

    @ns_friendship.response(204, 'Friendship deleted')
    def delete(self, id):
        """Delete a friendship by ID"""
        friendship = Friendship.query.get(id)
        if not friendship:
            ns_friendship.abort(404, message="Friendship {} doesn't exist".format(id))
        db.session.delete(friendship)
        db.session.commit()
        return '', 204


# Follow routes
@ns_follow.route('/')
class FollowList(Resource):
    @ns_follow.marshal_list_with(follow_schema)
    def get(self):
        """List all follows"""
        follows = Follow.query.all()
        return follows

    @ns_follow.expect(follow_schema)
    @ns_follow.marshal_with(follow_schema, code=201)
    def post(self):
        """Create a new follow"""
        data = request.json
        new_follow = Follow(**data)
        db.session.add(new_follow)
        db.session.commit()
        return new_follow, 201


@ns_follow.route('/<int:id>')
@ns_follow.response(404, 'Follow not found')
class FollowResource(Resource):
    @ns_follow.marshal_with(follow_schema)
    def get(self, id):
        """Get a follow by ID"""
        follow = Follow.query.get(id)
        if not follow:
            ns_follow.abort(404, message="Follow {} doesn't exist".format(id))
        return follow

    @ns_follow.expect(follow_schema)
    @ns_follow.marshal_with(follow_schema)
    def put(self, id):
        """Update a follow by ID"""
        follow = Follow.query.get(id)
        if not follow:
            ns_follow.abort(404, message="Follow {} doesn't exist".format(id))
        data = request.json
        follow.follower_id = data['follower_id']
        follow.followed_id = data['followed_id']
        db.session.commit()
        return follow

    @ns_follow.response(204, 'Follow deleted')
    def delete(self, id):
        """Delete a follow by ID"""
        follow = Follow.query.get(id)
        if not follow:
            ns_follow.abort(404, message="Follow {} doesn't exist".format(id))
        db.session.delete(follow)
        db.session.commit()
        return '', 204