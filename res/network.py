import boto3
import botocore
import json
import config
import res.utils as utils
import res.glob  as glob

# =======================================================================================================================
#
#  Supported services   : API Gateway (simple), VPC (in 'compute' module)
#  Unsupported services : Route 53, Cloud Front, Direct Connect
#
# =======================================================================================================================


#  ------------------------------------------------------------------------
#
#    API Gateway (simple) 
#
#  ------------------------------------------------------------------------

def get_apigateway_inventory(oId):
    """
        Returns API Gateway inventory

        :param ownerId: ownerId (AWS account)
        :type ownerId: string
        :param region_name: region name
        :type region_name: string

        :return: API Gateway inventory
        :rtype: json

        ..note:: http://boto3.readthedocs.io/en/latest/reference/services/apigateway.html
        ..todo:: add --> plans, api keys, custom domain names, client certificates, vpc links
    """
    return glob.get_inventory(
        ownerId = oId,
        aws_service = "apigateway", 
        aws_region = "all", 
        function_name = "get_rest_apis", 
        key_get = "items",
        detail_function = "", 
        key_get_detail = "",
        key_selector = ""
    )

    '''apigateway_inventory = []
    
    for region in config.regions:

        region_name = region['RegionName']
        utils.display(ownerId, region_name, "apigateway inventory")

        client = boto3.client('apigateway', region_name)

        for apigateway in client.get_rest_apis().get('items'):
            apigateway_inventory.append(json.loads(utils.json_datetime_converter(apigateway)))

    config.logger.info('API Gateway inventory, region {}, get_api_inventory'.format(region_name))

    return apigateway_inventory'''


#
# Hey, doc: we're in a module!
#
if (__name__ == '__main__'):
    print('Module => Do not execute')