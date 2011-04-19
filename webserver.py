import os
from flask import Flask, render_template, request, redirect,url_for
from repository import HGRepository as Repository

app = Flask(__name__)


@app.route("/")
def list_of_repos():
    return render_template('repos.html', repos=os.listdir(REPO_DIR))

@app.route("/create_repo", methods=['POST'])
def create_repo():
    repo_path=request.form['repo_path']
    Repository.init(os.path.join(REPO_DIR,repo_path))
    repo=Repository(os.path.join(REPO_DIR,repo_path))
    repo.commit('DEFAULT USER', 'Initial commit', 0, {'snippet':''})
    return redirect(url_for('repo', repo_path=repo_path, rev='tip'))

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
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--repositories", dest="repositories", default='repositories',
                      help="store repositories in DIR", metavar="DIR")

    (options, args) = parser.parse_args()
    
    # make repository directory
    import os
    global REPO_DIR
    REPO_DIR=options.repositories
    if not os.path.exists(REPO_DIR):
        # slight race condition
        os.makedirs(REPO_DIR)

    app.run(debug=True)
