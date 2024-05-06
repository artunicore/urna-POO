from flask import render_template, redirect, url_for, Blueprint, request
from models import User, Vote

eleicao_bp = Blueprint('eleicao', __name__)

@eleicao_bp.route('/votar', methods=['GET', 'POST'])
def votar():
    if request.method == 'POST':
        if not request.form:
            return render_template('mensagem.html', exibir_modal_erro=True)


        cpf = request.form['cpf']
        candidato_id = request.form['candidato_id']

        if Vote.select().where(Vote.user == cpf).exists():
            return render_template('mensagem.html', mensagem='Você já votou.')

        usuario = User.get(User.cpf == cpf)
        if Vote.select().where(Vote.apartamento == usuario.apartamento).exists():
            return render_template('mensagem.html', mensagem='Já foi registrado um voto neste apartamento.')

        Vote.create(user=cpf, voted_for=candidato_id, apartamento=usuario.apartamento)
        return redirect(url_for('eleicao.votar'))

    candidatos = User.select().where(User.tipo == 'candidato')
    return render_template('votacao.html', candidatos=candidatos)