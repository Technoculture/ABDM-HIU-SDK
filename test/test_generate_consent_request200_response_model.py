# coding: utf-8

"""
    HIU API SDK

    Health Information User API for handling consent and health information requests.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm-hiu-sdk.abdm-hiu-sdk.model.generate_consent_request200_response_model import GenerateConsentRequest200ResponseModel

class TestGenerateConsentRequest200ResponseModel(unittest.TestCase):
    """GenerateConsentRequest200ResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GenerateConsentRequest200ResponseModel:
        """Test GenerateConsentRequest200ResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GenerateConsentRequest200ResponseModel`
        """
        model = GenerateConsentRequest200ResponseModel()
        if include_optional:
            return GenerateConsentRequest200ResponseModel(
                message = 'Consent request generated'
            )
        else:
            return GenerateConsentRequest200ResponseModel(
        )
        """

    def testGenerateConsentRequest200ResponseModel(self):
        """Test GenerateConsentRequest200ResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()