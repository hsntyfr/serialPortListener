import serialPortListener

listener = serialPortListener.SerialListener()
listener.getAvailablePorts()
listener.getBaudrate()
listener.getFileName()
listener.openSerial()
listener.writeToFile()