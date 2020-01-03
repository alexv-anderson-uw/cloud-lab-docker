"""
Constructs a XenVM and installs PySpark

Instructions:
Wait for the profile instance to start, and then log in to the VM via the
ssh port specified below.  (Note that in this case, you will need to access
the VM through a high port on the physical host, since we have not requested
a public IP address for the VM itself.)
"""

import geni.portal as portal
import geni.rspec.pg as pg

request = portal.context.makeRequestRSpec()

node = request.RawPC("node")

node.cores = 8     # Effective Cores
node.ram = 8192 # 1024 * 4 # RAM = MB/GB * #GB
node.disk = 16      # Disk Space

# Ubuntu 16.04 LTS 64-bit
node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"

# Setup Python tools
# node.addService(pg.Execute(shell="sh", command="/local/repository/python.sh"))

# Intall PySpark
# node.addService(pg.Execute(shell="sh", command="/local/repository/pyspark.sh"))

portal.context.printRequestRSpec()
