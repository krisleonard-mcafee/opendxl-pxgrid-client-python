import os
import sys

from dxlbootstrap.util import MessageUtils
from dxlclient.client_config import DxlClientConfig
from dxlclient.client import DxlClient

root_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(root_dir + "/../..")
sys.path.append(root_dir + "/..")

from dxlciscopxgridclient.client import CiscoPxGridClient

# Import common logging and configuration
from common import *

# Configure local logger
logging.getLogger().setLevel(logging.ERROR)
logger = logging.getLogger(__name__)

# Create DXL configuration from file
config = DxlClientConfig.create_dxl_config_from_file(CONFIG_FILE)

# IP address of the endpoint for which to apply the policy
HOST_IP = "<SPECIFY_IP_ADDRESS>"

# Create the client
with DxlClient(config) as dxl_client:

    # Connect to the fabric
    dxl_client.connect()

    logger.info("Connected to DXL fabric.")

    # Create client wrapper
    client = CiscoPxGridClient(dxl_client)

    try:
        # Invoke 'apply endpoint policy by IP' method on service
        resp_dict = client.anc.apply_endpoint_policy_by_ip(HOST_IP,
                                                           "quarantine_policy")

        # Print out the response (convert dictionary to JSON for pretty
        # printing)
        print("Response:\n{0}".format(
            MessageUtils.dict_to_json(resp_dict, pretty_print=True)))
    except Exception as ex:
        # An exception should be raised if the 'quarantine_policy' has already
        # been applied to the endpoint, the 'quarantine_policy' has not been
        # created, or if no session has been established for the endpoint.
        print(str(ex))