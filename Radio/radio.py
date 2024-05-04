import serial
import sys
import time

class Radio():
    def __init__(self, port, baudrate, timeOut):
        self.__PORT = port
        self.__BAUDRATE = baudrate
        self.__TIMEOUT = timeOut
        #self.__RADIO = serial.Serial(self.__PORT, self.__BAUDRATE, timeout = self.__TIMEOUT)      

    def sendSelf(self, x):
        self.__RADIO.write(bytes(x+"\r\n", 'utf-8'))

    def send(self, address, x):
            self.__RADIO.write(bytes("AT+SEND=%d,%d,%s\r\n" %(address, sys.getsizeof(x)-49, x), 'utf-8'))
    
    def read(self):
        print(self.__RADIO.readline().decode())

    def readAll(self):
        print(self.__RADIO.read_all().decode())
    
    def close(self):
         self.__RADIO.close()

    # Initiallizing the radio
    def reset(self):
         self.sendSelf("AT+RESET")
    
    # <Spreading Factor> Larger SF = better sensitivity and longer transmission time
    # <Bandwidth> Smaller BW = better sensitivity and longer transmission time
    # <Coding Rate> Determines the redundant bits. Lower CR = faster transmission time
    # <Programmed Preamble> Larger PP = less loss of data and longer transmission time
    # 
    # Recommended:
    # Within 3 km: (10, 7, 1, 7)
    # More than 3 km: (12, 4, 1, 7)
    def setParam(self, sf, bw, cr, pp):
         self.__SF = sf
         self.__BW = bw
         self.__CR = cr
         self.__PP = pp
         self.sendSelf("AT+PARAMETER=%d,%d,%d,%d" %(self.__SF, self.__BW, self.__CR, self.__PP))
         
    # <Frequency> 915MHz in Canada
    def setFRQ(self, fq):
         self.__FQ = fq
         self.sendSelf("AT+BAND=%d" %self.__FQ)

    # <Address> Address of the radio module. 0~65535
    def setADR(self, adr):
         self.__ADR = adr
         self.sendSelf("AT+ADDRESS=%d" %self.__ADR)

    # <Network> Public network of LoRa. Radios must be in same group to communicate. 0~16
    def setNTW(self, ntw):
         self.__NTW = ntw
         self.sendSelf("AT+NETWORKID=%d" %self.__NTW)

    # <Password> Must have same password for data to be recognized. 32 character AES password.
    def setPASS(self, PASS):
         self.__PASS = PASS
         if self.__PASS is None: return 
         else: self.sendSelf("AT+CPIN=%s" %self.__PASS)

    # <Output Power>
    def setOP(self, op):
         self.__OP = op
         self.sendSelf("AT+CRFOP=%d" %self.__OP)

    # Batch initialize
    def radioSetup(self, SF, BW, CR, PP, FQ, ADR, NTW, PASS, OP):
         self.setParam(SF, BW, CR, PP)
         time.sleep(0.1)
         self.read()

         self.setFRQ(FQ)
         time.sleep(0.1)
         self.read()

         self.setADR(ADR)
         time.sleep(0.1)
         self.read()

         self.setNTW(NTW)
         time.sleep(0.1)
         self.read()

         self.setPASS(PASS)
         time.sleep(0.1)
         self.read()

         self.setOP(OP)
         time.sleep(0.1)
         self.read()

     #decoding the message
    def parseMsg (self, data):
         if(data[:5] == "+RCV="):
              x = data.split(",")
              self.__SENDER = x[0][5:]
              self.__DATASIZE = int(x[1])
              self.__DATA = x[2]
              self.__RSSI = int(x[3])
              self.__SNR = int(x[4])

              print(data)
              print(self.__SENDER)
              print(self.__DATASIZE)
              print(self.__DATA)
              print(self.__RSSI)
              print(self.__SNR)