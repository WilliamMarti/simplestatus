from flask import Flask, request, session, redirect, render_template, g, url_for, jsonify
from functools import wraps

import requests, sqlite3, os,socket



application = Flask(__name__)
application.config['DEBUG'] = True
application.secret_key = 'as3r14saf3tGWEF'


@application.route("/")
def home(title=None):

	title = "Simple Status"

	servicename = "github"
	servicechecktype = "https"
	serviceurl = 'https://github.com/'
	status = requests.get(serviceurl).status_code

	servicehost = 'github.com'
	port = 443
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	tcpstatus = "Up"

	try:

		s.connect((servicehost, port))

	except Exception:

		tcpstatus = "Down"

	finally:

		s.close()


	return render_template('home.html', 
							title=title, 
							servicename=servicename, servicechecktype=servicechecktype, serviceurl=serviceurl, status=status,
							tcp="tcp", tcpstatus=tcpstatus)

if __name__ == "__main__":
	application.run(host='0.0.0.0')