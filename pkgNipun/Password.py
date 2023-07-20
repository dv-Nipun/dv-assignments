import random
import string
import os

def get_excluded_letters(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        excluded_letters = ''.join(line.strip() for line in file)
    return excluded_letters

def generate_password(exclude_letters):
    """
    Generate a random password of length between 6 and 12 characters.

    Args:
        exclude_letters (str): A string containing excluded letters.

    Returns:
        str: The generated password.
    """
    length = random.randint(6, 12)
    password = []

    password.append(random.choice(string.digits))  # random digit generated
    password.append(random.choice(string.ascii_uppercase))  # random uppercase alphabet
    password.append(random.choice(string.ascii_lowercase))  # random lowercase alphabet

    for _ in range(length - 3):
        char = random.choice(string.ascii_letters + string.digits)
        while char in exclude_letters:
            char = random.choice(string.ascii_letters + string.digits)
        password.append(char)

    return ''.join(password)

def gen_password_with_exclusions(excluded_letters):
   
    return generate_password(excluded_letters)

def main():
    """
    Read excluded letters from "Place.csv" and "Name.csv", combine them, and generate a password
    excluding the letters from the files.
    """
    module_dir = os.getcwd()
    place_file_name = 'Place.csv'
    name_file_name = 'Name.csv'

    place_file_path = os.path.join(module_dir, place_file_name)
    name_file_path = os.path.join(module_dir, name_file_name)

    excluded_place = get_excluded_letters(place_file_path)
    excluded_name = get_excluded_letters(name_file_path)

    excluded_letters = excluded_place + excluded_name

    generated_password = gen_password_with_exclusions(excluded_letters)
    print(generated_password)

if __name__ == "__main__":
    main()
