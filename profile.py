"""
Allocates a PC running Ubuntu 18

Instructions:
Wait for the profile instance to start, and then log in to the VM via SSH.
Temporary HD partition will be mounted to /bs_part
"""

import geni.portal as portal
import geni.rspec.pg as pg

portal.context.defineParameter( "image", "Image", portal.ParameterType.IMAGE, "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD" )
portal.context.defineParameter( "node_type", "Node Type", portal.ParameterType.NODETYPE, "" )
portal.context.defineParameter( "num_nodes", "Number of nodes", portal.ParameterType.INTEGER, 1 )
portal.context.defineParameter( "extra_hd_size", "Size of temporary HD partition in GB (Ask for at least 5GB more than you need)", portal.ParameterType.INTEGER, 0 )
portal.context.defineParameter( "docker", "Install Docker?", portal.ParameterType.BOOLEAN, True )
portal.context.defineParameter( "p3_tools", "Install Python3 tools?", portal.ParameterType.BOOLEAN, False )
portal.context.defineParameter( "pyspark", "Install PySpark?", portal.ParameterType.BOOLEAN, False )

# Retrieve the values the user specifies during instantiation.
params = portal.context.bindParameters()

request = portal.context.makeRequestRSpec()

if params.num_nodes < 1 or params.num_nodes > 4:
    portal.context.reportError( portal.ParameterError( "You must choose at least 1 and no more than 4 nodes." ) )

nodes = []
for node_index in range(0, params.num_nodes):
    node = request.RawPC("node{}".format(node_index))
    nodes.append(node)
    if len(params.node_type.strip()) > 0:
        node.hardware_type = params.node_type

    node.disk_image = params.image

    if params.docker:
        if params.extra_hd_size > 0:
            node.addService(pg.Execute(shell="bash", command="/local/repository/docker-block-store.bash"))
        else:
            node.addService(pg.Execute(shell="bash", command="/local/repository/docker.bash"))

    if params.p3_tools:
        node.addService(pg.Execute(shell="bash", command="/local/repository/python.bash"))

    if params.pyspark:
        if not params.p3_tools:
            node.addService(pg.Execute(shell="bash", command="/local/repository/python.bash"))
        node.addService(pg.Execute(shell="bash", command="/local/repository/pyspark.bash"))

    if params.extra_hd_size > 0:
        bs = node.Blockstore("bs", "/bs_part")
        bs.size = "{}GB".format(params.extra_hd_size)

if params.num_nodes > 1:
    ifaces = []
    for node_index, node in enumerate(nodes):
        iface = node.addInterface("if{}".format(node_index))
        iface.addAddress(pg.IPv4Address("192.168.1.{}".format(node_index), "255.255.255.0"))
        ifaces.append(iface)
    
    link = request.LAN("lan")
    for iface in ifaces:
        link.addInterface(iface)

portal.context.printRequestRSpec()
