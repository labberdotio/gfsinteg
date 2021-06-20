
# 
# Copyright (c) 2021, John Grundback
# All rights reserved.
# 

import unittest



class MainTest(unittest.TestCase):

    # def test_test1(self):

    #     from gfs.decoder.decoder import GFSModelDecoder
    #     from gfs.model.model import GFSModel

    #     path = "./src/py/test1.json"

    #     file = open(path, "r")
    #     data = file.read()
    #     models = GFSModelDecoder().decode(data)

    #     self.assertIsNotNone(models)
    #     self.assertEqual(len(models), 1)

    #     for model in models:
    #         self.assertEqual(model.getID(), "1")
    #         self.assertEqual(model.getName(), "myname")
    #         self.assertEqual(model.getName(), "myname")
    #         self.assertEqual(model.getType(), "somelabel")

    # def test_test2(self):

    #     from gfs.schema.schema import GFSSchema
    #     from gfs.schema.schema import GFSSchemaDecoder

    #     path = "./src/py/schema.json"

    #     file = open(path, "r")
    #     data = file.read()

    #     # GFSSchema.build(json.JSONDecoder.decode(self, data))
    #     root = GFSSchemaDecoder().decode(data)
    #     print(root)

    #     defs = root.getDefs()
    #     for cdef in defs:
    #         print(cdef)

    # def test_test3(self):

    #     from gfs.schema.schema import GFSSchema
    #     from gfs.schema.schema import GFSSchemaDecoder

    #     path = "./src/py/schema.json"

    #     file = open(path, "r")
    #     data = file.read()

    #     # GFSSchema.build(json.JSONDecoder.decode(self, data))
    #     root = GFSSchemaDecoder().decode(data)
    #     # print(root)

    #     # path2 = "./src/py/machines.json"

    #     # file2 = open(path2, "r")
    #     # data2 = file2.read()

    #     # cdef = root.getDef('Machine')
    #     # print(cdef)

    #     # # models = cdef.decode(data2)
    #     # # print(models)

    #     # models = cdef.models(data2)
    #     # print(models)

    def test_test4(self):

        from gfs.integration.integration import GFSITG

        # gfs_ns = "gfs1" # os.environ.get("GFS_NAMESPACE", "gfs1")
        gfs_host = "localhost" # os.environ.get("GFS_HOST", "localhost")
        gfs_port = "5000" # os.environ.get("GFS_PORT", "5000")
        gfs_username = None # os.environ.get("GFS_USERNAME", "root")
        gfs_password = None # os.environ.get("GFS_PASSWORD", "root")

        print('1')

        integration = GFSITG(
            gfs_host = gfs_host,
            gfs_port = gfs_port,
            gfs_username = gfs_username,
            gfs_password = gfs_password,
        )
        print(integration)

        fullschema = integration.schema()
        print(" ** ")
        print(fullschema)
        print(" ** ")

        fullschema.getName()
        fullschema.get('name')

        fullschema.getType()
        fullschema.get('type')

        fullschema.getDefinitions()
        fullschema.get('definitions')

        # # ?
        # # machineSchema = integration.typeSchema('Machine')

        # machineSchema = fullschema.getDefinitions().getMachine()
        # machineSchema = fullschema.get('definitions').get('Machine')

        # machine = machineSchema.new()
        # machine = machineSchema.create({
        #     'name': 'new name'
        # })

        # machine = machineSchema.load(1)
        # machine = machineSchema.update(
        #     1, 
        #     {
        #         'name': 'new name'
        #     }
        # )
        # machine = machineSchema.delete(1)

        # machine = machine.create()
        # machine.setName('new name')
        # machine.set('name', 'new name')
        # machine.update()



if __name__ == "__main__":

    unittest.main()
