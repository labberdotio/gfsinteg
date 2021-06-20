
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

        **kwargs):
        self.configure(

            gfs_host,
            gfs_port,
            gfs_username,
            gfs_password

        )

    def configure(
        self,

        gfs_host,
        gfs_port,
        gfs_username,
        gfs_password,

        **kwargs):

        self.gfs_host = gfs_host
        self.gfs_port = gfs_port
        self.gfs_username = gfs_username
        self.gfs_password = gfs_password

        self.api_namespace = "gfs1"

        # 

        return self

    def schema(self):

        print(" ! ")

        from gfs.schema.schema import GFSSchema
        from gfs.schema.schema import GFSSchemaDecoder

        path = "./src/py/schema.json"

        file = open(path, "r")
        data = file.read()

        # print(data)

        # GFSSchema.build(json.JSONDecoder.decode(self, data))
        root = GFSSchemaDecoder().decode(data)
        # print(root)

        print(" !! ")
        print(root)

        return root
