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
        self.labelBattery = QLabel("Battery Voltage: ")
        self.labelDescent = QLabel("Descent Rate: ")
        self.labelDataRate = QLabel("Telemetry Data Rate: ")
        self.labelSuccessRate = QLabel("Telemetry Packet Success Rate: ")
        self.button = QPushButton("Switch State")
        self.buttonPanel1 = QPushButton(text="meow1")
        self.buttonPanel2 = QPushButton(text="meow2")
        self.buttonPanel3 = QPushButton(text="meow3")
        self.buttonPanel4 = QPushButton(text="meow4")
        self.labelTime = QLabel("Mission Elapsed Time: ")
        self.labelTime.setText(f"Mission Elapsed Time: {random.randint(0, 100)}")


        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QVBoxLayout()
        layout5 = QVBoxLayout()

        layout1.setContentsMargins(10,10,10,10)
        layout1.setSpacing(20)
        layout2.setContentsMargins(10,10,10,10)
        layout2.setSpacing(20)
        layout3.setContentsMargins(10,10,10,10)
        layout3.setSpacing(20)
        layout4.setContentsMargins(10,10,10,10)
        layout4.setSpacing(20)
        layout5.setContentsMargins(10,10,10,10)
        layout5.setSpacing(20)
        
        

        layout2.addWidget(self.graphWidget1)
        layout2.addWidget(self.graphWidget2)

        layout1.addLayout( layout2 )
        layout1.addLayout( layout3 )

        layout3.addWidget(self.buttonPanel1)

        layout3.addWidget(self.buttonPanel2)
        layout3.addWidget(self.buttonPanel3)
        
        layout3.addLayout( layout4 )
        layout3.addLayout( layout5 )
        
        layout4.addWidget(self.labelGPS)
        layout4.addWidget(self.labelState)
        layout4.addWidget(self.labelTime)
        layout4.addWidget(self.labelBattery)
        layout4.addWidget(self.labelDescent)
        layout4.addWidget(self.labelDataRate)
        layout4.addWidget(self.labelSuccessRate)
        layout4.addWidget(self.button)
        
        
        layout5.addWidget(self.labelDescent)


        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt6())  # Apply the dark theme

    main = MainWindow()
    main.show()

    sys.exit(app.exec())
