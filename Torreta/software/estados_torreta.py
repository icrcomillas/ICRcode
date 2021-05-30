from software.estado import Estado

# Inicio de la declaración de estados

class Arranque(Estado):
    """
    Estado de arranque del sistema, si todo va OK pasa al estado de recepción.
    En caso de que ocurra un error, pasa al estado de fallo
    """

    def on_event(self, event):
        if event == 'OK':
            return Recepcion()
        elif event == 'KO':
            return Fallo_Mortal()

        return self

class Fallo_Mortal(Estado):
    """
    Si el sistema se encuentra aquí es que ha sucedido un error.
    En caso de proceder a un reinicio, pasa al estado de Arranque.
    """

    def on_event(self, event):
        if event == 'reinicio':
            return Arranque()

        return self

class Recepcion(Estado):
    """
    Recepción de la señal.
    """

    def on_event(self, event):
        if event == 'OK':
            return EstimacionGruesa()
        elif event == 'KO':
            return Fallo_Mortal()

        return self

class EstimacionGruesa(Estado):
    """
    En este estado se realiza la estimación gruesa de la señal, para detectar la posible actividad en 
    la banda de frecuencias actual.
    """

    def on_event(self, event):
        if event == 'no_detectado':
            return ModificacionPortadora()
        elif event == 'detectado':
            return Espera()
        elif event == 'KO':
            return Fallo_Mortal()

        return self

class ModificacionPortadora(Estado):
    """
    Este estado es la consecuencia de no detectarse actividad en la etapa anterior de estimación gruesa.
    Aquí se procede a modificar la frecuencia de la portadora, para cambiar de canal. Una vez modificada
    la frecuencia, retorna al estado de recepcion. 
    """

    def on_event(self, event):
        if event == 'OK':
            return Recepcion()
        elif event == 'KO':
            return Fallo_Mortal()

        return self

class Espera(Estado):
    """
    En primer lugar se incrementa el contador. Se arranca un temporizador. TODO: cuidado con el contador!
    """

    def on_event(self, event):
        if event == 'limite_espera':
            return Transmision()
        elif event == 'KO':
            return Fallo_Mortal()

        return self

class Transmision(Estado):
    """
    En este estado se realiza la transmisión para cortar las comunicaciones. Se arranca un temporizador. 
    TODO: cuidado con el contador!
    """

    def on_event(self, event):
        if event == 'limite_transmision':
            return Analisis()
        elif event == 'KO':
            return Fallo_Mortal()

        return self

class Analisis(Estado):
    """
    Una vez expira el temporizador de transmisión, en este estado se realiza un analisis en el rango de 
    frecuencias para determinar si continua la actividad, y por tanto, si se debe seguir transmitiendo ahí.
    """

    def on_event(self, event):
        if event == 'detectado':
            return Transmision()
        if event == 'no_detectado':
            return Recepcion()
        elif event == 'KO':
            return Fallo_Mortal()

        return self

# Fin de la declaración de estados