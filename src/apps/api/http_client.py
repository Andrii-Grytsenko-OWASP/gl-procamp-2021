from enum import Enum

from requests import *


class HttpClient:
    pass


class HttpMethod(Enum):
    GET = get
    POST = post
    PUT = put
    PATCH = patch
    DELETE = delete
    HEAD = head
    OPTIONS = options
