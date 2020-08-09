from core.client import *
from core.util import *
import pytest

@feature('活动预定接口')
@title('正确预定')
@order(order=3)
def test_order01():
    '''
    预定活动
    '''
    client = Client(url='order/', method=METHOD.POST, body_type=BODY_TYPE.FORM)
    client.set_header('uid', '4')
    client.set_header('key', 'ab97f63764b608f6d01909d67b4a1c6d')
    client.set_body("rstr", 123)
    client.set_body("eid", 10)
    client.send()
    client.check_status_code_is_200()
    client.check_res_times_less_than(1000)
    client.check_json_value('error_code', 0)


