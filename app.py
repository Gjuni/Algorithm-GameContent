from flask import Flask
from flask import render_template, Blueprint

from user.userController import user
from thread.threadController import thread


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

app.register_blueprint(user)
app.register_blueprint(thread)

if __name__ == "__main__":
    app.run(debug=True)