from django.forms import DateTimeField
from flask import Flask, render_template, request, url_for, redirect, flash
from markupsafe import escape
import requests
import json
import datetime

app = Flask(__name__)
nome = 'jesiel'
sexo = 'male'
avatar = requests.get(f'https://avatars.dicebear.com/api/{sexo}/{nome}.png')
print(avatar.text)


@app.route('/')
def index():
	requisicao = requests.get('https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/users').json()
	return render_template('home/home.html', data=requisicao)

@app.route('/perfil/<string:perfil_id>', methods=['POST', 'GET'])
def perfil(perfil_id):
	perfil_id=perfil_id
	# for key in data:
	# 	if key['id'] == perfil_id:
	# 		perfil = key['name']

	requisicao = requests.put(f'https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/users/{perfil_id}').json()
	for key in requisicao:
		print(key)
	return render_template('perfil.html', perfil=requisicao)

@app.route('/pagina_add', methods=['POST', 'GET'])
def pagina_add():
	return render_template('add_user.html')

@app.route('/pagina_add/salvar', methods=['POST', 'GET'])
def salvar():
	if request.method == 'POST':
		nome = request.form['nome']
		email = request.form['email']
		idade = request.form['idade']
		sexo = request.form['sexo']
		date = datetime.datetime.now().strftime('%d/%m/%Y ás %H:%M')
		avatar = f'https://avatars.dicebear.com/api/{sexo}/{nome}.png'
		
		
		try:
			requisicao = requests.post('https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/users', data=({'name': nome, 'avatar': avatar, 'email': email, 'idade': idade, 'createdAt': date}))
			flash(f'{nome}, {avatar}, {email} {idade} anos', 'success')
			return redirect(url_for('index'))
		except:
			flash(f'Não foi possivel adicionar o usuário {nome}', 'warning')

	return render_template('home/home.html')

@app.route('/delete_user/<string:user_id>', methods=['GET'])
def delete_user(user_id):
	print(user_id)
	try:
		requisicao = requests.delete(f'https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/users/{user_id}')
		flash(f'{user_id} deletado com sucesso.', 'danger')
	except:
		flash(f'{user_id} deletado com sucesso.', 'warning')

	return redirect(url_for('index'))




if __name__ == '__main__':
	app.secret_key='12345'
	app.run(debug=True, port=8089)