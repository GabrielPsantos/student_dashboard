from flask import url_for
from .flask_base_tests_cases import TestFlaskBase
from datetime import datetime


class TestStudentUpdate(TestFlaskBase):
    def test_update_grade(self):
        self.create_user()
        token = self.create_token()
        data = {"grade_name": "8 ano"}

        response = self.client.post(url_for('grade.create'),
                                    json=data,
                                    headers=token)
        data_student = {
            "grade_id": response.json['grade_id'],
            "name": "Pedrinho",
            "email": "mail@mail.com",
            "age": 13
        }

        response = self.client.post(url_for('student.create'),
                                    json=data_student,
                                    headers=token)

        data_student.update({
            'name': 'Cleiton',
            'student_id': response.json['student_id']
        })
        response_update = self.client.put(url_for('student.update'),
                                          json=data_student,
                                          headers=token)

        data_student['created_updated_at'] = \
            response_update.json['created_updated_at']

        self.assertEqual(data_student, response_update.json)

    def test_update_non_inserted_grade(self):
        self.create_user()
        token = self.create_token()
        data_student = {
            "grade_id": 1,
            "name": "Pedrinho",
            "email": "mail@mail.com",
            "age": 13,
            "student_id": 13
        }

        response = self.client.put(
            url_for('student.update'), json=data_student, headers=token
        )

        self.assertEqual({}, response.json)
        self.assertEqual(404, response.status_code)

    def test_update_grade_error(self):
        self.create_user()
        token = self.create_token()
        data = {"grade_name": "8 ano"}

        response_grade = self.client.post(url_for('grade.create'),
                                          json=data,
                                          headers=token)
        data_student = {
            "grade_id": response_grade.json['grade_id'],
            "name": "Pedrinho",
            "email": "mail@mail.com",
            "age": 13
        }

        response_create = self.client.post(url_for('student.create'),
                                           json=data_student,
                                           headers=token)

        data_student.update({
            'student_id': response_create.json['student_id']
        })

        data_student.pop('name')
        data_student.pop('email')

        response_update = self.client.put(url_for('student.update'),
                                          json=data_student,
                                          headers=token)
        expected = {
            'email': ['Missing data for required field.'],
            'name': ['Missing data for required field.']
        }
        self.assertEqual(expected, response_update.json)
