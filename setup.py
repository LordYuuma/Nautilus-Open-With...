# setup.py --- 
# 
# Filename: setup.py
# Description: 
# Author: Lord Yuuma
# Maintainer: Lord Yuuma
# Created: Mon Apr 18 20:07:22 2016 (+0200)
# Version: 
# Package-Requires: ()
# Last-Updated: Mon Apr 18 23:17:19 2016 (+0200)
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

from setuptools import setup

package = 'nautilus-open-with-menu'
version = '0.2'

setup(name=package,
      version=version,
      description="Add an Open With... menu to Nautilus",
      author="Lord Yuuma von Combobreaker",
      author_email="lordyuuma@gmail.com",
      license="GPLv3",

      data_files=[("/usr/share/nautilus-python/extensions", ["nautilus-open-with-menu.py"])])

