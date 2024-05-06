from flask import Flask ,render_template

#Rotas
from routes.eleicoes_route import eleicao_bp
from routes.registro_route import registro_bp
from routes.resultados import resultado_bp

#Database
from models import initialize_db

#inicializa o Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'

#blueprints
app.register_blueprint(eleicao_bp, url_prefix='/eleicao')
app.register_blueprint(registro_bp, url_prefix='/cadastro')
app.register_blueprint(resultado_bp, url_prfix='/resultado')

#rota da pagina inicial
@app.route('/')
def home():
    return render_template('index.html')

initialize_db()

if __name__ == "__main__":
    app.run(debug=True)