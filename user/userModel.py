import datetime
from config.mongodb import get_db
import random
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
import os
import re

load_dotenv()

## 코드 생성 로직
def generateCodeModel(email):
    db = get_db()
    users_collection = db['users'] ## users 라는 데이터베이스 생성
    
    stringCode = 'abcdefghijklmnopqrstuvwxyz0123456789'
    stringCode = list(stringCode)

    # 6자리 만큼 랜덤으로 뽑아서 문자열 생성
    code = ''.join(random.choice(stringCode) for _ in range(6))

    users_collection.update_one(
        {"email": email},
        {"$set": {"code": code }}, ## 이미 매일이 존재하면 수정함.
        upsert=True
    )

    print(f"인증 코드 생성/저장 완료: {email} / {code}")
    return code

## 메일 전송 로직
def sendmail(mail, code):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    send_email = os.getenv("SECRET_ID")
    send_pwd = os.getenv("SECRET_PASS")

    server.login(send_email, send_pwd)

    # MIMEText를 사용하여 메일 본문과 제목 설정
    body = f"Verify Code : {code}"
    msg = MIMEText(body)
    msg['Subject'] = "Verify Mail Sent"
    msg['From'] = send_email
    msg['To'] = mail

    server.sendmail(send_email, mail, msg.as_string())
    server.quit()

## 사용자 확인 로직
def userPassword(email, password):
    db = get_db()
    users_collection = db['users']

    # DB에서 이메일과 인증 코드가 모두 일치하는 사용자 찾기
    user = users_collection.find_one({"email": email, "code": password})

    if user:
        # 로그인 성공 시 코드 삭제
        users_collection.update_one({"email": user["email"]}, {"$unset": {"code": ""}})
        return True
    
    return False

#이메일 정규식 표현 추가
def checkMail(email) :
    # email 정규식 패턴
    email_pattern = r'[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}'

    check = bool(re.fullmatch(email_pattern, email))

    if check == False:
        return False
    else :
        return True