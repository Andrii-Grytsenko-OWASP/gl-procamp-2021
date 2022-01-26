# Data for testing LoginPage Page
from src.config.config import CFG
from src.helpers.utils import get_random_string


def generate_email():
    return get_random_string(length=5) + "@" + \
           get_random_string(length=4) + "." + \
           get_random_string(length=3)


def generate_password():
    return get_random_string(upper_case=True, numbers=True, special=True)


register_data = [
    ({"description": "Register with random credentials",
      "name": get_random_string(), "job_title": get_random_string(), "organization": get_random_string(),
      "email": generate_email(), "password": generate_password(),
      "expected_result": True}),
    ({"description": "Register with random credentials",
      "name": get_random_string(), "job_title": get_random_string(), "organization": get_random_string(),
      "email": generate_email(), "password": generate_password(),
      "expected_result": True}),
]
register_data_ids = [
    f'Test description [{item["description"]}]'
    for item in register_data]
