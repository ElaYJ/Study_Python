class NormalTV:

    def __init__(self, i=32, c='black', r='full-HD'):
        self.inch = i
        self.color = c
        self.resolution = r
        self.smartTV = 'off'
        self.aiTV = 'off'

    def turnOn(self):
        print('TV power on!!')

    def turnOff(self):
        print('TV power off!!')

    def printTVInfo(self):
        print(f'inch: {self.inch}inch')
        print(f'color: {self.color}')
        print(f'resolution: {self.resolution}')
        print(f'smartTV: {self.smartTV}')
        print(f'aiTV: {self.aiTV}')


class TV4k(NormalTV):

    def __init__(self, i, c, r='4k'):
        super().__init__(i, c, r)

    def setSmartTV(self, s):
        self.smartTV = s


class TV8k(NormalTV):

    def __init__(self, i, c, r='8k'):
        super().__init__(i, c, r)

    def setSmartTV(self, s):
        self.smartTV = s

    def setAiTV(self, a):
        self.aiTV = a


if __name__ == '__main__':
    my4KTv = TV4k(65, 'silver', '4K')
    my4KTv.setSmartTV('on')
    my4KTv.turnOn()
    my4KTv.printTVInfo()
    my4KTv.turnOff()

    my8KTv = TV8k(75, 'black', '8K')
    my8KTv.setSmartTV('on')
    my8KTv.setAiTV('on')
    my8KTv.turnOn()
    my8KTv.printTVInfo()
    my8KTv.turnOff()
