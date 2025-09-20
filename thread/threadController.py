from flask import Blueprint, render_template, request, redirect, url_for, send_file
from datetime import datetime, timezone  # UTC는 timezone.utc로 사용 가능
from config.mongodb import get_db
from bson.objectid import ObjectId
from config.RSS import dailySecure, downloadDailySecure
from config.RSS import sercureRule, downloadsercureRule

thread = Blueprint('thread', __name__, url_prefix='/thread')

@thread.route('/write', methods=['GET'])
def writePage():
    print("check writepage")
    return render_template('thread_write.html')

# 글 작성 처리 (POST)
@thread.route('/upload', methods=['POST'])
def writePost():
    print("check writepost")
    db = get_db("school")
    threads = db['thread']

    title = request.form['title']
    body = request.form['body']

    threads.insert_one({
        "threadTitle": title,
        "threadBody": body,
        "uploadDate": datetime.now(timezone.utc)
    })

    return redirect(url_for('thread.allThreads'))

# 글 전체 보기 (목록)
@thread.route('/all', methods=['GET'])
def allThreads():
    print("check allthread")
    db = get_db("school")
    
    threads = list(db['thread'].find().sort("uploadDate", -1))
    
    return render_template('thread_all.html', threads=threads)


# 글 상세 보기
@thread.route('/<thread_id>')
def getOne(thread_id):
    convId = ObjectId(thread_id)
    db = get_db("school")

    doc = db['thread'].find_one({"_id": convId})
    
    if 'comments' not in doc:
        doc['comments'] = []
    
    return render_template('thread_spe.html', post=doc)



@thread.route('/dailySecure', methods=['GET'])
def dailyNews():
    feed = dailySecure()
    return render_template('daily_rss.html', feed=feed)

@thread.route('/secureNews', methods=['GET'])
def secureNews():
    feed = sercureRule()
    return render_template('secureRule.html', feed=feed)

@thread.route('/downloadDaily', methods=['GET'])
def downloadDaily():
    buffer, filename = downloadDailySecure()
    return send_file(
        buffer,
        download_name=filename,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True
    )

@thread.route('/downloadSecure', methods=['GET'])
def downloadSecure():
    buffer, filename = downloadsercureRule()
    return send_file(
        buffer,
        download_name=filename,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        as_attachment=True
    )
