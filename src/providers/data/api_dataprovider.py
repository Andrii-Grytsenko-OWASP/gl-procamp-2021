# Data for testing LoginPage Page
from src.config.config import CFG
from src.helpers.enums import ApiResponseType

api_data = [
    ({"description": "Login with invalid credentials",
      "email": "valid@ema.il", "password": "secret_password",
      "expected_result": ApiResponseType.error}),
    ({"description": "Login with valid credentials",
      "email": CFG.USER_EMAIL, "password": CFG.USER_PASSWORD,
      "expected_result": ApiResponseType.ok}),
]
api_data_ids = [
    f'Test description [{item["description"]}]'
    for item in api_data]
