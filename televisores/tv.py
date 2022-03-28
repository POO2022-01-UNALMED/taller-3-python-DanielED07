from televisores.marca import Marca


class TV:
    _numTV = 0
    canal = 1
    precio = 500
    volumen = 1

    def __init__(self, marca, estado):

        self._marca = marca
        self.estado = estado
        TV._numTV += 1

    def getMarca(self):
        return self._marca

    def getControl(self):
        return self.control

    def getPrecio(self):
        return self.precio

    def getVolumen(self):
        return self.volumen

    def getCanal(self):
        return self.canal

    def setMarca(self):
        self.marca = Marca

    def setControl(self, control):
        self.control = control

    def setPrecio(self, precio):
        self.precio = precio

    def setVolumen(self, volumen):
        if(self.estado == True and self.volumen >= 0 and self.volumen <= 7):
            self.volumen = volumen

    def setCanal(self, canal):
        if(self.estado == True and self.canal >= 1 and self.canal <= 120):
            self.canal = canal

    @classmethod
    def setNumTV(cls, num):
        cls._numTV = num

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    def canalUp(self):
        if(self.estado == True and self.canal < 120):
            self.setCanal(self.canal+1)

    def canalDown(self):
        if(self.estado == True and self.canal > 1):
            self.setCanal(self.canal-1)

    def VolumenUp(self):
        if(self.estado == True and self.volumen < 7):
            self.setVolumen(self.volumen+1)

    def VolumenDown(self):
        if(self.estado == True and self.volumen > 0):
            self.setVolumen(self.volumen-1)

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
