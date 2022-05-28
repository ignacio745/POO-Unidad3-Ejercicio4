from Calefactor import Calefactor
from CalefactorElectrico import CalefactorElectrico
from CalefactorGas import CalefactorGas
from ManejadorCalefactores import ManejadorCalefactores
from IngresadorTeclado import IngresadorTeclado


class Menu:
    __switcher = None
    __ingresador = None
    
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.salir
                          }
        self.__ingresador = IngresadorTeclado()
        
    

    def opcion(self, unManejadorCalefactores: ManejadorCalefactores,op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op in ('1', '2', '3'):
            func(unManejadorCalefactores)
        else:
            func()
    
    
    def salir(self):
        print('Usted salio del programa')


    def opcion1(self, unManejadorCalefactores: ManejadorCalefactores):
        costoMetrosCubicos = self.__ingresador.inputInt("Ingrese el costo por metro cubico: ")
        cantidadMetrosCubicos = self.__ingresador.inputInt("Ingrese la cantidad de metros cubicos: ")
        unCalefactorGas:CalefactorGas = unManejadorCalefactores.getCalefactor(unManejadorCalefactores.getIndiceCalefactorAGasMenorConsumo())
        print("El calefactor de menor consumo es de la marca {0} modelo {1} y tiene un costo de ${2}".format(unCalefactorGas.getMarca(), unCalefactorGas.getModelo(), unCalefactorGas.getCalorias() * cantidadMetrosCubicos * costoMetrosCubicos))


    def opcion2(self, unManejadorCalefactores: ManejadorCalefactores):
        costokwh = self.__ingresador.inputInt("Ingrese el costo del Kilowatt-hora: ")
        cantidadHoras = self.__ingresador.inputInt("Ingrese la cantidad de horas que se usara el calefactor: ")
        unCalefactorElectrico:CalefactorElectrico = unManejadorCalefactores.getCalefactor(unManejadorCalefactores.getIndiceCalefactorElectricoMenorConsumo())
        print("El calefactor de menor consumo es de la marca {0} modelo {1} y tiene un costo de ${2}".format(unCalefactorElectrico.getMarca(), unCalefactorElectrico.getModelo(), unCalefactorElectrico.getPotenciaMaxima() * costokwh * cantidadHoras))



    def opcion3(self, unManejadorCalefactores:ManejadorCalefactores):
        costoMetrosCubicos = self.__ingresador.inputInt("Ingrese el costo por metro cubico: ")
        cantidadMetrosCubicos = self.__ingresador.inputInt("Ingrese la cantidad de metros cubicos: ")
        costokwh = self.__ingresador.inputInt("Ingrese el costo del Kilowatt-hora: ")
        cantidadHoras = self.__ingresador.inputInt("Ingrese la cantidad de horas que se usara el calefactor: ")
        unCalefactor = unManejadorCalefactores.getCalefactor(unManejadorCalefactores.getIndiceCalefactorMenorConsumo(costoMetrosCubicos, cantidadMetrosCubicos, costokwh, cantidadHoras))
        print(unCalefactor)



    def ejecutarMenu(self, unManejadorCalefactores: ManejadorCalefactores):
            opcion = "0"
            while opcion != "4":
                print("Ingrese la opcion deseada")
                print("[1] Mostrar calefactor a gas de menor consumo")
                print("[2] Mostrar calefactor electrico de menor consumo")
                print("[3] Mostrar calefactor de menor consumo")
                print("[4] Salir")
                opcion = input("--> ")  
                self.opcion(unManejadorCalefactores, opcion)