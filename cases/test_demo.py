import pytest

# @pytest.fixture
# def api():
#     def __api(name):
#         print('运行fixture')
#         return {
#             "name": name,
#             "orders": []
#         }
#     return __api


def test_demo01():
    print(1)
    assert False
    # client = api('登录')
    # client.set_body("username", username)
    # client.set_body("password", password)
    # client.send()
    # client.check_status_code_is_200()
    # client.check_res_times_less_than(10)
    # client.check_json_value('error_code', error_code)


def test_demo02():
    print(2)