"""
Clase de tipo vehiculo
"""


class Vehiculo:

    def __init__(self, modelo: str = None, marca: str = None, color: str = None, estilo: str = None):
        self._modelo = modelo
        self._marca = marca
        self._color = color
        self._estilo = estilo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca_cambiado):
        self._marca = marca_cambiado

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color_cambiado):
        self._color = color_cambiado

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo_cambiado):
        self._modelo = modelo_cambiado

    @property
    def estilo(self):
        return self._estilo

    @estilo.setter
    def estilo(self, estilo_cambiado):
        self._estilo = estilo_cambiado
