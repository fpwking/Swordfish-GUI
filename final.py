import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton
from PyQt6.QtCore import QTimer
import pyqtgraph as pg
import qdarkstyle

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("CanSat GUI - Team Swordfish")
        self.showFullScreen()  # Make the application full screen

        # Create some widgets
        self.labelHeader = QLabel("Team Swordfish")
        self.labelHeader.setStyleSheet("font-size: 24px; font-weight: bold; color: white;")  # Make the header text larger and bold
        self.graphWidget1 = pg.PlotWidget(title="Graph 1")  # Add a title to the first graph
        self.graphWidget2 = pg.PlotWidget(title="Graph 2")  # Add a title to the second graph
        self.labelGPS = QLabel("GPS Coordinates: ")
        self.labelState = QLabel("State: ")
        self.labelTime = QLabel("Mission Elapsed Time: ")
        self.labelBattery = QLabel("Battery Voltage: ")
        self.labelDescent = QLabel("Descent Rate: ")
        self.labelDataRate = QLabel("Telemetry Data Rate: ")
        self.labelSuccessRate = QLabel("Telemetry Packet Success Rate: ")
        self.button = QPushButton("Switch State")
        
        # Create a layout for the labels
        layoutLabels = QVBoxLayout()
        layoutLabels.addWidget(self.labelGPS)
        layoutLabels.addWidget(self.labelState)
        layoutLabels.addWidget(self.labelTime)
        layoutLabels.addWidget(self.labelBattery)
        layoutLabels.addWidget(self.labelDescent)
        layoutLabels.addWidget(self.labelDataRate)
        layoutLabels.addWidget(self.labelSuccessRate)
        layoutLabels.addWidget(self.button)

        # Create a layout for the graphs
        layoutGraphs = QVBoxLayout()
        layoutGraphs.addWidget(self.graphWidget1)
        layoutGraphs.addWidget(self.graphWidget2)

        # Create a main layout
        layoutMain = QVBoxLayout()
        layoutMain.addWidget(self.labelHeader)
        layoutMain.addLayout(layoutGraphs)
        layoutMain.addLayout(layoutLabels)

        # Create a container
        container = QWidget()
        container.setLayout(layoutMain)

        # Set the central widget of the Window
        self.setCentralWidget(container)

        # Set up plot
        self.x = list(range(100))  # 100 time points
        self.y1 = [random.randint(0,100) for _ in range(100)]  # 100 data points for the first graph
        self.y2 = [random.randint(0,100) for _ in range(100)]  # 100 data points for the second graph

        self.graphWidget1.setBackground('w')
        self.graphWidget2.setBackground('w')
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line1 =  self.graphWidget1.plot(self.x, self.y1, pen=pen)
        self.data_line2 =  self.graphWidget2.plot(self.x, self.y2, pen=pen)

        # Set up timer
        self.timer = QTimer()
        self.timer.setInterval(500) # in milliseconds
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.y1 = self.y1[1:]  # remove the first y element
        self.y1.append(random.randint(0,100))  # add a new random value
        self.y2 = self.y2[1:]  # remove the first y element
        self.y2.append(random.randint(0,100))  # add a new random value

        # update line with new data
        self.data_line1.setData(self.x, self.y1)
        self.data_line2.setData(self.x, self.y2)

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
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())  # Apply the dark theme

    main = MainWindow()
    main.show()

    sys.exit(app.exec())
