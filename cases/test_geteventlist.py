from core.client import *
from core.util import *

@feature('查询活动列表接口')
@title('无条件查询')
@order(order=2)
def test_geteventlist01(get, set):
    '''
    查询所有活动
    '''
    client = Client(url='get_eventlist/', method=METHOD.GET, body_type=BODY_TYPE.FORM,
                    params={"rstr": get('rstr')})
    client.set_header("uid", get('uid'))
    client.set_header("key", get('key'))
    client.send()
    client.check_status_code_is_200()
    client.check_res_times_less_than(10)
    client.check_json_value('error_code', 0)
    id = client.json_path_value('event_list[0].id')
    set("event_id", id)


def test_geteventlist02(depends):
    '''
    查询所有活动
    '''
    client = Client(url='get_eventlist/', method=METHOD.GET, body_type=BODY_TYPE.FORM,
                    params={"key": depends('A', {"username": "aaaaa"}, 'data.key')})
