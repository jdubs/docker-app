from flask import render_template
from app import app
from git import Repo

import os

@app.route('/')
@app.route('/index')
def index():
    join = os.path.join
    repo = Repo()
    git_data = list(repo.iter_commits('master', max_count=50))
    return render_template('index.html', git_data=git_data)
