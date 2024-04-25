# coding: utf-8

"""
    Health Repository Provider Specifications for HIU

    The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm.models.patient_auth_init_response import PatientAuthInitResponse

class TestPatientAuthInitResponse(unittest.TestCase):
    """PatientAuthInitResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatientAuthInitResponse:
        """Test PatientAuthInitResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatientAuthInitResponse`
        """
        model = PatientAuthInitResponse()
        if include_optional:
            return PatientAuthInitResponse(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                auth = abdm.models.patient_auth_init_response_auth.PatientAuthInitResponse_auth(
                    transaction_id = '', 
                    mode = 'MOBILE_OTP', 
                    meta = abdm.models.auth_meta.AuthMeta(
                        hint = '', 
                        expiry = '2019-12-30T12:01:55Z', ), ),
                error = abdm.models.error.Error(
                    code = 1000, 
                    message = '', ),
                resp = abdm.models.request_reference.RequestReference(
                    request_id = '', )
            )
        else:
            return PatientAuthInitResponse(
                request_id = '5f7a535d-a3fd-416b-b069-c97d021fbacd',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                resp = abdm.models.request_reference.RequestReference(
                    request_id = '', ),
        )
        """

    def testPatientAuthInitResponse(self):
        """Test PatientAuthInitResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
