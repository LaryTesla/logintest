from flask import Flask, render_template, request, redirect,url_for,session
from test import con_my_sql
app = Flask(__name__)
app.secret_key = '123456'
@app.route("/")
def index_login():
    return render_template('login.html')
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index_login'))
@app.route("/register")
def index_register():
    return render_template('register.html')

@app.route("/index")
def index():
    if 'username' in session:
        return render_template('index.html')
    else:
        # 未登录 强制回登录页面
        return redirect(url_for('index_login'))

login_data = {
    "张三":"123456"
}
@app.route("/login", methods=['POST'])
def login():
    name = request.form.get("username")
    pwd = request.form.get("password")

    code = "select * from login_user where username ='%s'" % (name)
    cursor_ans = con_my_sql(code)
    cursor_select = cursor_ans.fetchall()
    print(cursor_select)
    if len(cursor_select) > 0:
        if pwd == cursor_select[0]['password']:
            session['username'] = name
            return redirect(url_for('index')) #url_for函数名
        else:
            return '密码错误 <a href="/">返回登录</a>'
    else:
        return '用户不存在  <a href="/">返回登录</a>'

@app.route("/register", methods=['POST'])
def register():
    name = request.form.get("username")
    pwd = request.form.get("password")
    pwd2 = request.form.get("confirm-password")
    if pwd != pwd2:
        return '两次密码不一致 <a href="/">返回登录</a> '
    code = "select * from login_user where username = '%s'" % (name)

    cursor_ans = con_my_sql(code)
    cursor_select = cursor_ans.fetchall()
    print(cursor_select)
    if len(cursor_select) > 0:
        return '用户已存在 <a href="/">返回登录</a>'
    else:
        code = "INSERT INTO `login_user` (`username`,`password`) VALUES ('%s','%s')" % (name, pwd)
        con_my_sql(code)
        return '注册成功 <a href="/">返回登录</a>'


if __name__ == "__main__":
    app.run(debug=True)
