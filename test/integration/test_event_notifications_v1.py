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
config_file = "../../event_notifications_v1.env"

# EN config values
instance_id = ""
search = ""
topic_name = "GCMTopic"
source_id = ""
topic_id = ""
topic_id2 = ""
topic_id3 = ""
destination_id = ""
destination_id1 = ""
destination_id2 = ""
destination_id3 = ""
destination_id4 = ""
destination_id5 = ""
destination_id6 = ""
destination_id7 = ""
destination_id8 = ""
destination_id9 = ""
destination_id10 = ""
destination_id11 = ""
destination_id12 = ""
destination_id13 = ""
destination_id14 = ""
destination_id15 = ""
destination_id16 = ""
safariCertificatePath = ""
subscription_id = ""
subscription_id1 = ""
subscription_id2 = ""
subscription_id3 = ""
subscription_id4 = ""
subscription_id5 = ""
subscription_id6 = ""
subscription_id7 = ""
subscription_id8 = ""
subscription_id9 = ""
subscription_id10 = ""
subscription_id11 = ""
subscription_id12 = ""
subscription_id13 = ""
subscription_id14 = ""
subscription_id15 = ""
subscription_id16 = ""
fcmServerKey = ""
fcmSenderId = ""
integration_id = ""
snow_client_id = ""
snow_client_secret = ""
snow_user_name = ""
snow_password = ""
snow_instance_name = ""
fcm_private_key = ""
fcm_project_id = ""
fcm_client_email = ""
code_engine_URL = ""
huawei_client_id = ""
huawei_client_secret = ""
cos_bucket_name = ""
cos_instance_id = ""
cos_end_point = ""
template_invitation_id = ""
template_notification_id = ""
slack_url = ""
teams_url = ""
pager_duty_api_key = ""
pager_duty_routing_key = ""


