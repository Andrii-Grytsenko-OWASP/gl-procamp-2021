from src.models.api.response.api_response import ApiResponse


class ApiResponseError(Exception):
    def __init__(self, response: ApiResponse, message="Api exception"):
        self.response = response
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}\n{self.response.code}: [{self.response.type}] {self.response.data}"


class ApiSessionError(Exception):
    def __init__(self):
        self.message = "Api session was not started"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
