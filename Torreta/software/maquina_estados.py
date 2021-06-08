from estados_torreta import Arranque

class MaquinaEstadosMeta(type):
    """
    Implementacion Singleton de la maquina de estados
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Posibles cambios del valor del argumento `__init__` no afectan a la instancia devuelta.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MaquinaEstados(metaclass = MaquinaEstadosMeta):
    """ 
    Maquina de estados de la torreta anti-drones
    """

    def __init__(self):
        """Inicialización de la máquina de estados"""

        # La maquina comienza en el estado de arranque
        self.estado = Arranque()

    def on_event(self, event):
        """
        Los eventos que surgan son delegados a la clase del estado correspondiente, de forma que cada
        estado gestiona su evento. El resultado devuelto por dicha clase será asignado como el estado 
        actual de la máquina. 
        """

        # El siguiente estado es el resultado de la llamada a la funcion 'on_event' del estado actual.
        self.estado = self.estado.on_event(event)

""" 
>>> from software.maquina_estados import MaquinaEstados
>>> maquina = MaquinaEstados() # Se crea una instancia de la máquina de estado
Estado actual: Arranque

>>> maquina.on_event('OK')
Estado actual: Recepcion

>>> maquina.estado
Recepcion

"""
