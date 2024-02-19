from api import fields, api, ma 
from marshmallow import Schema, fields
from flask_restx import Api,Resource,Namespace, fields

ns = Namespace('social-media')
api.add_namespace(ns)


#---------------------------API_MODELS------------------#


user_schema = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The username of the user'),
})

friendship_schema = api.model('Friendship', {
    'id': fields.Integer(readOnly=True, description='The friendship unique identifier'),
    'user_id': fields.Integer(required=True, description='The user identifier'),
    'friend_id': fields.Integer(required=True, description='The friend identifier'),
})

follow_schema = api.model('Follow', {
    'id': fields.Integer(readOnly=True, description='The follow unique identifier'),
    'follower_id': fields.Integer(required=True, description='The follower identifier'),
    'followed_id': fields.Integer(required=True, description='The followed identifier'),
})
