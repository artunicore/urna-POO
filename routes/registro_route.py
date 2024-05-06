from flask import render_template, request, redirect, url_for, Blueprint
from models import User

registro_bp = Blueprint('cadastro', __name__)

@registro_bp.route('/registrar_usuario', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':

        if not request.form:
            return render_template('mensagem.html', exibir_modal_erro=True)


        nome = request.form['nome']
        cpf = request.form['cpf']
        bloco = request.form['bloco']
        apartamento = request.form['apartamento']
        tipo = request.form['tipo']
        

        # Verificar se o usuário já está registrado
        if User.select().where(User.cpf == cpf).exists():
            return render_template('mensagem.html', mensagem='Usuário já registrado.')

        # Criar um novo usuário no banco de dados
        User.create(nome=nome, cpf=cpf, bloco=bloco, apartamento=apartamento, tipo=tipo)
    
        return redirect(url_for('home'))

    return render_template('cadastro.html')