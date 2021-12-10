# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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
config_file = '../../event_notifications.env'

# EN config values
instance_id = ''
search = ''
topic_name = 'GCMTopic'
source_id = ''
topic_id = ''
topic_id2 = ''
destination_id = ''
destination_id2 = ''
destination_idsms = ''
subscription_id = ''
subscription_id2 = ''
subscription_idsms = ''


class TestEventNotificationsV1():
    """
    Integration Test Class for EventNotificationsV1
    """

    @classmethod
    def setup_class(cls):
        global instance_id
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
            assert instance_id is not None


        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_list_sources(self):

        global source_id
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

            if offset == 0:
                source_id = SourceList.from_dict(source_list).sources[0].id
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
    def test_create_topic(self):
        # Construct a dict representation of a Rules model
        global topic_id, topic_id2
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

        description = "Topic for GCM notifications"
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

        description = "Topic 2 for GCM notifications"
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

        assert topic_id2 is not ''
        assert topic_id is not ''
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
        global destination_id
        destination_config_params_model = {
            'url': 'https://gcm.com',
            'verb': 'get',
            'custom_headers': {},
            'sensitive_headers': ['gcm_apikey'],
        }

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {
            'params': destination_config_params_model,
        }

        name = "GCM_destination"
        typeVal = "webhook"
        description = "GCM  Destination"

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
        global destination_id2, destination_idsms
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
                elif destination.id != destination_id and destination.type == "sms_ibm":
                    destination_idsms = destination.id
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
            'custom_headers': {},
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
    def test_create_subscription(self):
        # Construct a dict representation of a SubscriptionCreateAttributesSMSAttributes model
        global subscription_id, subscription_id2, subscription_idsms
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

        name = 'subscription_web_2'
        description = 'Subscription 2 for web'
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
        subscription_create_attributes_model = {
            'to': ["+12048089972", "+12014222730"]
        }
        name = "subscription_sms"
        description = "Subscription for sms"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_idsms,
            topic_id=topic_id,
            attributes=subscription_create_attributes_model,
            description=description
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get('name')
        subscription_description = subscription_response.get('description')
        subscription_idsms = subscription_response.get('id')

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

        name = 'GCM_sub_updated'
        description = 'Update GCM subscription'
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

        # Email update
        subscription_update_attributes_model = {
            'to': {
                'add': ['testereq1@gmail.com', 'tester553@ibm.com'],
                'remove': ['tester1@gmail.com']
            },
            'add_notification_payload': True,
            "reply_to_mail": "reply_to_mail@us.com",
            "reply_to_name": "US News",
            "from_name": "IBM",
            'unsubscribed': {
                'remove': ['tester3@ibm.com']
            }
        }

        name = 'subscription_email_3'
        description = 'Update email subscription'
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id2,
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
        assert subscription_new_id == subscription_id2
        assert subscription_description == description

        # SMS update
        subscription_update_attributes_model = {
            'to': ['+120480009972', '+1201499990']
        }

        name = 'subscription_sms+1'
        description = 'update Subscription for sms'
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_idsms,
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
        assert subscription_new_id == subscription_idsms
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

        for id in [topic_id, topic_id2]:
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

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #
