from pytest import *

from src.providers.data.register_page_dataprovider import *


@fixture(params=register_data, ids=register_data_ids)
def dp_register_page(request):
    return request.param
