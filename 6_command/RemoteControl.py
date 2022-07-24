from abc import ABC, abstractmethod
from typing import List

from Commands import *


class RemoteControl:
    on_commands: List[Command]
    off_commands: List[Command]
    undo_command: Command

    def __init__(self, slots: int):
        self.on_commands = []
        self.off_commands = []

        for i in range(slots):
            self.on_commands.append(NoCommand())
            self.off_commands.append(NoCommand())

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()

    def __str__(self) -> str:  # override
        s = "\n------ Remote Control ------\n"
        for i in range(len(self.on_commands)):
            s += f"[slot {i}] {self.on_commands[i].__class__.__name__}\t{self.off_commands[i].__class__.__name__}\n"
        return s


class RemoteControlWithUndo:
    on_commands: List[Command]
    off_commands: List[Command]
    undo_command: Command

    def __init__(self, slots: int):
        self.on_commands = []
        self.off_commands = []

        for i in range(slots):
            self.on_commands.append(NoCommand())
            self.off_commands.append(NoCommand())
            self.undo_command = NoCommand()

    def set_command(self, slot: int, on_command: Command, off_command: Command):
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command

    def on_button_was_pushed(self, slot: int):
        self.on_commands[slot].execute()
        self.undo_command = self.on_commands[slot]

    def off_button_was_pushed(self, slot: int):
        self.off_commands[slot].execute()
        self.undo_command = self.off_commands[slot]

    def undo_button_was_pushed(self):
        self.undo_command.undo()

    def __str__(self) -> str:  # override
        s = "\n------ Remote Control ------\n"
        for i in range(len(self.on_commands)):
            s += f"[slot {i}] {self.on_commands[i].__class__.__name__}\t{self.off_commands[i].__class__.__name__}\n"
        s += f"[undo] {self.undo_command.__class__.__name__}\n"
        return s


if __name__ == "__main__":
    print("\n\nTesting SimpleRemoteControl")

    # invoker
    remote = SimpleRemoteControl()

    # receivers
    light = Light("Light")
    garage_door = GarageDoor("GarageDoor")

    # commands (with pointer to receiver)
    light_on = LightOnCommand(light)
    garage_open = GarageDoorUpCommand(garage_door)

    # give the invoker the command object
    remote.set_command(light_on)
    remote.button_was_pressed()

    remote.set_command(garage_open)
    remote.button_was_pressed()

    print("\n\nTesting RemoteControl")
    remote_control = RemoteControl(7)

    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = CeilingFan("Living Room")
    garage_door = GarageDoor("Garage")
    stereo = Stereo("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)
    ceiling_fan_on = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)
    garage_door_up = GarageDoorUpCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)
    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_control.set_command(3, stereo_on_with_cd, stereo_off)

    print(remote_control)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.on_button_was_pushed(3)
    remote_control.off_button_was_pushed(3)

    print("\n\nTesting undo")

    remote_control = RemoteControlWithUndo(7)
    living_room_light = Light("Living Room")
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print(remote_control)

    remote_control.undo_button_was_pushed()
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(0)
    print(remote_control)
    remote_control.undo_button_was_pushed()

    print("\n\nTesting ceiling fan undo")

    remote_control = RemoteControlWithUndo(7)
    ceiling_fan = CeilingFan("Living Room")
    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_medium = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    remote_control.set_command(0, ceiling_fan_medium, ceiling_fan_off)
    remote_control.set_command(1, ceiling_fan_high, ceiling_fan_off)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print(remote_control)

    remote_control.undo_button_was_pushed()

    remote_control.on_button_was_pushed(1)
    print(remote_control)
    remote_control.undo_button_was_pushed()

    print("\n\nTesting macro command")
    light = Light("Living Room")
    tv = TV("Living Room")
    stereo = Stereo("Living Room")
    hottub = HotTub("Patio")

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)
    tv_on = TVOnCommand(tv)
    tv_off = TVOffCommand(tv)
    hottub_on = HotTubOnCommand(hottub)
    hottub_off = HotTubOffCommand(hottub)
    stereo_on = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    party_on = [light_on, stereo_on, tv_on, hottub_on]
    party_off = [light_off, stereo_off, tv_off, hottub_off]

    party_on_macro = MacroCommand(party_on)
    party_off_macro = MacroCommand(party_off)

    remote_control = RemoteControlWithUndo(7)
    remote_control.set_command(0, party_on_macro, party_off_macro)
    print(remote_control)
    print("--- Pushing Macro On ---")
    remote_control.on_button_was_pushed(0)
    print("--- Pushing Macro Off ---")
    remote_control.off_button_was_pushed(0)
    print("--- Pushing Undo ---")
    remote_control.undo_button_was_pushed()
