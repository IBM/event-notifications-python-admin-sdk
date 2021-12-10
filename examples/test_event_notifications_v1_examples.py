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
Examples for EventNotificationsV1
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
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
config_file = '../event_notifications.env'

event_notifications_service = None

config = None

# EN config values
instance_id = ''
search = ''
topic_name = 'Admin Topic Compliance'
source_id = ''
topic_id = ''
destination_id = ''
subscription_id = ''


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
        global instance_id
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
            assert instance_id is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason='External configuration not available, skipping...'
    )

    @needscredentials
    def test_list_sources_example(self):
        """
        list_sources request example
        """
        global source_id
        try:
            print('\nlist_sources() result:')
            # begin-list_sources

            source_list = event_notifications_service.list_sources(
                instance_id
            ).get_result()

            print(json.dumps(source_list, indent=2))

            # end-list_sources

            source_id = SourceList.from_dict(source_list).sources[0].id

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
        global destination_id

        try:
            print('\ncreate_destination() result:')
            # begin-create_destination

            destination_config_params_model = {
                'url': 'https://gcm.com',
                'verb': 'get',
                'custom_headers': {'Authorization': 'aaa-r-t-fdsfs-55kfjsd-fsdfs', },
                'sensitive_headers': ['gcm_apikey'],
            }

            # Construct a dict representation of a DestinationConfig model
            destination_config_model = {
                'params': destination_config_params_model,
            }

            name = 'GCM_destination'
            typeVal = 'webhook'
            description = 'GCM Destination'

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeVal,
                description=description,
                config=destination_config_model
            ).get_result()

            print(json.dumps(destination, indent=2))

            # end-create_destination

            destination = DestinationResponse.from_dict(destination)
            destination_id = destination.id

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_destinations_example(self):
        """
        list_destinations request example
        """
        try:
            print('\nlist_destinations() result:')
            # begin-list_destinations

            destination_list = event_notifications_service.list_destinations(
                instance_id
            ).get_result()

            print(json.dumps(destination_list, indent=2))

            # end-list_destinations

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

            # Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
            destination_config_params_model = {
                'url': 'https://cloud.ibm.com/webhook/send_message',
                'verb': 'post',
                'sensitive_headers': ['authorization'],
            }

            # Construct a dict representation of a DestinationConfig model
            destination_config_model = {
                'params': destination_config_params_model,
            }

            name = 'Admin GCM Compliance'
            description = 'This destination is for creating admin GCM webhook to receive compliance notifications'
            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id,
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
        global subscription_id
        try:
            print('\ncreate_subscription() result:')
            # begin-create_subscription

            subscription_create_attributes_model = {
                'signing_enabled': False,
            }

            name = 'subscription_web'
            description = 'Subscription for web'
            subscription = event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id,
                topic_id,
                attributes=subscription_create_attributes_model,
                description=description
            ).get_result()

            print(json.dumps(subscription, indent=2))

            # end-create_subscription

            subscription_id = subscription.get('id')

        except ApiException as e:
            pytest.fail(str(e))

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

            # Construct a dict representation of a SubscriptionUpdateAttributesSMSAttributes model
            subscription_update_attributes_model = {
                'signing_enabled': True,
            }

            name = 'GCM_sub_updated'
            description = 'Update GCM subscription'
            subscription = event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model
            ).get_result()

            print(json.dumps(subscription, indent=2))

            # end-update_subscription

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

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: EventNotificationsV1
##############################################################################
