class Morador:
    def __init__(self, nome, apartamento):
        self.nome = nome
        self.apartamento = apartamento

class Candidato(Morador):
    def __init__(self, nome, apartamento, numero):
        super().__init__(nome, apartamento)
        self.numero = numero
        self.votos = 0

class Apartamento:
    def __init__(self, numero):
        self.numero = numero
        self.moradores = []
        self.votou = False

    def adicionar_morador(self, morador):
        self.moradores.append(morador)

class Urna:
    def __init__(self):
        self.candidatos = []
        self.apartamentos = []
        self.votacao_terminou = False

    def adicionar_candidato(self, candidato):
        self.candidatos.append(candidato)

    def adicionar_apartamento(self, apartamento):
        self.apartamentos.append(apartamento)

    def votar(self, candidato, apartamento):
        if not apartamento.votou:
            candidato.votos += 1
            apartamento.votou = True

    def verificar_termino_votacao(self):
        for apartamento in self.apartamentos:
            if not apartamento.votou:
                return False
        self.votacao_terminou = True
        return True

def main():
    # Cadastro
    moradores = []
    candidatos = []

    while True:
        nome = input("Digite o nome do morador (ou 'fim' para encerrar o cadastro): ")
        if nome.lower() == 'fim':
            break

        apartamento = int(input("Digite o número do apartamento: "))
        eh_candidato = input("O morador é candidato? (s/n): ").lower() == 's'

        if eh_candidato:
            numero_candidato = int(input("Digite o número do candidato: "))
            candidato = Candidato(nome, apartamento, numero_candidato)
            candidatos.append(candidato)
            moradores.append(candidato)
        else:
            morador = Morador(nome, apartamento)
            moradores.append(morador)

    # Configuração
    urna = Urna()
    for candidato in candidatos:
        urna.adicionar_candidato(candidato)

    apartamentos = []
    for morador in moradores:
        if morador not in candidatos:
            numero_apartamento = morador.apartamento
            if numero_apartamento not in apartamentos:
                apartamento = Apartamento(numero_apartamento)
                apartamento.adicionar_morador(morador)
                urna.adicionar_apartamento(apartamento)
                apartamentos.append(numero_apartamento)
            else:
                for ap in urna.apartamentos:
                    if ap.numero == numero_apartamento:
                        ap.adicionar_morador(morador)

    # Votação
    print("\033[1;32m         CANDIDATOS    \033[m")
    for candidato in urna.candidatos:
      print(f''' \033[1;33m {'-' * 30}
            Nome: {candidato.nome}
            Número: {candidato.numero}\033[m''')
    while not urna.votacao_terminou:
        for apartamento in urna.apartamentos:
            if not apartamento.votou:
                print(f"\033[1;30m\nMoradores do apartamento {apartamento.numero}:")
                for morador in apartamento.moradores:
                    print(morador.nome)
                voto = int(input("Digite o número do candidato em quem deseja votar: \033[m"))
                for candidato in urna.candidatos:
                    if candidato.numero == voto:
                        urna.votar(candidato, apartamento)
                        break

        urna.verificar_termino_votacao()

    # Publicação dos resultados
    print("\nResultado da eleição:")
    for candidato in urna.candidatos:
        print(f"Candidato {candidato.numero}: {candidato.nome} - Votos: {candidato.votos}")


if __name__ == "__main__":
    main()