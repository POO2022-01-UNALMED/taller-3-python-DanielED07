from televisores.tv import TV


class Control:

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def setCanal(self, canal):
        if(isinstance(self._tv, TV)):
            if(self._tv.estado == True and self._tv.canal >= 1 and self._tv.canal <= 120):
                self._tv.setCanal(canal)

    def getTv(self):
        return self.tv

    def canalUp(self):
        if(self._tv.estado == True and self._tv.canal < 120):
            self._tv.setCanal(self.canal+1)

    def canalDown(self):
        if(self._tv.estado == True and self._tv.canal > 1):
            self._tv.setCanal(self._tv.canal-1)

    def volumenUp(self):
        if(self._tv.estado == True and self._tv.volumen < 7):
            self._tv.setVolumen(self._tv.volumen+1)

    def volumenDown(self):
        if(self._tv.estado == True and self._tv.volumen > 0):
            self._tv.setVolumen(self._tv.volumen-1)

    def turnOn(self):
        self._tv.estado = True

    def turnOff(self):
        self._tv.estado = False
