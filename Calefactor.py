import abc
from abc import ABC


class Calefactor(ABC):
    __marca = ""
    __modelo = ""

    def __init__(self, marca:str, modelo:str) -> None:
        self.__marca = marca
        self.__modelo = modelo

    
    def getMarca(self) -> str:
        return self.__marca
    
    def getModelo(self) -> str:
        return self.__modelo
    

    def __str__(self) -> str:
        cadena = "Marca: {0}\n".format(self.__marca)
        cadena += "Modelo: {0}".format(self.__modelo)
        return cadena