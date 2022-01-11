import logging
import os

from pytest import *

from src.helpers import utils


@fixture(scope="class")
def logger():
    log_file = logging.FileHandler(os.path.join(utils.get_root_path(), 'logs', 'testing.log'), 'a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file.setFormatter(formatter)
    _logger = logging.getLogger(None)
    _logger.setLevel(logging.INFO)
    for handler in _logger.handlers[:]:
        _logger.removeHandler(handler)
    _logger.addHandler(log_file)
    yield _logger
    del _logger
