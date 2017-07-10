
import unittest
import DataIncubator
import io

class DiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = DataIncubator.app.test_client()

    def test_image_upload(self):
        response = self.app.post('/img/', content_type='multipart/form-data',data={'picture': (io.BytesIO(b'test image file'), 'testimage.jpeg')})
        self.assertEqual(response.data,b'test image file')

if __name__ == '__main__':
    unittest.main()