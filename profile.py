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
portal.context.defineParameter( "extra_hd_size", "Size of temporary HD partition in GB (Ask for 5GB more than you need)", portal.ParameterType.INTEGER, 0 )
portal.context.defineParameter( "docker", "Install Docker?", portal.ParameterType.BOOLEAN, True )
portal.context.defineParameter( "p3_tools", "Install Python3 tools?", portal.ParameterType.BOOLEAN, False )
portal.context.defineParameter( "pyspark", "Install PySpark?", portal.ParameterType.BOOLEAN, False )

# Retrieve the values the user specifies during instantiation.
params = portal.context.bindParameters()

request = portal.context.makeRequestRSpec()

node = request.RawPC("node")
if len(params.node_type.strip()) > 0:
    node.hardware_type = params.node_type

node.disk_image = params.image

if params.docker:
    node.addService(pg.Execute(shell="bash", command="/local/repository/docker.bash"))

if params.p3_tools:
    node.addService(pg.Execute(shell="bash", command="/local/repository/python.bash"))

if params.pyspark:
    if not params.p3_tools:
        node.addService(pg.Execute(shell="bash", command="/local/repository/python.bash"))
    node.addService(pg.Execute(shell="bash", command="/local/repository/pyspark.bash"))


portal.context.printRequestRSpec()

if params.extra_hd_size > 0:
    bs = node.Blockstore("bs", "/bs_part")
    bs.size = "{}GB".format(params.extra_hd_size)
