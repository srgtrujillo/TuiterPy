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

from model.user.user_repository import UserRepository


class InMemoryUsers(UserRepository):

    def __init__(self):
        self.user_list = []
        self.post_list = []

    def get(self, user_name):
        users = filter(lambda u: u.name == user_name, self.user_list)
        return users and users[0] or None

    def create(self, user):
        self.user_list.append(user)

    def follow(self, follower, followed):
        user = self.get(follower.name)
        if user:
            user.add_follow(followed)

    def get_post_by_user(self, user):
        return filter(lambda p: p.get_user() == user, self.post_list)

    def add(self, post):
        self.post_list.append(post)
