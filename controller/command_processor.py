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


class CommandProcessor(object):

    POST = "->"
    FOLLOWS = "follows"
    WALL = "wall"

    POST_COMMAND = ".* %s .*" % POST
    FOLLOW_COMMAND = ".* %s .*" % FOLLOWS
    WALL_COMMAND = ".* %s" % WALL
    EXIT_COMMAND = "exit"
    READ_COMMAND = ".*"

    def __init__(self, commands):
        self.commands = commands

    def process(self, command):
        map(lambda c: c.process(),
            filter(lambda c: c.matches(command), self.commands))

    def exit(self, command):
        return command == self.EXIT_COMMAND
