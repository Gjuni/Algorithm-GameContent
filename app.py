from flask import Flask
from flask import render_template, Blueprint

from user.userController import user
from thread.threadController import thread
from comment.commentController import comment



app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

app.register_blueprint(user)
app.register_blueprint(thread)
app.register_blueprint(comment)


if __name__ == "__main__":
    app.run(debug=True)