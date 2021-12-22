from flask import url_for
from .flask_base_tests_cases import TestFlaskBase
from datetime import datetime


class TestStudentDelete(TestFlaskBase):
    def test_delete_non_existent_grade(self):
        self.create_user()
        token = self.create_token()
        response = self.client.delete(
            url_for("student.delete", student_id="11"), headers=token
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_without_grade_id(self):
        self.create_user()
        token = self.create_token()
        response = self.client.delete(url_for("student.delete"), headers=token)
        self.assertEqual(response.status_code, 401)

    def test_delete_grade_success(self):
        self.create_user()
        token = self.create_token()
        data = {"grade_name": "8 ano"}
        expected_grade = {
            "grade_id": 1,
            "grade_name": "8 ano",
            "created_updated_at": datetime.now().strftime("%Y-%m-%d"),
        }

        response = self.client.post(url_for("grade.create"), json=data, headers=token)
        data_student = {
            "grade_id": response.json["grade_id"],
            "name": "Pedrinho",
            "email": "mail@mail.com",
            "age": 13,
        }

        response_student = self.client.post(
            url_for("student.create"), json=data_student, headers=token
        )
        response = self.client.delete(
            url_for("student.delete", student_id=response_student.json["student_id"]),
            headers=token,
        )

        self.assertEqual(response.status_code, 204)
