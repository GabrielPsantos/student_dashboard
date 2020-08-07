from flask import url_for
from .flask_base_tests_cases import TestFlaskBase
from datetime import datetime


class TestGradeUpdate(TestFlaskBase):
    def test_update_grade(self):
        self.create_user()
        token = self.create_token()
        estado_inicial = {"grade_name": "8 ano"}

        r = self.client.post(url_for('grade.create'),
                             headers=token,
                             json=estado_inicial)

        final_state = {
            "grade_id": r.json['grade_id'],
            "grade_name": "9 ano",
        }

        response = self.client.put(
            url_for('grade.update'), json=final_state, headers=token
        )

        final_state['created_updated_at'] = r.json['created_updated_at']

        self.assertEqual(final_state, response.json)

    def test_update_non_inserted_grade(self):
        self.create_user()
        token = self.create_token()
        final_state = {
            "grade_id": 99,
            "grade_name": "9 ano",
        }

        response = self.client.put(
            url_for('grade.update'), json=final_state, headers=token
        )

        self.assertEqual({}, response.json)
        self.assertEqual(404, response.status_code)

    def test_update_grade_error(self):
        self.create_user()
        token = self.create_token()
        estado_inicial = {"grade_name": "8 ano"}

        final_state = {"grade_name": "9 ano"}

        expected = {
            'grade_id': ['Missing data for required field.']
        }

        self.client.post(url_for('grade.create'),
                         json=estado_inicial,
                         headers=token)

        response = self.client.put(
            url_for('grade.update'),
            json=final_state,
            headers=token
        )
        self.assertEqual(expected, response.json)
