# -*- encoding: utf-8 -*-

import sqlite3
from datetime import datetime
from jenkinsapi.jenkins import Jenkins

try:
    J = Jenkins('http://localhost:8080')
except Exception, e:
    print e
    J = None

db = sqlite3.connect('jobs')
cursor = db.cursor()
# cursor.execute('CREATE TABLE jobs(id INTEGER PRIMARY KEY, name TEXT, status TEXT, time TEXT)')
# db.commit()

if J:
    jobs_list = J.get_jobs_list()
    for job in jobs_list:
        name = '%s' % job
        status = J[name].is_queued_or_running()
        now_time = datetime.now()
        cursor.execute('INSERT INTO jobs(name, status, time) VALUES(?,?,?)', (name, status, now_time))
