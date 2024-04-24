from radio import Radio
import serial

# sup = serial.Serial('COM5', 9600, timeout=0.1)
# print(sup.readline().decode())
# sup.write(bytes("AT\r\n", 'utf-8'))
# print(sup.readline().decode())
# sup.close()

GROUND = Radio('COM5', 9600, timeout=0.1)
CANSAT = Radio('COM7', 9600, timeout=0.1)

GROUND.sendThis()
GROUND.read()