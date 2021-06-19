
# 
# Copyright (c) 2019, 2020, 2021, John Grundback
# All rights reserved.
# 



class GFSError(Exception):

    def __init__(self, path = None):
        self.path = path



# 
# GFS GraphQL client error class
# 
class GFSGQLError(GFSError):

    def __init__(self, error):
        pass
