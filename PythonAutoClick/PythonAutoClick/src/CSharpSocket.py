import socket
from time import sleep
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class CSharpSocket():

     def __init__(self):
         self.host = "127.0.0.1"
         self.port =  25001
         self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         self.sock.connect((self.host, self.port))

     def Disconnect(self):
         self.sock.close()

     def SendData(self, message):
         self.sock.sendall(message.encode("UTF-8")) #Converting string to Byte, and sending it to C#

     def RecieveData(self):
         receivedData = self.sock.recv(1024).decode("UTF-8") #receiveing data in Byte fron C#, and converting it to String
         return str(receivedData)

     def Trace(self,msg, delay = 0):
         try:
             sleep(delay)
             self.SendData(msg)
             print(msg)
         except Exception as e:
             raise ValueError(str(e))

     def TraceError(self,msg):
         self.Trace("[Python Error] " + msg)

 #Debug when no socket is available

#@singleton
#class CSharpSocket():

#   def __init__(self):
#       pass

#   def Disconnect(self):
#       pass

#   def SendData(self, message):
#       pass
#   def RecieveData(self):
#       pass   

#   def Trace(self,msg, delay = 0):
#       print(msg)

#   def TraceError(self,msg):
#       self.Trace("[Python Error] " + msg)
