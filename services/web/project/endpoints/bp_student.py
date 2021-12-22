from flask import Blueprint, request, current_app, jsonify
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from project.serializer.serializer import StudentSchema, StudentSchemaUpdate
from project.model.model import Student

bp_student = Blueprint("student", __name__)


@bp_student.route("/student/", methods=["GET"])
@jwt_required()
def listOneAll():
    sSchema = StudentSchema(many=True)

    s_name = request.args.get("name")
    s_email = request.args.get("email")
    s_age = request.args.get("age")
    s_grade = request.args.get("grade")
    s_student_id = request.args.get("student_id")

    if s_student_id:
        result = Student.query.filter(Student.student_id == s_student_id).all()
    elif s_name:
        result = Student.query.filter(Student.name == s_name)
    elif s_email:
        result = Student.query.filter(Student.email == s_email)
    elif s_age:
        result = Student.query.filter(Student.age == s_age)
    elif s_grade:
        result = Student.query.filter(Student.grade_id == s_grade)
    else:
        result = Student.query.all()

    data = sSchema.jsonify(result)
    status = 404 if not data else 200
    return data, status


@bp_student.route("/student/", methods=["POST"])
@jwt_required()
def create():
    sSchema = StudentSchema()
    try:
        payload = sSchema.load(request.json)
        current_app.db.session.add(payload)
        current_app.db.session.commit()
        result = sSchema.jsonify(payload)
    except SQLAlchemyError as e:
        current_app.db.session.rollback()
        return jsonify({"error": "Data related error"}), 500
    except ValidationError as e:
        return jsonify(e.messages), 422
    except Exception as e:
        return jsonify({"error": "Please check console output"}), 500
    else:
        return result


@bp_student.route("/student/", methods=["PUT"])
@jwt_required()
def update():
    sSchema = StudentSchemaUpdate()
    try:
        payload = sSchema.load(request.json)
        student_id = payload.student_id
        query = Student.query.get(student_id)
        if not query:
            return jsonify({}), 404
        current_app.db.session.merge(payload)
        current_app.db.session.commit()
        result = sSchema.jsonify(payload)
    except ValidationError as e:
        return jsonify(e.messages), 422
    except Exception as e:
        return jsonify({"error": "Please check console output"}), 500
    else:
        return result


@bp_student.route("/student/", methods=["DELETE"])
@jwt_required()
def delete():
    s_id = request.args.get("student_id")
    if not s_id:
        return jsonify({"error": 'Missing Field "student_id"'}), 401
    s_obj = Student.query.filter(Student.student_id == s_id).first()
    if not s_obj:
        return jsonify({}), 404
    else:
        current_app.db.session.delete(s_obj)
        current_app.db.session.commit()
        return jsonify({}), 204
