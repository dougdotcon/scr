import unittest
from flask import Flask
from app.views import app
from models import Product

class TestViews(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_dashboard(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_admin_dashboard(self):
        response = self.client.get('/admin')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

import unittest

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        product = Product('Product 1', 'Description 1', 10.0)
        self.assertEqual(product.title, 'Product 1')
        self.assertEqual(product.description, 'Description 1')
        self.assertEqual(product.price, 10.0)

if __name__ == '__main__':
    unittest.main()
    
def test_dashboard(self):
    response = self.client.get('/')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Welcome to the dashboard', response.data)

def test_admin_dashboard(self):
    response = self.client.get('/admin')
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'Welcome, admin', response.data)