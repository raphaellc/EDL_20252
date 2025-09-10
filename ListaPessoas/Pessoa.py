class Pessoa:
    __nome:str
    __idade:int
    __altura:float
    
    def __init__(self, nome:str, idade:int, altura:float):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
    #interfaces públicas da classe pessoa 
    def getNome(self):
        return self.__nome
    def getIdade(self):
        return self.__idade
    def getAltura(self):
        return self.__altura
    def setNome(self, nome:str):
        self.__nome = nome
    def setIdade(self, idade:int):
        self.__idade = idade    
    def setAltura(self, altura:float):
        self.__altura = altura

    def __str__(self):
        return f"Nome: {self.__nome}, Idade: {self.__idade}, Altura: {self.__altura}"