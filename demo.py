import xlrd
def get_data_from_sheet(name):
    data = []
    workbook = xlrd.open_workbook('../suite.xlsx')
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