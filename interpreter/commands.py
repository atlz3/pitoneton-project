from .errors import PitonetonError

class CommandProcessor:
    def __init__(self, variables):
        self.variables = variables

    def process(self, command):
        if command.startswith('let '):
            self._let_command(command)
        elif command.startswith('print '):
            self._print_command(command)
        elif command.startswith('if '):
            self._if_command(command)
        else:
            raise PitonetonError(f'Unknown command: {command}')

    def _let_command(self, command):
        parts = command[4:].split('=')
        if len(parts) != 2:
            raise PitonetonError('Invalid let statement')
        var_name = parts[0].strip()
        value = eval(parts[1].strip(), {}, self.variables)
        self.variables[var_name] = value

    def _print_command(self, command):
        value = command[6:].strip()
        if value in self.variables:
            print(self.variables[value])
        else:
            print(eval(value, {}, self.variables))

    def _if_command(self, command):
        # Example of adding a simple if condition
        parts = command[3:].split(' then ')
        if len(parts) != 2:
            raise PitonetonError('Invalid if statement')
        condition = parts[0].strip()
        action = parts[1].strip()
        if eval(condition, {}, self.variables):
            self.process(action)