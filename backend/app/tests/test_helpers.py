from .base import BaseTestCase
from app.helpers import to_base_62

class helperTest(BaseTestCase):

    def test_base62_conversion(self):

        converted = to_base_62(100)

        self.assertEqual(converted, '1c')
        self.assertIsInstance(converted, str)

    def test_base62_conversion_invalid_input(self):
        self.assertRaises(TypeError, to_base_62, "100")
        self.assertRaises(TypeError, to_base_62, -10)






    




