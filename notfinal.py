import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import QTimer
import pyqtgraph as pg

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("CanSat GUI - Team Swordfish")
        self.setStyleSheet("background-color: #dddddd;")
        self.showFullScreen()  # Make the application full screen

        # Create some widgets
        self.labelHeader = QLabel("Team Swordfish")
        self.labelHeader.setStyleSheet("font-size: 32px; font-weight: bold; color: white; border-radius: 15px;")  # Make the header text larger and bold

        # Create a grid layout for the button panel
        self.buttonPanel = QGridLayout()

        # Create 9 buttons and add them to the grid layout
        for i in range(9):
            button = QPushButton(text=f"Button {i+1}")
            button.setStyleSheet("font-size: 32px; padding: 10px; margin:10px;")
            self.buttonPanel.addWidget(button, i // 3, i % 3)

        # Create some widgets
        self.labelHeader = QLabel("Team Swordfish")
        self.labelHeader.setStyleSheet("font-size: 32px; font-weight: bold; color: white;")  # Make the header text larger and bold
        self.graphWidget1 = pg.PlotWidget(title="Graph 1")  # Add a title to the first graph
        self.graphWidget2 = pg.PlotWidget(title="Graph 2")  # Add a title to the second graph
        self.labelGPS = QLabel("GPS Coordinates: ")
        self.labelState = QLabel("State: ")
        self.labelBattery = QLabel("Battery Voltage: ")
        self.labelDescent = QLabel("Descent Rate: ")
        self.labelDataRate = QLabel("Telemetry Data Rate: ")
        self.labelSuccessRate = QLabel("Telemetry Packet Success Rate: ")
        self.labelExtra1 = QLabel("Extra 1")
        self.labelExtra2 = QLabel("Extra 2")
        self.labelExtra3 = QLabel("Extra 3")
        self.button = QPushButton("Switch State")
        self.buttonPanel1 = QPushButton(text="meow1")
        self.buttonPanel2 = QPushButton(text="meow2")
        self.buttonPanel3 = QPushButton(text="meow3")
        self.buttonPanel4 = QPushButton(text="meow4")
        self.labelTime = QLabel("Mission Elapsed Time: ")
        self.labelTime.setText(f"Mission Elapsed Time: {random.randint(0, 100)}")
        
        self.labelGPS.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelState.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelBattery.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelDescent.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelDataRate.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelSuccessRate.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelTime.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelExtra1.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelExtra2.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")
        self.labelExtra3.setStyleSheet("font-size: 32px; font-weight: ; border-radius: 15px;")

        self.button.setStyleSheet("font-size: 32px; padding: 10px; margin:10px; margin-top: 50px;")
        
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

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout4 = QVBoxLayout()
        layout5 = QVBoxLayout()

        layout1.setContentsMargins(20,20,20,20)
        layout1.setSpacing(20)
        layout2.setContentsMargins(20,20,20,20)
        layout2.setSpacing(20)

        layout4.setContentsMargins(30,30,30,30)
        layout4.setSpacing(10)


        
        

        layout2.addWidget(self.graphWidget1)
        layout2.addWidget(self.graphWidget2)

        layout1.addLayout( layout2 )
        layout1.addLayout( layout3 )

                # Add the button panel to the layout
        layout3.addLayout(self.buttonPanel)
        
        layout3.addLayout( layout4 )
        layout3.addLayout( layout5 )
        
        layout4.addWidget(self.labelGPS)
        layout4.addWidget(self.labelState)
        layout4.addWidget(self.labelTime)
        layout4.addWidget(self.labelBattery)
        layout4.addWidget(self.labelDescent)
        layout4.addWidget(self.labelDataRate)
        layout4.addWidget(self.labelSuccessRate)
        #layout4.addWidget(self.labelExtra1)
        #layout4.addWidget(self.labelExtra2)
        #layout4.addWidget(self.labelExtra3)
        layout4.addWidget(self.button)
        
        
        layout5.addWidget(self.labelDescent)
        


        # Set a fixed width for the widgets
        self.graphWidget1.setFixedWidth(600)
        self.graphWidget2.setFixedWidth(600)


        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)
        
        
    def update_plot_data(self):
        self.y1 = self.y1[1:]  # remove the first y element
        self.y1.append(random.randint(0,100))  # add a new random value
        self.y2 = self.y2[1:]  # remove the first y element
        self.y2.append(random.randint(0,100))  # add a new random value

        # update line with new data
        self.data_line1.setData(self.x, self.y1)
        self.data_line2.setData(self.x, self.y2)

        # update labels
        self.labelGPS.setText(f"GPS Coordinates: {round(random.uniform(-180, 180),2)}, {round(random.uniform(-90, 90),2)}")
        self.labelState.setText(f"State: {random.choice(['Launch Detected', 'Apogee Detected', 'Landing Detected'])}")
        self.labelTime.setText(f"Mission Elapsed Time: {random.randint(0, 100)}")
        self.labelBattery.setText(f"Battery Voltage: {round(random.uniform(3.5, 4.2),4)}")
        self.labelDescent.setText(f"Descent Rate: {round(random.uniform(0, 10),4)}")
        self.labelDataRate.setText(f"Telemetry Data Rate: {random.randint(0, 1000)} bits/s")
        self.labelSuccessRate.setText(f"Telemetry Packet Success Rate: {round(random.uniform(0.5, 1)*100,2)}%")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec())