class TestEventNotificationsV1:
    """
    Integration Test Class for EventNotificationsV1
    """

    @classmethod
    def setup_class(cls):
        global instance_id, fcmServerKey, fcmSenderId, safariCertificatePath, fcm_project_id, fcm_private_key, fcm_client_email, huawei_client_id, huawei_client_secret, cos_instance_id, cos_end_point, cos_bucket_name, slack_url, teams_url, pager_duty_api_key, pager_duty_routing_key
        if os.path.exists(config_file):
            os.environ["IBM_CREDENTIALS_FILE"] = config_file

            cls.event_notifications_service = EventNotificationsV1.new_instance()
            assert cls.event_notifications_service is not None

            cls.config = read_external_sources(EventNotificationsV1.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.event_notifications_service.enable_retries()

            instance_id = cls.config["GUID"]
            fcmServerKey = cls.config["FCM_KEY"]
            fcmSenderId = cls.config["FCM_ID"]
            safariCertificatePath = cls.config["SAFARI_CERTIFICATE"]
            snow_client_id = cls.config["SNOW_CLIENT_ID"]
            snow_client_secret = cls.config["SNOW_CLIENT_SECRET"]
            snow_user_name = cls.config["SNOW_USER_NAME"]
            snow_password = cls.config["SNOW_PASSWORD"]
            snow_instance_name = cls.config["SNOW_INSTANCE_NAME"]
            fcm_client_email = cls.config["FCM_CLIENT_EMAIL"]
            fcm_project_id = cls.config["FCM_PROJECT_ID"]
            fcm_private_key = cls.config["FCM_PRIVATE_KEY"]
            code_engine_URL = cls.config["CODE_ENGINE_URL"]
            huawei_client_id = cls.config["HUAWEI_CLIENT_ID"]
            huawei_client_secret = cls.config["HUAWEI_CLIENT_SECRET"]
            cos_instance_id = cls.config["COS_INSTANCE"]
            cos_bucket_name = cls.config["COS_BUCKET_NAME"]
            cos_end_point = cls.config["COS_ENDPOINT"]
            slack_url = cls.config["SLACK_URL"]
            teams_url = cls.config["MS_TEAMS_URL"]
            pager_duty_api_key = cls.config["PD_API_KEY"]
            pager_duty_routing_key = cls.config["PD_ROUTING_KEY"]
            assert instance_id is not None
            assert fcmServerKey is not None
            assert fcmSenderId is not None
            assert fcm_client_email is not None
            assert fcm_project_id is not None
            assert fcm_private_key is not None
            assert snow_client_id is not None
            assert snow_client_secret is not None
            assert snow_user_name is not None
            assert snow_password is not None
            assert snow_instance_name is not None
            assert code_engine_URL is not None
            assert cos_end_point is not None
            assert cos_instance_id is not None
            assert cos_bucket_name is not None
            assert slack_url is not None

        print("Setup complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...",
    )

    @needscredentials
    def test_list_integrations(self):
        global integration_id
        list_integrations_response = self.event_notifications_service.list_integrations(
            instance_id, limit=1, offset=0, search=search
        )

        assert list_integrations_response.get_status_code() == 200
        integration_response = list_integrations_response.get_result()
        integrations = integration_response.get("integrations")
        assert integrations[0] is not None
        integration_id = integrations[0].get("id")

    @needscredentials
    def test_get_integration(self):
        get_integration_response = self.event_notifications_service.get_integration(instance_id, id=integration_id)

        assert get_integration_response.get_status_code() == 200
        integration_response = get_integration_response.get_result()
        assert integration_response is not None

    @needscredentials
    def test_update_integration(self):
        integration_metadata = {
            "endpoint": "https://private.us-south.kms.cloud.ibm.com",
            "crn": "crn:v1:staging:public:kms:us-south:a/****:****::",
            "root_key_id": "sddsds-f326-4688-baaf-611750e79b61",
        }

        update_integration_response = self.event_notifications_service.replace_integration(
            instance_id,
            id=integration_id,
            type="kms",
            metadata=integration_metadata,
        )

        assert update_integration_response.get_status_code() == 200
        integration_response = update_integration_response.get_result()
        assert integration_response is not None

    @needscredentials
    def test_create_sources(self):
        global source_id
        create_sources_response = self.event_notifications_service.create_sources(
            instance_id,
            name="Event Notification Create Source Acme",
            description="This source is used for Acme Bank",
            enabled=False,
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
                instance_id, limit=limit, offset=offset, search=search
            )
            assert list_sources_response.get_status_code() == 200
            source_list = list_sources_response.get_result()
            assert source_list is not None

            if source_list.get("total_count") <= offset:
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
        get_source_response = self.event_notifications_service.get_source(instance_id, source_id)

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
            name="Event Notification update Source Acme",
            description="This source is used for updated Acme Bank",
            enabled=True,
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
            "enabled": False,
            "event_type_filter": "$.notification_event_info.event_type == 'cert_manager'",
            "notification_filter": "$.notification.findings[0].severity == 'MODERATE'",
        }

        # Construct a dict representation of a TopicUpdateSourcesItem model
        topic_update_sources_item_model = {
            "id": source_id,
            "rules": [rules_model],
        }

        description = "Topic for Webhook notifications"
        create_topic_response = self.event_notifications_service.create_topic(
            instance_id,
            name=topic_name,
            description=description,
            sources=[topic_update_sources_item_model],
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
            sources=[topic_update_sources_item_model],
        )

        assert create_topic_response.get_status_code() == 201
        topic_response = create_topic_response.get_result()
        assert topic_response is not None

        topic = TopicResponse.from_dict(topic_response)
        assert topic is not None

        assert topic.name == name
        assert topic.description == description

        topic_id2 = topic.id

        description = (
            "This topic is used for routing all compliance related notifications to the appropriate destinations"
        )
        name = "FCM_topic"

        create_topic_response = self.event_notifications_service.create_topic(
            instance_id,
            name=name,
            description=description,
            sources=[topic_update_sources_item_model],
        )

        assert create_topic_response.get_status_code() == 201
        topic_response = create_topic_response.get_result()
        assert topic_response is not None

        topic = TopicResponse.from_dict(topic_response)
        assert topic is not None

        assert topic.name == name
        assert topic.description == description

        topic_id3 = topic.id

        assert topic_id2 is not ""
        assert topic_id is not ""
        assert topic_id3 is not ""

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
                instance_id, limit=limit, offset=offset, search=search
            )

            assert list_topics_response.get_status_code() == 200
            topic_list = list_topics_response.get_result()
            assert topic_list is not None

            if topic_list.get("total_count") <= offset:
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
        get_topic_response = self.event_notifications_service.get_topic(instance_id, id=topic_id, include=search)

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
            "enabled": True,
            "event_type_filter": "$.notification_event_info.event_type == 'core_cert_manager'",
            "notification_filter": "$.notification.findings[0].severity == 'SEVERE'",
        }

        # Construct a dict representation of a TopicUpdateSourcesItem model
        topic_update_sources_item_model = {
            "id": source_id,
            "rules": [rules_model],
        }

        description = "Updated Topic for GCM notifications"
        name = topic_name + "2"
        replace_topic_response = self.event_notifications_service.replace_topic(
            instance_id,
            id=topic_id,
            name=name,
            description=description,
            sources=[topic_update_sources_item_model],
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
        global destination_id, destination_id3, destination_id4, destination_id5, destination_id6, destination_id7, destination_id8, destination_id9, destination_id10, destination_id11, destination_id12, destination_id13, destination_id14, destination_id15, destination_id16
        destination_config_params_model = {
            "url": "https://gcm.com",
            "verb": "get",
            "custom_headers": {"gcm_apikey": "apikey"},
            "sensitive_headers": ["gcm_apikey"],
        }

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {
            "params": destination_config_params_model,
        }

        name = "Webhook_destination"
        typeval = "webhook"
        description = "Webhook Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id = destination.id

        fcm_config_params = {"server_key": fcmServerKey, "sender_id": fcmSenderId}
        destination_config_model = {
            "params": fcm_config_params,
        }
        name = "FCM_destination"
        typeval = "push_android"
        description = "FCM Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id3 = destination.id

        slack_config_params = {
            "url": slack_url,
        }

        destination_config_model = {
            "params": slack_config_params,
        }

        name = "Slack_destination"
        typeval = "slack"
        description = "Slack Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id4 = destination.id

        safari_config_params = {
            "cert_type": "p12",
            "password": "password",
            "website_url": "https://ensafaripush.mybluemix.net",
            "website_name": "NodeJS Starter Application",
            "url_format_string": "https://ensafaripush.mybluemix.net/%@/?flight=%@",
            "website_push_id": "web.net.mybluemix.ensafaripush",
        }

        destination_config_model = {
            "params": safari_config_params,
        }

        name = "Safari_destination"
        typeval = "push_safari"
        description = "Safari Destination"

        certificatefile = open(safariCertificatePath, "rb")
        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
            certificate=certificatefile,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id5 = destination.id

        msteams_config_params = {
            "url": teams_url,
        }

        destination_config_model = {
            "params": msteams_config_params,
        }

        name = "MSTeams_destination"
        typeval = "msteams"
        description = "MSteams Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id6 = destination.id

        cf_config_params = {
            "url": "https://www.ibmcfendpoint.com/",
            "api_key": "apikey",
        }

        destination_config_model = {
            "params": cf_config_params,
        }
        name = "Cloud_Functions_destination"
        typeval = "ibmcf"
        description = "This is a Cloud Functions Destination for actions"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id7 = destination.id

        chrome_config_params = {
            "website_url": "https://www.xyz.pqr",
            "api_key": "AAxxxxxxxxxxxxxxxxx4z",
        }

        destination_config_model = {
            "params": chrome_config_params,
        }
        name = "Chrome_destination"
        typeval = "push_chrome"
        description = "This is a Chrome Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id8 = destination.id

        fire_config_params = {"website_url": "https://cloud.ibm.com"}

        destination_config_model = {
            "params": fire_config_params,
        }
        name = "Firefox_destination"
        typeval = "push_firefox"
        description = "This is a Firefox Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id9 = destination.id

        pd_config_params = {
            "api_key": pager_duty_api_key,
            "routing_key": pager_duty_routing_key,
        }

        destination_config_model = {
            "params": pd_config_params,
        }
        name = "Pager_Duty_destination"
        typeval = "pagerduty"
        description = "This is a PagerDuty Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id10 = destination.id

        snow_config_params = {
            "client_id": snow_client_id,
            "client_secret": snow_client_secret,
            "username": snow_user_name,
            "password": snow_password,
            "instance_name": snow_password,
        }

        destination_config_model = {
            "params": snow_config_params,
        }
        name = "Service_Now_destination"
        typeval = "servicenow"
        description = "This is a ServiceNow Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id11 = destination.id

        fcm_config_params = {
            "project_id": fcm_project_id,
            "private_key": fcm_private_key,
            "client_email": fcm_client_email,
        }
        destination_config_model = {
            "params": fcm_config_params,
        }
        name = "FCM_V1_destination"
        typeval = "push_android"
        description = "FCM V1 Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id12 = destination.id

        destination_config_params_model = {
            "url": code_engine_URL,
            "verb": "get",
            "custom_headers": {"authorization": "apikey"},
            "sensitive_headers": ["authorization"],
        }

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {
            "params": destination_config_params_model,
        }

        name = "code_engine_destination"
        typeval = "ibmce"
        description = "code engine Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id13 = destination.id

        destination_config_model = {
            "params": {
                "bucket_name": cos_bucket_name,
                "instance_id": cos_instance_id,
                "endpoint": cos_end_point,
            }
        }

        name = "COS_destination"
        typeval = "ibmcos"
        description = "COS Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id14 = destination.id

        destination_config_model = {
            "params": {
                "client_id": huawei_client_id,
                "client_secret": huawei_client_secret,
                "pre_prod": False,
            }
        }

        name = "Huawei_destination"
        typeval = "push_huawei"
        description = "Huawei Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id15 = destination.id

        destination_config_model = {
            "params": {
                "domain": "test.event-notifications.test.cloud.ibm.com",
            }
        }

        name = "custom_email_destination"
        typeval = "smtp_custom"
        description = "Custom Email Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            config=destination_config_model,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None

        destination = DestinationResponse.from_dict(destination_response)

        assert destination is not None
        assert destination.name == name
        assert destination.description == description
        assert destination.type == typeval

        destination_id16 = destination.id

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
    def test_destination(self):
        test_destination_response = self.event_notifications_service.test_destination(instance_id, id=destination_id4)

        assert test_destination_response.get_status_code() == 200

    @needscredentials
    def test_create_template(self):
        # Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
        global template_invitation_id, template_notification_id

        template_config_model = {
            "body": "<!DOCTYPE html><html><head><title>IBM Event Notifications</title></head><body><p>Hello! Invitation template</p><table><tr><td>Hello invitation link:{{ ibmen_invitation }} </td></tr></table></body></html>",
            "subject": "Hi this is invitation for invitation message",
        }

        name = "template_invitation"
        typeval = "smtp_custom.invitation"
        description = "invitation template"

        create_template_response = self.event_notifications_service.create_template(
            instance_id,
            name,
            type=typeval,
            params=template_config_model,
            description=description,
        )

        assert create_template_response.get_status_code() == 201
        template_response = create_template_response.get_result()
        assert template_response is not None

        template = TemplateResponse.from_dict(template_response)

        assert template is not None
        assert template.name == name
        assert template.description == description
        assert template.type == typeval

        template_invitation_id = template.id

        name = "template_notification"
        typeval = "smtp_custom.notification"
        description = "notification template"

        create_template_response = self.event_notifications_service.create_template(
            instance_id,
            name,
            type=typeval,
            params=template_config_model,
            description=description,
        )

        assert create_template_response.get_status_code() == 201
        template_response = create_template_response.get_result()
        assert template_response is not None

        template = TemplateResponse.from_dict(template_response)

        assert template is not None
        assert template.name == name
        assert template.description == description
        assert template.type == typeval

        template_notification_id = template.id

    @needscredentials
    def test_list_destinations(self):
        global destination_id2, destination_id1
        more_results = True
        limit = 1
        offset = 0

        while more_results:
            list_destinations_response = self.event_notifications_service.list_destinations(
                instance_id, limit=limit, offset=offset, search=search
            )

            assert list_destinations_response.get_status_code() == 200
            destination_list = list_destinations_response.get_result()
            assert destination_list is not None

            destinations = DestinationList.from_dict(destination_list)
            assert destinations is not None

            for i in range(0, len(destinations.destinations)):
                destination = destinations.destinations[i]
                if destination.id != destination_id and destination.type == "smtp_ibm":
                    destination_id2 = destination.id
                    if destination_id1 != "":
                        break
                if destination.type == "sms_ibm":
                    destination_id1 = destination.id
                    if destination_id2 != "":
                        break
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
    def test_list_templates(self):
        more_results = True
        limit = 1
        offset = 0

        while more_results:
            list_templates_response = self.event_notifications_service.list_templates(
                instance_id, limit=limit, offset=offset, search=search
            )

            assert list_templates_response.get_status_code() == 200
            templates_list = list_templates_response.get_result()
            assert templates_list is not None

            templates = TemplateList.from_dict(templates_list)
            assert templates is not None

            if templates.total_count <= offset:
                more_results = False
            offset += 1

    @needscredentials
    def test_get_destination(self):
        get_destination_response = self.event_notifications_service.get_destination(instance_id, id=destination_id)

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
    def test_get_template(self):
        get_template_response = self.event_notifications_service.get_template(instance_id, id=template_invitation_id)

        assert get_template_response.get_status_code() == 200
        template_response = get_template_response.get_result()
        assert template_response is not None

    @needscredentials
    def test_update_destination(self):
        # Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
        destination_config_params_model = {
            "url": "https://cloud.ibm.com/nhwebhook/sendwebhook",
            "verb": "post",
            "custom_headers": {"authorization": "authorization token"},
            "sensitive_headers": ["authorization"],
        }

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {
            "params": destination_config_params_model,
        }

        name = "Admin GCM Compliance"
        description = "This destination is for creating admin GCM webhook to receive compliance notifications"
        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id
        assert res_name == name
        assert res_description == description

        fcm_config_params = {"server_key": fcmServerKey, "sender_id": fcmSenderId}

        destination_config_model = {
            "params": fcm_config_params,
        }
        name = "FCM_destination_update"
        description = "FCM Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id3,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id3
        assert res_name == name
        assert res_description == description

        slack_config_params = {
            "url": slack_url,
        }

        destination_config_model = {
            "params": slack_config_params,
        }

        name = "Slack_destination_update"
        description = "Slack Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id4,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id4
        assert res_name == name
        assert res_description == description

        safari_destination_config_params_model = {
            "cert_type": "p12",
            "password": "password",
            "website_url": "https://ensafaripush.mybluemix.net",
            "website_name": "NodeJS Starter Application",
            "url_format_string": "https://ensafaripush.mybluemix.net/%@/?flight=%@",
            "website_push_id": "web.net.mybluemix.ensafaripush",
        }

        # Construct a dict representation of a DestinationConfig model
        safari_destination_config_model = {
            "params": safari_destination_config_params_model,
        }

        certificatefile = open(safariCertificatePath, "rb")
        name = "Safari Dest"
        description = "This destination is for Safari"
        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id5,
            name=name,
            description=description,
            config=safari_destination_config_model,
            certificate=certificatefile,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id5
        assert res_name == name
        assert res_description == description

        msteams_config_params = {
            "url": teams_url,
        }

        destination_config_model = {
            "params": msteams_config_params,
        }

        name = "MSTeams_destination_update"
        description = "MSteams Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id6,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id6
        assert res_name == name
        assert res_description == description

        destination_config_params_model = {
            "url": "https://www.ibmcfendpoint.com/",
            "api_key": "apikey",
        }

        destination_config_model = {
            "params": destination_config_params_model,
        }
        name = "Cloud_Functions_dest"
        description = "This is a Cloud Functions Destination"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id7,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id7
        assert res_name == name
        assert res_description == description

        chrome_config_params = {
            "website_url": "https://www.xyz.pqr",
            "api_key": "AAxxxxxxxxxxxxxxxxx4z",
        }

        destination_config_model = {
            "params": chrome_config_params,
        }
        name = "Chrome_destination_update"
        description = "This is a Chrome Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id8,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id8
        assert res_name == name
        assert res_description == description

        fire_config_params = {"website_url": "https://cloud.ibm.com"}

        destination_config_model = {
            "params": fire_config_params,
        }
        name = "Firefox_destination_update"
        description = "This is a Firefox Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id9,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id9
        assert res_name == name
        assert res_description == description

        pd_config_params = {
            "api_key": pager_duty_api_key,
            "routing_key": pager_duty_routing_key,
        }

        destination_config_model = {
            "params": pd_config_params,
        }
        name = "PagerDuty_destination_update"
        description = "This is a PagerDuty Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id10,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id10
        assert res_name == name
        assert res_description == description

        snow_config_params = {
            "client_id": snow_client_id,
            "client_secret": snow_client_secret,
            "username": snow_user_name,
            "password": snow_password,
            "instance_name": snow_password,
        }

        destination_config_model = {
            "params": snow_config_params,
        }

        name = "Service_Now_destination_update"
        description = "This is a ServiceNow Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id11,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id11
        assert res_name == name
        assert res_description == description

        fcm_config_params = {
            "project_id": fcm_project_id,
            "private_key": fcm_private_key,
            "client_email": fcm_client_email,
        }
        destination_config_model = {
            "params": fcm_config_params,
        }
        name = "FCM_destination_V1_update"
        description = "FCM Destination V1 update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id12,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id12
        assert res_name == name
        assert res_description == description

        destination_config_params_model = {
            "url": code_engine_URL,
            "verb": "post",
            "custom_headers": {"authorization": "authorization token"},
            "sensitive_headers": ["authorization"],
        }

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {
            "params": destination_config_params_model,
        }

        name = "code engine updated"
        description = "This destination is updated for code engine notifications"
        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id13,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id13
        assert res_name == name
        assert res_description == description

        destination_config_model = {
            "params": {
                "bucket_name": cos_bucket_name,
                "instance_id": cos_instance_id,
                "endpoint": cos_end_point,
            }
        }

        name = "COS_destination_update"
        description = "COS Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id14,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id14
        assert res_name == name
        assert res_description == description

        destination_config_model = {
            "params": {
                "client_id": huawei_client_id,
                "client_secret": huawei_client_secret,
                "pre_prod": False,
            }
        }

        name = "Huawei_destination_update"
        description = "Huawei Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id15,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id15
        assert res_name == name
        assert res_description == description

        destination_config_model = {"params": {"domain": "test.event-notifications.test.cloud.ibm.com"}}

        name = "Custom_Email_destination_update"
        description = "Custom Email Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id16,
            name=name,
            description=description,
            config=destination_config_model,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id16
        assert res_name == name
        assert res_description == description

        spf_response = self.event_notifications_service.update_verify_destination(
            instance_id,
            id=destination_id16,
            type="spf",
        )
        assert spf_response.get_status_code() == 200
        spf_verification_response = spf_response.get_result()
        assert spf_verification_response is not None

        dkim_response = self.event_notifications_service.update_verify_destination(
            instance_id,
            id=destination_id16,
            type="dkim",
        )
        assert dkim_response.get_status_code() == 200
        dkim_verification_response = dkim_response.get_result()
        assert dkim_verification_response is not None
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
    def test_update_template(self):
        template_config_model = {
            "body": "<!DOCTYPE html><html><head><title>IBM Event Notifications</title></head><body><p>Hello! Invitation template</p><table><tr><td>Hello invitation link:{{ ibmen_invitation }} </td></tr></table></body></html>",
            "subject": "Hi this is invitation for invitation message",
        }

        template_name = "template_invitation"
        typeval = "smtp_custom.invitation"
        description = "invitation template"

        update_template_response = self.event_notifications_service.update_template(
            instance_id,
            id=template_invitation_id,
            name=template_name,
            type=typeval,
            description=description,
            params=template_config_model,
        )

        assert update_template_response.get_status_code() == 200
        template_response = update_template_response.get_result()

        assert template_response is not None
        assert template_response.get("name") == template_name
        assert template_response.get("description") == description
        assert template_response.get("type") == typeval
        assert template_response.get("id") == template_invitation_id

        template_name = "template_notification"
        typeval = "smtp_custom.notification"
        description = "notification template"

        update_template_response = self.event_notifications_service.update_template(
            instance_id,
            id=template_notification_id,
            name=template_name,
            type=typeval,
            description=description,
            params=template_config_model,
        )

        assert update_template_response.get_status_code() == 200
        template_response = update_template_response.get_result()
        assert template_response is not None
        assert template_response.get("name") == template_name
        assert template_response.get("description") == description
        assert template_response.get("type") == typeval
        assert template_response.get("id") == template_notification_id

    @needscredentials
    def test_create_subscription(self):
        # Construct a dict representation of a SubscriptionCreateAttributesSMSAttributes model
        global subscription_id, subscription_id1, subscription_id2, subscription_id3, subscription_id4, subscription_id5, subscription_id6, subscription_id7, subscription_id8, subscription_id9, subscription_id10, subscription_id11, subscription_id12, subscription_id13, subscription_id14, subscription_id15, subscription_id16
        subscription_create_attributes_model = {
            "signing_enabled": False,
        }

        name = "subscription_web"
        description = "Subscription for web"
        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id,
            topic_id,
            attributes=subscription_create_attributes_model,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id = subscription_response.get("id")
        assert subscription_name == name
        assert subscription_description == description

        subscription_create_attributes_model = {
            "invited": ["+12064512559", "+12064512559"],
        }

        name = "subscription_sms"
        description = "Subscription for sms"
        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id1,
            topic_id=topic_id,
            attributes=subscription_create_attributes_model,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id1 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        subscription_create_attributes_model = {
            "invited": ["tester1@gmail.com", "tester3@ibm.com"],
            "add_notification_payload": True,
            "reply_to_mail": "reply_to_mail@us.com",
            "reply_to_name": "US News",
            "from_name": "IBM",
        }

        name = "subscription_email"
        description = "Subscription for email"
        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id2,
            topic_id=topic_id,
            attributes=subscription_create_attributes_model,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id2 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        # FCM
        name = "FCM subscription"
        description = "Subscription for the FCM"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id3,
            topic_id=topic_id3,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id3 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "slack subscription"
        description = "Subscription for the slack"

        subscription_create_attributes_model = {
            "attachment_color": "#0000FF",
        }

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id4,
            topic_id=topic_id,
            description=description,
            attributes=subscription_create_attributes_model,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id4 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "safari subscription"
        description = "Subscription for the safari"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id5,
            topic_id=topic_id,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id5 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "MSTeams subscription"
        description = "Subscription for the MSTeams"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id6,
            topic_id=topic_id,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id6 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "cloud functions subscription"
        description = "Subscription for the cloud functions"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id7,
            topic_id=topic_id,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id7 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "chrome subscription"
        description = "Subscription for the chrome"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id8,
            topic_id=topic_id,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id8 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "Firefox subscription"
        description = "Subscription for the firefox"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id9,
            topic_id=topic_id,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id9 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "PagerDuty subscription"
        description = "Subscription for the PagerDuty"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id10,
            topic_id=topic_id,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id10 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "ServiceNow subscription"
        description = "Subscription for the ServiceNow"

        subscription_create_attributes_model = {
            "assigned_to": "user",
            "assignment_group": "group",
        }

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id11,
            topic_id=topic_id,
            description=description,
            attributes=subscription_create_attributes_model,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id11 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "FCM V1 subscription"
        description = "Subscription for the FCM V11"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id12,
            topic_id=topic_id3,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id12 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        subscription_create_attributes_model = {
            "signing_enabled": False,
        }

        name = "subscription_code_engine"
        description = "Subscription for code engine"
        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id13,
            topic_id,
            attributes=subscription_create_attributes_model,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id13 = subscription_response.get("id")
        assert subscription_name == name
        assert subscription_description == description

        name = "COS destination subscription"
        description = "Subscription for the COS destination"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id14,
            topic_id=topic_id,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id14 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "Huawei destination subscription"
        description = "Subscription for the Huawei destination"

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id15,
            topic_id=topic_id,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id15 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        subscription_create_attributes_model = {
            "invited": ["nitishkulkarni005@gmail.com", "tester3@ibm.com"],
            "add_notification_payload": True,
            "reply_to_mail": "reply_to_mail@us.com",
            "reply_to_name": "US News",
            "from_name": "IBM",
            "from_email": "test@test.event-notifications.test.cloud.ibm.com",
            "template_id_invitation": template_invitation_id,
            "template_id_notification": template_notification_id,
        }

        name = "subscription_custom_email"
        description = "Subscription for custom email"
        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id16,
            topic_id=topic_id,
            attributes=subscription_create_attributes_model,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id16 = subscription_response.get("id")

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
                instance_id, offset=offset, limit=limit, search=search
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
        get_subscription_response = self.event_notifications_service.get_subscription(instance_id, id=subscription_id)

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
            "signing_enabled": True,
        }

        name = "Webhook_sub_updated"
        description = "Update Webhook subscription"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id,
            name=name,
            description=description,
            attributes=subscription_update_attributes_model,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_new_id = subscription_response.get("id")
        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        assert subscription_name == name
        assert subscription_new_id == subscription_id
        assert subscription_description == description

        sms_update_attributes_invite_model = {"add": ["+12064512559"]}

        sms_update_attributes_toremove_model = {"remove": ["+12064512559"]}

        subscription_update_attributes_model = {
            "invited": sms_update_attributes_invite_model,
            "subscribed": sms_update_attributes_toremove_model,
            "unsubscribed": sms_update_attributes_toremove_model,
        }

        name = "subscription_sms update"
        description = "Subscription for sms updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id1,
            name=name,
            description=description,
            attributes=subscription_update_attributes_model,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        email_update_attributes_invite_model = {"add": ["tester4@ibm.com"]}

        email_update_attributes_toremove_model = {"remove": ["tester3@ibm.com"]}

        subscription_update_attributes_model = {
            "invited": email_update_attributes_invite_model,
            "add_notification_payload": True,
            "reply_to_mail": "reply_to_mail@us.com",
            "reply_to_name": "US News",
            "from_name": "IBM",
            "subscribed": email_update_attributes_toremove_model,
            "unsubscribed": email_update_attributes_toremove_model,
        }

        name = "subscription_email update"
        description = "Subscription for email updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id2,
            name=name,
            description=description,
            attributes=subscription_update_attributes_model,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "FCM update"
        description = "Subscription for FCM updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id3,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "Slack update"
        description = "Subscription for slack updated"
        subscription_update_attributes_model = {
            "attachment_color": "#0000FF",
        }
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id4,
            name=name,
            description=description,
            attributes=subscription_update_attributes_model,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "safari update"
        description = "Subscription for safari updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id5,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "MSTeams update"
        description = "Subscription for MSTeams updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id6,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "cloud functions update"
        description = "Subscription for cloud functions updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id7,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "chrome update"
        description = "Subscription for chrome updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id8,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "Firefox update"
        description = "Subscription for Firefox updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id9,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "PagerDuty update"
        description = "Subscription for PagerDuty updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id10,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        subscription_update_attributes_model = {
            "assigned_to": "user",
            "assignment_group": "group",
        }

        name = "ServiceNow update"
        description = "Subscription for ServiceNow updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id11,
            name=name,
            description=description,
            attributes=subscription_update_attributes_model,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "FCM V1 update"
        description = "Subscription for FCM V1 updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id12,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        subscription_update_attributes_model = {
            "signing_enabled": True,
        }

        name = "code_engine_sub_updated"
        description = "Update code engine subscription"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id13,
            name=name,
            description=description,
            attributes=subscription_update_attributes_model,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_new_id = subscription_response.get("id")
        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        assert subscription_name == name
        assert subscription_new_id == subscription_id13
        assert subscription_description == description

        name = "COS subscription update"
        description = "Subscription for COS updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id14,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        name = "Huawei subscription update"
        description = "Subscription for Huawei updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id15,
            name=name,
            description=description,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

        assert subscription_name == name
        assert subscription_description == description

        custom_email_update_attributes_invite_model = {"add": ["tester4@ibm.com", "nitishkulkarni005@gmail.com"]}

        custom_email_update_attributes_to_remove_model = {"remove": ["tester3@ibm.com"]}

        subscription_update_attributes_model = {
            "invited": custom_email_update_attributes_invite_model,
            "add_notification_payload": True,
            "reply_to_mail": "reply_to_mail@us.com",
            "reply_to_name": "US News",
            "from_name": "IBM",
            "from_email": "test@test.event-notifications.test.cloud.ibm.com",
            "subscribed": custom_email_update_attributes_to_remove_model,
            "unsubscribed": custom_email_update_attributes_to_remove_model,
            "template_id_invitation": template_invitation_id,
            "template_id_notification": template_notification_id,
        }

        name = "subscription_custom_email update"
        description = "Subscription for custom email updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id16,
            name=name,
            description=description,
            attributes=subscription_update_attributes_model,
        )

        assert update_subscription_response.get_status_code() == 200
        subscription_response = update_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")

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
    def test_send_notifications(self):
        # Construct a dict representation of a NotificationDevices model
        notification_devices_model = {
            "platforms": [
                "push_huawei",
                "push_android",
                "push_ios",
                "push_chrome",
                "push_firefox",
            ]
        }

        # Construct a dict representation of a Lights model
        lights_model = {
            "led_argb": "RED",
            "led_on_ms": 0,
            "led_off_ms": "20",
        }

        # Construct a dict representation of a Style model
        style_model = {
            "type": "picture_notification",
            "title": "hello",
            "url": "url.ibm.com",
        }

        # Construct a dict representation of a NotificationFCMBodyMessageData model
        notification_fcm_body_message_data_model = {
            "android": {
                "notification": {
                    "title": "Alert message",
                    "body": "Bob wants to play Poker",
                },
                "data": {
                    "name": "Robert",
                    "description": "notification for the Poker",
                },
            },
        }

        notification_huawei_body_message_data_model = {
            "android": {
                "notification": {
                    "title": "Alert message",
                    "body": "Bob wants to play Poker",
                },
                "data": {
                    "name": "Robert",
                    "description": "notification for the Poker",
                },
            },
        }

        # Construct a dict representation of a NotificationFCMBodyMessageENData model
        notification_fcm_body_model = {
            "message": notification_fcm_body_message_data_model,
        }

        notification_huawei_body_model = {
            "message": notification_huawei_body_message_data_model,
        }

        # Construct a dict representation of a NotificationAPNSBodyMessageData model
        notification_apns_body_message_data_model = {
            "alert": "Alert message",
            "badge": 38,
            "interactiveCategory": "InteractiveCategory",
            "iosActionKey": "IosActionKey",
            "payload": {"foo": "bar"},
            "sound": "sound.wav",
            "titleLocKey": "TitleLocKey",
            "locKey": "LocKey",
            "launchImage": "image.png",
            "titleLocArgs": ["TitleLocArgs1"],
            "locArgs": ["LocArgs1"],
            "title": "Message Title",
            "subtitle": "Message SubTitle",
            "attachmentUrl": "https://testimage.sub.png",
            "type": "DEFAULT",
            "apnsCollapseId": "ApnsCollapseID",
            "apnsThreadId": "ApnsThreadID",
            "apnsGroupSummaryArg": "ApnsGroupSummaryArg",
            "apnsGroupSummaryArgCount": 38,
        }

        # Construct a dict representation of a NotificationAPNSBodyMessageENData model
        notification_apns_body_model = {
            "en_data": notification_apns_body_message_data_model,
        }

        notification_id = "1234-1234-sdfs-234"
        notification_severity = "MEDIUM"
        type_value = "com.acme.offer:new"
        notifications_source = "1234-1234-sdfs-234:test"

        notificationSafariBodymodel = {
            "saf": {
                "alert": "Game Request",
                "badge": 5,
            },
        }

        htmlbody = (
            '"Hi  ,<br/>Certificate expiring in 90 days.<br/><br/>Please login to '
            '<a href="https: //cloud.ibm.com/security-compliance/dashboard">'
            'Security and Complaince dashboard</a> to find more information<br/>"'
        )
        mailto = '["abc@ibm.com", "def@us.ibm.com"]'

        notification_create_model = {
            "ibmenseverity": notification_severity,
            "ibmenfcmbody": json.dumps(notification_fcm_body_model),
            "ibmenpushto": json.dumps(notification_devices_model),
            "ibmenapnsbody": json.dumps(notification_apns_body_model),
            "ibmenhuaweibody": json.dumps(notification_huawei_body_model),
            "ibmenhtmlbody": htmlbody,
            "ibmensubject": "Findings on IBM Cloud Security Advisor",
            "ibmenmailto": mailto,
            "ibmensourceid": source_id,
            "ibmendefaultshort": "Alert Message",
            "ibmendefaultlong": "Alert for closing offers",
            "ibmensafaribody": json.dumps(notificationSafariBodymodel),
            "id": notification_id,
            "source": notifications_source,
            "type": type_value,
            "specversion": "1.0",
            "time": "2019-01-01T12:00:00.000Z",
        }

        send_notifications_response = self.event_notifications_service.send_notifications(
            instance_id, body=notification_create_model
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

        notification_create_model1 = {
            "ibmenseverity": notification_severity,
            "ibmenfcmbody": json.dumps(notification_fcm_body_model),
            "ibmenpushto": json.dumps(notification_devices_model),
            "ibmenapnsbody": json.dumps(notification_apns_body_model),
            "ibmensourceid": source_id,
            "ibmendefaultshort": "teststring",
            "ibmendefaultlong": "teststring",
            "ibmensafaribody": json.dumps(notificationSafariBodymodel),
            "ibmenapnsheaders": json.dumps(message_apns_headers),
            "id": notification_id,
            "source": notifications_source,
            "type": type_value,
            "specversion": "1.0",
            "time": "2019-01-01T12:00:00.000Z",
        }

        send_notifications_response = self.event_notifications_service.send_notifications(
            instance_id, body=notification_create_model1
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
            "user_ids": ["userId"],
        }

        # Construct a dict representation of a Lights model
        lights_model = {
            "led_argb": "RED",
            "led_on_ms": 0,
            "led_off_ms": "20",
        }

        # Construct a dict representation of a Style model
        style_model = {
            "type": "picture_notification",
            "title": "hello",
            "url": "url.ibm.com",
        }

        # Construct a dict representation of a NotificationFCMBodyMessageData model
        notification_fcm_body_message_data_model = {
            "alert": "Alert message",
            "collapse_key": "collapse_key",
            "interactive_category": "category_test",
            "icon": "test.png",
            "delay_while_idle": True,
            "sync": True,
            "visibility": "0",
            "redact": "redact test alert",
            "payload": {},
            "priority": "MIN",
            "sound": "newSound",
            "time_to_live": 0,
            "lights": lights_model,
            "android_title": "IBM test title",
            "group_id": "Group_ID_1",
            "style": style_model,
            "type": "DEFAULT",
        }

        # Construct a dict representation of a NotificationFCMBodyMessageENData model
        notification_fcm_body_model = {
            "en_data": notification_fcm_body_message_data_model,
        }

        # Construct a dict representation of a NotificationAPNSBodyMessageData model
        notification_apns_body_message_data_model = {
            "alert": "Alert message",
            "badge": 38,
            "interactiveCategory": "InteractiveCategory",
            "iosActionKey": "IosActionKey",
            "payload": {"foo": "bar"},
            "sound": "sound.wav",
            "titleLocKey": "TitleLocKey",
            "locKey": "LocKey",
            "launchImage": "image.png",
            "titleLocArgs": ["TitleLocArgs1"],
            "locArgs": ["LocArgs1"],
            "title": "Message Title",
            "subtitle": "Message SubTitle",
            "attachmentUrl": "https://testimage.sub.png",
            "type": "DEFAULT",
            "apnsCollapseId": "ApnsCollapseID",
            "apnsThreadId": "ApnsThreadID",
            "apnsGroupSummaryArg": "ApnsGroupSummaryArg",
            "apnsGroupSummaryArgCount": 38,
        }

        # Construct a dict representation of a NotificationAPNSBodyMessageENData model
        notification_apns_body_model = {
            "en_data": notification_apns_body_message_data_model,
        }

        message_apns_headers = {
            "apns-collapse-id": "123",
        }

        notification_safari_body_model = {
            "saf": {
                "alert": "Game Request",
                "badge": 5,
            },
        }

        notification_id = "1234-1234-sdfs-234"
        notification_severity = "MEDIUM"
        type_value = "com.acme.offer:new"
        notifications_source = "1234-1234-sdfs-234:test"

        # Construct a dict representation of a NotificationCreate model
        notification_create_model = {
            "ibmenseverity": notification_severity,
            "ibmenfcmbody": json.dumps(notification_fcm_body_model),
            "ibmenpushto": json.dumps(notification_devices_model),
            "ibmenapnsheaders": json.dumps(message_apns_headers),
            "ibmenapnsbody": json.dumps(notification_apns_body_model),
            "ibmensafaribody": json.dumps(notification_safari_body_model),
            "ibmensourceid": source_id,
            "id": notification_id,
            "source": notifications_source,
            "type": type_value,
            "specversion": "1.0",
            "time": "2019-01-01T12:00:00.000Z",
        }

        notification_id1 = "1234-1111-sdfs-234"
        notification_severity1 = "HIGH"
        type_value1 = "com.ibm.cloud.compliance.certificate_manager:certificate_expired"
        notifications_source1 = "1234-1234-sdfs-234:test"

        notification_create_model1 = {
            "ibmenseverity": notification_severity1,
            "ibmenfcmbody": json.dumps(notification_fcm_body_model),
            "ibmenpushto": json.dumps(notification_devices_model),
            "ibmenapnsheaders": json.dumps(message_apns_headers),
            "ibmenapnsbody": json.dumps(notification_apns_body_model),
            "ibmensafaribody": json.dumps(notification_safari_body_model),
            "ibmensourceid": source_id,
            "id": notification_id1,
            "source": notifications_source1,
            "type": type_value1,
            "specversion": "1.0",
            "time": "2019-01-01T12:00:00.000Z",
        }

        send_bulk_notifications_response = self.event_notifications_service.send_bulk_notifications(
            instance_id=instance_id,
            bulk_messages=[notification_create_model, notification_create_model1],
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
        for id in [
            subscription_id,
            subscription_id1,
            subscription_id2,
            subscription_id3,
            subscription_id4,
            subscription_id5,
            subscription_id6,
            subscription_id7,
            subscription_id8,
            subscription_id9,
            subscription_id10,
            subscription_id11,
            subscription_id12,
            subscription_id13,
            subscription_id14,
            subscription_id15,
            subscription_id16,
        ]:
            delete_subscription_response = self.event_notifications_service.delete_subscription(instance_id, id)

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
            delete_topic_response = self.event_notifications_service.delete_topic(instance_id, id)

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
        for id in [
            destination_id,
            destination_id3,
            destination_id4,
            destination_id5,
            destination_id6,
            destination_id7,
            destination_id8,
            destination_id9,
            destination_id10,
            destination_id11,
            destination_id12,
            destination_id13,
            destination_id14,
            destination_id15,
            destination_id16,
        ]:
            delete_destination_response = self.event_notifications_service.delete_destination(instance_id, id)
        print(
            "\ndelete_destination() response status code: ",
            delete_destination_response.get_status_code(),
        )

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #

    @needscredentials
    def test_delete_template(self):
        for id in [template_invitation_id, template_notification_id]:
            delete_template_response = self.event_notifications_service.delete_template(instance_id, id)
        print(
            "\ndelete_template() response status code: ",
            delete_template_response.get_status_code(),
        )

    @needscredentials
    def test_delete_source(self):
        delete_source_response = self.event_notifications_service.delete_source(instance_id, id=source_id)

        assert delete_source_response.get_status_code() == 204

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 401
        # 404
        # 500
        #
