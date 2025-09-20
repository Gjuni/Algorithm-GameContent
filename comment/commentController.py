from flask import Flask
from flask import render_template, Blueprint, request, redirect, url_for
from config.mongodb import get_db
from bson.objectid import ObjectId
from datetime import timedelta

from datetime import datetime, timezone  # UTC는 timezone.utc로 사용 가능

comment = Blueprint('commnet', __name__, url_prefix='/commnet')

# KST(한국 표준시) = UTC+9
KST = timezone(timedelta(hours=9))

@comment.route("/<thread_id>", methods=['POST'])
def add(thread_id):
    db = get_db("school")
    threads = db['thread']
    
    try:
        convId = ObjectId(thread_id)
        conmmentText = request.form.get('comments', '').strip()

        if conmmentText:
            now = datetime.now(KST)
            threads.update_one(
                {"_id": convId}, 
                {"$push": {"comments": {"comment": conmmentText, "uploadDate": now}}}
            )
    except Exception as e:
        print(f"댓글 추가 중 오류 발생: {e}")
    
    return redirect(url_for('thread.getOne', thread_id=thread_id)) # 다시 본 게시물로 넘어감
