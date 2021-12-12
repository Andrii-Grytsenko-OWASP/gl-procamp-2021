from pytest import *

from src.providers.data.login_page_dataprovider import *


@fixture(params=login_data, ids=login_data_ids)
def dp_login_page(request):
    return request.param
