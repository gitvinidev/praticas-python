class VeiculoEspacial:
    def __init__(self, nome, coordenadas_atuais):
        self.nome = nome
        self.coordenadas_atuais = coordenadas_atuais
        self.log_de_missoes = []

    def mover(self, nova_coordenada):
        self.log_de_missoes.append(nova_coordenada)
        
