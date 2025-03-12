import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QDesktopWidget
from ui.Interfaz import Ui_widgetPadre  # Asegúrate de importar correctamente la clase generada

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_widgetPadre()
        self.ui.setupUi(self)

        # Ajusta la UI para trabajar con QMainWindow
        widgetPadre = QWidget(self)
        self.ui.setupUi(widgetPadre)  # Configura la interfaz en el widgetPadre
        self.setCentralWidget(widgetPadre)  # Establece el widget central

        # Ajustamos el título de la ventana
        self.setWindowTitle("Clasificador de Especies Arboreas")

        # Obtén el tamaño de la pantalla
        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        screen_height = screen.height()

        # Establece el tamaño de la ventana, ajustando a la pantalla completa pero con espacio para la barra de tareas
        self.setGeometry(0, 0, screen_width, screen_height)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Muestra la ventana
    sys.exit(app.exec_())  # Ejecuta el ciclo de eventos de la aplicación
