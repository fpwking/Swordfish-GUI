import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import random

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("CanSat GUI")

        # Create some widgets
        self.graphWidget = pg.PlotWidget()
        self.labelGPS = QLabel("GPS Coordinates: ")
        self.labelState = QLabel("State: ")
        self.labelTime = QLabel("Mission Elapsed Time: ")
        self.labelBattery = QLabel("Battery Voltage: ")
        self.labelDescent = QLabel("Descent Rate: ")
        self.labelDataRate = QLabel("Telemetry Data Rate: ")
        self.labelSuccessRate = QLabel("Telemetry Packet Success Rate: ")
        self.button = QPushButton("Switch State")

        # Create a layout
        layout = QVBoxLayout()
        layout.addWidget(self.graphWidget)
        layout.addWidget(self.labelGPS)
        layout.addWidget(self.labelState)
        layout.addWidget(self.labelTime)
        layout.addWidget(self.labelBattery)
        layout.addWidget(self.labelDescent)
        layout.addWidget(self.labelDataRate)
        layout.addWidget(self.labelSuccessRate)
        layout.addWidget(self.button)

        # Create a container
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the Window
        self.setCentralWidget(container)

        # Set up plot
        self.x = list(range(100))  # 100 time points
        self.y = [random.randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        # Set up timer
        self.timer = QTimer()
        self.timer.setInterval(500) # in milliseconds
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.y = self.y[1:]  # remove the first y element
        self.y.append(random.randint(0,100))  # add a new random value

        # update line with new data
        self.data_line.setData(self.x, self.y)

        # update labels
        self.labelGPS.setText(f"GPS Coordinates: {random.uniform(-180, 180)}, {random.uniform(-90, 90)}")
        self.labelState.setText(f"State: {random.choice(['Launch Detected', 'Apogee Detected', 'Landing Detected'])}")
        self.labelTime.setText(f"Mission Elapsed Time: {random.randint(0, 100)}")
        self.labelBattery.setText(f"Battery Voltage: {random.uniform(3.5, 4.2)}")
        self.labelDescent.setText(f"Descent Rate: {random.uniform(0, 10)}")
        self.labelDataRate.setText(f"Telemetry Data Rate: {random.randint(0, 1000)} bits/s")
        self.labelSuccessRate.setText(f"Telemetry Packet Success Rate: {random.uniform(0, 1)*100}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec())
