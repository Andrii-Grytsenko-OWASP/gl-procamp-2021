README.md

UI Tests from "tests" directory require a chromedriver.exe in bin\ directory
Test require credentials:
- USER_NAME
- USER_PASSWORD

Credentials can be placed in {TARGET_ENVIRONMENT}.env file under src\config\presets directory or provided via environment variables

For running HW2 type in terminal:
pytest tests\test_api_login.py

Note: valid credentials should be provided in config files before running the test
