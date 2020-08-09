import pymysql

#1
connect = pymysql.connect(host='rm-2zekunr72cc85tf49no.mysql.rds.aliyuncs.com',
                port=3306, user='root', password='liulaoshi@123', db='event')

#2游标
cursor = connect.cursor()

#3 执行语句---影响条数
cursor.execute('select title from api_event')

#4 获取结果
# cursor.fetchone()

#多维元组((),(),())
print(cursor.fetchall())

