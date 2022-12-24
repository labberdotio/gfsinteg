
# 
# Copyright (c) 2022, John Grundback
# All rights reserved.
# 

from gfs.error.error import GFSError

from gfs.model.model import GFSModel



class GFSInstance(GFSModel):
    ID_FIELD = "id" # None
    NAME_FIELD = "name" # None
    TYPE_FIELD = "label" # None

    TYPESCHEMA_FIELD = "typeschema"
    TYPELABEL_FIELD = "typelabel"
    TYPELABELS_FIELD = "typelabels"

    # def __getattr__(self, attr):
    #     return None

    # # Gets called when an attribute is accessed
    # def __getattribute__(self, item):
    #     return object.__getattribute__(self, item)

    # Gets called when the item is not found via __getattribute__
    # def __getattr__(self, item):
    #     return super(GFSBaseSchema, self).__getattr__(item)

    # def __getattr__(self, name: str):
    def __getattr__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        return None

    def __setattr__(self, name, value):
        # print(" !! __setattr__ !! ")
        # print( name )
        # print( value )

        # print( self.typeschema.properties.get(name) )
        if not self.typeschema.properties.get(name):
            raise GFSError("Type " + str(self.typeschema.name) + " does not declare a property " + str(name) )

        else:
            print(" Setting " + str(name) + " to " + str(value))
            self.__dict__[name] = value

    def get(self, item):
        return self.attr(item) 
