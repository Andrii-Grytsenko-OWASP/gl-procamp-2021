# Data for testing LoginPage Page
from src.config.config import CFG

login_data = [
    ({"description": "Sign in on login page with invalid credentials",
      "email": "valid@ema.il", "password": "secret_password",
      "expected_result": False}),
    ({"description": "Sign in on login page with valid credentials",
      "email": CFG.USER_EMAIL, "password": CFG.USER_PASSWORD,
      "expected_result": True}),
]
login_data_ids = [
    f'Test description [{item["description"]}]'
    for item in login_data]
