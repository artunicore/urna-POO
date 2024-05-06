#lista para testar se as database tão recebendo informação

from models import *

lista_voto = Vote.select()
lista_users = User.select()

for u in lista_users:
    print('-', u.id,u.nome,u.cpf, u.bloco, u.tipo)