import os
from flask import Flask, render_template, request, redirect,url_for
from repository import HGRepository as Repository

app = Flask(__name__)


REPO_DIR='repos'

@app.route("/")
def list_of_repos():
    return render_template('repos.html', repos=os.listdir(REPO_DIR))

@app.route("/repo/<repo_path>/<rev>/")
def repo(repo_path,rev):
    repo=Repository(os.path.join(REPO_DIR, repo_path))
    file_data=dict((f,repo.file(f,rev)) for f in repo.list_files(rev))
    return render_template('repo.html', files=file_data, 
                           repo_path=repo_path, rev=rev,
                           message=repo.message(rev),
                           ancestors=reversed(repo.ancestors(rev)),
                           descendants=repo.descendants(rev))

@app.route("/repo/<repo_path>/<rev>/new_revision", methods=['POST'])
def new_revision(repo_path, rev):
    repo=Repository(os.path.join(REPO_DIR, repo_path))
    message=request.form['message']
    filedata=request.form.to_dict()
    filedata.pop('message')
    new_rev=repo.commit('DEFAULT USER', message, rev, filedata)
    print "NEW REVISION: ",new_rev
    return redirect(url_for('repo', repo_path=repo_path, rev=new_rev))

if __name__ == "__main__":
    app.run(debug=True)
