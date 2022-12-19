
# 
# Copyright (c) 2018, 2021, John Grundback
# All rights reserved.
# 

import importlib
import json

# https://gist.github.com/tokibito/5325207
# http://stackoverflow.com/questions/1176136/convert-string-to-python-class-object

# python 3, also seems to work with Python 2.7.10
def class_for_name_py3(class_name, module_name = False):
    C = False
    M = False
    if module_name:
        M = importlib.import_module(module_name)
    if M:
        C = getattr(M, class_name)
    else:
        C = globals()[class_name]
    return C

# python < 2.7, works with Python 2.7.10
def class_for_name_py27(class_name, module_name = False):
    C = False
    M = False
    if module_name:
        M = __import__(module_name, globals(), locals(), class_name)
    if M:
        C = getattr(M, class_name)
    else:
        C = globals()[class_name]
    return C

def class_for_name(class_name, module_name = False):
    return class_for_name_py3(class_name, module_name)

def postprocessor(path, key, value):
    if key and value and not key.startswith('@') and isinstance(value, dict):
        value['__class__'] = key
        # value['__type__'] = key
    return key, value

class GFSModelDecoder(json.JSONDecoder):

    def __init__(self, format = "JSON", class_name_hint = False, module_name_hint = False):
        json.JSONDecoder.__init__(self, object_hook=self.asModel)
        self.format = format
        self.class_name_hint = class_name_hint
        self.module_name_hint = module_name_hint
        self.default_class_name = "GFSModel"
        self.default_module_name = "gfs.model.model"

    def cleanup(self, data):
        return data

    def model(self, data, key = False):
        m = self.decode(data)
        if key:
            return getattr(m, key)
        else:
            return m

    def decode(self, data, key = False):
        data = self.cleanup(data)
        if self.format == "XML":
            import xmltodict
            data = xmltodict.parse(data, postprocessor=postprocessor)
            data = json.dumps(data)
        # Call parent class method
        return json.JSONDecoder.decode(self, data)

    def moduleForName(self, name):
        return name

    def classForName(self, name):
        return name

    def moduleName(self, data, **kwargs):
        module_name = None
        if '__module__' in data:
            module_name = self.moduleForName(data.pop('__module__'))
        elif self.module_name_hint:
            module_name = self.module_name_hint
        else:
            module_name = self.default_module_name
        return module_name

    def className(self, data, **kwargs):
        class_name = None
        if '__class__' in data:
            class_name = self.classForName(data.pop('__class__'))
        elif self.class_name_hint:
            class_name = self.class_name_hint
        else:
            class_name = self.default_class_name
        return class_name

    def asModel(self, data, **kwargs):

        module_name = self.moduleName(data, **kwargs)
        class_name = self.className(data, **kwargs)

        if module_name and class_name:
            M = class_for_name(class_name, module_name)
            m = M(**data)
        elif class_name:
            M = class_for_name(class_name, None)
            m = M(**data)
        else:
            M = class_for_name(self.default_class_name, 
                self.default_module_name)
            m = M(**data)
        return m
