import os
from flask import Flask, render_template
app = Flask(__name__)


REPO_DIR='repos'

@app.route("/")
def list_of_repos():
    return render_template('repos.html', repos=os.listdir(REPO_DIR))


if __name__ == "__main__":
    app.run(debug=True)
