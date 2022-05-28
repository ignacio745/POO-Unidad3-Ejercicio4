from Calefactor import Calefactor
from CalefactorElectrico import CalefactorElectrico
from CalefactorGas import CalefactorGas
import csv
import numpy as np

class ManejadorCalefactores:
    __dimension = 0
    __incremento = 5
    __cantidad = 5
    __calefactores = None

    def __init__(self, dimension:int):
        self.__dimension = dimension
        self.__incremento = 5
        self.__cantidad = 0
        self.__calefactores = np.empty(self.__dimension, Calefactor)
    

    def agregarCalefactor(self, unCalefactor:Calefactor) -> None:
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__calefactores.resize(self.__dimension)
        self.__calefactores[self.__cantidad] = unCalefactor
        self.__cantidad += 1
    
    def cargarCsvElectricos(self, nombreArchivo:str) -> None:
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        contador = 0
        for fila in reader:
            contador += 1
            try:
                unCalefactorElectrico = CalefactorElectrico(fila[0], fila[1], int(fila[2]))
            except:
                print("[ERROR] No se pudo cargar el calefactor electrico de la fila {0}".format(contador))
            else:
                self.agregarCalefactor(unCalefactorElectrico)
    

    def cargarCsvAGas(self, nombreArchivo:str):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        contador = 0
        for fila in reader:
            contador += 1
            try:
                unCalefactorGas = CalefactorGas(fila[0], fila[1], fila[2], int(fila[3]))
            except:
                print("[ERROR] No se pudo cargar el calefactor a gas de la fila {0}".format(contador))
            else:
                self.agregarCalefactor(unCalefactorGas)
    
    
    def getCalefactor(self, indice: int) -> Calefactor:
        """
        Retorna un calefactor del manejador dado su indice.
        """

        assert 0 <= indice < self.__cantidad, "El indice esta fuera de rango"
        return self.__calefactores[indice]
    

    def getIndicePrimerCalefactorGas(self) -> int:
        i = 0
        while not isinstance(self.__calefactores[i], CalefactorGas) and i < self.__cantidad:
            i += 1
        if i == self.__cantidad:
            i = -1
        return i


    def getIndiceCalefactorAGasMenorConsumo(self) -> int:
        menor = indicePrimerCalefactorGas = self.getIndicePrimerCalefactorGas()
        for i in range(indicePrimerCalefactorGas, self.__cantidad):
            if isinstance(self.__calefactores[i], CalefactorGas) and self.__calefactores[i] < self.__calefactores[menor]:
                menor = i
        return menor
    
    
    def getIndicePrimerCalefactorElectrico(self) -> int:
        i = 0
        while not isinstance(self.__calefactores[i], CalefactorElectrico) and i < self.__cantidad:
            i += 1
        if i == self.__cantidad:
            i = -1
        return i
    

    def getIndiceCalefactorElectricoMenorConsumo(self) -> int:
        menor = indicePrimerCalefactorElectrico = self.getIndicePrimerCalefactorElectrico()
        for i in range(indicePrimerCalefactorElectrico, self.__cantidad):
            if isinstance(self.__calefactores[i], CalefactorElectrico) and self.__calefactores[i] < self.__calefactores[menor]:
                menor = i
        return menor
    

    def getIndiceCalefactorMenorConsumo(self, costom3: int, cantidadm3: int, costokwh: int, consumoHora: int) -> (CalefactorElectrico | CalefactorGas):
        """
        Retorna el indice del calefactor de menor consumo.
        
        Parametros
        ----------
        costom3: int
            Costo por metro cúbico de gas.
        cantidadm3: int
            Cantidad de metros cúbicos de gas a usar.
        costokwh: int
            Costo del kilowatt hora.
        consumoHora: int
            Cantidad de horas que se usara.
        """

        indiceCalefactorMenor = 0
        indiceCalefactorGasMenor = self.getIndiceCalefactorAGasMenorConsumo()
        indiceCalefactorElectricoMenor = self.getIndiceCalefactorElectricoMenorConsumo()
        calefactorGasMenor:CalefactorGas = self.__calefactores[indiceCalefactorGasMenor]
        calefactorElectricoMenor:CalefactorElectrico = self.__calefactores[indiceCalefactorElectricoMenor]
        consumoGas = calefactorGasMenor.getCalorias()/1000 * cantidadm3 * costom3
        consumoElectrico = calefactorElectricoMenor.getPotenciaMaxima()/1000 * costokwh * consumoHora
        if consumoGas < consumoElectrico:
            indiceCalefactorMenor = indiceCalefactorGasMenor
        else:
            indiceCalefactorMenor = indiceCalefactorElectricoMenor
        return indiceCalefactorMenor