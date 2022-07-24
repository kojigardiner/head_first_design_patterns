# Device base class
class Device:
    name: str

    def __init__(self, name: str):
        self.name = name


class Light(Device):
    def __init__(self, name: str):
        super().__init__(name)

    def on(self):
        print(f"{self.name}: turning light on")

    def off(self):
        print(f"{self.name}: turning light off")


class GarageDoor(Device):
    def __init__(self, name: str):
        super().__init__(name)

    def up(self):
        print(f"{self.name}: garage door going up")

    def down(self):
        print(f"{self.name}: garage door going down")

    def stop(self):
        print(f"{self.name}: garage door stopping")

    def light_on(self):
        print(f"{self.name}: garage door light on")

    def light_off(self):
        print(f"{self.name}: garage door light off")


class Stereo(Device):
    volume: int

    def __init__(self, name: str):
        super().__init__(name)

    def on(self):
        print(f"{self.name}: stereo is on")

    def off(self):
        print(f"{self.name}: stereo is off")

    def set_cd(self):
        print(f"{self.name}: stereo is playing cd")

    def set_dvd(self):
        print(f"{self.name}: stereo is playing dvd")

    def set_radio(self):
        print(f"{self.name}: stereo is playing radio")

    def set_volume(self, volume: int):
        self.volume = volume

        print(f"{self.name}: stereo volume is {self.volume}")


class CeilingFan(Device):
    HIGH: int = 3
    MEDIUM: int = 2
    LOW: int = 1
    OFF: int = 0
    speed: int

    def __init__(self, name: str):
        super().__init__(name)
        self.speed = self.OFF

    # def on(self):
    #     print(f"{self.name}: ceiling fan on")

    # def off(self):
    #     print(f"{self.name}: ceiling fan off")

    def high(self):
        self.speed = self.HIGH
        print(f"{self.name}: ceiling fan high")

    def medium(self):
        self.speed = self.MEDIUM
        print(f"{self.name}: ceiling fan medium")

    def low(self):
        self.speed = self.LOW
        print(f"{self.name}: ceiling fan low")

    def off(self):
        self.speed = self.OFF
        print(f"{self.name}: ceiling fan off")

    def get_speed(self):
        return self.speed


class HotTub(Device):
    temp: int

    def __init__(self, name: str):
        super().__init__(name)
        temp = 98

    def on(self):
        print(f"{self.name}: hot tub on")

    def off(self):
        print(f"{self.name}: hot tub off")

    def set_temp(self, temp: int):
        self.temp = temp
        print(f"{self.name}: hot tub temperature is {temp}")

    def jets_on(self):
        print(f"{self.name}: hot tub jets on")

    def jets_off(self):
        print(f"{self.name}: hot tub jets off")


class TV(Device):
    channel: str

    def __init__(self, name: str):
        super().__init__(name)
        channel = "3"

    def on(self):
        print(f"{self.name}: tv on")

    def off(self):
        print(f"{self.name}: tv off")

    def set_input_channel(self, channel: str):
        self.channel = channel
        print(f"{self.name}: tv input set to {channel}")
