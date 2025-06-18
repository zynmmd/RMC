import serial.tools.list_ports
import pyvjoy
import keyboard
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.1xx",5655))
s.listen(5)
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portsList = []
current_roll_value = 0
import time

def data2(value, min_in, max_in, min_out, max_out):
    normalized = int(((max_in - value) / (max_in - min_in)) * (max_out - min_out) + min_out)
    return max(min_out, min(max_out, normalized))
for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))

val = input("Select Port: COM")

for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)
clientsocket,address = s.accept()
serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
last_time = time.time()
ax_velocity = time.time()
print(f"connect from {address} has been made")
while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        time.sleep(0.1)
        "print(packet.decode('utf-8').rstrip('\n'))"
        data = packet.decode('utf-8').rstrip('\n')
        
        
                
        roll,pitch = data.strip().split(",")
        clientsocket.send(bytes(data + "\n", "UTF-8"))
