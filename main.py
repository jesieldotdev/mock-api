from flask import Flask, render_template, request, url_for, redirect, flash
from markupsafe import escape
import requests
import json

app = Flask(__name__)



@app.route('/')
def index():
	data = requests.get('https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/users').json()

	return render_template('home/home.html', data=data)

@app.route('/perfil/<string:perfil_id>', methods=['POST', 'GET'])
def perfil(perfil_id):
	perfil_id=perfil_id
	for key in data:
		if key['id'] == perfil_id:
			perfil = key['name']
	return render_template('perfil.html', perfil=perfil)

@app.route('/pagina_add', methods=['POST', 'GET'])
def pagina_add():
	return render_template('add_user.html')

@app.route('/pagina_add/salvar', methods=['POST', 'GET'])
def salvar():
	if request.method == 'POST':
		nome = request.form['nome']
		email = request.form['email']
		idade = request.form['idade']
		print(requests.post('https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/users', data=({'name': nome, 'email': email, 'idade': idade})))
		flash(f'{nome},{email} {idade} anos', 'success')
		return redirect(url_for('index'))
	return render_template('home/home.html')

@app.route('/delete_user/<string:user_id>', methods=['GET'])
def delete_user(user_id):
	print(requests.delete('https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/users', json=({'id': user_id})))
	flash(f'{user_id}', 'success')
	return redirect(url_for('index'))




if __name__ == '__main__':
	app.secret_key='12345'
	app.run(debug=True, port=8089)