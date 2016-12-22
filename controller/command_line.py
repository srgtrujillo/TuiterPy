# -*- encoding: utf-8 -*-
################################################################################
#    TuiterPy - A Python Command Line Social Network Application
#    Copyright (C) 2016  Sergio Trujillo (sergiotrujillomartinez@gmail.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################


class CommandLine(object):

    def __init__(self, view, processor):
        self.view = view
        self.processor = processor
        self.exit = False

    def start(self):
        self.view.show_welcome()

    def resume(self):
        self.view.show_prompt()
        command_line = self.view.read_command_line()
        self.process(command_line)

    def process(self, command):
        if self.processor.exit(command):
            self.view.show_farewell()
            self.exit = True
        else:
            printer = self.processor.process(command)
            printer.print_command()

    def is_exit(self):
        return self.exit
