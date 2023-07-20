import random
import string
import os
import csv

def get_excluded_strings(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        excluded_strings = {line.strip() for line in file}
    return excluded_strings

def generate_password(exclude_strings):
    """
    Generate a random password of length between 6 and 12 characters.

    Args:
        exclude_strings (set): A set containing excluded strings.

    Returns:
        str: The generated password.
    """
    length = random.randint(6, 12)
    password = []

    password.append(random.choice(string.digits))  # random digit generated
    password.append(random.choice(string.ascii_uppercase))  # random uppercase alphabet
    password.append(random.choice(string.ascii_lowercase))  # random lowercase alphabet

    available_chars = string.ascii_letters + string.digits

    while len(password) < length:
        char = random.choice(available_chars)
        while any(excluded_str in ''.join(password) + char for excluded_str in exclude_strings):
            char = random.choice(available_chars)
        password.append(char)

    random.shuffle(password)
    generated_password = ''.join(password)

    return generated_password

def gen_password_with_exclusions(excluded_strings):
    return generate_password(excluded_strings)

def main():
    """
    Read excluded strings from "Place.csv" and "Name.csv", combine them, and generate a password
    excluding the strings from the files.
    """
    module_dir = os.getcwd()
    place_file_name = 'Place.csv'
    name_file_name = 'Name.csv'

    place_file_path = os.path.join(module_dir, place_file_name)
    name_file_path = os.path.join(module_dir, name_file_name)

    excluded_place = get_excluded_strings(place_file_path)
    excluded_name = get_excluded_strings(name_file_path)

    excluded_strings = excluded_place.union(excluded_name)

    generated_password = gen_password_with_exclusions(excluded_strings)
    print(generated_password)

if __name__ == "__main__":
    main()
