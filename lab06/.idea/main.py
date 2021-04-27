import unittest

class Commands():
    def __init__(self, system_name):
        self.system_name = system_name

        self.linux_commands = {
            'ping': {
                'description': 'Use the ping command to check your connectivity status to a server'
            },
            'uptime': {
                'description': 'Show how long the system has been running + load.'
            },

            'pwd': {
                'description': 'Use the pwd command to find out the path of the current working directory (folder) you’re in'
            },
            'ps': {
                'description': 'Display your currently running processes.',
                '-ef': 'Display all the currently running processes on the system.'
            },
            'hostname': {
                'description': 'Show system host name.',
                '-i': 'Display all local IP addresses of the host.'
            }
        }

        self.windows_commands = {
            'cls': {
                'description': 'Used to clean screen.'
            },
            'mkdir': {
                'description': 'Creates a directory or subdirectory.'
            },

            'cmd': {
                'description': 'Open another console '
            },
            'shutdown': {
                'description': 'Shut downs system.',
                '/s': 'Shuts down system immediately.',
                '/r': 'Restarts system.'
            },
            'vol': {
                'description': 'Displays the disk / volume label and serial number'
            }
        }

        if system_name == "Windows":
            self.commands = self.windows_commands
        elif system_name == "Linux":
            self.commands = self.linux_commands
        else:
            raise Exception("Wrong system name!")

    def does_command_exist(self, command):
        command = command.lower()
        if not isinstance(command, str):
            return None
        good = command.lower().split()
        if len(good) < 1:
            return None
        return good

    def show_command(self, command):
        command = command.lower()
        is_good = self.does_command_exist(command)
        if is_good is None:
            return None

        if is_good[0] in self.commands:
            command = self.commands[is_good[0]]
            if len(is_good) > 1:
                if is_good[1] in command:
                    return command[is_good[1]]
                else:
                    return command['description']
            else:
                return command['description']
        else:
            return None


class TestCommands(unittest.TestCase):
    def test_system_name_windows(self):
        system_name = "Windows"
        commands = Commands(system_name)
        assert commands.system_name == system_name

    def test_system_name_linux(self):
        system_name = "Linux"
        commands = Commands(system_name)
        assert commands.system_name == system_name

class TestLinux(unittest.TestCase):
    def linuxTestPing(self):
        command = Commands("Linux")
        result = command.show_command('ping')
        assert result == 'Use the ping command to check your connectivity status to a server'

    def linuxTestPwd(self):
        command = Commands("Linux")
        result = command.show_command('pwd')
        assert result == 'Use the pwd command to find out the path of the current working directory (folder) you’re in'

    def linuxTestPsEf(self):
        command = Commands("Linux")
        result = command.show_command('ps -ef')
        assert result == 'Display all the currently running processes on the system.'

    def linuxTestHostnameI(self):
        command = Commands("Linux")
        result = command.show_command('hostname -i')
        assert result == 'Display all local IP addresses of the host.'

    def linuxTestUptime(self):
        command = Commands("Linux")
        result = command.show_command('uptime')
        assert result == 'Show how long the system has been running + load.'

class TestWindows(unittest.TestCase):
    def windowsTestCls(self):
        command = Commands("Windows")
        result = command.show_command('cls')
        assert result == 'Used to clean screen.'

    def windowsTestMkdir(self):
        command = Commands("Windows")
        result = command.show_command('mkdir')
        assert result == 'Creates a directory or subdirectory.'

    def windowsTestCmd(self):
        command = Commands("Windows")
        result = command.show_command('cmd')
        assert result == 'Open another console '

    def windowsTestShutdownS(self):
        command = Commands("Windows")
        result = command.show_command('shutdown /s')
        assert result == 'Shuts down system immediately.'

    def windowsTestVol(self):
        command = Commands("Windows")
        result = command.show_command('vol')
        assert result == 'Displays the disk / volume label and serial number'


if __name__ == '__main__':
    unittest.main()