import os
import unittest

from flask import current_app
from flask_testing import TestCase

from manage import app

from main.config import basedir

class TestDevConfig(TestCase):
    def create_app(self):
        app.config.from_object('main.config.DevConfig')
        return app
    
    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
    
class TestTestConfig(TestCase):
    def create_app(self):
        app.config.from_object('main.config.TestConfig')
        return app
    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

class TestProdConfig(TestCase):
    def create_app(self):
        app.config.from_object('main.config.ProdConfig')
        return app
    def test_app_is_testing(self):
        self.assertFalse(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)

if __name__ == '__main__':
    unittest.main()