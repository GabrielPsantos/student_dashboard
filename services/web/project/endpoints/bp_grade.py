from flask import Blueprint, request, current_app, jsonify
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from project.serializer.serializer import GradeSchema, GradeSchemaUpdate
from project.model.model import Grade

bp_grade = Blueprint("grade", __name__)


@bp_grade.route("/grade/", methods=["GET"])
@jwt_required()
def listOneAll():
    rSchema = GradeSchema(many=True)
    g_grade_id = request.args.get("grade_id")
    g_grade_name = request.args.get("grade_name")

    if g_grade_id:
        result = Grade.query.filter(Grade.grade_id == g_grade_id)
    elif g_grade_name:
        result = Grade.query.filter(Grade.grade_name == g_grade_name)
    else:
        result = Grade.query.all()

    data = rSchema.jsonify(result)
    status = 404 if not data else 200
    return data, status


@bp_grade.route("/grade/", methods=["POST"])
@jwt_required()
def create():
    gSchema = GradeSchema()
    try:
        payload = gSchema.load(request.json)
        current_app.db.session.add(payload)
        current_app.db.session.commit()
        result = gSchema.jsonify(payload)
    except SQLAlchemyError as e:
        current_app.db.session.rollback()
        return jsonify({"error": "Data related error"}), 422
    except ValidationError as e:
        return jsonify(e.messages), 422
    except Exception as e:
        return jsonify({"error": "Please check console output"}), 500
    else:
        return result


@bp_grade.route("/grade/", methods=["PUT"])
@jwt_required()
def update():
    gSchema = GradeSchemaUpdate()
    try:
        payload = gSchema.load(request.json)
        grade_id = payload.grade_id
        query = Grade.query.get(grade_id)
        if not query:
            return jsonify({}), 404
        current_app.db.session.merge(payload)
        current_app.db.session.commit()
        updated = Grade.query.get(grade_id)
        result = gSchema.jsonify(updated)
    except ValidationError as e:
        return jsonify(e.messages), 422
    except Exception as e:
        return jsonify({"error": "Please check console output"}), 500
    else:
        return result


@bp_grade.route("/grade/", methods=["DELETE"])
@jwt_required()
def delete():
    g_id = request.args.get("grade_id")
    if not g_id:
        return jsonify({"error": 'Missing Field "grade_id"'}), 401
    g_obj = Grade.query.filter(Grade.grade_id == g_id).first()
    if not g_obj:
        return jsonify({}), 404
    else:
        current_app.db.session.delete(g_obj)
        current_app.db.session.commit()
        return jsonify({}), 204
