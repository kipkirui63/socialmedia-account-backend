
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, UniqueConstraint, ForeignKey


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable = False)



     # Define relationships
    friendships = db.relationship('Friendship', back_populates='user', lazy=True)
    followers = db.relationship('Follow', foreign_keys='Follow.followed_id', 
                                back_populates='followed', lazy=True)
    following = db.relationship('Follow', foreign_keys='Follow.follower_id', 
                                back_populates='follower', lazy=True)

    # Association proxies
    friends = association_proxy('friendships', 'friend')
    followers_names = association_proxy('followers', 'follower.name')
    following_names = association_proxy('following', 'followed.name')



class Friendship(db.Model):
    __tablename__ = 'friendships'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    friend_id = db.Column(db.Integer,nullable = False)


    user = db.relationship('User', back_populates='friendships')
    friend = db.relationship('User')

    __table_args__ = (
        UniqueConstraint('user_id' , name='user_unique_constraint'),
        UniqueConstraint('friend_id', name='friend_unique_constraint')
    )




class Follow(db.Model):
    __tablename__ = 'follows'

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)


    follower = db.relationship('User', back_populates='following', foreign_keys=[follower_id])
    followed = db.relationship('User', back_populates='followers', foreign_keys=[followed_id])



    __table_args__ = (
        UniqueConstraint('follower_id', name='follower_unique_constraint'),
        UniqueConstraint('followed_id', name='followed_unique_constraint')
    )






