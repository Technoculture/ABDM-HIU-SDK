# coding: utf-8

"""
Health Repository Provider Specifications for HIU

The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent

The version of the OpenAPI document: 0.5
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

import unittest

from abdm.models.subscription_approval_notification_notification import (
    SubscriptionApprovalNotificationNotification,
)


class TestSubscriptionApprovalNotificationNotification(unittest.TestCase):
    """SubscriptionApprovalNotificationNotification unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> SubscriptionApprovalNotificationNotification:
        """Test SubscriptionApprovalNotificationNotification
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `SubscriptionApprovalNotificationNotification`
        """
        model = SubscriptionApprovalNotificationNotification()
        if include_optional:
            return SubscriptionApprovalNotificationNotification(
                subscription_request_id = 'request id of the subscription',
                status = 'GRANTED',
                subscription = abdm.models.hiu_subscription.HIUSubscription(
                    id = 'subscription Id', 
                    patient = abdm.models.consent_manager_patient_id.ConsentManagerPatientID(
                        id = 'hinapatel@ndhm', ), 
                    hiu = abdm.models.organization_representation.OrganizationRepresentation(
                        id = '', ), 
                    sources = [
                        abdm.models.hiu_subscription_context.HIUSubscriptionContext(
                            hip = abdm.models.organization_representation.OrganizationRepresentation(
                                id = '', ), 
                            categories = [
                                'LINK'
                                ], 
                            period = abdm.models.subscription_period.SubscriptionPeriod(
                                from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), )
                        ], )
            )
        else:
            return SubscriptionApprovalNotificationNotification(
                status = 'GRANTED',
        )
        """

    def testSubscriptionApprovalNotificationNotification(self):
        """Test SubscriptionApprovalNotificationNotification"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
