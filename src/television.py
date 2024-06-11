class television:

    def __init__(self):
        self.on = False
        self.volume = 0
        self.channel = 0

    def is_on(self):
        self.on = True
        return self.on

    def is_off(self):
        self.on = False
        return self.on

    def can_increase_volume(self, volume):
        self.volume = volume
        if self.volume < 100:
            self.volume = self.volume + 1
            return self.volume

    def can_decrease_volume(self, volume):
        self.volume = volume
        if self.volume > 0:
            self.volume = self.volume - 1
            return self.volume

    def increase_channel(self, channel):
        self.channel = channel
        if channel < 50:
            self.channel = self.channel + 1
            return self.channel

    def decrease_channel(self, channel):
        self.channel = channel
        if channel > 0:
            self.channel = self.channel - 1
            return self.channel
