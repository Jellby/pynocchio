# coding=UTF-8
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from PySide import QtGui


class Page(object):

    def __init__(self, data, title, number):
        self._pixmap = False
        self.data = data
        self.title = title
        self.number = number

    @property
    def pixmap(self):
        if not self._pixmap:
            self._pixmap = QtGui.QPixmap()
            self._pixmap.loadFromData(self.data)
        return self._pixmap
