from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256
import datetime
from sqlalchemy.sql import func

db = SQLAlchemy()


def configure(app):
    db.init_app(app)
    app.db = db


class User(db.Model):
    __tablename__ = "users"

    def __init__(self, email, username, password, **kwargs):
        super(User, self).__init__(**kwargs)
        self.email = email
        self.username = username
        self.password = password

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def gen_hash(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)


class Grade(db.Model):
    __tablename__ = "grade"
    grade_id = db.Column(db.Integer, primary_key=True)
    grade_name = db.Column(db.String(30), unique=True)
    created_updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=func.now()
    )


class Student(db.Model):
    __tablename__ = "student"
    student_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    grade_id = db.Column(db.Integer, db.ForeignKey("grade.grade_id"))
    grade = db.relationship(
        "Grade", backref="students", lazy="select", cascade="all, delete"
    )
    created_updated_at = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, onupdate=func.now()
    )
