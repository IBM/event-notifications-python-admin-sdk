# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Examples for EventNotificationsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import os
import pytest
from ibm_eventnotifications.event_notifications_v1 import *

#
# This file provides an example of how to use the Event Notifications service.
#
# The following configuration properties are assumed to be defined:
# EVENT_NOTIFICATIONS_URL=<service base url>
# EVENT_NOTIFICATIONS_AUTH_TYPE=iam
# EVENT_NOTIFICATIONS_APIKEY=<IAM apikey>
# EVENT_NOTIFICATIONS_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = '../event_notifications_v1.env'

event_notifications_service = None

config = None

# EN config values
instance_id = ''
search = ''
topic_name = 'Admin Topic Compliance'
source_id = ''
topic_id = ''
destination_id = ''
destination_id1 = ''
destination_id2 = ''
destination_id3 = ''
destination_id4 = ''
destination_id5 = ''
destination_id6 = ''
destination_id7 = ''
destination_id8 = ''
destination_id9 = ''
destination_id10 = ''
safariCertificatePath = ''
subscription_id = ''
subscription_id1 = ''
subscription_id2 = ''
subscription_id3 = ''
fcmServerKey = ''
fcmSenderId = ''

##############################################################################
# Start of Examples for Service: EventNotificationsV1
##############################################################################
# region
class TestEventNotificationsV1Examples():
    """
    Example Test Class for EventNotificationsV1
    """

    @classmethod
    def setup_class(cls):
        global instance_id, fcmServerKey, fcmSenderId, safariCertificatePath
        global event_notifications_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            event_notifications_service = EventNotificationsV1.new_instance(
            )

            # end-common
            assert event_notifications_service is not None

            # Load the configuration
            global config
            config = read_external_sources(EventNotificationsV1.DEFAULT_SERVICE_NAME)

            instance_id = config['GUID']
            fcmServerKey = config['FCM_KEY']
            fcmSenderId = config['FCM_ID']
            safariCertificatePath = config['SAFARI_CERTIFICATE']
            assert instance_id is not None
            assert fcmServerKey is not None
            assert fcmSenderId is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_sources_example(self):
        """
        create_sources request example
        """
        global source_id
        try:
            print('\ncreate_sources() result:')
            # begin-create_sources

            source_response = event_notifications_service.create_sources(
                instance_id,
                name='Event Notification Create Source Acme',
                description='This source is used for Acme Bank',
                enabled=False
            ).get_result()

            print(json.dumps(source_response, indent=2))

            # end-create_sources

            source = SourceResponse.from_dict(source_response)
            source_id = source.id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_sources_example(self):
        """
        list_sources request example
        """
        try:
            print('\nlist_sources() result:')
            # begin-list_sources

            source_list = event_notifications_service.list_sources(
                instance_id
            ).get_result()

            print(json.dumps(source_list, indent=2))

            # end-list_sources

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_source_example(self):
        """
        get_source request example
        """
        try:
            print('\nget_source() result:')
            # begin-get_source

            source = event_notifications_service.get_source(
                instance_id,
                id=source_id
            ).get_result()

            print(json.dumps(source, indent=2))

            # end-get_source

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_source_example(self):
        """
        update_source request example
        """
        try:
            print('\nupdate_source() result:')
            # begin-update_source

            source = event_notifications_service.update_source(
                instance_id,
                id=source_id,
                name='Event Notification update Source Acme',
                description='This source is used for updated Acme Bank',
                enabled=True
            ).get_result()

            print(json.dumps(source, indent=2))

            # end-update_source

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_topic_example(self):
        """
        create_topic request example
        """
        global topic_id
        try:
            print('\ncreate_topic() result:')
            # begin-create_topic

            rules_model = {
                'enabled': False,
                'event_type_filter': '$.notification_event_info.event_type == \'cert_manager\'',
                'notification_filter': '$.notification.findings[0].severity == \'MODERATE\'',
            }

            # Construct a dict representation of a TopicUpdateSourcesItem model
            topic_update_sources_item_model = {
                'id': source_id,
                'rules': [rules_model],
            }

            topic = event_notifications_service.create_topic(
                instance_id,
                name=topic_name,
                description='This topic is used for routing all compliance related notifications to the appropriate destinations',
                sources=[topic_update_sources_item_model]
            ).get_result()

            print(json.dumps(topic, indent=2))

            # end-create_topic

            topic = TopicResponse.from_dict(topic)
            topic_id = topic.id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_topics_example(self):
        """
        list_topics request example
        """
        try:
            print('\nlist_topics() result:')
            # begin-list_topics

            topic_list = event_notifications_service.list_topics(
                instance_id
            ).get_result()

            print(json.dumps(topic_list, indent=2))

            # end-list_topics

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_topic_example(self):
        """
        get_topic request example
        """
        try:
            print('\nget_topic() result:')
            # begin-get_topic

            topic = event_notifications_service.get_topic(
                instance_id,
                id=topic_id
            ).get_result()

            print(json.dumps(topic, indent=2))

            # end-get_topic

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_topic_example(self):
        """
        replace_topic request example
        """
        try:
            print('\nreplace_topic() result:')
            # begin-replace_topic

            rules_model = {
                'enabled': True,
                'event_type_filter': '$.notification_event_info.event_type == \'core_cert_manager\'',
                'notification_filter': '$.notification.findings[0].severity == \'SEVERE\'',
            }

            # Construct a dict representation of a TopicUpdateSourcesItem model
            topic_update_sources_item_model = {
                'id': source_id,
                'rules': [rules_model],
            }

            description = 'Updated Topic for GCM notifications'
            name = 'Updated Admin Topic Compliance'
            topic = event_notifications_service.replace_topic(
                instance_id,
                id=topic_id,
                name=name,
                description=description,
                sources=[topic_update_sources_item_model]
            ).get_result()

            print(json.dumps(topic, indent=2))

            # end-replace_topic

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_destination_example(self):
        """
        create_destination request example
        """
        global destination_id, destination_id3, destination_id4, destination_id5, destination_id6, destination_id7, destination_id8, destination_id9, destination_id10
        try:
            print('\ncreate_destination() result:')
            # begin-create_destination

            destination_config_params_model = {
                "server_key": fcmServerKey,
                "sender_id": fcmSenderId,
                "pre_prod": False
            }

            destination_config_model = {
                'params': destination_config_params_model,
            }
            name = "FCM_destination"
            typeVal = "push_android"
            description = "FCM Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeVal,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))

            destination = DestinationResponse.from_dict(destination)
            destination_id = destination.id

            # Webhook
            destination_config_params_model = {
                'url': 'https://gcm.com',
                'verb': 'get',
                'custom_headers': {'gcm_apikey': 'apikey'},
                'sensitive_headers': ['gcm_apikey'],
            }

            # Construct a dict representation of a DestinationConfig model
            destination_config_model = {
                'params': destination_config_params_model,
            }

            name = "Webhook_destination"
            typeval = "webhook"
            description = "Webhook Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))

            destination = DestinationResponse.from_dict(destination)
            destination_id3 = destination.id

            # slack
            slack_config_params = {
                'url': 'https://api.slack.com/myslack',
            }

            destination_config_model = {
                'params': slack_config_params,
            }

            name = "Slack_destination"
            typeval = "slack"
            description = "Slack Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model
            ).get_result()
            print(json.dumps(destination, indent=2))

            destination = DestinationResponse.from_dict(destination)
            destination_id4 = destination.id

            # Safari
            safari_config_params = {
                'cert_type': 'p12',
                'password': 'safari',
                'website_url': 'https://ensafaripush.mybluemix.net',
                'website_name': 'NodeJS Starter Application',
                'url_format_string': 'https://ensafaripush.mybluemix.net/%@/?flight=%@',
                'website_push_id': 'web.net.mybluemix.ensafaripush',
                "pre_prod": False
            }

            destination_config_model = {
                'params': safari_config_params,
            }

            name = "Safari_destination"
            typeVal = "push_safari"
            description = "Safari Destination"

            certificatefile = open(safariCertificatePath, 'rb')
            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeVal,
                description=description,
                config=destination_config_model,
                certificate=certificatefile,
            ).get_result()
            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id5 = destination.id

            # MSTeams
            msteams_config_params = {
                'url': 'https://teams.microsoft.com',
            }

            destination_config_model = {
                'params': msteams_config_params,
            }

            name = "MSTeams_destination"
            typeval = "msteams"
            description = "MSteams Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model
            ).get_result()
            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id6 = destination.id

            # cloud functions
            cf_config_params = {
                "url": "https://www.ibmcfendpoint.com/",
                "api_key": "wewelkndliejoiewe898"
            }

            destination_config_model = {
                'params': cf_config_params,
            }
            name = "Cloud_Functions_destination"
            typeVal = "ibmcf"
            description = "This is a Cloud Functions Destination for actions"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeVal,
                description=description,
                config=destination_config_model
            ).get_result()
            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id7 = destination.id

            # chrome
            chrome_config_params = {
                "website_url": "https://www.ibmcfendpoint.com/",
                "api_key": "wedleknlwenwern9832jhde",
                "public_key": "",
                "pre_prod": False
            }

            destination_config_model = {
                'params': chrome_config_params,
            }
            name = "Chrome_destination"
            typeval = "push_chrome"
            description = "This is a Chrome Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model
            ).get_result()
            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id8 = destination.id

            # Firefox
            fire_config_params = {
                "website_url": "https://cloud.ibm.com",
                "public_key": "ksddkasjdaksd",
                "pre_prod": False
            }

            destination_config_model = {
                'params': fire_config_params,
            }
            name = "Firefox_destination"
            typeval = "push_firefox"
            description = "This is a Firefox Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id9 = destination.id

            pd_config_params = {
                "api_key": "akdnaklsdawioeqowi",
                "routing_key": "ksddkasjdakssdsd"
            }

            destination_config_model = {
                'params': pd_config_params,
            }
            name = "Pager_Duty_destination"
            typeval = "pagerduty"
            description = "This is a PagerDuty Destination"

            destination = event_notifications_service.event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model
            ).get_result()

            destination = DestinationResponse.from_dict(destination)

            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id10 = destination.id
            # end-create_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_destinations_example(self):
        """
        list_destinations request example
        """
        global destination_id1, destination_id2
        more_results = True
        limit = 1
        offset = 0
        try:
            print('\nlist_destinations() result:')
            # begin-list_destinations

            destination_list = event_notifications_service.list_destinations(
                instance_id
            ).get_result()

            # end-list_destinations
            print(json.dumps(destination_list, indent=2))

            destinations = DestinationList.from_dict(destination_list)
            assert destinations is not None

            for i in range(0, len(destinations.destinations)):
                destination = destinations.destinations[i]
                if destination.id != destination_id and destination.type == 'smtp_ibm':
                    destination_id2 = destination.id
                    if destination_id1 != '':
                        break
                if destination.type == 'sms_ibm':
                    destination_id1 = destination.id
                    if destination_id2 != '':
                        break
            if destinations.total_count <= offset:
                more_results = False
            offset += 1
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_destination_example(self):
        """
        get_destination request example
        """
        try:
            print('\nget_destination() result:')
            # begin-get_destination

            destination = event_notifications_service.get_destination(
                instance_id,
                id=destination_id
            ).get_result()

            print(json.dumps(destination, indent=2))

            # end-get_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_destination_example(self):
        """
        update_destination request example
        """
        try:
            print('\nupdate_destination() result:')
            # begin-update_destination

            # FCM
            destination_config_params_model = {
                "server_key": fcmServerKey,
                "sender_id": fcmSenderId
            }

            destination_config_model = {
                'params': destination_config_params_model,
            }
            name = "Admin FCM Compliance"
            description = "This destination is for creating admin FCM to receive compliance notifications"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id,
                name=name,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))

            # webhook
            destination_config_params_model = {
                'url': 'https://cloud.ibm.com/nhwebhook/sendwebhook',
                'verb': 'post',
                'custom_headers': {'authorization': 'authorization token'},
                'sensitive_headers': ['authorization'],
            }

            # Construct a dict representation of a DestinationConfig model
            destination_config_model = {
                'params': destination_config_params_model,
            }

            name = "Admin GCM Compliance"
            description = "This destination is for creating admin GCM webhook to receive compliance notifications"
            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id3,
                name=name,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))

            # Slack
            slack_config_params = {
                'url': 'https://api.slack.com/myslack',
            }

            destination_config_model = {
                'params': slack_config_params,
            }

            name = "Slack_destination_update"
            description = "Slack Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id4,
                name=name,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))

            # Safari
            safari_destination_config_params_model = {
                'cert_type': 'p12',
                'password': 'safari',
                'website_url': 'https://ensafaripush.mybluemix.net',
                'website_name': 'NodeJS Starter Application',
                'url_format_string': 'https://ensafaripush.mybluemix.net/%@/?flight=%@',
                'website_push_id': 'web.net.mybluemix.ensafaripush',
            }

            # Construct a dict representation of a DestinationConfig model
            safari_destination_config_model = {
                'params': safari_destination_config_params_model,
            }

            certificatefile = open(safariCertificatePath, 'rb')
            name = "Safari Dest"
            description = "This destination is for Safari"
            update_destination_response = event_notifications_service.update_destination(
                instance_id,
                id=destination_id5,
                name=name,
                description=description,
                config=safari_destination_config_model,
                certificate=certificatefile
            ).get_result()

            print(json.dumps(update_destination_response, indent=2))

            # MSTeams
            msteams_config_params = {
                'url': 'https://teams.microsoft.com',
            }

            destination_config_model = {
                'params': msteams_config_params,
            }

            name = "MSTeams_destination_update"
            description = "MSteams Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id6,
                name=name,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))

            # Cloud Functions
            destination_config_params_model = {
                "url": "https://www.ibmcfendpoint.com/",
                "api_key": "wqowieqwoieqsfsdfs899eoqwieu"
            }

            destination_config_model = {
                'params': destination_config_params_model,
            }
            name = "Cloud_Functions_dest"
            description = "This is a Cloud Functions Destination"

            update_destination_response = event_notifications_service.update_destination(
                instance_id,
                id=destination_id7,
                name=name,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(update_destination_response, indent=2))

            # Chrome
            chrome_config_params = {
                "website_url": "https://www.ibmcfendpoint.com/",
                "api_key": "wedleknlwenwern9832jhde",
                "public_key": "",
                "pre_prod": False
            }

            destination_config_model = {
                'params': chrome_config_params,
            }
            name = "Chrome_destination_update"
            description = "This is a Chrome Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id8,
                name=name,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))

            # Firefox
            fire_config_params = {
                "website_url": "https://cloud.ibm.com",
                "public_key": "ksddkasjdaksd",
                "pre_prod": False
            }

            destination_config_model = {
                'params': fire_config_params,
            }
            name = "Firefox_destination_update"
            description = "This is a Firefox Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id9,
                name=name,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))

            pd_config_params = {
                "api_key": "sdskndlsndflsklskdf",
                "routing_key": "ksddkasjdaksdsdsd"
            }

            destination_config_model = {
                'params': pd_config_params,
            }
            name = "PagerDuty_destination_update"
            description = "This is a PagerDuty Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id10,
                name=name,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))
            # end-update_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_subscription_example(self):
        """
        create_subscription request example
        """
        global subscription_id, subscription_id1, subscription_id2, subscription_id3
        try:
            print('\ncreate_subscription() result:')
            # begin-create_subscription

            # FCM
            name = 'FCM subscription'
            description = 'Subscription for the FCM'
            subscription = event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id,
                topic_id,
                description=description
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id = subscription.get('id')

            subscription_create_attributes_model = {
                'invited': ["+12064512559", "+12064512559"],
            }

            name = 'subscription_sms'
            description = 'Subscription for sms'
            subscription = event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id=destination_id1,
                topic_id=topic_id,
                attributes=subscription_create_attributes_model,
                description=description
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id1 = subscription.get('id')

            # Email
            subscription_create_attributes_model = {
                'invited': ["tester1@gmail.com", "tester3@ibm.com"],
                'add_notification_payload': True,
                "reply_to_mail": "reply_to_mail@us.com",
                "reply_to_name": "US News",
                "from_name": "IBM"
            }

            name = 'subscription_email'
            description = 'Subscription for email'
            subscription = event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id=destination_id2,
                topic_id=topic_id,
                attributes=subscription_create_attributes_model,
                description=description
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id2 = subscription.get('id')

            # webhook
            subscription_create_attributes_model = {
                'signing_enabled': False,
            }

            name = 'subscription_web'
            description = 'Subscription for web'
            subscription = event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id3,
                topic_id,
                attributes=subscription_create_attributes_model,
                description=description
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id3 = subscription.get('id')

        except ApiException as e:
            pytest.fail(str(e))

        # end-create_subscription

    @needscredentials
    def test_list_subscriptions_example(self):
        """
        list_subscriptions request example
        """
        try:
            print('\nlist_subscriptions() result:')
            # begin-list_subscriptions

            subscription_list = event_notifications_service.list_subscriptions(
                instance_id
            ).get_result()

            print(json.dumps(subscription_list, indent=2))

            # end-list_subscriptions

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_subscription_example(self):
        """
        get_subscription request example
        """
        try:
            print('\nget_subscription() result:')
            # begin-get_subscription

            subscription = event_notifications_service.get_subscription(
                instance_id,
                id=subscription_id
            ).get_result()

            print(json.dumps(subscription, indent=2))

            # end-get_subscription

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_subscription_example(self):
        """
        update_subscription request example
        """
        try:
            print('\nupdate_subscription() result:')
            # begin-update_subscription

            # FCM
            name = 'Update_FCM_subscription'
            description = 'Update FCM subscription'
            subscription = event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id,
                name=name,
                description=description,
            ).get_result()

            print(json.dumps(subscription, indent=2))

            # SMS
            sms_update_attributes_invite_model = {'add': ['+12064512559']}

            sms_update_attributes_toremove_model = {'remove': ['+12064512559']}

            subscription_update_attributes_model = {
                'invited': sms_update_attributes_invite_model,
                "subscribed": sms_update_attributes_toremove_model,
                "unsubscribed": sms_update_attributes_toremove_model
            }

            name = 'subscription_sms update'
            description = 'Subscription for sms updated'
            subscription = self.event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id1,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model,
            ).get_result()
            print(json.dumps(subscription, indent=2))

            # Email
            email_update_attributes_invite_model = {'add': ['tester4@ibm.com']}

            email_update_attributes_toremove_model = {'remove': ['tester3@ibm.com']}

            subscription_update_attributes_model = {
                'invited': email_update_attributes_invite_model,
                'add_notification_payload': True,
                "reply_to_mail": "reply_to_mail@us.com",
                "reply_to_name": "US News",
                "from_name": "IBM",
                "subscribed": email_update_attributes_toremove_model,
                "unsubscribed": email_update_attributes_toremove_model
            }

            name = 'subscription_email update'
            description = 'Subscription for email updated'
            update_subscription_response = event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id2,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model,
            )

            subscription_response = update_subscription_response.get_result()
            print(json.dumps(subscription_response, indent=2))

            # webhook
            subscription_update_attributes_model = {
                'signing_enabled': True,
            }

            name = 'Webhook_sub_updated'
            description = 'Update Webhook subscription'
            update_subscription_response = event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id3,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model
            )

            subscription_response = update_subscription_response.get_result()
            print(json.dumps(subscription_response, indent=2))
            # end-update_subscription
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_send_notifications_example(self):
        """
        send_notifications request example
        """
        try:
            print('\nsend_notifications() result:')

            notification_id = "1234-1234-sdfs-234"
            notification_severity = "MEDIUM"
            type_value = "com.acme.offer:new"
            date = '2019-01-01T12:00:00.000Z'
            notifications_source = "1234-1234-sdfs-234:test"
            
            # begin-send_notifications

            notification_devices_model = {
                'user_ids': ['userId'],
            }

            notification_apns_body_model = {
                "aps": {
                    "alert": "Game Request",
                    "badge": 5,
                },
            }
            notification_fcm_body_model = {
                "notification": {
                    "title": "Portugal vs. Denmark",
                    "body": "great match!",
                },
            }

            message_apns_headers = {
                "apns-collapse-id": "123",
            }

            notificationSafariBodymodel = {
                'saf': {
                    'alert': 'Game Request',
                    'badge': 5,
                },
            }

            notification_create_model = {
                'ibmenseverity': notification_severity,
                'ibmenfcmbody': json.dumps(notification_fcm_body_model),
                'ibmenpushto': json.dumps(notification_devices_model),
                'ibmenapnsbody': json.dumps(notification_apns_body_model),
                'ibmensourceid': source_id,
                'ibmendefaultshort': 'teststring',
                'ibmendefaultlong': 'teststring',
                'ibmensafaribody': json.dumps(notificationSafariBodymodel),
                'id': notification_id,
                'source': notifications_source,
                'type': type_value,
                'specversion': '1.0',
                'time': '2019-01-01T12:00:00.000Z',
            }

            send_notifications_response = event_notifications_service.send_notifications(
                instance_id,
                body=notification_create_model
            ).get_result()

            print(json.dumps(send_notifications_response, indent=2))

            # end-send_notifications

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_subscription_example(self):
        """
        delete_subscription request example
        """
        try:
            # begin-delete_subscription

            response = event_notifications_service.delete_subscription(
                instance_id,
                id=subscription_id
            )
            # end-delete_subscription
            print('\ndelete_subscription() response status code: ', response.get_status_code())

            for id in [subscription_id1, subscription_id2, subscription_id3]:
                delete_subscription_response = event_notifications_service.delete_subscription(
                    instance_id,
                    id
                )
            print('\ndelete_subscription() response status code: ', delete_subscription_response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_topic_example(self):
        """
        delete_topic request example
        """
        try:
            # begin-delete_topic

            response = event_notifications_service.delete_topic(
                instance_id,
                id=topic_id
            )

            # end-delete_topic
            print('\ndelete_topic() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_destination_example(self):
        """
        delete_destination request example
        """
        try:
            # begin-delete_destination

            response = event_notifications_service.delete_destination(
                instance_id,
                id=destination_id
            )

            # end-delete_destination
            print('\ndelete_destination() response status code: ', response.get_status_code())

            for id in [destination_id3, destination_id4, destination_id5, destination_id6, destination_id7, destination_id8, destination_id9, destination_id10]:
                delete_destination_response = event_notifications_service.delete_destination(
                    instance_id,
                    id
                )
            print('\ndelete_destination() response status code: ', delete_destination_response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_source_example(self):
        """
        delete_source request example
        """
        try:
            # begin-delete_source

            response = event_notifications_service.delete_source(
                instance_id,
                id=source_id
            )

            # end-delete_source
            print('\ndelete_source() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: EventNotificationsV1
##############################################################################
