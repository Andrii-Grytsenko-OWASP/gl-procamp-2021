from pytest import *

from src.providers.data.api_dataprovider import *


@fixture(params=api_data, ids=api_data_ids)
def dp_api(request):
    return request.param
