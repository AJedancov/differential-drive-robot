import socket, select
import serial
import sys
import threading



ros_path = '/opt/ros/kinetic/lib/python2.7/dist-packages'
if ros_path in sys.path:
    sys.path.remove(ros_path)
import cv2
sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')

print("\n=== Server Start ===\n" )

s = serial.Serial()
s.baudrate = 9600
s.port = '/dev/ttyUSB0'   # for Raspberry
# s.port = '/dev/ttyACM0'     # for Linux
s.timeout = 0.5
s.open()

# ========================
# socket.SOCK_STREAM - TCP
# socket.SOCK_DGRAM - UDP
# AF_INET - IPv4
# ========================

HOST = '192.168.0.110'
# HOST = '127.0.0.1'
PORT = 15000


def readDataFromArduino():
    while True:
        if(event_break.is_set()):
            break

        # ==== read data ===
        dataSerial = s.readline().decode('utf-8').rstrip()
        if (not dataSerial):
            continue 
        print("dataSerial:", dataSerial, "\n")


event_break = threading.Event()

th_read_serial = threading.Thread(target=readDataFromArduino)
th_read_serial.start()


sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sck.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sck.bind((HOST, PORT))
sck.listen()
conn, addr = sck.accept()
print("Connect to: ", addr, "\n")


while True:
    data = conn.recv(1)
    print(data)
    if (data == b'\x03'):
        event_break.set()
        break
    
    s.write(data)

    # dataSerial = s.read_all()
    # print(dataSerial)
conn.close()

th_read_serial.join()