from alchemize import Attr, JsonMappedModel


class User(JsonMappedModel):
    __mapping__ = {
        "email": Attr("email", str),
        "password": Attr("password", str),
    }

    def __init__(self, email: str = None, password: str = None):
        self.email = email
        self.password = password
