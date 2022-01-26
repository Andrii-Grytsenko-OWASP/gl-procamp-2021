Home task 4: Test framework with docker running support

Fom docker framework can perform api tests only

Steps to use:
1. download framework from github: git clone --branch Home_Task_4_docker https://github.com/Andrii-Grytsenko-OWASP/gl-procamp-2021.git
2. provide credentials: fill variables USER_EMAIL and USER_PASSWORD in src/config/presets/test.env file with valid credentials
3. buld docker image: docker build -t framework .
4. run docker container: docker run -v <full/path/to/cloned/repository>/logs:/app/logs framework

By default framework will execute tests/test_api_dashboard.py tests
Log of running tests will be available in file <full/path/to/cloned/repository>/logs/testing.log

Note: in order to get logs from docker you should specify full path to your local folder in command "docker run ..."
