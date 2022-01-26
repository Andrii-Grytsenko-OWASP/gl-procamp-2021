import inspect
import os
import os.path
import sys
import urllib.parse
import random
import string


def get_root_path(follow_symlinks=True) -> str:
    if getattr(sys, 'frozen', False):  # py2exe, PyInstaller, cx_Freeze
        _path = os.path.abspath(sys.executable)
    else:
        _path = inspect.getabsfile(get_root_path)
    if follow_symlinks:
        _path = os.path.realpath(_path)
    parts = os.path.dirname(_path).split(os.path.sep)
    _path = os.path.sep.join(parts[:-2])
    return _path


def get_url(base_url: str, endpoint: str) -> str:
    return urllib.parse.urljoin(base_url, endpoint)


def get_random_string(length=8, upper_case=False, numbers=False, special=False):
    random_string = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
    if upper_case:
        random_string = random.choice(string.ascii_uppercase) + random_string[:-1]
    if numbers:
        random_string = random.choice("1234567890") + random_string[:-1]
    if special:
        random_string = random.choice("!@#$%^*-_+=") + random_string[:-1]
    return random_string
