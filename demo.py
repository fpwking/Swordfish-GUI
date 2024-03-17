import PyQt6
import pyqtgraph as pg
import time
import random

class MainWindow(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.start_time = time.time()

        self.x = []
        self.y = []

        self.plot_graph = pg.PlotWidget()
        self.line = self.plot_graph.plot(self.x, self.y)

        self.label = PyQt6.QtWidgets.QLabel()

        self.button = PyQt6.QtWidgets.QPushButton("Press me")
        self.button.pressed.connect(self.button_press)

        self.layout = PyQt6.QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.plot_graph)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.widget = PyQt6.QtWidgets.QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.timer = PyQt6.QtCore.QTimer()
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.update)
        self.timer.start()
    
    def update(self):
        elapsed_time = time.time() - self.start_time

        self.x.append(elapsed_time)
        self.y.append(random.uniform(0, 100)) # Generate random data for testing purposes. On the actual GUI, this will be replaced with data recieved from the radio

        if len(self.x) > 100:
            self.x.pop(0)
            self.y.pop(0)

        self.line.setData(self.x, self.y)

        self.label.setText("Time: " + str(elapsed_time))
    
    def button_press(self):
        print("Button pressed")

app = PyQt6.QtWidgets.QApplication([])
main = MainWindow()
main.show()
app.exec()