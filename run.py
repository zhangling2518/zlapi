import pytest
import subprocess
import time
from dingtalkchatbot.chatbot import DingtalkChatbot
from cases.conftest import *
from core.util import *

if __name__ == '__main__':
    tmp = time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    cmd = get_cases()
    cmd.append('-s')
    cmd.append('--alluredir=./report/json')
    cmd.append('--clean-alluredir')
    cmd.append('--reruns=3')
    pytest.main(cmd)

    # subprocess.Popen('allure generate ./report/json -o ./report/html/final', shell=True)
    subprocess.call('allure generate ./report/json -o ./report/html/'+tmp, shell=True)
    # webhook = 'https://oapi.dingtalk.com/robot/send?access_token=f021392bde0168121fb42b113bd825f60513dd49c525888c38ca3c45e4d4138b'
    # xiaoding = DingtalkChatbot(webhook)
    # xiaoding.send_text(msg='接口测试结果：执行{total}，成功{passed}， 失败{failed}，报告地址:xxxxxx'.format(
    #     total=DATA['total'], passed=DATA['passed'], failed=DATA['failed']
    # ), is_at_all=False,
    #                    at_mobiles=['15810215321'])
