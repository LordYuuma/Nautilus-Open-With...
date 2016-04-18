# nautilus-open-with-menu.py ---
#
# Filename: nautilus-open-with-menu.py
# Description:
# Author: Lord Yuuma
# Maintainer: Lord Yuuma
# Created: Mon Apr 18 17:50:46 2016 (+0200)
# Version:
# Package-Requires: ()
# Last-Updated: Mon Apr 18 23:27:37 2016 (+0200)
#           By: Lord Yuuma
# URL:
# Doc URL:
# Keywords:
# Compatibility:
#
#

# Commentary:
#
#
#
#

# Change Log:
#
#
#
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>.
#
#

# Code:

import gi
gi.require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject, Gio

from functools import reduce
from operator import and_


class NautilusOpenWithMenu(Nautilus.MenuProvider, GObject.GObject):

    def __init__(self):
        pass

    def get_file_items(self, window, files):
        if not len(files):
            return None

        root_item = Nautilus.MenuItem(name="NautilusOpenWithMenu::root",
                                      label="Open With...")
        sub_menu = Nautilus.Menu()
        root_item.set_submenu(sub_menu)

        # for a large number of files, this is a good optimization, especially when they all have the same mimetype
        # consider for instance opening thousand of music files with VLC or something similar and having to check all applications for each file
        mimetypes = list(set([file.get_mime_type() for file in files]))

        # here we search for ApplicationInfos, that are common for all
        # because we want them to open ALL the files, they have to be a subset of the applications that can open the first
        apps = [app_info for app_info in Gio.app_info_get_all_for_type(mimetypes[0])]

        # here we build the list of name of applications that can be used for all files
        names = [set([app_info.get_name() for app_info in Gio.app_info_get_all_for_type(type)])
                 for type in mimetypes]
        names = list(reduce(and_, names))

        # and then we reduce our application list to what is left
        apps = [app for app in apps if app.get_name() in names]

        if len(apps) < 2 and len(mimetypes) == 1 or len(apps) == 0:
            return []

        for app in apps:
            item = Nautilus.MenuItem(name="NautilusOpenWithMenu::{}".format(app.get_name()),
                                     label=app.get_name(),
                                     icon=app.get_icon())
            item.connect('activate', self.callback, app, files)
            sub_menu.append_item(item)

        return [root_item]

    def callback(self, menu, app, files):
        fs = [Gio.File.new_for_uri(file.get_uri()) for file in files]
        app.launch(fs)
