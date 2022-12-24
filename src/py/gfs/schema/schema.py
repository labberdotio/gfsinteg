
# 
# Copyright (c) 2020, 2021, John Grundback
# All rights reserved.
# 

# 
from __future__ import print_function
from future.utils import iteritems

# 
import json
import simplejson as json
import jsonschema
from jsonschema import validate
# from jsonschema._validators import dependencies

from gfs.common.log import GFSLogger

from gfs.error.error import GFSError

from gfs.model.model import GFSModel
from gfs.model.instance import GFSInstance

from gfs.decoder.decoder import GFSModelDecoder



# 
class GFSBaseSchema(GFSModel):

    logger = GFSLogger.getLogger("GFSBaseSchema")

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
        self.__dict__[name] = value

    def get(self, item):
        return self.attr(item)



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

    # def type(self):
    #     return self.attr("type")

    def typeschema(self, name):
        return self.attr("definitions").get(name)

    # def definitions(self):
    #     return self.attr("definitions")

    # def defs(self):
    #     return self.attr("definitions").getDefinitions()

    # def def(self, type):
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
        m = self.decode(data)
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

    def schema(self):
        schema = self.__dict__.copy()
        schema["properties"] = self.__dict__["properties"].__dict__
        return schema

    def validate(self, **kwargs):

        schema = self.schema()

        instance = kwargs
        # schema = {}
        try:
            # isValid = 
            validate(
                instance=instance, 
                schema=schema
            )

        # except Exception as e:
        except jsonschema.exceptions.ValidationError as err:

            raise GFSError(
                "Failed to validate " + str("self.label()") + 
                ", with data: " + str(kwargs) + 
                ", because: " + str(err.message)
            )
    
        except Exception as e:

            raise GFSError(
                "Failed to validate " + str("self.label()") + 
                ", with data: " + str(kwargs) + 
                ", because: " + str(e)
            )
    
        # self.logger.exit("validate", etime)

    def new(self, data = {}):
        # return GFSModel(**data)

        clazz = type(self.name, (GFSInstance,object), dict(
            typeschema = self, 
            typelabel = self.name, 
            typelabels = self.name
        ))

        # print( clazz )
        # print( clazz.typeschema )
        # print( clazz.typelabel )
        # print( clazz.typelabels )
        
        return clazz(**data)

    def create(self, data = {}):
        # return GFSModel(**data)

        clazz = type(self.name, (GFSInstance,object), dict(
            typeschema = self, 
            typelabel = self.name, 
            typelabels = self.name
        ))

        # print( clazz )
        # print( clazz.typeschema )
        # print( clazz.typelabel )
        # print( clazz.typelabels )
        
        return clazz(**data)

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
