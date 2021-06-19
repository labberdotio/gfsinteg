
# 
# Copyright (c) 2017, 2021, John Grundback
# All rights reserved.
# 

# import sys
# import types

import importlib
import json

# https://gist.github.com/tokibito/5325207
# http://stackoverflow.com/questions/1176136/convert-string-to-python-class-object


class GFSModel(object):
    ID_FIELD = "id" # None
    NAME_FIELD = "name" # None
    TYPE_FIELD = "label" # None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key != "__class__":
                setattr(self, key, value)

    def __str__(self):
        return "%s - ID: %s, NAME: %s, TYPE: %s" % (
            type(self), self.getID(), self.getName(), self.getType()
        )

    def attr(self, key):
        if not hasattr(self, key):
            return None
        return getattr(self, key)

    def isString(self, key):
        if not hasattr(self, key):
            return False
        if isinstance(getattr(self, key), (str, unicode)):
            return True
        else:
            return False

    def asArray(self, key):
        if not hasattr(self, key):
            return []
        if isinstance(getattr(self, key), list):
            return getattr(self, key)
        else:
            items = []
            items.append(getattr(self, key))
            return items

    def ID(self):
        return self.getID()

    def getID(self):
        if not self.ID_FIELD:
            return None
        return self.attr(self.ID_FIELD)

    def getName(self):
        if not self.NAME_FIELD:
            return None
        name = None
        if isinstance(self.NAME_FIELD, list):
            for attr in self.NAME_FIELD:
                if self.attr(attr):
                    name = self.attr(attr)
        else:
            name = self.attr(self.NAME_FIELD)
        return name

    def getType(self):
        if not self.TYPE_FIELD:
            return None
        return self.attr(self.TYPE_FIELD)
