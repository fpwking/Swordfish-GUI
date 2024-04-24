from serial import Serial
import sys

class Radio(Serial):
    def __innit__(self):
         super().__init__()

    def sendThis (self):
        self.write(bytes("AT\r\n", 'utf-8'))

    def send (self, address, x):
            msg = bytes(x, 'utf-8')
            self.write("AT+SEND=" + address + "," + sys.getsizeof(msg) + "," + msg + "\r\n")
    
    def read(self):
        print(self.readline().decode())


    
