
# 
# Copyright (c) 2022, John Grundback
# All rights reserved.
# 

from gfs.common.log import GFSLogger

from gfs.error.error import GFSError

from gfs.model.model import GFSModel
from gfs.model.instance import GFSInstance



class GFSModelFactory(object):

    TYPESCHEMA_FIELD = "typeschema"
    TYPELABEL_FIELD = "typelabel"
    TYPELABELS_FIELD = "typelabels"

    def model(self, **kwargs):

        clazz = type(self.typeschema.name, (GFSInstance,object), dict(
            typeschema = self.typeschema, 
            typelabel = self.typeschema.name, 
            typelabels = self.typeschema.name
        ))

        # print( clazz )
        # print( clazz.typeschema )
        # print( clazz.typelabel )
        # print( clazz.typelabels )
        
        return clazz(**kwargs)