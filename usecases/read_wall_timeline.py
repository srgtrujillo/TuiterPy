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

from model.post.timeline import Timeline


class ReadWallTimeline(object):

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def get_it(self, user_name):
        user = self.user_repository.get_user(user_name)
        if not user:
            return Timeline()
        return self._get_timeline(user)

    def _get_timeline(self, user):
        timeline = Timeline()
        timeline.add_all(self.user_repository.get_posts_by_user(user))
        for following in user.followings():
            timeline.add_all(self.user_repository.get_posts_by_user(following))
        return timeline
