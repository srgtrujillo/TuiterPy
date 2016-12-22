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


class View(object):

    def show_welcome(self):
        raise NotImplementedError

    def show_farewell(self):
        raise NotImplementedError

    def show_prompt(self):
        raise NotImplementedError

    def read_command_line(self):
        raise NotImplementedError

    def show_user_timeline(self, timeline):
        raise NotImplementedError

    def show_wall_timeline(self, timeline):
        raise NotImplementedError
