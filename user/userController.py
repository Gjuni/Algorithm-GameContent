from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from datetime import datetime
from config.mongodb import get_db
from user.userService import loginService, generateCode
# 1. Blueprint 객체를 생성합니다. route 정의 ./user 기본 라우트
user = Blueprint('user', __name__, url_prefix='/user')


@user.route('/') # /user
def index():
    return render_template('user.html')

# 인증 코드 요청
@user.route('/code', methods=['POST'])
def code():
    email = request.json.get('email')
    check = generateCode(email)

    if check == False:
        return jsonify({"success": False})
    else :
        # 작업이 성공했음을 알리는 JSON 응답을 반환합니다.
        return jsonify({"success": True})
        
    


# 로그인 로직
@user.route('/login', methods=['POST'])
def login():
    email = request.form['email'] ## html에서 name 속성을 통해 받은 값을 받음.
    password = request.form['password'] ## id로 html에서 식별함.

    check = loginService(email, password)
    
    if check:
        print("login success")
        return redirect(url_for('thread.allThreads'))  # 성공 시 thread_all.html로 이동
    else :
        print("login fail")
        return render_template('user.html')