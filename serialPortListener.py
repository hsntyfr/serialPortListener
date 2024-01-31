import serial
import subprocess

class SerialListener:
    def __init__(self):
        self.ser = None
        self.port = None
        self.baudrate = None
        self.fileName = None

    def getAvailablePorts(self):
        print("Available ports: ")
        ports = subprocess.run("ls /dev/tty.*", shell=True, capture_output=True, text=True).stdout.split('\n')

        index = 1
        for port in ports:
            if port != '':
                print(str(index) + " " + port)
                index += 1

        print("\nEnter port number: ")
        port = input()
        self.port = ports[int(port) - 1]

    def getBaudrate(self):
        print("Enter baudrate: ")
        self.baudrate = input()

    def getFileName(self):
        while True:
            print("Enter file name: ")
            self.fileName = input()
            if self.fileName == '':
                print("File name cannot be empty")
                continue
            if self.fileName[-4:] != '.txt':
                self.fileName += '.txt'
            with open(self.fileName, 'w') as file:
                if file.readable():
                    print("File already exists. Do you want to overwrite it? (y/n)")
                    choice = input()
                    if choice == 'y':
                        break
                    else:
                        continue
                else:
                    break

    def openSerial(self):
        while True:
            try:
                self.ser = serial.Serial(self.port, self.baudrate)
                break
            except:
                print("Error opening port")
                print("Port is already in use or does not exist")
                self.getAvailablePorts()
                self.getBaudrate()

    def writeToFile(self):
        print("\nData is written to file...")
        print("Interrupt the connection to stop writing to file")

        with open(self.fileName, 'w') as file:
            while True:
                if self.ser.in_waiting > 0:
                    data = self.ser.readline().decode('utf-8').strip()
                    file.write(data + '\n')

    def closeSerial(self):
        self.ser.close()
        print("Serial connection closed")