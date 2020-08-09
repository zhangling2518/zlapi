from core.client import *
from core.util import *
from cases.test_demo import *
import pytest
# data = [('zhangsan', 'MTIzMTIzNDU2', 0, '正确登录'),
#         ('zhangsan', '123456', 10000, '密码错误'),
#         ('zhangsan', '', 10001, '密码为空')]

# @pytest.mark.parametrize('username, password, error_code, msg', csv('login.csv'))
@data('username, password, error_code, msg', csv('login.csv'))
@feature('用户登录接口')
@title('登录数据测试')
@order(order=1)
def test_login01(username, password, error_code, msg):
    client = Client(url='login/', method=METHOD.POST, body_type=BODY_TYPE.FORM)
    client.set_body("username", username)
    client.set_body("password", password)
    client.send()
    client.check_status_code_is_200()
    client.check_res_times_less_than(10)
    client.check_json_value('error_code', error_code)


def test_login02(api):
    '''
    密码错误
    '''
    # client = Client(url='login/', method=METHOD.POST, body_type=BODY_TYPE.FORM)
    api.set_body("username", "zhangsan")
    api.set_body("password", "123456")
    api.send()
    api.check_status_code_is_200()
    api.check_res_times_less_than(1000)
    api.check_json_value('error_code', 10000)

# def test_login(api):
#     api.set_header()
#     api.send()
#     api.check_status_code_is_200()