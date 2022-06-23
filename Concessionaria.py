class Concessionaria():
    def __init__(self, nome, cnpj, localizacao, carros = []):
        self.nome = nome
        self.cnpj = cnpj
        self.localizacao = localizacao
        self.carros = carros

    def comprar(self):
      listaAux = []
      for i in range(8):
        print("Carros: ",self.carros)
        escolha = int(input("Escolha o carro a ser comprado: "))
        listaAux.append(self.carros[escolha])
        del self.carros[escolha]
        print("Carrinho de Compra: ", listaAux)

    @property
    def chassi(self):
        return self.chassi

    @chassi.setter
    def chassi(self, novo_chassi):
        raise ValueError("IMPOSSIVEL ALTERAR DIRETAMENTE")

class Veiculo():
  def __init__(self, marca, modelo, ano, chassi = []):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.__chassi = chassi

  @property
  def chassi(self):
    return self.chassi

  @chassi.setter
  def chassi(self, novo_chassi):
    raise ValueError("IMPOSSIVEL ALTERAR DIRETAMENTE")

class Carro(Veiculo):
  def __init__(self, marca, modelo, ano, chassi, potencia = []):
    super().__init__(marca, modelo, ano, chassi)
    self.potencia = potencia
