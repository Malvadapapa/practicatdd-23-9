class MaquinaPapel:
    def __init__(self, _modelo, color):
        self._modelo = _modelo
        self.color = color
        self.estado = False

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, nuevo_valor):
        self._modelo = nuevo_valor

    def __str__(self):
        return f'La maquina es el modelo {self._modelo} y es de color {self.color}'
