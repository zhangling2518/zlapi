import pytest
from core.util import *
from core.client import *

DATA = {"total": 0, "passed": 0, "failed": 0, "error": 0}
DATA.update(get_global_info())

@pytest.fixture
def get():
    def __get(name):
        return DATA[name]
    return __get

@pytest.fixture
def set():
    def __set(name, value):
        DATA[name] = value
    return __set


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    result = yield
    data = result.get_result()
    if data.when == 'call':
        DATA['total'] += 1
        print(data.nodeid)
        if data.outcome == 'passed':
            DATA['passed'] += 1
        elif data.outcome == 'failed':
            DATA['failed'] += 1
        elif data.outcome == 'error':
            DATA['error'] += 1


# @pytest.fixture
# def api():
#     def __api(name):
#         url, method, body_type = get_api_info(name)
#         client = Client(url=url, method=method, body_type=body_type)
#         return client
#     return __api

@pytest.fixture
def api(request):
    url, method, body_type = get_api_info(request.module.__name__.split('.')[1][5:])
    client = Client(url=url, method=method, body_type=body_type)
    return client


