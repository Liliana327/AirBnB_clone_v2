#!/usr/bin/python3
''' DatabaseStorage
'''
import os
import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize Method dbs engine
        """
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        connection = "mysql+mysqldb://{}:{}@{}/{}" \
                     .format(user, passwd, host, db)
        self.__engine = create_engine(connection, pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        all dicts
        """
        classes = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
        objs = {}

        if cls is None:
            for class_nm in classes:
                query = self.__session.query(eval(class_nm)).all()
                for obj in query:
                    key = obj.__class__.__name__ + '.' + obj.id
                    objs[key] = obj
        else:
            query = self.__session.query(eval(cls)).all()
            for obj in query:
                key = obj.__class__.__name__ + '.' + obj.id
                objs[key] = obj
        return objs

    def new(self, obj):
        """
        new
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """
        save
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """
        reload
        """
        Base.metadata.create_all(self.__engine)
        maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(maker)

    def close(self):
        """call remove() method on the private session attribute
        """
        self.__session.remove()
