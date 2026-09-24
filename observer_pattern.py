class Display:
    def update(self, temp):
        print("Temperature is", temp)


class WeatherStation:
    def __init__(self):
        self.devices = []

    def add(self, device):
        self.devices.append(device)

    def setTemp(self, temp):
        for d in self.devices:
            d.update(temp)


d1 = Display()
d2 = Display()

station = WeatherStation()

station.add(d1)
station.add(d2)

station.setTemp(30)