# coding: utf-8

"""
Health Repository Provider Specifications for HIU

The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm.models.consent_manager_patient_id import ConsentManagerPatientID


class TestConsentManagerPatientID(unittest.TestCase):
    """ConsentManagerPatientID unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ConsentManagerPatientID:
        """Test ConsentManagerPatientID
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `ConsentManagerPatientID`
        """
        model = ConsentManagerPatientID()
        if include_optional:
            return ConsentManagerPatientID(
                id = 'hinapatel@ndhm'
            )
        else:
            return ConsentManagerPatientID(
                id = 'hinapatel@ndhm',
        )
        """

    def testConsentManagerPatientID(self):
        """Test ConsentManagerPatientID"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
