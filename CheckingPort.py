from numpy import true_divide
import serial


port = serial.Serial('/dev/ttyUSB0', 9600)
#port = serial.Serial('/dev/pts/4', 9600)

def CheckPort(status):
    try:
        data = port.readline().decode('utf-8').strip('\n\r')
        if status == 0 : return data
        elif status == 1 : print (data)
        
    except serial.serialutil.SerialException:
        pass

if __name__ == "__main__":
    print("start")
    while True:
        CheckPort(1)