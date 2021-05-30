class Estado(object):
    """
    Declaración de la clase 'Estado' que proporciona funcionalidad
    para cada uno de los distintos estados de la máquina
    """

    def __init__(self):
        print ('Estado actual:', str(self))
        
    def on_event(self, event):
        """
        Aquí se gestionan los eventos de este estado.
        """
        pass

    def __repr__(self):
        """
        Descripcion del estado
        """
        return self.__str__()

    def __str__(self):
        """
        Devuelve el nombre del estado
        """
        return self.__class__.__name__
