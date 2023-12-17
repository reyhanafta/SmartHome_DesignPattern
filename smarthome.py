class SmartHomeSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.components = []
        return cls._instance

    def register_component(self, component):
        self.components.append(component)

    def get_components(self):
        return self.components

class SmartHomeFacade:
    def __init__(self):
        self.system = SmartHomeSystem()

    def add_component(self, component):
        self.system.register_component(component)

    def get_components(self):
        return self.system.get_components()

class Command:
    def __init__(self, operation):
        self.operation = operation

    def execute(self):
        self.operation()

class Device:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class TV(Device):
    def turn_on(self):
        print("TV is turned on")

    def turn_off(self):
        print("TV is turned off")

class AC(Device):
    def turn_on(self):
        print("AC is turned on")

    def turn_off(self):
        print("AC is turned off")

class CommandOn(Command):
    def __init__(self, device):
        super().__init__(device.turn_on)

class CommandOff(Command):
    def __init__(self, device):
        super().__init__(device.turn_off)

class RemoteControl:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, command):
        self.commands[name] = command

    def execute_command(self, name):
        self.commands[name].execute()

facade = SmartHomeFacade()
tv = TV()
ac = AC()

facade.add_component(tv)
facade.add_component(ac)

remote = RemoteControl()
remote.add_command("tv_on", CommandOn(tv))
remote.add_command("tv_off", CommandOff(tv))
remote.add_command("ac_on", CommandOn(ac))
remote.add_command("ac_off", CommandOff(ac))

remote.execute_command("tv_off")
remote.execute_command("ac_on")

# output:
# TV off
# AC on