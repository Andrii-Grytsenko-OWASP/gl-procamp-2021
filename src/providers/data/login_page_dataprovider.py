# Data for testing LoginPage Page
login_data = [
    ({"email": "valid@ema.il", "password": "secret_password", "exit_code": 200}),
]
login_data_ids = [
    f'LoginPage with credentials [Email: {item["email"]}], Password: {item["password"]}, Expected code={item["exit_code"]}'
    for item in login_data]
