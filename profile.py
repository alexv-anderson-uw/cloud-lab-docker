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

node = request.XenVM("node")
node.cores = 2
node.ram = 2048
node.disk = 8

portal.context.printRequestRSpec()