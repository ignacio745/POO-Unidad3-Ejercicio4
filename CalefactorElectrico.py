from Calefactor import Calefactor

class CalefactorElectrico(Calefactor):
    __potenciaMaxima = None

    def __init__(self, marca: str, modelo: str, potenciaMaxima:int) -> None:
        super().__init__(marca, modelo)
        self.__potenciaMaxima = potenciaMaxima

    def getPotenciaMaxima(self) -> int:
        return self.__potenciaMaxima
    

    def __gt__(self, otro) -> bool:
        resultado = False
        if isinstance(otro, CalefactorElectrico):
            resultado = self.getPotenciaMaxima() > otro.getPotenciaMaxima()
        return resultado
    
    def __lt__(self, otro) -> bool:
        resultado = True
        if isinstance(otro, CalefactorElectrico):
            resultado = self.getPotenciaMaxima() < otro.getPotenciaMaxima()
        return resultado
    

    def __str__(self) -> str:
        cadena = "Tipo: Calefactor Electrico\n"
        cadena += super().__str__()
        cadena += "\nPotencia Maxima: {0}".format(self.__potenciaMaxima)
        return cadena