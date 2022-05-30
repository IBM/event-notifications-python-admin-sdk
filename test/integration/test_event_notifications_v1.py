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
Integration Tests for EventNotificationsV1
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from ibm_eventnotifications.event_notifications_v1 import *

# Config file name
config_file = '../../event_notifications_v1.env'

# EN config values
instance_id = ''
search = ''
topic_name = 'GCMTopic'
source_id = ''
topic_id = ''
topic_id2 = ''
topic_id3 = ''
destination_id = ''
destination_id2 = ''
destination_id3 = ''
destination_id4 = ''
subscription_id = ''
subscription_id2 = ''
subscription_id3 = ''
fcmServerKey = ''
fcmSenderId = ''

class TestEventNotificationsV1():
    """
    Integration Test Class for EventNotificationsV1
    """

    @classmethod
    def setup_class(cls):
        global instance_id, fcmServerKey, fcmSenderId
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.event_notifications_service = EventNotificationsV1.new_instance(
            )
            assert cls.event_notifications_service is not None

            cls.config = read_external_sources(
                EventNotificationsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.event_notifications_service.enable_retries()

            instance_id = cls.config['GUID']
            fcmServerKey = cls.config['FCM_KEY']
            fcmSenderId = cls.config['FCM_ID']
            assert instance_id is not None
            assert fcmServerKey is not None
            assert fcmSenderId is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_create_sources(self):

        global source_id
        create_sources_response = self.event_notifications_service.create_sources(
            instance_id,
            name='Event Notification Create Source Acme',
            description='This source is used for Acme Bank',
            enabled=False
        )

        assert create_sources_response.get_status_code() == 201
        source_response = create_sources_response.get_result()
        assert source_response is not None

        source = SourceResponse.from_dict(source_response)
        source_id = source.id
        assert source_id is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 404
        # 409
        # 415
        # 500
        #

    @needscredentials
    def test_list_sources(self):

        more_results = True
        limit = 1
        offset = 0

        while more_results:
            list_sources_response = self.event_notifications_service.list_sources(
                instance_id,
                limit=limit,
                offset=offset,
                search=search
            )
            assert list_sources_response.get_status_code() == 200
            source_list = list_sources_response.get_result()
            assert source_list is not None

            if source_list.get('total_count') <= offset:
                more_results = False
            offset += 1

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 500
        #

    @needscredentials
    def test_get_source(self):

        get_source_response = self.event_notifications_service.get_source(
            instance_id,
            source_id
        )

        assert get_source_response.get_status_code() == 200
        source = get_source_response.get_result()
        assert source is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_update_source(self):

        update_source_response = self.event_notifications_service.update_source(
            instance_id,
            id=source_id,
            name='Event Notification update Source Acme',
            description='This source is used for updated Acme Bank',
            enabled=True
        )

        assert update_source_response.get_status_code() == 200
        source = update_source_response.get_result()
        assert source is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 404
        # 409
        # 415
        # 500
        #

    @needscredentials
    def test_create_topic(self):

        global topic_id, topic_id2, topic_id3
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

        description = "Topic for Webhook notifications"
        create_topic_response = self.event_notifications_service.create_topic(
            instance_id,
            name=topic_name,
            description=description,
            sources=[topic_update_sources_item_model]
        )

        assert create_topic_response.get_status_code() == 201
        topic_response = create_topic_response.get_result()
        assert topic_response is not None

        topic = TopicResponse.from_dict(topic_response)
        assert topic is not None

        assert topic.name == topic_name
        assert topic.description == description

        topic_id = topic.id

        description = "Topic 2 for Webhook notifications"
        name = "topic2"

        create_topic_response = self.event_notifications_service.create_topic(
            instance_id,
            name=name,
            description=description,
            sources=[topic_update_sources_item_model]
        )

        assert create_topic_response.get_status_code() == 201
        topic_response = create_topic_response.get_result()
        assert topic_response is not None

        topic = TopicResponse.from_dict(topic_response)
        assert topic is not None

        assert topic.name == name
        assert topic.description == description

        topic_id2 = topic.id

        description = "This topic is used for routing all compliance related notifications to the appropriate destinations"
        name = "FCM_topic"

        create_topic_response = self.event_notifications_service.create_topic(
            instance_id,
            name=name,
            description=description,
            sources=[topic_update_sources_item_model]
        )

        assert create_topic_response.get_status_code() == 201
        topic_response = create_topic_response.get_result()
        assert topic_response is not None

        topic = TopicResponse.from_dict(topic_response)
        assert topic is not None

        assert topic.name == name
        assert topic.description == description

        topic_id3 = topic.id

        assert topic_id2 is not ''
        assert topic_id is not ''
        assert topic_id3 is not ''

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 404
        # 409
        # 415
        # 500
        #

    @needscredentials
    def test_list_topics(self):

        more_results = True
        limit = 1
        offset = 0

        while more_results:
            list_topics_response = self.event_notifications_service.list_topics(
                instance_id,
                limit=limit,
                offset=offset,
                search=search
            )

            assert list_topics_response.get_status_code() == 200
            topic_list = list_topics_response.get_result()
            assert topic_list is not None

            if topic_list.get('total_count') <= offset:
                more_results = False
            offset += 1

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 500
        #

    @needscredentials
    def test_get_topic(self):

        get_topic_response = self.event_notifications_service.get_topic(
            instance_id,
            id=topic_id,
            include=search
        )

        assert get_topic_response.get_status_code() == 200
        topic = get_topic_response.get_result()
        assert topic is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_replace_topic(self):

        # Construct a dict representation of a Rules model
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

        description = "Updated Topic for GCM notifications"
        name = topic_name + "2"
        replace_topic_response = self.event_notifications_service.replace_topic(
            instance_id,
            id=topic_id,
            name=name,
            description=description,
            sources=[topic_update_sources_item_model]
        )

        assert replace_topic_response.get_status_code() == 200
        topic = replace_topic_response.get_result()
        assert topic is not None

        topic = Topic.from_dict(topic)
        assert topic is not None

        assert topic.name == name
        assert topic.description == description
        assert topic_id == topic.id

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 404
        # 409
        # 415
        # 500
        #

    @needscredentials
    def test_create_destination(self):

        # Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
        global destination_id, destination_id3, destination_id4
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
        typeVal = "webhook"
        description = "Webhook Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeVal,
            description=description,
            config=destination_config_model
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeVal

        destination_id = destination.id

        fcm_config_params = {
            "server_key": fcmServerKey,
            "sender_id" : fcmSenderId
        }

        destination_config_model = {
            'params': fcm_config_params,
        }
        name = "FCM_destination"
        typeVal = "push_android"
        description = "FCM Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeVal,
            description=description,
            config=destination_config_model
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeVal

        destination_id3 = destination.id

        slack_config_params = {
            'url': 'https://api.slack.com/myslack',
        }

        destination_config_model = {
            'params': slack_config_params,
        }

        name = "Slack_destination"
        typeVal = "slack"
        description = "Slack Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeVal,
            description=description,
            config=destination_config_model
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeVal

        destination_id4 = destination.id
        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 409
        # 415
        # 500
        #

    @needscredentials
    def test_list_destinations(self):

        global destination_id2
        more_results = True
        limit = 1
        offset = 0

        while more_results:
            list_destinations_response = self.event_notifications_service.list_destinations(
                instance_id,
                limit=limit,
                offset=offset,
                search=search
            )

            assert list_destinations_response.get_status_code() == 200
            destination_list = list_destinations_response.get_result()
            assert destination_list is not None

            destinations = DestinationList.from_dict(destination_list)
            assert destinations is not None

            for i in range(0, len(destinations.destinations)):
                destination = destinations.destinations[i]
                if destination.id != destination_id and destination.type == 'smtp_ibm':
                    destination_id2 = destination.id
            if destinations.total_count <= offset:
                more_results = False
            offset += 1

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 500
        #

    @needscredentials
    def test_get_destination(self):

        get_destination_response = self.event_notifications_service.get_destination(
            instance_id,
            id=destination_id
        )

        assert get_destination_response.get_status_code() == 200
        destination = get_destination_response.get_result()
        assert destination is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_update_destination(self):

        # Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
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
        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id,
            name=name,
            description=description,
            config=destination_config_model
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get('id')
        res_name = destination_response.get('name')
        res_description = destination_response.get('description')

        assert res_id == destination_id
        assert res_name == name
        assert res_description == description

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 404
        # 409
        # 415
        # 500
        #

    @needscredentials
    def test_list_destination_devices(self):

        list_destination_devices_response = self.event_notifications_service.list_destination_devices(
            instance_id,
            id=destination_id3,
            limit=1,
            offset=0,
            search=''
        )

        assert list_destination_devices_response.get_status_code() == 200
        destination_devices_list = list_destination_devices_response.get_result()
        assert destination_devices_list is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_get_destination_devices_report(self):

        get_destination_devices_report_response = self.event_notifications_service.get_destination_devices_report(
            instance_id,
            id=destination_id3,
            days=1
        )

        assert get_destination_devices_report_response.get_status_code() == 200
        destination_devices_report = get_destination_devices_report_response.get_result()
        assert destination_devices_report is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_create_subscription(self):

        # Construct a dict representation of a SubscriptionCreateAttributesSMSAttributes model
        global subscription_id, subscription_id2, subscription_id3
        subscription_create_attributes_model = {
            'signing_enabled': False,
        }

        name = 'subscription_web'
        description = 'Subscription for web'
        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id,
            topic_id,
            attributes=subscription_create_attributes_model,
            description=description
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get('name')
        subscription_description = subscription_response.get('description')
        subscription_id = subscription_response.get('id')
        assert subscription_name == name
        assert subscription_description == description

        subscription_create_attributes_model = {
            'to': ["tester1@gmail.com", "tester3@ibm.com"],
            'add_notification_payload': True,
            "reply_to_mail": "reply_to_mail@us.com",
            "reply_to_name": "US News",
            "from_name": "IBM"
        }

        name = 'subscription_email'
        description = 'Subscription for email'
        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id2,
            topic_id=topic_id,
            attributes=subscription_create_attributes_model,
            description=description
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get('name')
        subscription_description = subscription_response.get('description')
        subscription_id2 = subscription_response.get('id')

        assert subscription_name == name
        assert subscription_description == description

        # SMS

        name = "FCM subscription"
        description = "Subscription for the FCM"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id3,
            topic_id=topic_id3,
            description=description
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get('name')
        subscription_description = subscription_response.get('description')
        subscription_id3 = subscription_response.get('id')

        assert subscription_name == name
        assert subscription_description == description

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 404
        # 409
        # 415
        # 500
        #

    @needscredentials
    def test_list_subscriptions(self):

        more_results = True
        limit = 1
        offset = 0

        while more_results:
            list_subscriptions_response = self.event_notifications_service.list_subscriptions(
                instance_id,
                offset=offset,
                limit=limit,
                search=search
            )

            assert list_subscriptions_response.get_status_code() == 200
            subscription_list = list_subscriptions_response.get_result()
            assert subscription_list is not None
            subscription = SubscriptionList.from_dict(subscription_list)
            assert subscription is not None
            if subscription.total_count <= offset:
                more_results = False
            offset += 1

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 500
        #

    @needscredentials
    def test_get_subscription(self):

        get_subscription_response = self.event_notifications_service.get_subscription(
            instance_id,
            id=subscription_id
        )

        assert get_subscription_response.get_status_code() == 200
        subscription = get_subscription_response.get_result()
        assert subscription is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_update_subscription(self):

        # Construct a dict representation of a SubscriptionUpdateAttributesSMSAttributes model
        subscription_update_attributes_model = {
            'signing_enabled': True,
        }

        name = 'Webhook_sub_updated'
        description = 'Update Webhook subscription'
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id,
            name=name,
            description=description,
            attributes=subscription_update_attributes_model
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_new_id = subscription_response.get('id')
        subscription_name = subscription_response.get('name')
        subscription_description = subscription_response.get('description')
        assert subscription_name == name
        assert subscription_new_id == subscription_id
        assert subscription_description == description

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 404
        # 409
        # 415
        # 500
        #

    @needscredentials
    def test_send_notifications(self):
        # Construct a dict representation of a NotificationDevices model
        notification_devices_model = {
            'user_ids': ['userId'],
        }

        # Construct a dict representation of a Lights model
        lights_model = {
            'led_argb': 'RED',
            'led_on_ms': 0,
            'led_off_ms': '20',
        }

        # Construct a dict representation of a Style model
        style_model = {
            'type': 'picture_notification',
            'title': 'hello',
            'url': 'url.ibm.com',
        }

        # Construct a dict representation of a NotificationFCMBodyMessageData model
        notification_fcm_body_message_data_model = {
            'alert': 'Alert message',
            'collapse_key': 'collapse_key',
            'interactive_category': 'category_test',
            'icon': 'test.png',
            'delay_while_idle': True,
            'sync': True,
            'visibility': '0',
            'redact': 'redact test alert',
            'payload': {},
            'priority': 'MIN',
            'sound': 'newSound',
            'time_to_live': 0,
            'lights': lights_model,
            'android_title': 'IBM test title',
            'group_id': 'Group_ID_1',
            'style': style_model,
            'type': 'DEFAULT',
        }

        # Construct a dict representation of a NotificationFCMBodyMessageENData model
        notification_fcm_body_model = {
            'en_data': notification_fcm_body_message_data_model,
        }

        
        # Construct a dict representation of a NotificationAPNSBodyMessageData model
        notification_apns_body_message_data_model = {
            'alert': 'Alert message',
            'badge': 38,
            'interactiveCategory': 'InteractiveCategory',
            'iosActionKey': 'IosActionKey',
            'payload': {'foo': 'bar'},
            'sound': 'sound.wav',
            'titleLocKey': 'TitleLocKey',
            'locKey': 'LocKey',
            'launchImage': 'image.png',
            'titleLocArgs': ['TitleLocArgs1'],
            'locArgs': ['LocArgs1'],
            'title': 'Message Title',
            'subtitle': 'Message SubTitle',
            'attachmentUrl': 'https://testimage.sub.png',
            'type': 'DEFAULT',
            'apnsCollapseId': 'ApnsCollapseID',
            'apnsThreadId': 'ApnsThreadID',
            'apnsGroupSummaryArg': 'ApnsGroupSummaryArg',
            'apnsGroupSummaryArgCount': 38,
        }

        # Construct a dict representation of a NotificationAPNSBodyMessageENData model
        notification_apns_body_model = {
            'en_data': notification_apns_body_message_data_model,
        }

        notification_id = "1234-1234-sdfs-234"
        notification_severity = "MEDIUM"
        type_value = "com.acme.offer:new"
        notifications_source = "1234-1234-sdfs-234:test"

        send_notifications_response = self.event_notifications_service.send_notifications(
            instance_id,
            ce_ibmenseverity=notification_severity,
            ce_id=notification_id,
            ce_source=notifications_source,
            ce_ibmensourceid=source_id,
            ce_type=type_value,
            body={},
            ce_time='2019-01-01T12:00:00.000Z',
            ce_ibmenpushto=json.dumps(notification_devices_model),
            ce_ibmenfcmbody=json.dumps(notification_fcm_body_model),
            ce_ibmenapnsheaders=json.dumps(notification_apns_body_model),
            ce_specversion='1.0'
        )

        assert send_notifications_response.get_status_code() == 202
        notification_response = send_notifications_response.get_result()
        assert notification_response is not None

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

        send_notifications_response = self.event_notifications_service.send_notifications(
            instance_id,
            ce_ibmenseverity=notification_severity,
            ce_id=notification_id,
            ce_source=notifications_source,
            ce_ibmensourceid=source_id,
            ce_type=type_value,
            body={},
            ce_time='2019-01-01T12:00:00.000Z',
            ce_ibmenpushto=json.dumps(notification_devices_model),
            ce_ibmenfcmbody=json.dumps(notification_fcm_body_model),
            ce_ibmenapnsbody=json.dumps(notification_apns_body_model),
            ce_ibmenapnsheaders=json.dumps(message_apns_headers),
            ce_specversion='1.0'
        )

        assert send_notifications_response.get_status_code() == 202
        notification_response = send_notifications_response.get_result()
        assert notification_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 415
        # 500
        #

    @needscredentials
    def test_send_bulk_notifications(self):

        # Construct a dict representation of a NotificationDevices model
        notification_devices_model = {
            'user_ids': ['userId'],
        }

        # Construct a dict representation of a Lights model
        lights_model = {
            'led_argb': 'RED',
            'led_on_ms': 0,
            'led_off_ms': '20',
        }

        # Construct a dict representation of a Style model
        style_model = {
            'type': 'picture_notification',
            'title': 'hello',
            'url': 'url.ibm.com',
        }

        # Construct a dict representation of a NotificationFCMBodyMessageData model
        notification_fcm_body_message_data_model = {
            'alert': 'Alert message',
            'collapse_key': 'collapse_key',
            'interactive_category': 'category_test',
            'icon': 'test.png',
            'delay_while_idle': True,
            'sync': True,
            'visibility': '0',
            'redact': 'redact test alert',
            'payload': {},
            'priority': 'MIN',
            'sound': 'newSound',
            'time_to_live': 0,
            'lights': lights_model,
            'android_title': 'IBM test title',
            'group_id': 'Group_ID_1',
            'style': style_model,
            'type': 'DEFAULT',
        }

        # Construct a dict representation of a NotificationFCMBodyMessageENData model
        notification_fcm_body_model = {
            'en_data': notification_fcm_body_message_data_model,
        }

        # Construct a dict representation of a NotificationAPNSBodyMessageData model
        notification_apns_body_message_data_model = {
            'alert': 'Alert message',
            'badge': 38,
            'interactiveCategory': 'InteractiveCategory',
            'iosActionKey': 'IosActionKey',
            'payload': {'foo': 'bar'},
            'sound': 'sound.wav',
            'titleLocKey': 'TitleLocKey',
            'locKey': 'LocKey',
            'launchImage': 'image.png',
            'titleLocArgs': ['TitleLocArgs1'],
            'locArgs': ['LocArgs1'],
            'title': 'Message Title',
            'subtitle': 'Message SubTitle',
            'attachmentUrl': 'https://testimage.sub.png',
            'type': 'DEFAULT',
            'apnsCollapseId': 'ApnsCollapseID',
            'apnsThreadId': 'ApnsThreadID',
            'apnsGroupSummaryArg': 'ApnsGroupSummaryArg',
            'apnsGroupSummaryArgCount': 38,
        }

        # Construct a dict representation of a NotificationAPNSBodyMessageENData model
        notification_apns_body_model = {
            'en_data': notification_apns_body_message_data_model,
        }

        message_apns_headers = {
            "apns-collapse-id": "123",
        }

        notification_id = "1234-1234-sdfs-234"
        notification_severity = "MEDIUM"
        type_value = "com.acme.offer:new"
        notifications_source = "1234-1234-sdfs-234:test"

        # Construct a dict representation of a NotificationCreate model
        notification_create_model = {
            'ibmenseverity': notification_severity,
            'ibmenfcmbody': json.dumps(notification_fcm_body_model),
            'ibmenpushto': json.dumps(notification_devices_model),
            'ibmenapnsheaders': json.dumps(message_apns_headers),
            'ibmenapnsbody': json.dumps(notification_apns_body_model),
            'ibmensourceid': source_id,
            'id': notification_id,
            'source': notifications_source,
            'type': type_value,
            'specversion': '1.0',
            'time': '2019-01-01T12:00:00.000Z',
        }

        notification_id1 = "1234-1111-sdfs-234"
        notification_severity1 = "HIGH"
        type_value1 = "com.ibm.cloud.compliance.certificate_manager:certificate_expired"
        notifications_source1 = "1234-1234-sdfs-234:test"

        notification_create_model1 = {
            'ibmenseverity': notification_severity1,
            'ibmenfcmbody': json.dumps(notification_fcm_body_model),
            'ibmenpushto': json.dumps(notification_devices_model),
            'ibmenapnsheaders': json.dumps(message_apns_headers),
            'ibmenapnsbody': json.dumps(notification_apns_body_model),
            'ibmensourceid': source_id,
            'id': notification_id1,
            'source': notifications_source1,
            'type': type_value1,
            'specversion': '1.0',
            'time': '2019-01-01T12:00:00.000Z',
        }

        send_bulk_notifications_response = self.event_notifications_service.send_bulk_notifications(
            instance_id=instance_id,
            bulk_messages=[notification_create_model,notification_create_model1]
        )

        assert send_bulk_notifications_response.get_status_code() == 202
        bulk_notification_response = send_bulk_notifications_response.get_result()
        assert bulk_notification_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 415
        # 500
        #

    @needscredentials
    def test_delete_subscription(self):
        for id in [subscription_id, subscription_id2]:
            delete_subscription_response = self.event_notifications_service.delete_subscription(
                instance_id,
                id
            )

            assert delete_subscription_response.get_status_code() == 204

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_delete_topic(self):

        for id in [topic_id, topic_id2, topic_id3]:
            delete_topic_response = self.event_notifications_service.delete_topic(
                instance_id,
                id
            )

            assert delete_topic_response.get_status_code() == 204

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_delete_destination(self):

        delete_destination_response = self.event_notifications_service.delete_destination(
            instance_id,
            id=destination_id
        )

        assert delete_destination_response.get_status_code() == 204

        delete_destination_response = self.event_notifications_service.delete_destination(
            instance_id,
            id=destination_id3
        )

        assert delete_destination_response.get_status_code() == 204

        delete_destination_response = self.event_notifications_service.delete_destination(
            instance_id,
            id=destination_id4
        )

        assert delete_destination_response.get_status_code() == 204

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_delete_source(self):

        delete_source_response = self.event_notifications_service.delete_source(
            instance_id,
            id=source_id
        )

        assert delete_source_response.get_status_code() == 204

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #
