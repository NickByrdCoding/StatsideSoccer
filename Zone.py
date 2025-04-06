class Zone:
    def __init__(self, channel, third):
        self.number = (third - 1) * 5 + channel
        self.channel = channel
        self.third = third