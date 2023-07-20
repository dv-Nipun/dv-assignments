import unittest

from Password import generate_password


class GeneratePasswordTest(unittest.TestCase):

    def test_generate_password_with_no_excluded_strings(self):
        excluded_strings = set()
        generated_password = generate_password(excluded_strings)
        self.assertRegex(generated_password, r'[a-zA-Z0-9]{6,12}')

    def test_generate_password_with_excluded_strings(self):
        excluded_strings = {'password', '123456', 'helloworld'}
        generated_password = generate_password(excluded_strings)
        self.assertNotIn(generated_password, excluded_strings)
        self.assertRegex(generated_password, r'[a-zA-Z0-9]{6,12}')


if __name__ == '__main__':
    unittest.main()
