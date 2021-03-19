import matplotlib.pyplot as plt


class graficas():
    def __init__(self):
        super().__init__()
    def mostrarGrafica(self,datosx,datosy,titulo):
        fig, ax = plt.subplots()
        #se realiza el calculo del espectro de la señal
        ax.plot(datosx,datosy)
        ax.set_title(titulo)
        plt.show()