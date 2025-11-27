import unittest
from main import app

class RootPageTestCase(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый клиент
        self.app = app.test_client()
        self.app.testing = True

    # Тесты для главной страницы
    def test_index_redirect(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 302)  # Проверка на редирект
        self.assertEqual(response.location, '/addition')

class AdditionPageTestCase(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый клиент
        self.app = app.test_client()
        self.app.testing = True

    def test_addition_success(self):
        response = self.app.get('/addition?x=5&y=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '8.0')

    def test_addition_missing_params(self):
        response = self.app.get('/addition')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'Не переданы числа в параметрах запроса `x` и `y`')

class MultiplicationPageTestCase(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый клиент
        self.app = app.test_client()
        self.app.testing = True

    def test_multiplication_success(self):
        response = self.app.get('/multiplication?x=5&y=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '15.0')

    def test_multiplication_zero(self):
        response = self.app.get('/multiplication?x=0&y=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '0.0')

class AdditionPageTestCase(unittest.TestCase):
    def setUp(self):
        # Создаем тестовый клиент
        self.app = app.test_client()
        self.app.testing = True

    def test_subtraction_success(self):
        response = self.app.get('/subtraction?x=5&y=3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '2.0')

    def test_subtraction_negative_result(self):
        response = self.app.get('/subtraction?x=3&y=5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '-2.0')

class MultiplicationPageTestCase(unittest.TestCase):

    def setUp(self):
        # Создаем тестовый клиент
        self.app = app.test_client()
        self.app.testing = True

    def test_division_success(self):
        response = self.app.get('/division?x=10&y=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '5.0')

    def test_division_float(self):
        response = self.app.get('/division?x=5&y=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '2.5')

    def test_division_by_zero(self):
        response = self.app.get('/division?x=5&y=0')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), 'division by zero')

    def test_division_negative(self):
        response = self.app.get('/division?x=-10&y=2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '-5.0')

if __name__ == '__main__':
    unittest.main()
