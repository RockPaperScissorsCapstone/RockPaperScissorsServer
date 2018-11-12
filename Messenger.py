class Messenger:
    ipAddress = [""]

    def __init__(self):
        print("messenger is running")

    def addIpAddress(self,param):
        self.ipAddress.append(param)

    def getList(self):
        return self.ipAddress

    def removeFromList(self, param):
        self.ipAddress.remove(param)