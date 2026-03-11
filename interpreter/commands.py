# Обработка команд для языка Питонетон

class CommandProcessor:
    def __init__(self, variables):
        self.variables = variables

    def process(self, command):
        if command.startswith('let '):
            self._let_command(command)
        elif command.startswith('print '):
            self._print_command(command)
        else:
            raise ValueError(f'Unknown command: {command}')

    def _let_command(self, command):
        parts = command[4:].split('=')
        if len(parts) != 2:
            raise ValueError('Invalid let statement')
        var_name = parts[0].strip()
        value = parts[1].strip()
        self.variables[var_name] = value

    def _print_command(self, command):
        value = command[6:].strip()
        if value in self.variables:
            print(self.variables[value])
        else:
            print(value)