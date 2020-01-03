"""
Constructs a XenVM and installs PySpark

Instructions:
Wait for the profile instance to start, and then log in to the VM via the
ssh port specified below.  (Note that in this case, you will need to access
the VM through a high port on the physical host, since we have not requested
a public IP address for the VM itself.)
"""

import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

node = request.RawPC("node")
node.cores = 64
node.ram = 8192
node.disk = 16
# Ubuntu 16.04 LTS 64-bit
# node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD"

portal.context.printRequestRSpec()
