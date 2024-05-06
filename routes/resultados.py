from flask import render_template, Blueprint
from models import Vote, User
from peewee import fn
import plotly.graph_objs as go

resultado_bp = Blueprint('resultado', __name__)

@resultado_bp.route('/resultado')
def resultados():
    print("Acessou a rota /resultados")
    # Consultar o banco de dados para contar os votos de cada candidato
    resultados = Vote.select(Vote.voted_for, fn.COUNT(Vote.id).alias('total_votos')).group_by(Vote.voted_for)

    # Extrair os dados para plotar o gráfico de barras
    candidatos = []
    votos = []
    for resultado in resultados:
        candidato = User.get(User.id == resultado.voted_for)
        candidatos.append(candidato.nome)
        votos.append(resultado.total_votos)
        print(f"Candidato: {candidato.nome}, Votos: {resultado.total_votos}")

    # Criar o gráfico de barras
    grafico = go.Figure(data=[go.Bar(x=candidatos, y=votos)])

    # Converter o gráfico em HTML
    grafico_html = grafico.to_html(full_html=False)
    print(f"HTML do gráfico: {grafico_html}")

    return render_template('resultados.html', grafico_html=grafico_html)