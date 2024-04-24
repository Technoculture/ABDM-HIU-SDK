# coding: utf-8

"""
    Health Repository Provider Specifications for HIU

    The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  

    The version of the OpenAPI document: 0.5
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from abdm.api.gateway_api import GatewayAPI


class TestGatewayAPI(unittest.TestCase):
    """GatewayAPI unit test stubs"""

    def setUp(self) -> None:
        self.api = GatewayAPI()

    def tearDown(self) -> None:
        pass

    def test_v05_certs_get(self) -> None:
        """Test case for v05_certs_get

        Get certs for JWT verification
        """
        pass

    def test_v05_consent_requests_init_post(self) -> None:
        """Test case for v05_consent_requests_init_post

        Create consent request
        """
        pass

    def test_v05_consent_requests_status_post(self) -> None:
        """Test case for v05_consent_requests_status_post

        Get consent request status
        """
        pass

    def test_v05_consents_fetch_post(self) -> None:
        """Test case for v05_consents_fetch_post

        Get consent artefact
        """
        pass

    def test_v05_consents_hiu_on_notify_post(self) -> None:
        """Test case for v05_consents_hiu_on_notify_post

        Consent notification
        """
        pass

    def test_v05_health_information_cm_request_post(self) -> None:
        """Test case for v05_health_information_cm_request_post

        Health information data request
        """
        pass

    def test_v05_health_information_notify_post(self) -> None:
        """Test case for v05_health_information_notify_post

        Notifications corresponding to events during data flow
        """
        pass

    def test_v05_patients_find_post(self) -> None:
        """Test case for v05_patients_find_post

        Identify a patient by her consent-manager user-id
        """
        pass

    def test_v05_patients_status_on_notify_post(self) -> None:
        """Test case for v05_patients_status_on_notify_post

        Acknowledgment by HIU
        """
        pass

    def test_v05_sessions_post(self) -> None:
        """Test case for v05_sessions_post

        Get access token
        """
        pass

    def test_v05_subscription_requests_cm_init_post(self) -> None:
        """Test case for v05_subscription_requests_cm_init_post

        Request for subscription
        """
        pass

    def test_v05_subscription_requests_hiu_on_notify_post(self) -> None:
        """Test case for v05_subscription_requests_hiu_on_notify_post

        Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.
        """
        pass

    def test_v05_subscriptions_hiu_on_notify_post(self) -> None:
        """Test case for v05_subscriptions_hiu_on_notify_post

        Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.
        """
        pass

    def test_v05_users_auth_confirm_post(self) -> None:
        """Test case for v05_users_auth_confirm_post

        Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation
        """
        pass

    def test_v05_users_auth_fetch_modes_post(self) -> None:
        """Test case for v05_users_auth_fetch_modes_post

        Get a patient's authentication modes relevant to specified purpose
        """
        pass

    def test_v05_users_auth_init_post(self) -> None:
        """Test case for v05_users_auth_init_post

        Initialize authentication from HIP
        """
        pass

    def test_v05_users_auth_on_notify_post(self) -> None:
        """Test case for v05_users_auth_on_notify_post

        callback API by HIU/HIPs as acknowledgement of auth notification
        """
        pass

    def test_v05_well_known_openid_configuration_get(self) -> None:
        """Test case for v05_well_known_openid_configuration_get

        Get openid configuration
        """
        pass


if __name__ == '__main__':
    unittest.main()