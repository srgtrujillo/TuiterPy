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

from command import Command


class ReadWallTimeLineCommand(Command):

    def __init__(self, pattern, printer, read_wall_timeline):
        super(ReadWallTimeLineCommand, self).__init__(pattern)
        self.printer = printer
        self.read_wall_timeline = read_wall_timeline

    def process(self):
        match = self.get_match()
        timeline = self.read_wall_timeline.get_it(match.group(1))
        self.printer.load(timeline)
        return self.printer
