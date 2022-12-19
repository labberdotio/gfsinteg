
# 
# Copyright (c) 2021, John Grundback
# All rights reserved.
# 



class GFSITG(object):

    def __init__(
        self,

        gfs_host,
        gfs_port,
        gfs_username,
        gfs_password,

        gfs_ns,

        **kwargs):
        self.configure(

            gfs_host = gfs_host,
            gfs_port = gfs_port,
            gfs_username = gfs_username,
            gfs_password = gfs_password,

            gfs_ns = gfs_ns,

        )

    def configure(
        self,

        gfs_host,
        gfs_port,
        gfs_username,
        gfs_password,

        gfs_ns,

        **kwargs):

        self.gfs_host = gfs_host
        self.gfs_port = gfs_port
        self.gfs_username = gfs_username
        self.gfs_password = gfs_password

        self.gfs_ns = gfs_ns

        # 

        return self

    def schema(self):

        from gfs.schema.schema import GFSSchema
        from gfs.schema.schema import GFSSchemaDecoder

        path = "./src/py/schema.json"

        file = open(path, "r")
        data = file.read()

        # GFSSchema.build(json.JSONDecoder.decode(self, data))
        root = GFSSchemaDecoder().decode(data)

        return root
