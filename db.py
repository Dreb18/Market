from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from sqlalchemy import orm
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


def create_db(app):
    db = SQLAlchemy(app)

    class Product(db.Model, UserMixin):
        __tablename__ = 'Product'
        id = sqlalchemy.Column(sqlalchemy.Integer,
                            primary_key=True, autoincrement=True)
        image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        price = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        info = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        url = sqlalchemy.Column(sqlalchemy.String, nullable=True)
        brand = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    db.create_all()

