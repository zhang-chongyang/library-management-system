import os
from os import system, name
import pymssql

# 学号
student_number = "201900800290"
# 系统名
sys_name = "BOOKS"
# 数据库名
db_name = sys_name + "_" + student_number
# 系统文件路径
path = "D:\\" + db_name + "\\DB\\"
# 数据库路径
db_file_path = path + db_name
# 日志名
log_name = db_name + "_log"
# 日志文件路径
log_file_path = path + log_name


# 建库建表
def createDB():
    # 开启自动提交
    conn.autocommit(True)
    # 确保数据库文件保存路径存在
    if not os.path.exists(path):
        os.makedirs(path)
    # 建立数据库
    create_db_sql = "create database " + db_name + " on primary (name = '" + db_name + "',\
            filename ='" + db_file_path + ".mdf') \
            log on (name = '" + log_name + "',filename = '" + log_file_path + ".ldf') "
    cur.execute(create_db_sql)
    formatePrint('数据库"' + db_name + '"创建成功')
    conn.autocommit(False)


def dropDB():
    conn.autocommit(True)
    drop_db_sql = "drop database " + db_name
    cur.execute(drop_db_sql)
    formatePrint('数据库"' + db_name + '"已删除')
    conn.autocommit(False)


# 系统格式化输出
def formatePrint(sth):
    print("【" + sth + "】")


# 控制台清屏
def clear():
    # for windows
    if name == 'nt':
        system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        system('clear')


# 提示用户继续
def goAhead():
    input("按任意键继续...")
    clear()


# 用户界面通过输入主机地址、端口号、账号、密码完成数据库连接。
clear()
os.system("color 02")
print('''
   ____   _                        __ _                _     _                    __      __                 __ _  
  |_  /  | |_     __ _    _ _     / _` |    o O O   _ | |   (_)    __ _      o O O\ \    / /__ _    _ _     / _` | 
   / /   | ' \   / _` |  | ' \    \__, |   o       | || |   | |   / _` |    o      \ \/\/ // _` |  | ' \    \__, | 
  /___|  |_||_|  \__,_|  |_||_|   |___/   TS__[O]  _\__/   _|_|_  \__,_|   TS__[O]  \_/\_/ \__,_|  |_||_|   |___/  

''')
print("=======图书管理系统初始化=========")
host = input("请输入主机地址：")
port = input("请输入端口号：")
user = input("请输入数据库登录账号：")
password = input("请输入数据库登录密码：")
formatePrint("正在登录...")
# 连接数据库
conn = pymssql.connect(host=host, database='master', user=user, password=password)
cur = conn.cursor()
formatePrint("登录成功")
s = input("按任意键继续...")
clear()
# 判断数据库是否已经存在
sql = "select * from sys.databases where name  = '" + db_name + "'"
cur.execute(sql)
data = cur.fetchall()
if len(data) == 0:
    while True:
        print("=======图书管理系统初始化=========")
        ch = input("第一次使用本系统，是否初始化数据库？（Y/N）")
        if ch == 'Y' or ch == 'y':
            formatePrint("正在初始化数据库...")
            createDB()
            formatePrint("初始化数据库成功")
            goAhead()
            break
        elif ch == 'N' or ch == 'n':
            formatePrint("退出系统")
            goAhead()
            break
        else:
            formatePrint("非法字符，请重新输入")
            goAhead()
else:
    while True:
        print("=======图书管理系统初始化=========")
        ch = input("数据库已存在，是否重置数据库？（Y/N）")
        if ch == 'Y' or ch == 'y':
            formatePrint("正在重置数据库...")
            dropDB()
            createDB()
            formatePrint("数据库重置成功")
            goAhead()
            break
        elif ch == 'N' or ch == 'n':
            formatePrint("退出系统")
            goAhead()
            break
        else:
            formatePrint("非法字符，请重新输入")
            goAhead()
print("===================================")
