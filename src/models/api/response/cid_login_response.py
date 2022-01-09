from alchemize import Attr, JsonMappedModel


class LoginResponse(JsonMappedModel):
    __mapping__ = {
        "jwt": Attr("jwt", str),
        "token": Attr("token", str),
        "expires": Attr("expires", str),
    }

    def __init__(self, jwt: str = None, token: str = None, expires: str = None):
        self.jwt = jwt
        self.token = token
        self.expires = expires
