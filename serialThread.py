import serial
from PyQt5.QtCore import pyqtSignal, QThread
import serial.tools.list_ports
import time

class SerialCommunicate(QThread):
    
    Mesaj = pyqtSignal(str)
    
    def __init__(self) -> None:
        super(SerialCommunicate, self).__init__() #Qthread dan Miras almamızı sağlıyor.
        self.seriport = serial.Serial()            #seriport bağlantısı için nesne tanımlaması 
        

class SerialThread():
    def __init__(self) -> None:
        self.Comm = SerialCommunicate()
        self.initUI()
    def initUI(self):
        self.ports = serial.tools.list_ports.comports() #Windows cihazlarda Portları listelememizi sağlıyor
        for i in self.ports :
            self.port = str(i)
        time.sleep(0.2)
    
    def connection(self) :
        self.p = self.port.split()
        self.Comm.seriport.baudrate = 9600
        self.Comm.seriport.port = self.p[0]
        try:
            self.Comm.seriport.open()
        except:
            print("Bağlantı Başarısız")
        if (self.Comm.seriport.isOpen()) :
            print("Bağlantı Gerçekleşti ")

    def disconnect(self) :
        if self.Comm.seriport.isOpen():
            self.Comm.seriport.close()
            if self.Comm.seriport.isOpen() == False:
                print("bağlantı kesildi".center(70,"-")) 
        else :
            print("Seri port zaten kapalı..".center(70,"-"),end= "\n")