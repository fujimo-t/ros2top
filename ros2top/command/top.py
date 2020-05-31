from asciimatics.screen import ManagedScreen
from ros2cli.command import CommandExtension
from time import sleep

class TopCommand(CommandExtension):
    def main(self, *, parser, args):
        with ManagedScreen() as screen:
            screen.print_at('test', 0, 0)
            screen.refresh()
            sleep(10)

        return 0
