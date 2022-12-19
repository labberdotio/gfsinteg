
# 
# Copyright (c) 2020, 2021, John Grundback
# All rights reserved.
# 

# 
from __future__ import print_function
from future.utils import iteritems

from gfs.common.log import GFSLogger

from gfs.model.model import GFSModel
from gfs.decoder.decoder import GFSModelDecoder



# 
class GFSBaseSchema(GFSModel):

    logger = GFSLogger.getLogger("GFSBaseSchema")

    # def __getattr__(self, attr):
    #     print(" __getattr__ ")
    #     print(attr)
    #     return None

    # # Gets called when an attribute is accessed
    # def __getattribute__(self, item):
    #     print(" __getattribute__ ")
    #     print(item)
    #     return super(GFSBaseSchema, self).__getattribute__(item)
    #     # return self.get(item)

    # # Gets called when the item is not found via __getattribute__
    # def __getattr__(self, item):
    #     print(" __getattr__ ")
    #     print(item)
    #     # return super(GFSBaseSchema, self).__setattr__(item, 'orphan')
    #     # return self.get(item)
    #     # return self[item]
    #     return super(GFSBaseSchema, self).__getattr__(item)
    #     # return getattr(self, item)

    # def get(self, item):
    #     print(" !! GET !! ")
    #     print(item)
    #     return self.attr(item)



# TODO: Not sure this is correct, but I need a full schema
class GFSSchema(GFSBaseSchema):
    ID_FIELD = "id" # None
    NAME_FIELD = "name" # None
    TYPE_FIELD = "label" # None

    logger = GFSLogger.getLogger("GFSSchema")



# 
class GFSSchemaProperty(GFSSchema):

    logger = GFSLogger.getLogger("GFSSchemaProperty")



# 
class GFSSchemaDefinitions(GFSSchema):

    logger = GFSLogger.getLogger("GFSSchemaDefinitions")

    def getDefinitions(self):
        defs = []
        for prop, value in iteritems(vars(self)):
            if prop and len(prop) > 0:
                defs.append(value)
        return defs

    def getDefinition(self, type):
        for prop, value in iteritems(vars(self)):
            if prop and len(prop) > 0:
                if prop == type:
                    return value
        return None



# 
class GFSRootSchema(GFSSchema):

    logger = GFSLogger.getLogger("GFSRootSchema")

    def __str__(self):
        return "ROOT SCHEMA: %s \n - NAME: %s, TYPE: %s" % (
            type(self), self.getName(), self.getType()
        )

    # def getType(self):
    #     return self.attr("type")

    # def getDefinitions(self):
    #     return self.attr("definitions")

    # def getDefs(self):
    #     return self.attr("definitions").getDefinitions()

    # def getDef(self, type):
    #     return self.attr("definitions").getDefinition(type)



# 
class GFSTypeSchema(GFSSchema, GFSModelDecoder):

    logger = GFSLogger.getLogger("GFSTypeSchema")

    def __str__(self):
        return "TYPE SCHEMA: %s - NAME: %s, TYPE: %s" % (
            type(self), self.getName(), self.attr("type")
        )

    def model(self, data):
        m = self.decode(data)
        return m.get(
            "data", {}
        ).get(
            self.attr("name"), {}
        )

    def models(self, data):
        print(" !!! ")
        print(data)
        m = self.decode(data)
        print(m)
        return m.get(
            "data", {}
        ).get(
            self.attr("name") + "s", {}
        )

    # def decode(self, data, key = False):
    #     from gfs.decoder.decoder import GFSModelDecoder
    #     from gfs.model.model import GFSModel
    #     decode = GFSModelDecoder().decode(
    #         data, 
    #         key
    #     ), 
    #     return decode



# 
class GFSSchemaDecoder(GFSModelDecoder):

    logger = GFSLogger.getLogger("GFSSchemaDecoder")

    def __init__(self, format = "JSON", class_name_hint = False, module_name_hint = False):
        GFSModelDecoder.__init__(
            self, 
            format=format, 
            class_name_hint=class_name_hint, 
            module_name_hint=module_name_hint, 
        )
        self.default_class_name = "GFSSchema"
        self.default_module_name = "gfs.schema.schema"

    def className(self, data, **kwargs):

        # "type": "object",
        # "name": "root",
        # "title": "root",
        # "definitions": {
        if "name" in data and "type" in data and "definitions" in data:
            return "GFSRootSchema"

        # "type": "object",
        # "name": "Compose",
        # "version": 1,
        # "id": 237,
        # "title": "Compose",
        # "typelabel": "Compose",
        elif "name" in data and "type" in data and "properties" in data:
            return "GFSTypeSchema"

        # "data": {
        #     "type": "string"
        # },
        elif "type" in data:
            return "GFSSchemaProperty"

        # "definitions": {
        #     "Compose": {
        elif "name" not in data and "type" not in data:
            return "GFSSchemaDefinitions"

        # Nothing else
        return "GFSSchema"
