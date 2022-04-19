from flask import Flask, render_template, request, url_for
from markupsafe import escape
import requests
import json

app = Flask(__name__)

payload = []
data = requests.get('https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/users').json()



@app.route('/')
def index():
	return render_template('home.html', data=data)

@app.route('/perfil/<string:perfil_id>', methods=['POST', 'GET'])
def perfil(perfil_id):
	perfil_id=perfil_id
	for key in data:
		if key['id'] == perfil_id:
			perfil = key['name']
	return render_template('perfil.html', perfil=perfil)



if __name__ == '__main__':
	app.run(debug=True, port=8089)