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
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ3OTlmNjM1YjkwMDA3MTE5YmEyNyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA1NTI5NjgsImV4cCI6MTYzMDU2MDE2OCwiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9kdWN0IiwiZ2V0OnByb2R1Y3QiLCJwYXRjaDpwcm9kdWN0IiwicG9zdDpwcm9kdWN0Il19.ei_sJ03f2dya9QzVUlEqwmWvEyoNDx1OtEArQcpokmscuBP-55qqCGoekQZmx7JnOLhVGzgSSHf4JMKKDTDwtzfEL1r7cHiXrEHGSAIBT-TF0bM_GSbirfNZCOwX4RCCD08MvOlAu5hipTLwhhYA8LiANn-H159IWDdfpRb-6tnfyewU2HZfqk0ySNKTdpBFzNA4vAEWxMk9rkjpmVi05x9FQixgNsF4Qe-qF2c_nTQMWVMjpCXbq6saILKYLBzNlxqk-7z_QASudP4lKpcC0mggZLUOifXTnru7_R-nLxlS0L_YmVd-NJP4GKH-sUG3Wba-MW2LDbknQWWXTrLoNw'
            }
        res = self.client().get('/home/1',headers=seller_jwt)
        data = json.loads(res.data)

        self.assertEqual(res.status_code,200)
        self.assertTrue(data["sellers"])

    def test_get_wrong_seller_id(self):
        seller_jwt = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ3OTlmNjM1YjkwMDA3MTE5YmEyNyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA1NTI5NjgsImV4cCI6MTYzMDU2MDE2OCwiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9kdWN0IiwiZ2V0OnByb2R1Y3QiLCJwYXRjaDpwcm9kdWN0IiwicG9zdDpwcm9kdWN0Il19.ei_sJ03f2dya9QzVUlEqwmWvEyoNDx1OtEArQcpokmscuBP-55qqCGoekQZmx7JnOLhVGzgSSHf4JMKKDTDwtzfEL1r7cHiXrEHGSAIBT-TF0bM_GSbirfNZCOwX4RCCD08MvOlAu5hipTLwhhYA8LiANn-H159IWDdfpRb-6tnfyewU2HZfqk0ySNKTdpBFzNA4vAEWxMk9rkjpmVi05x9FQixgNsF4Qe-qF2c_nTQMWVMjpCXbq6saILKYLBzNlxqk-7z_QASudP4lKpcC0mggZLUOifXTnru7_R-nLxlS0L_YmVd-NJP4GKH-sUG3Wba-MW2LDbknQWWXTrLoNw'
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
            'Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ5M2ExZDdlZTU0MDA3MmE1MzZmMyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA1NTMyMjMsImV4cCI6MTYzMDU2MDQyMywiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpwcm9kdWN0Il19.UU1d2hP-jm28KveBzS94Jma3dfEZwhkMopaheEPBtx5YZ5dCvbdVhYcg0HcKQ36WGCu5USI-2ri9gwwjl2lJPXRd3TcWqbphatNI9Ywc5WF_B7VKiyxxkfw_nvhVO-PoozIWgDh01xlaHrdFuV1hKTHDwwsZwzHpgH_Zg4zpMxw7T3GX_7zVc1IhIPW4Jm4vctulOtYaG8DnXVt6u4Sk_rkfgo5EtRKEuFGT_0IaO7WKWY1-Rhh9uAzypyyxb0ASTjwTylXMO-xv4cer0e9I5AeGz_c2y2ooK8OFxO649biF2cHyGIN-tusUS76n1X3ozlE_UQMqa5uR6YDk4k7xBw'
            }
        res = self.client().get('/home/1',headers=buyer_jwt)

        self.assertEqual(res.status_code,401)

    def test_delete_product(self):
        seller_jwt = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ3OTlmNjM1YjkwMDA3MTE5YmEyNyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA1NTI5NjgsImV4cCI6MTYzMDU2MDE2OCwiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9kdWN0IiwiZ2V0OnByb2R1Y3QiLCJwYXRjaDpwcm9kdWN0IiwicG9zdDpwcm9kdWN0Il19.ei_sJ03f2dya9QzVUlEqwmWvEyoNDx1OtEArQcpokmscuBP-55qqCGoekQZmx7JnOLhVGzgSSHf4JMKKDTDwtzfEL1r7cHiXrEHGSAIBT-TF0bM_GSbirfNZCOwX4RCCD08MvOlAu5hipTLwhhYA8LiANn-H159IWDdfpRb-6tnfyewU2HZfqk0ySNKTdpBFzNA4vAEWxMk9rkjpmVi05x9FQixgNsF4Qe-qF2c_nTQMWVMjpCXbq6saILKYLBzNlxqk-7z_QASudP4lKpcC0mggZLUOifXTnru7_R-nLxlS0L_YmVd-NJP4GKH-sUG3Wba-MW2LDbknQWWXTrLoNw'
            }
        res = self.client().delete('/delete/2',headers=seller_jwt)

        self.assertEqual(res.status_code,200)


if __name__ == "__main__":
    unittest.main()