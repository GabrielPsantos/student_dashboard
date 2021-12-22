from flask import url_for
from .flask_base_tests_cases import TestFlaskBase
from datetime import datetime


class TestStudentShow(TestFlaskBase):
    def test_show_empty_grade_query(self):
        self.create_user()
        token = self.create_token()
        response = self.client.get(url_for("student.listOneAll"), headers=token)
        self.assertEqual([], response.json)

    def test_show_single_student_inserted(self):
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

        response = self.client.get(url_for("student.listOneAll"), headers=token)
        self.assertEqual(1, len(response.json))

    def test_show_by_student_id(self):
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

        response = self.client.get(
            url_for(
                "student.listOneAll", student_id=response_student.json["student_id"]
            ),
            headers=token,
        )
        self.assertEqual(1, len(response.json))

    def test_show_by_student_name(self):
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

        data_student.update({"email": "mail2@mail2.com"})

        response_student = self.client.post(
            url_for("student.create"), json=data_student, headers=token
        )

        response = self.client.get(
            url_for("student.listOneAll", name=response_student.json["name"]),
            headers=token,
        )

        self.assertEqual(2, len(response.json))

    def test_show_by_student_email(self):
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

        data_student.update({"email": "mail2@mail2.com"})

        response_student = self.client.post(
            url_for("student.create"), json=data_student, headers=token
        )

        response = self.client.get(
            url_for("student.listOneAll", email=response_student.json["email"]),
            headers=token,
        )

        self.assertEqual(1, len(response.json))

    def test_show_by_student_age(self):
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

        data_student.update({"email": "mail2@mail2.com"})

        response_student = self.client.post(
            url_for("student.create"), json=data_student, headers=token
        )

        response = self.client.get(
            url_for("student.listOneAll", age=response_student.json["age"]),
            headers=token,
        )

        self.assertEqual(2, len(response.json))

    def test_show_by_student_grade(self):
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

        data_student.update({"email": "mail2@mail2.com"})

        response_student = self.client.post(
            url_for("student.create"), json=data_student, headers=token
        )

        response = self.client.get(
            url_for("student.listOneAll", grade=response_student.json["grade_id"]),
            headers=token,
        )

        self.assertEqual(2, len(response.json))
