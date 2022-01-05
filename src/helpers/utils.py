import inspect
import os
import os.path
import sys


def get_root_path(follow_symlinks=True):
    if getattr(sys, 'frozen', False):  # py2exe, PyInstaller, cx_Freeze
        _path = os.path.abspath(sys.executable)
    else:
        _path = inspect.getabsfile(get_root_path)
    if follow_symlinks:
        _path = os.path.realpath(_path)
    parts = os.path.dirname(_path).split(os.path.sep)
    _path = os.path.sep.join(parts[:-2])
    return _path
