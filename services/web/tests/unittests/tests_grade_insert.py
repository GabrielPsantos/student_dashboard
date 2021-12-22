from flask import url_for
from .flask_base_tests_cases import TestFlaskBase
from datetime import datetime


class TestGradeInsert(TestFlaskBase):
    def test_grade_insert_ok(self):
        self.create_user()
        token = self.create_token()
        data = {"grade_name": "8 ano"}
        expected = {
            "grade_id": 1,
            "grade_name": "8 ano",
            "created_updated_at": datetime.now().strftime("%Y-%m-%d"),
        }

        response = self.client.post(url_for("grade.create"), json=data, headers=token)
        self.assertEqual(expected, response.json)

    def test_grade_without_fields(self):
        self.create_user()
        token = self.create_token()
        dado = {}

        expected = {"grade_name": ["Missing data for required field."]}

        response = self.client.post(url_for("grade.create"), headers=token, json=dado)
        self.assertEqual(expected, response.json)
        self.assertEqual(response.status_code, 422)

    def test_duplicated_grades(self):
        self.create_user()
        token = self.create_token()
        data = {"grade_name": "8 ano"}
        expected = {
            "grade_id": 1,
            "grade_name": "8 ano",
            "created_updated_at": datetime.now().strftime("%Y-%m-%d"),
        }

        response = self.client.post(url_for("grade.create"), headers=token, json=data)
        self.assertEqual(response.json, expected)

        expected2 = {"error": "Data related error"}

        response_2 = self.client.post(url_for("grade.create"), headers=token, json=data)
        self.assertEqual(expected2, response_2.json)
        self.assertEqual(response_2.status_code, 422)
