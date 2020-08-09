import requests
import jsonpath
import allure
import json

class Client(object):
    base_url = 'http://123.56.99.53:9000/event/api/'

    def __init__(self, url, method, body_type=None, timeout=3, params=None):
        # self.url = Client.base_url + url
        self.url = url
        self.method = method
        self.params = params
        self.body_type = body_type
        self.timeout = timeout
        self.headers = {}
        self.data = {}
        self.res = None

    # @property
    # def headers(self):
    #     return self.__headers

    def set_header(self, key, value):
        self.headers[key] = value

    def set_headers(self, data):
        if isinstance(data, dict):
            self.headers = data
        else:
            raise Exception('请求头信息请以字典形式传递!')

    def set_body(self, key, value):
        self.data[key] = value

    def set_bodys(self, data):
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception('请求正文信息请以字典形式传递!')

    @allure.step('接口详细信息:')
    def send(self):
        if self.method == 'GET':
            self.res = requests.get(url=self.url, headers=self.headers,
                                    params=self.params, timeout=self.timeout)
        elif self.method == 'POST':
            if self.body_type == 'form':
                self.set_header('Content-Type', 'application/x-www-form-urlencoded')
                self.res = requests.post(url=self.url, headers=self.headers, params=self.params,
                                    data=self.data, timeout=self.timeout)
            elif self.body_type == 'files':
                self.res = requests.post(url=self.url, headers=self.headers, params=self.params,
                                         files=self.data, timeout=self.timeout)
            elif self.body_type == 'json':
                self.set_header('Content-Type', 'application/json')
                self.res = requests.post(url=self.url, headers=self.headers, params=self.params,
                                    json=self.data, timeout=self.timeout)
            else:
                raise Exception('请求正文格式错误!')
        allure.attach(self.url, '请求地址', allure.attachment_type.TEXT)
        allure.attach(self.method, '请求方法', allure.attachment_type.TEXT)
        allure.attach(json.dumps(self.headers), '请求头', allure.attachment_type.TEXT)
        allure.attach(json.dumps(self.data), '请求正文', allure.attachment_type.TEXT)
        allure.attach(str(self.res.status_code), '响应状态码', allure.attachment_type.TEXT)
        allure.attach(json.dumps(self.res_text), '响应正文', allure.attachment_type.TEXT)
        allure.attach(json.dumps(requests.utils.dict_from_cookiejar(self.cookies)), 'Cookie', allure.attachment_type.TEXT)
    @property
    def status_code(self):
        if self.res is not None:
            return self.res.status_code
        else:
            print('响应内容为空，状态码获取失败')
            return None

    @property
    def res_times(self):
        if self.res is not None:
            return round(self.res.elapsed.total_seconds()*1000)
        else:
            print('响应内容为空，响应时间获取失败')
            return None

    @property
    def res_text(self):
        if self.res is not None:
            return self.res.text
        else:
            print('响应内容为空，响应内容获取失败')
            return None

    @property
    def res_to_json(self):
        if self.res is not None:
            return self.res.json()
        else:
            print('响应内容为空，响应内容获取失败')
            return None

    @property
    def cookies(self):
        if self.res is not None:
            return self.res.cookies
        else:
            print('响应内容为空，cookies获取失败')
            return None

    def json_path_value(self, path):
        if not path.startswith('$.'):
            path = '$.' + path
        result = jsonpath.jsonpath(self.res_to_json, path)
        if self.res_to_json is not None:
            if result:
                return result[0]
            else:
                print('json字段取值失败: {path}'.format(path=path))
                return None
        else:
            print("响应内容为空，响应内容获取失败")

    @allure.step('响应状态码检查')
    def check_status_code_is_200(self):
        assert self.status_code == 200, '响应状态码错误。实际结果【{a}】，预期结果【{b}】'.format(
            a=self.status_code, b=200
        )
        # print('响应状态码检查成功')

    @allure.step('响应状态码检查')
    def check_status_code(self, status_code):
        assert self.status_code == status_code, '响应状态码错误。实际结果【{a}】，预期结果【{b}】'.format(
            a=self.status_code, b=status_code
        )
        print('响应状态码检查成功')

    @allure.step('响应时间检查')
    def check_res_times_less_than(self, times):
        assert self.res_times < times, '响应超时。实际结果【{a} ms】，预期结果【小于 {b} ms】'.format(
            a=self.res_times, b=times
        )
        print('响应时间检查成功')

    def check_res_equal(self, b):
        assert self.res_text == b, '响应内容不一致。实际结果【{a}】，预期结果【{b}】'.format(
            a=self.res_text, b=b
        )

    def check_res_contains(self, b):
        assert b in self.res_text, '响应内容未包含关键信息。实际结果【{a}】，关键信息为【{b}】'.format(
            a=self.res_text, b=b
        )

    @allure.step('响应json节点检查')
    def check_json_value(self, path, b):
        value = self.json_path_value(path)
        assert str(value) == str(b), '响应json节点检查失败。实际结果【{a}】，预期结果【{b}】， json节点的路径【{path}】'.format(
            a=value, b=b, path=path
        )
        print('响应json节点检查成功')

class METHOD(object):
    POST = 'POST'
    GET = 'GET'

class BODY_TYPE(object):
    FORM = 'form'
    FILES = 'files'
    JSON = 'json'


