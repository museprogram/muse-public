#!/usr/bin/python
##
## Copyright (c) 2014-2017 Leidos.
## 
## License: 3-clause BSD, see https://opensource.org/licenses/BSD-3-Clause
##
##
## Developed under contract #FA8750-14-C-0241
##

###################
from projectDB import MuseProjectDB

###################
db = MuseProjectDB()
db.dropProjectsTable()
db.createProjectsTable()