
import unittest
import DataIncubator

class DiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = DataIncubator.app.test_client()

    def test_empty_path(self):
        response = self.app.get('/')
        print(response)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()