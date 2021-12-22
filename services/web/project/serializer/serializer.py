from marshmallow import fields, post_load
from flask_marshmallow import Marshmallow
from project.model.model import User, Grade, Student

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class UserSchema(ma.Schema):
    class Meta:
        model = User

    email = fields.Email(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


class GradeSchema(ma.Schema):
    class Meta:
        model = Grade

    grade_id = fields.Integer(dump_only=True)
    grade_name = fields.Str(required=True)
    created_updated_at = fields.Date(dump_only=True)

    @post_load
    def make_grade(self, data, **kwargs):
        return Grade(**data)


class GradeSchemaUpdate(GradeSchema):
    grade_id = fields.Integer(required=True)


class StudentSchema(ma.Schema):
    class Meta:
        model = Student
        load_instance = False

    student_id = fields.Integer(dump_only=True)
    grade_id = fields.Integer(required=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    age = fields.Integer(required=True)
    created_updated_at = fields.Date(dump_only=True)

    @post_load
    def make_student(self, data, **kwargs):
        return Student(**data)


class StudentSchemaUpdate(StudentSchema):
    student_id = fields.Integer(required=True)
