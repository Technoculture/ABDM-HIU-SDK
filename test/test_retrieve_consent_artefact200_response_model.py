# coding: utf-8

"""
    HIU API SDK

    Health Information User API for handling consent and health information requests.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm-hiu-sdk.abdm-hiu-sdk.model.retrieve_consent_artefact200_response_model import RetrieveConsentArtefact200ResponseModel

class TestRetrieveConsentArtefact200ResponseModel(unittest.TestCase):
    """RetrieveConsentArtefact200ResponseModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RetrieveConsentArtefact200ResponseModel:
        """Test RetrieveConsentArtefact200ResponseModel
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RetrieveConsentArtefact200ResponseModel`
        """
        model = RetrieveConsentArtefact200ResponseModel()
        if include_optional:
            return RetrieveConsentArtefact200ResponseModel(
                consent_artefact = abdm-hiu-sdk.models.retrieve_consent_200_response_consent.retrieveConsent_200_response_consent(
                    id = 56, )
            )
        else:
            return RetrieveConsentArtefact200ResponseModel(
        )
        """

    def testRetrieveConsentArtefact200ResponseModel(self):
        """Test RetrieveConsentArtefact200ResponseModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()