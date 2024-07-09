from app import app
import unittest

class TestSimpleRoutes(unittest.TestCase):

    def test_welcome(self):
        tester = app.test_client(self)
        response = tester.get('/welcome', content_type='html/text')
        self.assertIn(b'welcome', response.data.lower())
        self.assertEqual(response.status_code, 200)

    def test_welcome_home(self):
        tester = app.test_client(self)
        response = tester.get('/welcome/home', content_type='html/text')
        self.assertIn(b'welcome home', response.data.lower())
        self.assertEqual(response.status_code, 200)

    def test_welcome_back(self):
        tester = app.test_client(self)
        response = tester.get('/welcome/back', content_type='html/text')
        self.assertIn(b'welcome back', response.data.lower())
        self.assertEqual(response.status_code, 200)

import unittest
from app import app

class GreetTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_welcome(self):
        result = self.app.get('/welcome')
        self.assertEqual(result.data.decode(), 'welcome')

    def test_welcome_home(self):
        result = self.app.get('/welcome/home')
        self.assertEqual(result.data.decode(), 'welcome home')

    def test_welcome_back(self):
        result = self.app.get('/welcome/back')
        self.assertEqual(result.data.decode(), 'welcome back')

if __name__ == '__main__':
    unittest.main()
