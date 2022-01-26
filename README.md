README.md

UI Tests from "tests" directory require a chromedriver.exe in bin\ directory
Test require credentials:
- USER_NAME
- USER_PASSWORD

Credentials can be placed in {TARGET_ENVIRONMENT}.env file under src\config\presets directory or provided via environment variables

For running Home_Work_3 tests type in terminal:
pytest tests\test_web_register_page.py

Note: the chromedriver.exe should be placed in bin\ directory

