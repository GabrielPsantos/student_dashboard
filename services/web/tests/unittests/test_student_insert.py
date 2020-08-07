from flask import url_for
from .flask_base_tests_cases import TestFlaskBase
from datetime import datetime


class TestStudentInsert(TestFlaskBase):
    def test_student_insert_ok(self):
        self.create_user()
        token = self.create_token()
        data = {"grade_name": "8 ano"}
        expected_grade = {
            "grade_id": 1,
            "grade_name": "8 ano",
            "created_updated_at": datetime.now().strftime('%Y-%m-%d')
        }

        response = self.client.post(url_for('grade.create'),
                                    json=data,
                                    headers=token)
        data_student = {
            "grade_id": response.json['grade_id'],
            "name": "Pedrinho",
            "email": "mail@mail.com",
            "age": 13
        }

        response_student = self.client.post(url_for('student.create'),
                                            json=data_student,
                                            headers=token)

        data_student['created_updated_at'] = \
            response_student.json['created_updated_at']

        data_student['student_id'] = response_student.json['student_id']

        self.assertEqual(data_student, response_student.json)

    def test_student_without_fields(self):
        self.create_user()
        token = self.create_token()
        dado = {}

        expected = {
            'age': ['Missing data for required field.'],
            'email': ['Missing data for required field.'],
            'grade_id': ['Missing data for required field.'],
            'name': ['Missing data for required field.']
        }

        response = self.client.post(
            url_for('student.create'), headers=token, json=dado)
        self.assertEqual(expected, response.json)
        self.assertEqual(response.status_code, 422)

    def test_duplicated_students(self):
        self.create_user()
        token = self.create_token()
        data = {"grade_name": "8 ano"}
        expected_grade = {
            "grade_id": 1,
            "grade_name": "8 ano",
            "created_updated_at": datetime.now().strftime('%Y-%m-%d')
        }

        response = self.client.post(url_for('grade.create'),
                                    json=data,
                                    headers=token)
        data_student = {
            "grade_id": response.json['grade_id'],
            "name": "Pedrinho",
            "email": "mail@mail.com",
            "age": 13
        }

        response_one = self.client.post(url_for('student.create'),
                                        json=data_student,
                                        headers=token)

        response_two = self.client.post(url_for('student.create'),
                                        json=data_student,
                                        headers=token)

        expected = {'error': 'Data related error'}

        self.assertEqual(expected, response_two.json)
        self.assertEqual(response_two.status_code, 500)
