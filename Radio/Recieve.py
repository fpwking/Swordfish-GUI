from radio import Radio
import time
import bitstring

GROUND = Radio('COM5', 9600, 0.1)
CANSAT = Radio('COM7', 9600, 0.1)

def setup():
    print("Ground")
    GROUND.radioSetup(10, 7, 1, 7, 915000000, 1, 1, None, 10)
    print("Cansat")
    CANSAT.radioSetup(10, 7, 2, 7, 915000000, 2, 1, None, 10)


CANSAT.readAll()
GROUND.send(2, " 7 bits (humid Xle of 8 bits can be sent. If you need to send 17 bits for example, 3 bytes are needed: 2 for the first 16 bits and one for the last bit (the remaining 7 bits can be reserved for further use).")
time.sleep(2)
CANSAT.read()
GROUND.send(2, "Convert to bits")
time.sleep(1)
GROUND.read()
CANSAT.read()

GROUND.close()
CANSAT.close()