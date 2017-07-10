
import unittest

class DiTestCase(unittest.TestCase):

    def test_empty_path(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in rv.data

if __name__ == '__main__':
    unittest.main()