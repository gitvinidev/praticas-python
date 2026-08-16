from VeiculoEspacial import VeiculoEspacial
from NaveCargueira import NaveCargueira

Galactic_Truck = NaveCargueira("Galactic Truck", (0, 0, 0), 1000)
Galactic_Truck.adicionar_carga("Células de combustível", 50)
Galactic_Truck.mover((10, 20, -5))
Galactic_Truck.mover((11, 13, -34))
for x in Galactic_Truck.log_de_missoes:
    print(f"Log de missões: {x}")