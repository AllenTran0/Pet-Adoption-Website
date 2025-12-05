"""Main Tests for API calls using stubs and mocks"""
import unittest
# from flask import Flask
from main import app
from signup import pets_invalid, pets_valid, quiz_answer_valid, quiz_answer_invalid

class SignupTestCase(unittest.TestCase):
    """"Test cases for application and questionnarie"""
    def setUp(self):
        """Sets up the client using the app created by flask"""
        self.app = app.test_client()
        self.app.testing = True

    def test_post_application(self):
        """Tests if the information retrieval from the front-end is successful"""
        response = self.app.post('/application', data={
            'first_name': 'Donald',
            'last_name': 'Trump',
            'phone_no': 456789012,
            'email_address': 'DonaldJTrump@gmail.com',
            'address': '123 Main St',
            'postal_code': '12345',
            'animal_type': 'dog'
        }, content_type='application/x-www-form-urlencoded')

        #Checks if the response is successful
        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['message'], 'Signup successful')

    def test_get_application(self):
        """Tests the user function in signup"""
        email_address = {'email_address': 'mark.zuckerberg@facebook.com'}
        response = self.app.get('/user', query_string=email_address)
        data = response.get_json()

        self.assertEqual(data['first_name'], "Mark")
        self.assertEqual(data['last_name'], 'Zuckerberg')
        self.assertEqual(data['phone_no'], 1234567890)
        self.assertEqual(data['email_address'], 'mark.zuckerberg@facebook.com')
        self.assertEqual(data['address'], '123 Main St')
        self.assertEqual(data['postal_code'], '12345')
        self.assertEqual(data['animal_type'], 'dog')

    def test_get_questionnarie(self):
        """Tests the information retrieval is successful"""
        #Valid quiz answers

        response1 = self.app.get('/questionnarie', query_string=quiz_answer_valid[0])
        self.assertEqual(response1.status_code, 200)
        data1 = response1.get_json()
        self.assertEqual(data1['specific_breed'], False)
        self.assertEqual(data1['service_type'], True)
        self.assertEqual(data1['hyper_allergenic'], False)
        self.assertEqual(data1['house_trained'], True)

        response2 = self.app.get('/questionnarie', query_string=quiz_answer_valid[1])
        data2 = response2.get_json()
        self.assertEqual(data2['specific_breed'], True)
        self.assertEqual(data2['service_type'], False)
        self.assertEqual(data2['hyper_allergenic'], True)
        self.assertEqual(data2['house_trained'], False)

        #Invalid quiz answers
        response3 = self.app.get('/questionnarie', query_string=quiz_answer_invalid)
        data3 = response3.get_json()
        self.assertEqual(data3['Error'], "Invalid boolean value")

    def test_post_questionnarie(self):
        """Tests the information that is retrieved from the 'database'
        and checking if the information is correct using post body"""

        #Testing valid
        response1 = self.app.post('/questionnarie/results', json=pets_valid[0])

        valid_data1 = response1.get_json()
        self.assertEqual(response1.status_code, 200)
        self.assertEqual(valid_data1['message'], "200. Succeeded in getting the information")
        self.assertEqual(valid_data1['specific_breed'], True)
        self.assertEqual(valid_data1['service_type'], True)
        self.assertEqual(valid_data1['hyper_allergenic'], False)
        self.assertEqual(valid_data1['house_trained'], False)

        response2 = self.app.post('/questionnarie/results', json=pets_valid[1])
        valid_data2 = response2.get_json()
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(valid_data2['message'], "200. Succeeded in getting the information")
        self.assertEqual(valid_data2['specific_breed'], False)
        self.assertEqual(valid_data2['service_type'], False)
        self.assertEqual(valid_data2['hyper_allergenic'], True)
        self.assertEqual(valid_data2['house_trained'], True)

        #Testing invalid
        #This will be status 200 since I did not use the abort method provided by flask
        #Instead I returned a json string to denote the error
        response3 = self.app.post('/questionnarie/results', json=pets_invalid[0])
        invalid_data1 = response3.get_json()
        self.assertEqual(response3.status_code, 200)
        self.assertEqual(invalid_data1['Error'], "Invalid boolean value")

        response4 = self.app.post('/questionnarie/results', json=pets_invalid[1])
        invalid_data2 = response4.get_json()
        self.assertEqual(response4.status_code, 200)
        self.assertEqual(invalid_data2['Error'], "Invalid boolean value")

class SettingsTestCase(unittest.TestCase):
    """Test cases for Settings API"""
    def setUp(self):
        """Sets up the client using the app created by flask"""
        self.app = app.test_client()
        self.app.testing = True

    # def test_post_settings(self):
    #     """Tests posting the settings from the database"""
    #     # response = self.app.post('/settings', json = {
    #     #     'dark_mode': "True",
    #     #     'text_size': "0",
    #     #     'image_size': "1",
    #     #     'high_contrast': "False"
    #     # })
    #     self.assertEqual(response.status_code, 200)
    #     #data = response.get_json()
    #     self.assertEqual(data['message'], "200. Succeeded in getting the settings")
    #     self.assertEqual(data['dark_mode'], True)
    #     self.assertEqual(data['text_size'], "small")
    #     self.assertEqual(data['image_size'], "medium")
    #     self.assertEqual(data['high_contrast'], False)

    # def test_settings(self):
    #     """Tests getting the settings from the database"""
    #     response = self.app.get('/settings')
    #     self.assertEqual(response.status_code, 200)
    #     data = response.get_json()
    #     self.assertEqual(data[])

class LoginTestCase(unittest.TestCase):
    """Tests cases for the login API"""
    def setUp(self):
        """Sets up the client using the app created by flask"""
        self.app = app.test_client()
        self.app.testing = True

    def test_login_success(self):
        """Tests if the logins are successful"""
        response = self.app.post('/login', json={'username': 'abc12345', 'password': '1234567890'})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['username'], 'abc12345')
        self.assertEqual(data['message'], 'Login successful')

    def test_login_missing(self):
        """Tests if the logins are missing"""
        response = self.app.post('/login', json={})

        self.assertEqual(response.status_code, 400)

        data = response.get_json()
        self.assertIn('error', data)
        self.assertIn(data['error'], "Cannot have nothing in username or password")


if __name__ == '__main__':
    unittest.main()
