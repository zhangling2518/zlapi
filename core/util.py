import csv as CSV
import pytest
import allure
import xml.etree.cElementTree as ET
import xlrd

data = pytest.mark.parametrize
order = pytest.mark.run
feature = allure.feature
title = allure.title

#从外部csv文件里，读取回参数化数据
def csv(filename):
    result = []
    with open('./data/'+filename, 'r', encoding='utf-8') as f:
        for i in CSV.reader(f):
            result.append(i)
    return result[1:]

#从config文件中读取要执行的测试用例
def get_cases():
    et = ET.ElementTree(file='./config.xml')
    cases = []
    for i in et.findall('.//用例集合/*'):
        if i.attrib['run'] == '1':

            cases.append('./cases/test_{file_name}.py::test_{method_name}'.format(
                file_name=i.tag.split('-')[0], method_name=i.tag.split('-')[1]
            ))
    return cases


def get_api_info(name):
    et = ET.ElementTree(file='../config.xml')
    url = ''
    method = ''
    body_type = ''
    for i in et.findall('.//接口模板/' + name+'/*'):
        if i.tag == '地址':
            url = i.text

        if i.tag == '方法类型':
            method = i.text

        if i.tag == '正文格式':
            body_type = i.text

    return url, method, body_type

def get_global_info():
    et = ET.ElementTree(file='./config.xml')
    globals = {}
    for i in et.findall('.//全局配置/*'):
        globals[i.tag] = i.text
    return globals

def get_global_data(name):
    data = {}
    workbook = xlrd.open_workbook('./suite.xlsx')
    try:
        sheet = workbook.sheet_by_name(name)
        for i in range(1, sheet.nrows):
            key = sheet.row_values(i)[0]
            value = sheet.row_values(i)[1]
            data[key] = value
        return data
    except xlrd.biffh.XLRDError:
        raise Exception('sheet页不存在')

def get_data_from_sheet(name):
    data = []
    workbook = xlrd.open_workbook('./suite.xlsx')
    try:
        sheet = workbook.sheet_by_name(name)
        headers = sheet.row_values(0)
        for i in range(1, sheet.nrows):
            dic = {}
            for index, value in enumerate(sheet.row_values(i)):
                dic[headers[index]] = value
            data.append(dic)
        return data
    except xlrd.biffh.XLRDError:
        raise Exception('sheet页不存在')