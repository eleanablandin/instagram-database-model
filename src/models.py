import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250),unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(20), unique=False, nullable=False)

class Profile(Base):
    __tablename__ = 'profile'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,  ForeignKey('user.id'))
    name = Column(String(250), unique=False, nullable=False)
    biography = Column(String, unique=False, nullable=False)
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,  ForeignKey('user.id'))
    description = Column(String(250), unique=False, nullable=False)
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment' 
    id = Column(Integer, primary_key=True)
    post_id =  Column(Integer,  ForeignKey('post.id'))
    autor_id =  Column(Integer, ForeignKey('user.id'))
    commentary = Column(String(250), unique=False, nullable=False)
    post = relationship(Post)
    user = relationship(User)

class Follows(Base):
    __tablename__ = 'follows'
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    followed_id = Column(Integer, ForeignKey('user.id'))
    user = user = relationship(User)


     


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e