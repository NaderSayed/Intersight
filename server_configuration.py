import client
from intersight.api import server_api
from intersight.model.ntp_policy import NtpPolicy
from intersight.api import ntp_api
from intersight.model.organization_organization_relationship import OrganizationOrganizationRelationship
from intersight.exceptions import NotFoundException
from pprint import pprint
import intersight
import sys
import urllib3


api_key = "api_key"
api_key_file = "/api_key_file_path"


api_client = client.get_api_client(api_key, api_key_file)

def create_organization(moid):
    return OrganizationOrganizationRelationship(class_id="mo.MoRef",
                                            object_type="organization.Organization",
                                            moid = moid)
                                                


def create_ntp_policy():
    api_instance = ntp_api.NtpApi(api_client)

    #disable InsecureRequestWarning
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    # Create an instance of organization.
    organization = create_organization("64c435056972652d305afefe")

    # NtpPolicy | The 'ntp.Policy' resource to create.
    ntp_policy = NtpPolicy()

    # Setting all the attributes for ntp_policy instance.
    ntp_policy.name = "sample_ntp_policy1"
    ntp_policy.description = "sample ntp policy."
    ntp_policy.organization = organization
    ntp_servers = [
        "10.10.10.250", "10.10.10.10", "10.10.10.20", "10.10.10.30"
    ]
    ntp_policy.ntp_servers = ntp_servers

    # example passing only required values which don't have defaults set
    try:
        # Create a 'ntp.Policy' resource.
        resp_ntp_policy = api_instance.create_ntp_policy(ntp_policy)
        pprint(resp_ntp_policy)
        return resp_ntp_policy
    except intersight.ApiException as e:
        print("Exception when calling NtpApi->create_ntp_policy: %s\n" % e)
        sys.exit(1)


# Creating NTP policy
ntp_policy_response = create_ntp_policy()

