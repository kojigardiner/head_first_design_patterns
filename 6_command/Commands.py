from abc import ABC, abstractmethod
from typing import List

from Devices import *


# Command abstract class
class Command(ABC):
    @abstractmethod
    def execute(self):
        raise NotImplementedError

    @abstractmethod
    def undo(self):
        raise NotImplementedError


# Commands
class LightOnCommand(Command):
    light: Light

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    light: Light

    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class GarageDoorUpCommand(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.up()

    def undo(self):
        self.garage_door.down()


class GarageDoorDownCommand(Command):
    garage_door: GarageDoor

    def __init__(self, garage_door: GarageDoor):
        self.garage_door = garage_door

    def execute(self):
        self.garage_door.down()

    def undo(self):
        self.garage_door.up()


class StereoOnWithCDCommand(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.on()
        self.stereo.set_cd()
        self.stereo.set_volume(11)

    def undo(self):
        pass


class StereoOffCommand(Command):
    stereo: Stereo

    def __init__(self, stereo: Stereo):
        self.stereo = stereo

    def execute(self):
        self.stereo.off()

    def undo(self):
        pass


class CeilingFanOnCommand(Command):
    ceiling_fan: CeilingFan

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.high()

    def undo(self):
        pass


# class CeilingFanOffCommand(Command):
#     ceiling_fan: CeilingFan

#     def __init__(self, ceiling_fan: CeilingFan):
#         self.ceiling_fan = ceiling_fan

#     def execute(self):
#         self.ceiling_fan.off()

#     def undo(self):
#         pass


class CeilingFanHighCommand(Command):
    ceiling_fan: CeilingFan
    prev_speed: int

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class CeilingFanMediumCommand(Command):
    ceiling_fan: CeilingFan
    prev_speed: int

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.medium()

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class CeilingFanLowCommand(Command):
    ceiling_fan: CeilingFan
    prev_speed: int

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.low()

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class CeilingFanOffCommand(Command):
    ceiling_fan: CeilingFan
    prev_speed: int

    def __init__(self, ceiling_fan: CeilingFan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.off()

    def undo(self):
        if self.prev_speed == CeilingFan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == CeilingFan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == CeilingFan.LOW:
            self.ceiling_fan.low()
        elif self.prev_speed == CeilingFan.OFF:
            self.ceiling_fan.off()


class NoCommand(Command):
    def __init__(self):
        pass

    def execute(self):
        pass

    def undo(self):
        pass


class HotTubOnCommand(Command):
    hottub: HotTub

    def __init__(self, hottub: HotTub):
        self.hottub = hottub

    def execute(self):
        self.hottub.on()
        self.hottub.set_temp(104)
        self.hottub.jets_on()

    def undo(self):
        self.hottub.jets_off()
        self.hottub.set_temp(98)
        self.hottub.off()


class HotTubOffCommand(Command):
    hottub: HotTub

    def __init__(self, hottub: HotTub):
        self.hottub = hottub

    def execute(self):
        self.hottub.jets_off()
        self.hottub.set_temp(98)
        self.hottub.off()

    def undo(self):
        self.hottub.on()
        self.hottub.jets_on()
        self.hottub.set_temp(104)


class TVOnCommand(Command):
    tv: TV

    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.set_input_channel("DVD")
        self.tv.on()

    def undo(self):
        self.tv.set_input_channel("3")
        self.tv.off()


class TVOffCommand(Command):
    tv: TV

    def __init__(self, tv: TV):
        self.tv = tv

    def execute(self):
        self.tv.set_input_channel("3")
        self.tv.off()

    def undo(self):
        self.tv.set_input_channel("DVD")
        self.tv.on()


class MacroCommand(Command):
    commands: List[Command]

    def __init__(self, commands: List[Command]):
        self.commands = commands

    def execute(self):
        for c in self.commands:
            c.execute()

    def undo(self):
        for c in reversed(self.commands):
            c.undo()


# Invoker
class SimpleRemoteControl:
    slot: Command

    def __init__(self):
        pass

    def set_command(self, command: Command):
        self.slot = command

    def button_was_pressed(self):
        self.slot.execute()
