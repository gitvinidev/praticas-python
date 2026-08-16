from VeiculoEspacial import VeiculoEspacial

class NaveCargueira(VeiculoEspacial):
    def __init__(self, nome, coordenadas, capacidade_maxima):
        super().__init__(nome, coordenadas)
        self.capacidade_maxima = capacidade_maxima
        self.inventario={}

    def adicionar_carga(self, item, quantidade):
        if item in self.inventario:
            self.inventario[item] += quantidade
        else:
            self.inventario[item] = quantidade

    @staticmethod
    def confirmar_veiculo(veiculos):
        return isinstance(veiculos, NaveCargueira)


