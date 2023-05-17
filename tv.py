#Class TV:
    #Properties:
        #channel: int
        #volumeLevel: int
        #on: bool
def __init__(self):
        self.channel = 1
        self.volumeLevel = 1
        self.on = False

    #Methods:
        #turnOn(): None
        def turnOn(self):
            self.on = True
        #turnOff(): None
        def turnOff(self):
            self.on = False
        #getChannel(): int
        def getChannel(self):
            return self.channel
        #setChannel(channel: int): None
        def setChannel(self, channel):
            if self.on and 1 <= channel <= 120:
                self.channel = channel
        #getVolume(): int
        def getVolume(self):
            return self.volumeLevel
        #setVolume(volumeLevel: int): None
        def setVolume(self, volumeLevel):
            if self.on and 1 <= volumeLevel <= 7:
                self.volumeLevel = volumeLevel

        #channelUp(): None
        #channelDown(): None
        #volumeUp(): None
        #volumeDown(): None


#Create an instance of TV called tv1
#Create an instance of TV called tv2

#Turn on tv1
#Set tv1's channel to 30
#Set tv1's volume level to 3

#Turn on tv2
#Set tv2's channel to 3
#Set tv2's volume level to 2

#Print tv1's information
#Print tv2's information 
