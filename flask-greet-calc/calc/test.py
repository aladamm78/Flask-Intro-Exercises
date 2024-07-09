import unittest
from app import app

class CalcTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add(self):
        response = self.app.get('/add?a=10&b=5')
        self.assertEqual(response.data.decode(), '15')

    def test_sub(self):
        response = self.app.get('/sub?a=10&b=5')
        self.assertEqual(response.data.decode(), '5')

    def test_mult(self):
        response = self.app.get('/mult?a=10&b=5')
        self.assertEqual(response.data.decode(), '50')

    def test_div(self):
        response = self.app.get('/div?a=10&b=5')
        self.assertEqual(response.data.decode(), '2.0')

if __name__ == '__main__':
    unittest.main()
