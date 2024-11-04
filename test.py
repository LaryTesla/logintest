# pymysql用connect方法进行连接
import pymysql

conn = pymysql.connect(host='localhost', port=3306,
                       user='root', passwd='123456',
                       database='demo01', charset='utf8mb4')


def con_my_sql(sql_code):
    try:
        conn.ping(reconnect=True)  # 保证数据库连接正常
        print(sql_code)
        # 通过游标对象对数据库服务器发出sql语句
        cursor = conn.cursor(pymysql.cursors.DictCursor)  # 返回数据是字典形式而不是数组
        cursor.execute(sql_code)
        # 提交
        conn.commit()
        # 关闭连接
        cursor.close()
        return cursor  # 普通执行返回1 就是执行成功

    except pymysql.MySQLError as err_massage:
        # 回滚
        conn.rollback()
        # 关闭连接
        conn.close()
        return type(err_massage)(err_massage)


# username = "张四"
# pwd = '123456'
# code = "INSERT INTO `login_user` (`username`,`password`) VALUES ('%s','%s')" % (username, pwd)
# print(con_my_sql(code))

# name = "张四"
# # # code = "select * from login_user"
# code = "select * from login_user where username = '%s'" % (name)
# cursor_ans = con_my_sql(code)
# cursor_select = cursor_ans
# print(cursor_select)
# a = cursor_ans.fetchall()
# print(a)  # 查询测试
# print(a[0]['password'])
# print(a[0])
