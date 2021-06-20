
from gfs.schema.schema import GFSSchema



    def __init__(
        self,

        gfs_ns,

        gfs_host,
        gfs_port,
        gfs_username,
        gfs_password,

        **kwargs):
        # super().__init__(**kwargs)
        self._config = None
        self.state = {}
        self.configure(
            gfs_ns,
            gfs_host,
            gfs_port,
            gfs_username,
            gfs_password
        )

    def configure(
        self,

        gfs_ns,

        gfs_host,
        gfs_port,
        gfs_username,
        gfs_password,

        **kwargs):

        self.gfs_ns = gfs_ns

        self.gfs_host = gfs_host
        self.gfs_port = gfs_port
        self.gfs_username = gfs_username
        self.gfs_password = gfs_password

        self.gfs_url = "http://" + self.gfs_host + ":" + self.gfs_port

        self.logger.info(' GremlinFS gfs host: ' + self.gfs_host)
        self.logger.info(' GremlinFS gfs port: ' + self.gfs_port)
        self.logger.info(' GremlinFS gfs username: ' + self.gfs_username)
        # self.logger.debug(' GremlinFS gfs password: ' + self.gfs_password)
        self.logger.info(' GremlinFS gfs URL: ' + self.gfs_url)



        return self


gfs_ns = os.environ.get("GFS_NAMESPACE", "gfs1")
gfs_host = os.environ.get("GFS_HOST", "localhost")
gfs_port = os.environ.get("GFS_PORT", "5000")
gfs_username = os.environ.get("GFS_USERNAME", "root")
gfs_password = os.environ.get("GFS_PASSWORD", "root")

integration = GFSITG(
    gfs_host = gfs_host,
    gfs_port = gfs_port,
    gfs_username = gfs_username,
    gfs_password = gfs_password,
)


fullschema = integration.schema()

fullschema.getName()
fullschema.get('name')

fullschema.getType()
fullschema.get('type')

fullschema.getDefinitions()
fullschema.get('definitions')

# ?
# machineSchema = integration.typeSchema('Machine')

machineSchema = fullschema.getDefinitions().getMachine()
machineSchema = fullschema.get('definitions').get('Machine')

machine = machineSchema.new()
machine = machineSchema.create({
    'name': 'new name'
})

machine = machineSchema.load(1)
machine = machineSchema.update(
    1, 
    {
        'name': 'new name'
    }
)
machine = machineSchema.delete(1)

machine = machine.create()
machine.setName('new name')
machine.set('name', 'new name')
machine.update()
