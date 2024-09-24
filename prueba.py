
class bolsos:
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca

class bolso_taekwondo(bolsos):
    def __init__(self,tipo_taekwondo, color, marca):
        self.tipo_taekwondo = tipo_taekwondo
        bolsos.__init__(self, color, marca)

bolsoitf = bolso_taekwondo('itf', 'rojo', 'adidas')

class mochila(bolsos):
    def __init__(self, has_ruedas, color, marca):
        self.__has_ruedas = has_ruedas
        bolsos.__init__(self, color, marca)

    @property # convierte en getter una funcion
    def has_ruedas(self):
        return self.__has_ruedas

    @has_ruedas.setter
    def has_ruedas(self, nuevo_valor):
         self.__has_ruedas = nuevo_valor

    def __str__(self):
        val = None

        if self.has_ruedas:
            val = 'Tiene ruedas'
        else:
            val = 'No tiene ruedas'

        return f'el color de la mochila es {del_cole.color}\nsu marca es {del_cole.marca}\ny {val}  '


del_cole = mochila(False, 'azul', 'adidas')

print(del_cole)