from .commands import CommandProcessor

class PitonetonInterpreter:
    def __init__(self):
        self.variables = {}
        self.command_processor = CommandProcessor(self.variables)

    def execute(self, command):
        self.command_processor.process(command)