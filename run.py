import time
import requests
from flask import Flask, session, request, redirect, url_for, render_template, Response
from model import sendmsg
from model.changepassword import Change
from model.login import Login
from model.md5 import Md5
from model.register import Users
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
lg = logging.getLogger("关键信息")
lg.setLevel("DEBUG")

app = Flask(__name__)
app.secret_key = 'LoenDSdtj\9bX#%@!!*(0&^%)'

name_sql = 'xiaoli'
password_sql = '123456'


@app.route('/')
def defalut():
    return redirect(url_for("login"))


@app.route('/login')
def login():
    return render_template("auth/login.html")


@app.route('/do_login', methods=['POST'])
def do_login():
    try:
        co = request.cookies['user_name']
        return redirect(url_for('show'))
    except:
        log = Login()
        for i in log.chaXunuser():
            if i[0] == request.form.get('user_name'):
                if i[1] == request.form.get('password'):
                    name = request.form.get('user_name')
                    session['user_name'] = name
                    res = Response('add cookies')
                    # 设置cookie并且设置有效期
                    res.set_cookie(key='user_name', value=request.form.get('user_name'), expires=time.time() + 6 * 60)
                    lg.info(request.form.get('user_name') + " 登录成功")
                    return redirect(url_for('show'))
                else:
                    lg.error("用户名或密码错误")
                    return render_template("auth/login.html", error="用户名或密码错误")
        else:
            lg.error("用户名不存在")
            return render_template("auth/login.html", error="用户不存在")


@app.route('/do_register', methods=['POST'])
def do_register():
    user = request.form.get('user')
    check_code = request.form.get('check_code')
    password = request.form.get('pass')
    re_password = request.form.get('repass')
    if check_code == session["check" + user]:
        if user == session[user]:
            if password == re_password:
                if password != "" and user != "":
                    try:
                        users = Users()
                        users.add_user(user, password)
                        lg.info(user + " 注册成功")
                        return "恭喜注册成功"
                    except:
                        lg.error(user + " 已注册账号")
                        return render_template("auth/register.html", re_error="该用户已注册")

                else:
                    return render_template("auth/register.html", re_error="用户名和密码不能为空")
            else:
                return render_template("auth/register.html", re_error="两次密码不一致")
        else:
            return render_template("auth/register.html", re_error="与当前手机号不一致")
    else:
        return render_template("auth/register.html", re_error="验证码不正确")
    pass


@app.route('/show')
def show():
    return render_template("blog/index.html", name=session['user_name'])


@app.route('/do_show', methods=['POST'])
def do_show():
    a = request.form.get("op")
    print(a)
    appid = "20220314001124419"
    q = request.form.get('before')
    q = q
    md = Md5()
    md.q = q
    from1 = "zh"
    form2 = "en"
    to = "en"
    to1 = "zh"
    salt = "123456"
    sign = md.encry()
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate?q=" + q + "&from=" + from1 + "&to=" + to + "&appid=" + appid + "&salt=" + salt + "&sign=" + sign
    url1 = "http://api.fanyi.baidu.com/api/trans/vip/translate?q=" + q + "&from=" + form2 + "&to=" + to1 + "&appid=" + appid + "&salt=" + salt + "&sign=" + sign

    try:
        if request.form.get("op") == "ze":
            re = requests.get(url)
            res = re.json()["trans_result"][0]["dst"]
            return render_template("blog/index.html", name=session["user_name"], shuru=q, shuchu=res)
        else:
            re1 = requests.get(url1)
            res = re1.json()["trans_result"][0]["dst"]
            return render_template("blog/index_.html", name=session["user_name"], shuru=q, shuchu=res)

    except:
        if request.form.get("op") == "ze":
            return render_template("blog/index.html", name=session["user_name"], error="请输入翻译的内容")
        else:
            return render_template("blog/index_.html", name=session["user_name"], error="请输入翻译的内容")


@app.route('/logout')
def logout():
    session.pop('user_name', None)
    return redirect(url_for('login'))


@app.route('/do_send', methods=["GET"])
def do_send():
    req = request.args.get("name")
    lg.info(req + " 注册&修改")
    send = sendmsg.Send()
    send.phone_number = req
    send.sendMessage()
    session["check" + req] = send.check_code
    lg.info(send.check_code + " 验证码")
    session[req] = req
    return "send"


@app.route('/register')
def register():
    return render_template("auth/register.html")


@app.route('/change_')
def change_():
    return render_template("auth/change_.html")


@app.route('/change', methods=['POST'])
def change():
    try:
        req = request.form.get("phone")
        # print(req)
        if req == session[req]:
            if session['check' + req] == request.form.get("code"):
                return render_template("auth/change.html", ph_one=session[req])
            else:
                return render_template("auth/change_.html", phone=req, error="手机号或验证码不正确")
        else:
            return render_template("auth/change_.html", phone=req, error="手机号或验证码不正确")
    except:
        return render_template("auth/change_.html", error="请先获取验证码")


@app.route('/do_change', methods=["POST"])
def do_change():
    new_pass = request.form.get('new_pass')
    re_new_pass = request.form.get('re_new_pass')
    if new_pass == re_new_pass and new_pass != "" and re_new_pass != "":
        if session[request.form.get("ph_one")] == request.form.get("ph_one"):
            change = Change()
            change.change_user(new_pass, session[request.form.get("ph_one")])
            return "修改密码成功"

    pass


if __name__ == '__main__':
    app.run(port=5000, debug=True)
