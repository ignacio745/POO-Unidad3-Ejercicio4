import imp
from Calefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula = ""
    __calorias = ""

    def __init__(self, marca: str, modelo: str, matricula:str, calorias:int) -> None:
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias
    
    
    def getMatricula(self) -> str:
        return self.__matricula
    
    
    def getCalorias(self) -> int:
        return self.__calorias
    

    def __gt__(self, otro) -> bool:
        resultado = False
        if isinstance(otro, CalefactorGas):
            resultado = self.getCalorias() > otro.getCalorias()
        return resultado

    
    def __lt__(self, otro) -> bool:
        resultado = True
        if isinstance(otro, CalefactorGas):
            resultado = self.getCalorias() < otro.getCalorias()
        return resultado
    
    
    def __str__(self) -> str:
        cadena = "Tipo: Calefactor a gas\n"
        cadena += super().__str__()
        cadena += "\nMatricula: {0}\n".format(self.__matricula)
        cadena += "Calorias: {0} calorias/m\u00b3".format(self.__calorias)
        return cadena