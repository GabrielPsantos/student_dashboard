from flask import url_for
from .flask_base_tests_cases import TestFlaskBase
from datetime import datetime


class TestGradeDelete(TestFlaskBase):
    def test_delete_non_existent_grade(self):
        self.create_user()
        token = self.create_token()
        response = self.client.delete(url_for('grade.delete',
                                              grade_id="11"), headers=token)
        self.assertEqual(response.status_code, 404)

    def test_delete_without_grade_id(self):
        self.create_user()
        token = self.create_token()
        response = self.client.delete(
            url_for('grade.delete'), headers=token)
        self.assertEqual(response.status_code, 401)

    def test_delete_grade_success(self):
        self.create_user()
        token = self.create_token()
        data1 = {"grade_name": "8 ano"}

        self.client.post(url_for('grade.create'),
                         json=data1, headers=token)
        response = self.client.delete(
            url_for('grade.delete',
                    grade_id="1"),
            headers=token
        )
        self.assertEqual(response.status_code, 204)
