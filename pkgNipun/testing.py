import unittest
from Password import generate_password , get_excluded_letters

class TestPasswordGenerator(unittest.TestCase):

    def setUp(self):
        self.place_file_path = 'Place.csv'  # Replace with the path to your Place.csv file
        self.name_file_path = 'Name.csv'    # Replace with the path to your Name.csv file

    def test_generate_password_length(self):
        # Test if the generated password has the correct length
        excluded_letters = get_excluded_letters(self.place_file_path) + get_excluded_letters(self.name_file_path)
        password = generate_password(excluded_letters)
        self.assertGreaterEqual(len(password), 6)
        self.assertLessEqual(len(password), 12)

    def test_generate_password_excluded_letters(self):
        # Test if the generated password does not contain any excluded letters
        excluded_letters = get_excluded_letters(self.place_file_path) + get_excluded_letters(self.name_file_path)
        password = generate_password(excluded_letters)
        for char in password:
            self.assertNotIn(char, excluded_letters)

if __name__ == '__main__':
    unittest.main()
