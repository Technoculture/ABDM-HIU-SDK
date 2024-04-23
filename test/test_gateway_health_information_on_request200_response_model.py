# coding: utf-8

"""
    HIU API SDK

    Health Information User API for handling consent and health information requests.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm-hiu-sdk.abdm-hiu-sdk.model.gateway_health_information_on_request200_response_model import GatewayHealthInformationOnRequest200ResponseModel

class TestGatewayHealthInformationOnRequest200ResponseModel(unittest.TestCase):
    """GatewayHealthInformationOnRequest200ResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GatewayHealthInformationOnRequest200ResponseModel:
        """Test GatewayHealthInformationOnRequest200ResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GatewayHealthInformationOnRequest200ResponseModel`
        """
        model = GatewayHealthInformationOnRequest200ResponseModel()
        if include_optional:
            return GatewayHealthInformationOnRequest200ResponseModel(
                message = 'Gateway health information request'
            )
        else:
            return GatewayHealthInformationOnRequest200ResponseModel(
        )
        """

    def testGatewayHealthInformationOnRequest200ResponseModel(self):
        """Test GatewayHealthInformationOnRequest200ResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()