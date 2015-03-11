import os,sys

def fw(path,data):
	f = open(path,"w")
	f.write(data)
	f.close()

cmds = ['adduser newuser',
		'adduser newuser sudo',
		'sudo apt-get update',
		'sudo apt-get upgrade -y',
		'sudo apt-get install -y python-dev python-pip python-virtualenv nginx gunicorn',
		'sudo mkdir /home/www && cd /home/www',
		'sudo python-virtualenv env',
		'source env/bin/activate',
		'sudo pip install Flask==0.10.1 beautifulsoup4',
		'mkdir /home/www/flask_project']
		
for cmd in cmds:
	os.system(cmd)

path ='/home/www/flask_project/app.py'
data = """# -*- coding:utf-8 -*-
import sys, time, os,db
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask, render_template,send_from_directory

app = Flask(__name__)

@app.route("/")
def main():
	data = db.querries()
	return render_template("entries.html",data = data)

if __name__ == '__main__':
	app.run()

"""

fw(path,data)

os.system('sudo mkdir /home/www/flask_project/static')
path = '/home/www/flask_project/static/index.html'
fw(path,"<h1>Test!</h1>")

cmds2 =	['sudo service nginx restart',
		'sudo rm /etc/nginx/sites-enabled/default',
		'sudo touch /etc/nginx/sites-available/flask_project',
		'sudo ln -s /etc/nginx/sites-available/flask_project /etc/nginx/sites-enabled/flask_project']

for cmd in cmds2:
	os.system(cmd)

path='/etc/nginx/sites-enabled/flask_project'
data ="""server {
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
    location /static {
        alias  /home/www/flask_project/static/;
    }
}"""

fw(path,data)


cmds3= ['sudo service nginx restart',
		'cd /home/www/flask_project && gunicorn app:app -b localhost:8000 &',
		'sudo apt-get install -y supervisor','chown -R newuser /home/www/flask_project/']

for cmd in cmds3:
	os.system(cmd)

path='/etc/supervisor/conf.d/flask_project.conf'
data = """[program:flask_project]
command = gunicorn app:app -b localhost:8000
directory = /home/www/flask_project
user = newuser
"""
fw(path,data)

cmds4 =['sudo pkill gunicorn',
		'sudo supervisorctl reread',
		'sudo supervisorctl update',
		'sudo supervisorctl start flask_project']

for cmd in cmds4:
	os.system(cmd)

path="/etc/init/newscrawler.conf"
initscr = """
start on [2345]
stop on [06]

script
    cd home/www/flask_project
    su newuser -c "python crawler.py"
end script
"""
fw(path,initscr)

print "add rc.local sudo service newscrawler start"