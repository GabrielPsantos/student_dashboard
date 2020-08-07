from flask import url_for
from .flask_base_tests_cases import TestFlaskBase
from datetime import datetime


class TestShow(TestFlaskBase):
    def test_show_empty_grade_query(self):
        self.create_user()
        token = self.create_token()
        response = self.client.get(
            url_for('grade.listOneAll'),
            headers=token
        )
        self.assertEqual([], response.json)

    def test_show_single_grade_inserted(self):
        self.create_user()
        token = self.create_token()
        data = {"grade_name": "8 ano"}

        response = self.client.post(url_for('grade.create'), headers=token,
                                    json=data)
        response = self.client.get(
            url_for('grade.listOneAll'), headers=token)
        self.assertEqual(1, len(response.json))

    def test_show_by_grade_id(self):
        self.create_user()
        token = self.create_token()
        data1 = {"grade_name": "8 ano"}

        response = self.client.post(
            url_for('grade.create'), json=data1, headers=token)
        response = self.client.get(url_for('grade.listOneAll',
                                           grade_id=response.json['grade_id']),
                                   headers=token)
        self.assertEqual(1, len(response.json))

    def test_show_by_grade_name(self):
        self.create_user()
        token = self.create_token()
        data1 = {"grade_name": "8 ano"}

        response = self.client.post(
            url_for('grade.create'), json=data1, headers=token)
        response = self.client.get(url_for('grade.listOneAll',
                                           grade_name=\
                                           response.json['grade_name']),
                                   headers=token)
        self.assertEqual(1, len(response.json))
