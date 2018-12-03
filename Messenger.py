class Messenger:
    ipAddress = [""]
    friendChallenge = [""]

    def __init__(self):
        print("messenger is running")

    def addIpAddress(self,param):
        self.ipAddress.append(param)

    def getList(self):
        return self.ipAddress

    def removeFromList(self, param):
        self.ipAddress.remove(param)

    def challengeMade(self, param):
        self.friendChallenge.append(param)

    def getChallengeList(self):
        return self.friendChallenge
    
    def removeFromChallengeList(self, param):
            self.friendChallenge.remove(param)