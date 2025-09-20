from flask import Flask
from flask import render_template, Blueprint, request, redirect, url_for
from config.mongodb import get_db
from bson.objectid import ObjectId



comment = Blueprint('commnet', __name__, url_prefix='/commnet')

@comment.route("/<thread_id>")
def add(thread_id):
    convId = ObjectId(thread_id)
    db = get_db("school")

    doc = db['thread'].find_one({"_id": convId})
    
    if doc :
        comments = request.form['comments']

        if comments == "" :
            # comment 가 존재하지 않습니다.
            return redirect(url_for('thread.getOne', thread_id=thread_id))
        else :
            # comment 가 존재합니다.
            threads = db['thread']

            threads.update_one({"_id": convId}, {"$push": {"comments": {"comment": comments, "uploadDate": datetime.now(timezone.utc)"}}})