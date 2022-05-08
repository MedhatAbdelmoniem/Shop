import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.sqltypes import JSON
from database.app.app import create_app, setup_db, Seller, Buyer

class SellerTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        pass

    def test_get_sellers_info(self):
        res = self.client().get('/home')
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertTrue(data["sellers"])
    
    def test_get_seller_info(self):
        seller_jwt = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ3OTlmNjM1YjkwMDA3MTE5YmEyNyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA2MDQ3MTEsImV4cCI6MTYzMDYxMTkxMSwiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9kdWN0IiwiZ2V0OnByb2R1Y3QiLCJwYXRjaDpwcm9kdWN0IiwicG9zdDpwcm9kdWN0Il19.a5zT5JamZ6psjOI_D_ggikoqwxLhoaNebl_MvCO0VyzW1AzmYcKsxyGdMNYJ4HODiQY5_jFuuUhp8ev8IdhtyUDShSJvJAMKLLc5zg4J86xesVlbWDtm6lu5dnMT8Qw5yV8NCO2TaA-z6_sPwbkjFSLWVGH9kCybcdRWNv0JJayx5ZrtPHGtoYzzbpcAtRVfZAils08HcYtDMEe9sCQzS7u-kbqxtHpy1fm-xu0WOg8p0sCi3L0fvXTi7TwKIsmZELLMITNgSDyycmOC7BzWvDlUNskikvjTbLwSBD8hke-f-sW3xEF1POEEiGrBK75TL5qm-qmnEEtTWpbZngujBw'
            }
        res = self.client().get('/home/1',headers=seller_jwt)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertTrue(data["sellers"])

    def test_get_wrong_seller_id(self):
        seller_jwt = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ3OTlmNjM1YjkwMDA3MTE5YmEyNyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA2MDQ3MTEsImV4cCI6MTYzMDYxMTkxMSwiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9kdWN0IiwiZ2V0OnByb2R1Y3QiLCJwYXRjaDpwcm9kdWN0IiwicG9zdDpwcm9kdWN0Il19.a5zT5JamZ6psjOI_D_ggikoqwxLhoaNebl_MvCO0VyzW1AzmYcKsxyGdMNYJ4HODiQY5_jFuuUhp8ev8IdhtyUDShSJvJAMKLLc5zg4J86xesVlbWDtm6lu5dnMT8Qw5yV8NCO2TaA-z6_sPwbkjFSLWVGH9kCybcdRWNv0JJayx5ZrtPHGtoYzzbpcAtRVfZAils08HcYtDMEe9sCQzS7u-kbqxtHpy1fm-xu0WOg8p0sCi3L0fvXTi7TwKIsmZELLMITNgSDyycmOC7BzWvDlUNskikvjTbLwSBD8hke-f-sW3xEF1POEEiGrBK75TL5qm-qmnEEtTWpbZngujBw'
            }
        res = self.client().get('/home/25',headers=seller_jwt)

        self.assertEqual(res.status_code,404)

    def test_wrong_access(self):
        wrong_seller_jwt = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ5M2ExZDdlZTU0MDA3MmE1MzZmMyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA1NDg0OTQsImV4cCI6MTYzMDU1NTY5NCwiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpwcm9kdWN0Il19.gsJsaUCl__8IZmaHkH4GAXwchaRSei5zSLfaHYWcbQS6m1_sjYQTcVbxc98QXcOWxxdVb9CaxQ1p7AJwWCCQy53D_wY0OdzJVJGk12S3F0-FfgtWV7eYwP6ANoJD8tS3CWTbSxVKJXyhT1RYu-0_4EYG_puXquB_Q_SG9vZTw9C8S9JOxrNNRr0e6zYn8QbMRLCvog-Vf5MuGc8WLR5SuCQGw_HEBm5wy6ao6vuPLlisc-bbD_234MJGRpNWw8hXjEcdHmI2YUmobJfb1v-1go_3wf8c93ZkgCq80IAQZAIlaHgW-b6LMjrKjnMQwFWRKTCaBQBKKeOYNiCTo8tppg'
            }
        res = self.client().get('/delete/1',headers=wrong_seller_jwt)

        self.assertEqual(res.status_code,405)

    def test_no_bearer(self):
        buyer_jwt = {
            'Content-Type': 'application/json',
            'Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ5M2ExZDdlZTU0MDA3MmE1MzZmMyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA2MDQ1MTYsImV4cCI6MTYzMDYxMTcxNiwiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpwcm9kdWN0Il19.mSIxX4lPph9HhZO3X9vqC-5M1ypwShRWcWo_ocbbAYvwWdjadHVIL1NIMY7glx4-yNhvwAaf-XwYO4e_LdVXf3A0ClCWtbH25mJJECBk7rhJsAcCZo9a5HxfNncw1HTCknOjgqlJ-8xLCuvTuCCJGX8HDSU8kmHDOzMMF2aQCMNtNhmwORAiEbRhj_WmXrb_-gEiz3vfO7whFyFDU0AmtY-J1hHH9dg9scAj0n4y-apPpY_J8OfEkzd2_ys1y6wGFgF4FmAZ4XPx0YmRjPUefiWSkij9ByfdhaMKHPuUVOLFlLTXO8GDqAWCI6EHq8VPb1sLUVQN9JlZG54PWWMeeA'
            }
        res = self.client().get('/home/1',headers=buyer_jwt)

        self.assertEqual(res.status_code,401)

    def test_delete_product(self):
        seller_jwt = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ3OTlmNjM1YjkwMDA3MTE5YmEyNyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA2MDQ3MTEsImV4cCI6MTYzMDYxMTkxMSwiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9kdWN0IiwiZ2V0OnByb2R1Y3QiLCJwYXRjaDpwcm9kdWN0IiwicG9zdDpwcm9kdWN0Il19.a5zT5JamZ6psjOI_D_ggikoqwxLhoaNebl_MvCO0VyzW1AzmYcKsxyGdMNYJ4HODiQY5_jFuuUhp8ev8IdhtyUDShSJvJAMKLLc5zg4J86xesVlbWDtm6lu5dnMT8Qw5yV8NCO2TaA-z6_sPwbkjFSLWVGH9kCybcdRWNv0JJayx5ZrtPHGtoYzzbpcAtRVfZAils08HcYtDMEe9sCQzS7u-kbqxtHpy1fm-xu0WOg8p0sCi3L0fvXTi7TwKIsmZELLMITNgSDyycmOC7BzWvDlUNskikvjTbLwSBD8hke-f-sW3xEF1POEEiGrBK75TL5qm-qmnEEtTWpbZngujBw'
            }
        res = self.client().delete('/delete/2',headers=seller_jwt)

        self.assertEqual(res.status_code,200)


if __name__ == "__main__":
    unittest.main()