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

from model.post.post import Post
from model.user.user import User


class AddPost(object):

    def __init__(self, user_repository, time_provider):
        self.user_repository = user_repository
        self.time_provider = time_provider

    def do_it(self, user_name, post):
        user = self._get_user(user_name)
        self.user_repository.add(
            Post(user, post, self.time_provider.time_now()))

    def _get_user(self, user_name):
        user = self.user_repository.get(user_name)
        if not user:
            user = self._create_user(user_name)
        return user

    def _create_user(self, user_name):
        user = User(user_name)
        self.user_repository.create(user)
        return user
