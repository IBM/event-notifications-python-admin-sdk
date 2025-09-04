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
from datetime import timezone, timedelta

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
destination_id4 = ""
destination_id5 = ""
destination_id6 = ""
destination_id8 = ""
destination_id9 = ""
destination_id10 = ""
destination_id11 = ""
destination_id12 = ""
destination_id13 = ""
destination_id14 = ""
destination_id15 = ""
destination_id16 = ""
destination_id17 = ""
destination_id18 = ""
destination_id19 = ""
destination_id20 = ""
safariCertificatePath = ""
subscription_id = ""
subscription_id1 = ""
subscription_id2 = ""
subscription_id4 = ""
subscription_id5 = ""
subscription_id6 = ""
subscription_id8 = ""
subscription_id9 = ""
subscription_id10 = ""
subscription_id11 = ""
subscription_id12 = ""
subscription_id13 = ""
subscription_id14 = ""
subscription_id15 = ""
subscription_id16 = ""
subscription_id17 = ""
subscription_id18 = ""
subscription_id19 = ""
subscription_id20 = ""
subscription_id21 = ""
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
code_engine_project_CRN = ""
huawei_client_id = ""
huawei_client_secret = ""
cos_bucket_name = ""
cos_instance_id = ""
cos_end_point = ""
template_invitation_id = ""
template_notification_id = ""
slack_template_id = ""
slack_url = ""
teams_url = ""
pager_duty_api_key = ""
pager_duty_routing_key = ""
template_body = ""
slack_template_body = ""
cos_instance_crn = ""
cos_integration_id = ""
smtp_config_id = ""
smtp_user_id = ""
slack_dm_token = ""
slack_channel_id = ""
webhook_template_id = ""
webhook_template_body = ""
scheduler_source_id = ""
pagerduty_template_body = ""
pagerduty_template_id = ""
event_streams_template_body = ""
event_streams_template_id = ""
event_streams_crn = ""
event_streams_topic = ""
event_streams_endpoint = ""
code_engine_app_template_id = ""
code_engine_job_template_id = ""
code_engine_app_template_body = ""
code_engine_job_template_body = ""


class TestEventNotificationsV1:
    """
    Integration Test Class for EventNotificationsV1
    """

    @classmethod
    def setup_class(cls):
        global instance_id, fcmServerKey, fcmSenderId, safariCertificatePath, fcm_project_id, fcm_private_key, fcm_client_email, huawei_client_id, huawei_client_secret, cos_instance_id, cos_end_point, cos_bucket_name, slack_url, teams_url, pager_duty_api_key, pager_duty_routing_key, template_body, cos_instance_crn, code_engine_project_CRN, slack_template_body, slack_dm_token, slack_channel_id, webhook_template_body, code_engine_URL, snow_client_id, snow_client_secret, snow_user_name, snow_password, snow_instance_name, scheduler_source_id, pagerduty_template_body, event_streams_template_body, event_streams_crn, event_streams_topic, event_streams_endpoint, code_engine_job_template_body, code_engine_app_template_body
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
            cos_instance_crn = cls.config["COS_INSTANCE_CRN"]
            slack_url = cls.config["SLACK_URL"]
            teams_url = cls.config["MS_TEAMS_URL"]
            pager_duty_api_key = cls.config["PD_API_KEY"]
            pager_duty_routing_key = cls.config["PD_ROUTING_KEY"]
            template_body = cls.config["TEMPLATE_BODY"]
            slack_template_body = cls.config["SLACK_TEMPLATE_BODY"]
            code_engine_project_CRN = cls.config["CODE_ENGINE_PROJECT_CRN"]
            slack_dm_token = cls.config["SLACK_DM_TOKEN"]
            slack_channel_id = cls.config["SLACK_CHANNEL_ID"]
            webhook_template_body = cls.config["WEBHOOK_TEMPLATE_BODY"]
            scheduler_source_id = cls.config["SCHEDULER_SOURCE_ID"]
            pagerduty_template_body = cls.config["PAGERDUTY_TEMPLATE_BODY"]
            event_streams_template_body = cls.config["EVENT_STREAMS_TEMPLATE_BODY"]
            event_streams_crn = cls.config["EVENT_STREAMS_CRN"]
            event_streams_endpoint = cls.config["EVENT_STREAMS_ENDPOINT"]
            event_streams_topic = cls.config["EVENT_STREAMS_TOPIC"]
            code_engine_job_template_body = cls.config["CODE_ENGINE_JOB_TEMPLATE_BODY"]
            code_engine_app_template_body = cls.config["CODE_ENGINE_APP_TEMPLATE_BODY"]
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
            assert template_body is not None
            assert cos_instance_crn is not None
            assert code_engine_project_CRN is not None
            assert slack_template_body is not None
            assert slack_dm_token is not None
            assert slack_channel_id is not None
            assert webhook_template_body is not None
            assert scheduler_source_id is not None
            assert pagerduty_template_body is not None
            assert event_streams_template_body is not None
            assert event_streams_crn is not None
            assert event_streams_endpoint is not None
            assert event_streams_topic is not None
            assert code_engine_job_template_body is not None
            assert code_engine_app_template_body is not None

        print("Setup complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...",
    )

    @needscredentials
    def test_create_integration(self):
        global cos_integration_id
        integration_metadata = {
            "endpoint": cos_end_point,
            "crn": cos_instance_crn,
            "bucket_name": cos_bucket_name,
        }

        create_integration_response = self.event_notifications_service.create_integration(
            instance_id,
            type="collect_failed_events",
            metadata=integration_metadata,
        )

        assert create_integration_response.get_status_code() == 201
        integration_response = create_integration_response.get_result()
        integration = IntegrationCreateResponse.from_dict(integration_response)
        cos_integration_id = integration.id
        assert integration_response is not None

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
            "endpoint": cos_end_point,
            "crn": cos_instance_crn,
            "bucket_name": cos_bucket_name,
        }

        replace_integration_response = self.event_notifications_service.replace_integration(
            instance_id,
            id=cos_integration_id,
            type="collect_failed_events",
            metadata=integration_metadata,
        )

        assert replace_integration_response.get_status_code() == 200
        integration_response = replace_integration_response.get_result()
        assert integration_response is not None

    @needscredentials
    def test_create_sources(self):
        global source_id
        create_sources_response = self.event_notifications_service.create_sources(
            instance_id,
            name="Event Notification Create Source Acme",
            description="This source is used for Acme Bank",
            enabled=True,
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
        global topic_id, topic_id2, topic_id3, topic_id4
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

        current_instant = datetime.now(timezone.utc)
        start_date = current_instant.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        end_date = current_instant + timedelta(minutes=1)
        end_formatted_date = end_date.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

        event_schedule_filter_attributes_model = {
            'starts_at': start_date,
            'ends_at': end_formatted_date,
            'expression': '* * * * *',
        }

        rules_model = {
            "enabled": True,
            "event_schedule_filter": event_schedule_filter_attributes_model,
        }

        # Construct a dict representation of a TopicUpdateSourcesItem model
        topic_create_sources_item_model = {
            "id": scheduler_source_id,
            "rules": [rules_model],
        }

        description = "Topic 4 for cron scheduler"
        name = "Scheduler topic4"
        create_topic_response = self.event_notifications_service.create_topic(
            instance_id,
            name=name,
            description=description,
            sources=[topic_create_sources_item_model],
        )

        assert create_topic_response.get_status_code() == 201
        topic_response = create_topic_response.get_result()
        assert topic_response is not None

        topic = TopicResponse.from_dict(topic_response)
        assert topic is not None

        assert topic.name == name
        assert topic.description == description

        topic_id4 = topic.id

        assert topic_id2 is not ""
        assert topic_id is not ""
        assert topic_id3 is not ""
        assert topic_id4 is not ""

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

        list_topics_response = self.event_notifications_service.list_topics(
            instance_id, limit=limit, offset=offset, search=search
        )

        assert list_topics_response.get_status_code() == 200
        topic_list = list_topics_response.get_result()
        assert topic_list is not None

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
        topic_res = replace_topic_response.get_result()
        assert topic_res is not None
        topic = TopicResponse.from_dict(topic_res)
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
        global destination_id, destination_id4, destination_id5, destination_id6, destination_id7, destination_id8, destination_id9, destination_id10, destination_id11, destination_id12, destination_id13, destination_id14, destination_id15, destination_id16, destination_id17, destination_id18, destination_id19, destination_id20
        destination_config_params_model = {
            "url": code_engine_URL,
            "verb": "post",
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

        slack_config_params = {"url": slack_url, "type": "incoming_webhook"}

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
            "type": "application",
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

        name = "custom_sms_destination"
        typeval = "sms_custom"
        description = "Custom sms Destination"

        create_destination_response = self.event_notifications_service.create_destination(
            instance_id,
            name,
            type=typeval,
            description=description,
            collect_failed_events=False,
        )

        assert create_destination_response.get_status_code() == 201
        destination_response = create_destination_response.get_result()
        assert destination_response is not None
        destination_id17 = destination_response.get('id')
        assert destination_response.get('name') == name
        assert destination_response.get('description') == description
        assert destination_response.get('type') == typeval

        destination_config_params_model = {
            "type": "job",
            "project_crn": code_engine_project_CRN,
            "job_name": "custom-job",
        }

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {
            "params": destination_config_params_model,
        }

        name = "code_engine_destination_job"
        typeval = "ibmce"
        description = "code engine Destination job"

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

        destination_id18 = destination.id

        slack_config_params = {"token": slack_dm_token, "type": "direct_message"}

        destination_config_model = {
            "params": slack_config_params,
        }

        name = "Slack_DM_destination"
        typeval = "slack"
        description = "Slack DM Destination"

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

        destination_id19 = destination.id

        destination_config_model = {
            "params": {
                "crn": event_streams_crn,
                "endpoint": event_streams_endpoint,
                "topic": event_streams_topic,
            }
        }

        name = "Event_Streams_destination"
        typeval = "event_streams"
        description = "Event Streams Destination"

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

        destination_id20 = destination.id
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
    def test_webhook_destination(self):
        test_destination_response = self.event_notifications_service.test_destination(instance_id, id=destination_id)
        test_webhook_notification_id = test_destination_response.get_result().get("notification_id")
        assert test_destination_response.get_status_code() == 202

        webhook_notification_status = self.event_notifications_service.get_notifications_status(
            instance_id, id=test_webhook_notification_id
        )
        assert webhook_notification_status.get_status_code() == 200

    @needscredentials
    def test_create_template(self):
        global template_invitation_id, template_notification_id, slack_template_id, webhook_template_id, pagerduty_template_id, event_streams_template_id, code_engine_app_template_id, code_engine_job_template_id

        template_config_model_json = {'body': template_body, 'subject': 'Hi this is invitation for invitation message'}

        template_config_model = TemplateConfigOneOfEmailTemplateConfig.from_dict(template_config_model_json)

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

        slack_template_config_model_json = {'body': slack_template_body}

        slack_template_config_model = TemplateConfigOneOfSlackTemplateConfig.from_dict(slack_template_config_model_json)

        name = "template_slack"
        typeval = "slack.notification"
        description = "slack template"

        create_template_response = self.event_notifications_service.create_template(
            instance_id,
            name,
            type=typeval,
            params=slack_template_config_model,
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

        slack_template_id = template.id

        webhook_template_config_model_json = {'body': webhook_template_body}

        webhook_template_config_model = TemplateConfigOneOfWebhookTemplateConfig.from_dict(
            webhook_template_config_model_json
        )

        name = "template_webhook"
        typeval = "webhook.notification"
        description = "webhook template"

        create_template_response = self.event_notifications_service.create_template(
            instance_id,
            name,
            type=typeval,
            params=webhook_template_config_model,
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

        webhook_template_id = template.id

        pagerduty_template_config_model_json = {'body': pagerduty_template_body}

        pagerduty_template_config_model = TemplateConfigOneOfPagerdutyTemplateConfig.from_dict(
            pagerduty_template_config_model_json
        )

        name = "template_pagerduty"
        typeval = "pagerduty.notification"
        description = "pagerduty template create"

        create_template_response = self.event_notifications_service.create_template(
            instance_id,
            name,
            type=typeval,
            params=pagerduty_template_config_model,
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

        pagerduty_template_id = template.id

        event_streams_template_config_model_json = {'body': event_streams_template_body}

        event_streams_template_config_model = TemplateConfigOneOfEventStreamsTemplateConfig.from_dict(
            event_streams_template_config_model_json
        )

        name = "template_event_streams"
        typeval = "event_streams.notification"
        description = "event streams template create"

        create_template_response = self.event_notifications_service.create_template(
            instance_id,
            name,
            type=typeval,
            params=event_streams_template_config_model,
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

        event_streams_template_id = template.id

        code_engine_app_template_config_model_json = {'body': code_engine_app_template_body}

        code_engine_app_template_config_model = TemplateConfigOneOfCodeEngineApplicationTemplateConfig.from_dict(
            code_engine_app_template_config_model_json
        )

        name = "template_code_engine_app"
        typeval = "ibmceapp.notification"
        description = "code engine app template create"

        create_template_response = self.event_notifications_service.create_template(
            instance_id,
            name,
            type=typeval,
            params=code_engine_app_template_config_model,
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
        code_engine_app_template_id = template.id

        code_engine_job_template_config_model_json = {'body': code_engine_job_template_body}

        code_engine_job_template_config_model = TemplateConfigOneOfCodeEngineJobTemplateConfig.from_dict(
            code_engine_job_template_config_model_json
        )

        name = "template_code_engine_job"
        typeval = "ibmcejob.notification"
        description = "code engine job template create"

        create_template_response = self.event_notifications_service.create_template(
            instance_id,
            name,
            type=typeval,
            params=code_engine_job_template_config_model,
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

        code_engine_job_template_id = template.id

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
            "url": code_engine_URL,
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

        slack_config_params = {"url": slack_url, "type": "incoming_webhook"}

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
            "type": "application",
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

        name = "Custom_SMS_destination_update"
        description = "Custom SMS Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id17,
            name=name,
            description=description,
        )

        assert update_destination_response.get_status_code() == 200
        destination_response = update_destination_response.get_result()
        assert destination_response is not None

        res_id = destination_response.get("id")
        res_name = destination_response.get("name")
        res_description = destination_response.get("description")

        assert res_id == destination_id17
        assert res_name == name
        assert res_description == description

        destination_config_params_model = {
            "type": "job",
            "project_crn": code_engine_project_CRN,
            "job_name": "custom-job",
        }

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {
            "params": destination_config_params_model,
        }

        name = "code engine job updated"
        description = "This destination is updated for code engine job notifications"
        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id18,
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

        assert res_id == destination_id18
        assert res_name == name
        assert res_description == description

        slack_config_params = {"token": slack_dm_token, "type": "direct_message"}

        destination_config_model = {
            "params": slack_config_params,
        }

        name = "Slack_DM_destination_update"
        description = "Slack DM Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id19,
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

        assert res_id == destination_id19
        assert res_name == name
        assert res_description == description

        destination_config_model = {
            "params": {
                "crn": event_streams_crn,
                "endpoint": event_streams_endpoint,
                "topic": event_streams_topic,
            }
        }

        name = "event_streams_destination_update"
        description = "Event Streams Destination update"

        update_destination_response = self.event_notifications_service.update_destination(
            instance_id,
            id=destination_id20,
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

        assert res_id == destination_id20
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
    def test_update_template(self):

        template_config_model_json = {'body': template_body, 'subject': 'Hi this is invitation for invitation message'}

        template_config_model = TemplateConfigOneOfEmailTemplateConfig.from_dict(template_config_model_json)

        template_name = "template_invitation"
        typeval = "smtp_custom.invitation"
        description = "invitation template"

        update_template_response = self.event_notifications_service.replace_template(
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

        update_template_response = self.event_notifications_service.replace_template(
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

        slack_template_config_model_json = {'body': slack_template_body}

        slack_template_config_model = TemplateConfigOneOfSlackTemplateConfig.from_dict(slack_template_config_model_json)

        name = "template_slack"
        typeval = "slack.notification"
        description = "slack template"

        update_template_response = self.event_notifications_service.replace_template(
            instance_id,
            id=slack_template_id,
            name=name,
            description=description,
            type=typeval,
            params=slack_template_config_model,
        )

        assert update_template_response.get_status_code() == 200
        template_response = update_template_response.get_result()

        assert template_response is not None
        assert template_response.get("name") == name
        assert template_response.get("description") == description
        assert template_response.get("type") == typeval
        assert template_response.get("id") == slack_template_id

        webhook_template_config_model_json = {'body': webhook_template_body}

        webhook_template_config_model = TemplateConfigOneOfWebhookTemplateConfig.from_dict(
            webhook_template_config_model_json
        )

        name = "template_webhook"
        typeval = "webhook.notification"
        description = "webhook template"

        update_template_response = self.event_notifications_service.replace_template(
            instance_id,
            id=webhook_template_id,
            name=name,
            description=description,
            type=typeval,
            params=webhook_template_config_model,
        )

        assert update_template_response.get_status_code() == 200
        template_response = update_template_response.get_result()

        assert template_response is not None
        assert template_response.get("name") == name
        assert template_response.get("description") == description
        assert template_response.get("type") == typeval
        assert template_response.get("id") == webhook_template_id

        pagerduty_template_config_model_json = {'body': pagerduty_template_body}

        pagerduty_template_config_model = TemplateConfigOneOfPagerdutyTemplateConfig.from_dict(
            pagerduty_template_config_model_json
        )

        name = "template_pagerduty"
        typeval = "pagerduty.notification"
        description = "pagerduty template"

        update_template_response = self.event_notifications_service.replace_template(
            instance_id,
            id=pagerduty_template_id,
            name=name,
            description=description,
            type=typeval,
            params=pagerduty_template_config_model,
        )

        assert update_template_response.get_status_code() == 200
        template_response = update_template_response.get_result()

        assert template_response is not None
        assert template_response.get("name") == name
        assert template_response.get("description") == description
        assert template_response.get("type") == typeval
        assert template_response.get("id") == pagerduty_template_id

        event_streams_template_config_model_json = {'body': event_streams_template_body}

        event_streams_template_config_model = TemplateConfigOneOfEventStreamsTemplateConfig.from_dict(
            event_streams_template_config_model_json
        )

        name = "template_event_streams"
        typeval = "event_streams.notification"
        description = "event streams template"

        update_template_response = self.event_notifications_service.replace_template(
            instance_id,
            id=event_streams_template_id,
            name=name,
            description=description,
            type=typeval,
            params=event_streams_template_config_model,
        )
        template_response = update_template_response.get_result()
        assert update_template_response.get_status_code() == 200

        assert template_response is not None
        assert template_response.get("name") == name
        assert template_response.get("description") == description
        assert template_response.get("type") == typeval
        assert template_response.get("id") == event_streams_template_id

        code_engine_app_template_config_model_json = {'body': code_engine_app_template_body}

        code_engine_app_template_config_model = TemplateConfigOneOfCodeEngineApplicationTemplateConfig.from_dict(
            code_engine_app_template_config_model_json
        )

        name = "template_code_engine_app_update"
        typeval = "ibmceapp.notification"
        description = "code engine application template"

        update_template_response = self.event_notifications_service.replace_template(
            instance_id,
            id=code_engine_app_template_id,
            name=name,
            description=description,
            type=typeval,
            params=code_engine_app_template_config_model,
        )
        template_response = update_template_response.get_result()
        assert update_template_response.get_status_code() == 200

        assert template_response is not None
        assert template_response.get("name") == name
        assert template_response.get("description") == description
        assert template_response.get("type") == typeval
        assert template_response.get("id") == code_engine_app_template_id

        code_engine_job_template_config_model_json = {'body': code_engine_job_template_body}

        code_engine_job_template_config_model = TemplateConfigOneOfCodeEngineJobTemplateConfig.from_dict(
            code_engine_job_template_config_model_json
        )

        name = "template_code_engine_job_update_template"
        typeval = "ibmceapp.notification"
        description = "code engine job template template"

        update_template_response = self.event_notifications_service.replace_template(
            instance_id,
            id=code_engine_job_template_id,
            name=name,
            description=description,
            type=typeval,
            params=code_engine_job_template_config_model,
        )
        template_response = update_template_response.get_result()
        assert update_template_response.get_status_code() == 200

        assert template_response is not None
        assert template_response.get("name") == name
        assert template_response.get("description") == description
        assert template_response.get("type") == typeval
        assert template_response.get("id") == code_engine_job_template_id

    @needscredentials
    def test_create_subscription(self):
        # Construct a dict representation of a SubscriptionCreateAttributesSMSAttributes model
        global subscription_id, subscription_id1, subscription_id2, subscription_id4, subscription_id5, subscription_id6, subscription_id8, subscription_id9, subscription_id10, subscription_id11, subscription_id12, subscription_id13, subscription_id14, subscription_id15, subscription_id16, subscription_id17, subscription_id18, subscription_id19, subscription_id20, subscription_id21
        subscription_create_attributes_model = {
            "signing_enabled": False,
            "template_id_notification": webhook_template_id,
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

        name = "slack subscription"
        description = "Subscription for the slack"

        subscription_create_attributes_model_json = {
            'attachment_color': '#0000FF',
            'template_id_notification': slack_template_id,
        }

        subscription_create_attributes_model = SubscriptionCreateAttributesSlackAttributes.from_dict(
            subscription_create_attributes_model_json
        )

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

        subscription_create_attributes_model_json = {
            'template_id_notification': pagerduty_template_id,
        }

        subscription_create_attributes_model = SubscriptionCreateAttributesPagerDutyAttributes.from_dict(
            subscription_create_attributes_model_json
        )

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id10,
            topic_id=topic_id,
            description=description,
            attributes=subscription_create_attributes_model,
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

        subscription_create_attributes_model = {'template_id_notification': code_engine_app_template_id}

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
            "invited": ["testuser@in.ibm.com"],
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

        subscription_create_attributes_model = {
            "invited": ["+12064512559", "+12064512559"],
        }

        name = "subscription_custom_sms"
        description = "Subscription for custom sms"
        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id17,
            topic_id=topic_id,
            attributes=subscription_create_attributes_model,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id17 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        subscription_create_attributes_model = {'template_id_notification': code_engine_job_template_id}

        name = "subscription_code_engine_job"
        description = "Subscription for code engine job"
        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id18,
            topic_id,
            attributes=subscription_create_attributes_model,
            description=description,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id18 = subscription_response.get("id")
        assert subscription_name == name
        assert subscription_description == description

        name = "slack DM subscription"
        description = "Subscription for the slack DM"

        channel_create_attributes_model_array = [{'id': slack_channel_id}]

        subscription_create_attributes_model_json = {
            'channels': channel_create_attributes_model_array,
            'template_id_notification': slack_template_id,
        }

        subscription_create_attributes_model = SubscriptionCreateAttributesSlackDirectMessageAttributes.from_dict(
            subscription_create_attributes_model_json
        )

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id19,
            topic_id=topic_id,
            description=description,
            attributes=subscription_create_attributes_model,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        subscription_id19 = subscription_response.get("id")

        assert subscription_name == name
        assert subscription_description == description

        name = "Scheduler subscription"
        description = "Subscription for the Scheduler as a source"

        subscription_create_attributes_model_json = {
            'attachment_color': '#0000FF',
            'template_id_notification': slack_template_id,
        }

        subscription_create_attributes_model = SubscriptionCreateAttributesSlackAttributes.from_dict(
            subscription_create_attributes_model_json
        )

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id4,
            topic_id=topic_id4,
            description=description,
            attributes=subscription_create_attributes_model,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        assert subscription_name == name
        assert subscription_description == description

        subscription_id20 = subscription_response.get("id")

        name = "Event Streams subscription"
        description = "Subscription for the Event Streams"

        subscription_create_attributes_model_json = {
            'template_id_notification': event_streams_template_id,
        }

        subscription_create_attributes_model = SubscriptionCreateAttributesEventstreamsAttributes.from_dict(
            subscription_create_attributes_model_json
        )

        create_subscription_response = self.event_notifications_service.create_subscription(
            instance_id,
            name,
            destination_id=destination_id20,
            topic_id=topic_id4,
            description=description,
            attributes=subscription_create_attributes_model,
        )

        assert create_subscription_response.get_status_code() == 201
        subscription_response = create_subscription_response.get_result()
        assert subscription_response is not None

        subscription_name = subscription_response.get("name")
        subscription_description = subscription_response.get("description")
        assert subscription_name == name
        assert subscription_description == description

        subscription_id21 = subscription_response.get("id")

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
            "template_id_notification": webhook_template_id,
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

        name = "Slack update"
        description = "Subscription for slack updated"

        subscription_update_attributes_model_json = {
            'attachment_color': '#0000FF',
            'template_id_notification': slack_template_id,
        }
        subscription_update_attributes_model = SubscriptionUpdateAttributesSlackAttributes.from_dict(
            subscription_update_attributes_model_json
        )

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

        subscription_update_attributes_model_json = {
            'template_id_notification': pagerduty_template_id,
        }
        subscription_update_attributes_model = SubscriptionUpdateAttributesPagerDutyAttributes.from_dict(
            subscription_update_attributes_model_json
        )

        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id10,
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

        subscription_update_attributes_model = {'template_id_notification': code_engine_app_template_id}

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

        sms_update_attributes_invite_model = {"add": ["+12064512559"]}

        sms_update_attributes_to_remove_model = {"remove": ["+12064512559"]}

        subscription_update_attributes_model = {
            "invited": sms_update_attributes_invite_model,
            "subscribed": sms_update_attributes_to_remove_model,
            "unsubscribed": sms_update_attributes_to_remove_model,
        }

        name = "subscription_custom_sms update"
        description = "Subscription for custom sms updated"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id17,
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

        subscription_update_attributes_model = {'template_id_notification': code_engine_job_template_id}

        name = "code_engine_job_sub_updated"
        description = "Update code engine job subscription"
        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id18,
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
        assert subscription_new_id == subscription_id18
        assert subscription_description == description

        name = "Slack DM subscription update"
        description = "Subscription for slack DM updated"

        channel_update_attributes_model_array = [{'id': slack_channel_id, 'operation': 'add'}]

        subscription_update_attributes_model_json = {
            'channels': channel_update_attributes_model_array,
            'template_id_notification': slack_template_id,
        }

        subscription_update_attributes_model = SubscriptionUpdateAttributesSlackDirectMessageUpdateAttributes.from_dict(
            subscription_update_attributes_model_json
        )

        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id19,
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

        name = "Event Streams subscription update"
        description = "Subscription for Event Streams updated"

        subscription_update_attributes_model_json = {
            'template_id_notification': event_streams_template_id,
        }

        subscription_update_attributes_model = SubscriptionUpdateAttributesEventstreamsAttributes.from_dict(
            subscription_update_attributes_model_json
        )

        update_subscription_response = self.event_notifications_service.update_subscription(
            instance_id,
            id=subscription_id21,
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
    def test_get_enabled_countries(self):
        get_enabled_countries_response = self.event_notifications_service.get_enabled_countries(
            instance_id, id=destination_id17
        )

        assert get_enabled_countries_response.get_status_code() == 200
        destination = get_enabled_countries_response.get_result()
        assert destination is not None

    @needscredentials
    def test_send_notifications(self):

        global notificationID
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

        markdown_content = "**Event Summary** \n\n**Toolchain ID:** `4414af34-a5c7-47d3-8f05-add4af6d78a6`  \n**Content Type:** `application/json`\n\n---\n\n *Pipeline Run Details*\n\n- **Namespace:** `PR`\n- **Trigger Name:** `manual`\n- **Triggered By:** `nitish.kulkarni3@ibm.com`\n- **Build Number:** `343`\n- **Pipeline Link:** [View Pipeline Run](https://cloud.ibm.com/devops/pipelines/tekton/e9cd5aa3-a3f2-4776-8acc-26a35922386e/runs/f29ac6f5-bd2f-4a26-abb8-4249be8dbab7?env_id=ibm:yp:us-south)"
        mailto = '["abc@ibm.com", "def@us.ibm.com"]'
        smsto = '["+911234567890", "+911224567890"]'
        slackto = '["C07FALXBH4G"]'
        mms = '{"content": "iVBORw0KGgoAAAANSUhEUgAAAFoAAAA4CAYAAAB9lO9TAAAAAXNSR0IArs4c6QAAActpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyI+CiAgICAgICAgIDx4bXA6Q3JlYXRvclRvb2w+QWRvYmUgSW1hZ2VSZWFkeTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8dGlmZjpPcmllbnRhdGlvbj4xPC90aWZmOk9yaWVudGF0aW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KKS7NPQAABO9JREFUeAHtW81x2zoQBhgn46NLYCpISpA6cCowfYjn3ZJUELmC5Og4h0AVPKeC8HWgDh5L8DGTTMR8KxoSBCzAX3us8WKGJrg/34KfqF2AkJWSJgwIA8KAMCAMCAPCgDAgDAgDwoAw8LQZ0GfFRT2egrpcmq9zwpkGzx9RXWqllsZ8Nb7GXg+Pq83SfDm3OKlzUVy8B1mfUjYxXRZTPC65ntVKfwOZ/xfFP7Npx1afFkVx0gUTJJ91seNsjvCkXHKKnrLK2k+EZ+GY83oGYlbGmFtXOS7uMRG9h+di2z5ifEefDmmPlQE9zVfxzy3y54puchq8rnT93D7Z4+PusLjoY/GParX+wQH3lJWwn5PPRHgE1dq0evEBRp/JcGxcrZ6fA8YQlt+K4u3rsfgHUgz9W2+uxxQnHxHF9p0vs9fQDS6CFgPFMNs8iVYw7PxnW0imwes/ivuMq1W9VOqZFMH+H8vDe2guJCbmC07eyLLSmKsyrg81aby6Si1E0r4UK8NM76oKo1JhTt0H56FQ1K83Od9qkZ8LpXSuerVwTEecP3LfR05OMq3WdCrpT9eWwgNGicPgYFuLL8Yz3JcLiNnFjfvBIT/TSvCEs43JMKYSusrVH3QxpBtxSXFvbHh/fWp98Y2gfi+Sra9/Zp/olsJS+SBt12m8XSHlcO7Pl4tGMnc82QpP5zxmGZf/XMV1orlXBvCBhe2sePsjlDYSOCTfonF+KTzOvotMK/3dL1y+39C4hA2sqlZ1dG7tx3KvwdEHu1K2cjZ1oOTNrAFz/o+RtYiSeC2+rLpS6pdhNXvCYXFRgHPA4Osf9b+FPpG7s0B3iMUQebN+gzkd3eyIVpdwriIAOeSnER3E+iauE40w8BQYQN4OW2pbCA6XKEKL0CsuSeHFvaIaSh3nfrHhrNNxm+032rWBb875czJMN18qtS6Qxz9yepLRlNRfPR9ijsYrS/0vdlmCghO78RZ5n3y7t2pswd1TR2Ydm0KxZ+hcVE6/YzeJ1xHDN3vxHpKFL92/TsXVK7KlN3N4Ol/v+/FXmPYtG01d4Vw2fe6vu+jh9CK7NwaQcsPWsm2Dt21XVegVl6TxdttgHMJD+DZp6Ljtqd7eN8aUY6x0RFq4LcamjtS2DT6ZS6AvIhFYcQoPDiWOOesIYdoXo6Fvf6Slfd24z/MWW0ox5whjmlBtxfCY7qdsbJu/h1gM3fHTZnC+JxhwcTeDqdKuv2/S+rSWfaLxiFzG3bIyruM1abzo6mwD1uLLB7yTtvhWrjNsaaM3kj5oc8JdiWbl3Xt5F8LtV+6F9B+QAfyu42IxPt5uO2oavO4jsoun/nF3Y7bRYttWNsbOjn6WtsbRveF3HfEVTneYTeI3ZD8RXtfQKxguyHhA3BJuBofT9AmDw+Tm9Yyxc3DC7kEXQ+TVZXhLYyRZQOpUMQ78dx27LaP0lhdHfrh6o/UBZjFz19p/Z9HoMoMPoHTtpP9IGMAP0ePbVt3HqFdLc03TI/wQfQq8dGStnuHt3VXlWvWPuxuzi0N9i4WnNtiSIj0VTeToM+p3bZhHR7drumLADmG3bQq8LZjfqZAiApIbo75x3TH7YfQJJDlmG1RsmaZzCGc4Ojd2wdLZ++EMb7AExmZs/F8rphwKFUC8in01JaZgCQPCgDAgDAgDwoAwIAwIA8KAMCAMPHUG/gKC0oz7fm25ogAAAABJRU5ErkJggg==", "content_type": "image/png"}'
        templates = '["' + slack_template_id + '"]'

        notification_create_model = {
            "ibmenseverity": notification_severity,
            "ibmenfcmbody": json.dumps(notification_fcm_body_model),
            "ibmenpushto": json.dumps(notification_devices_model),
            "ibmenapnsbody": json.dumps(notification_apns_body_model),
            "ibmenhuaweibody": json.dumps(notification_huawei_body_model),
            "ibmenhtmlbody": htmlbody,
            "ibmenmarkdown": markdown_content,
            "ibmensubject": "Findings on IBM Cloud Security Advisor",
            "ibmenmailto": mailto,
            "ibmensmsto": smsto,
            "ibmensmstext": "this is a sample text message",
            "ibmenslackto": slackto,
            "ibmenmms": mms,
            "ibmentemplates": templates,
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
        notificationID = notification_response.get('notification_id')

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
    def test_get_metrics(self):

        destination_type = "smtp_custom"
        gte = "2024-08-01T17:18:43Z"
        lte = "2024-08-02T11:55:22Z"
        email_to = "testuser@in.ibm.com"
        subject = "The Metric Test"

        get_metrics_response = self.event_notifications_service.get_metrics(
            instance_id,
            destination_type,
            gte,
            lte,
            destination_id=destination_id16,
            email_to=email_to,
            notification_id=notificationID,
            subject=subject,
        )

        assert get_metrics_response.get_status_code() == 200
        metric_response = get_metrics_response.get_result()
        assert metric_response is not None

    @needscredentials
    def test_create_smtp_configuration(self):

        global smtp_config_id
        name = "SMTP configuration"
        domain = "test.event-notifications.test.cloud.ibm.com"
        description = "SMTP description"

        create_smtp_config_response = self.event_notifications_service.create_smtp_configuration(
            instance_id, name, domain, description=description
        )

        assert create_smtp_config_response.get_status_code() == 201
        smtp_response = create_smtp_config_response.get_result()
        assert smtp_response is not None

        smtp_config = SMTPCreateResponse.from_dict(smtp_response)

        assert smtp_config is not None
        assert smtp_config.name == name
        assert smtp_config.description == description
        assert smtp_config.domain == domain

        smtp_config_id = smtp_config.id

    @needscredentials
    def test_verify_smtp(self):

        update_verify_smtp_response = self.event_notifications_service.update_verify_smtp(
            instance_id, type="dkim,spf,en_authorization", id=smtp_config_id
        )

        assert update_verify_smtp_response.get_status_code() == 200
        verify_response = update_verify_smtp_response.get_result()
        assert verify_response is not None

        smtp_verify = SMTPVerificationUpdateResponse.from_dict(verify_response)
        assert smtp_verify is not None

    @needscredentials
    def test_update_smtp_allowed_ips(self):

        subnets = ['192.168.1.64']
        update_smtp_allowed_ip_response = self.event_notifications_service.update_smtp_allowed_ips(
            instance_id, id=smtp_config_id, subnets=subnets
        )

        assert update_smtp_allowed_ip_response.get_status_code() == 200
        allowed_ip_response = update_smtp_allowed_ip_response.get_result()
        assert allowed_ip_response is not None

        allowed_ip = SMTPAllowedIPs.from_dict(allowed_ip_response)
        assert allowed_ip.subnets.pop() is not None

    @needscredentials
    def test_create_smtp_user(self):

        global smtp_user_id
        description = 'SMTP user description'
        create_smtp_user_response = self.event_notifications_service.create_smtp_user(
            instance_id, id=smtp_config_id, description=description
        )

        assert create_smtp_user_response.get_status_code() == 201
        create_user_response = create_smtp_user_response.get_result()
        assert create_user_response is not None

        smtp_user = SMTPUserResponse.from_dict(create_user_response)
        assert smtp_user.username is not None
        assert smtp_user.password is not None
        assert smtp_user.description == description
        smtp_user_id = smtp_user.id

    @needscredentials
    def test_list_smtp_configurations(self):

        limit = 1
        offset = 0
        list_smtp_config_response = self.event_notifications_service.list_smtp_configurations(
            instance_id,
            limit=limit,
            offset=offset,
            search=search,
        )

        assert list_smtp_config_response.get_status_code() == 200
        list_smtp_config_response = list_smtp_config_response.get_result()
        assert list_smtp_config_response is not None

        smtp_config_list = SMTPConfigurationsList.from_dict(list_smtp_config_response)
        assert smtp_config_list.total_count == 1

    @needscredentials
    def test_list_smtp_users(self):

        limit = 1
        offset = 0
        list_smtp_user_response = self.event_notifications_service.list_smtp_users(
            instance_id,
            id=smtp_config_id,
            limit=limit,
            offset=offset,
            search=search,
        )

        assert list_smtp_user_response.get_status_code() == 200
        list_smtp_user_response = list_smtp_user_response.get_result()
        assert list_smtp_user_response is not None

        smtp_user_list = SMTPUsersList.from_dict(list_smtp_user_response)
        assert smtp_user_list.total_count == 1

    @needscredentials
    def test_get_smtp_configuration(self):

        get_smtp_config_response = self.event_notifications_service.get_smtp_configuration(
            instance_id,
            id=smtp_config_id,
        )

        assert get_smtp_config_response.get_status_code() == 200
        get_smtp_config_response = get_smtp_config_response.get_result()
        assert get_smtp_config_response is not None

        smtp_config = SMTPConfiguration.from_dict(get_smtp_config_response)
        assert smtp_config is not None
        assert smtp_config.config.dkim is not None
        assert smtp_config.config.spf is not None
        assert smtp_config.config.en_authorization is not None

    @needscredentials
    def test_get_smtp_allowed_ip(self):

        get_smtp_allowed_ip_response = self.event_notifications_service.get_smtp_allowed_ips(
            instance_id,
            id=smtp_config_id,
        )

        assert get_smtp_allowed_ip_response.get_status_code() == 200
        get_smtp_allowed_ip_response = get_smtp_allowed_ip_response.get_result()
        assert get_smtp_allowed_ip_response is not None

        smtp_allowed_ip = SMTPAllowedIPs.from_dict(get_smtp_allowed_ip_response)
        assert smtp_allowed_ip.subnets.pop() is not None

    @needscredentials
    def test_get_smtp_user(self):

        get_smtp_user_response = self.event_notifications_service.get_smtp_user(
            instance_id, id=smtp_config_id, user_id=smtp_user_id
        )

        assert get_smtp_user_response.get_status_code() == 200
        get_smtp_user_response = get_smtp_user_response.get_result()
        assert get_smtp_user_response is not None

        smtp_user = SMTPUser.from_dict(get_smtp_user_response)
        assert smtp_user is not None

    @needscredentials
    def test_update_smtp_configuration(self):

        name = 'SMTP configuration update'
        description = 'SMTP configuration description update'
        update_smtp_config_response = self.event_notifications_service.update_smtp_configuration(
            instance_id,
            id=smtp_config_id,
            name=name,
            description=description,
        )

        assert update_smtp_config_response.get_status_code() == 200
        update_smtp_config_response = update_smtp_config_response.get_result()
        assert update_smtp_config_response is not None

        smtp_config = SMTPConfiguration.from_dict(update_smtp_config_response)
        assert smtp_config is not None
        assert smtp_config.name == name
        assert smtp_config.description == description

    @needscredentials
    def test_update_smtp_user(self):

        description = 'SMTP user description update'
        update_smtp_user_response = self.event_notifications_service.update_smtp_user(
            instance_id,
            id=smtp_config_id,
            user_id=smtp_user_id,
            description=description,
        )

        assert update_smtp_user_response.get_status_code() == 200
        update_smtp_user_response = update_smtp_user_response.get_result()
        assert update_smtp_user_response is not None

        smtp_user = SMTPUser.from_dict(update_smtp_user_response)
        assert smtp_user is not None
        assert smtp_user.description == description

    @needscredentials
    def test_list_predefined_templates(self):

        source = 'logs'
        type = 'slack.notification'
        list_predefined_templates_response = self.event_notifications_service.list_pre_defined_templates(
            instance_id,
            source,
            type,
        )

        assert list_predefined_templates_response.get_status_code() == 200
        list_predefined_templates_response = list_predefined_templates_response.get_result()
        assert list_predefined_templates_response is not None

    @needscredentials
    def test_get_predefined_template(self):

        template_id = '0cacb9a0-d43a-4042-920d-d4a3f7d4cbd5'

        get_predefined_template_response = self.event_notifications_service.get_pre_defined_template(
            instance_id,
            id=template_id,
        )

        assert get_predefined_template_response.get_status_code() == 200
        get_predefined_template_response = get_predefined_template_response.get_result()
        assert get_predefined_template_response is not None

    @needscredentials
    def test_delete_smtp_user(self):
        for id in [
            smtp_user_id,
        ]:
            delete_smtp_user_response = self.event_notifications_service.delete_smtp_user(
                instance_id, id=smtp_config_id, user_id=id
            )
        assert delete_smtp_user_response.get_status_code() == 204

    @needscredentials
    def test_delete_smtp_configuration(self):
        for id in [
            smtp_config_id,
        ]:
            delete_smtp_config_response = self.event_notifications_service.delete_smtp_configuration(
                instance_id, id=smtp_config_id
            )
        assert delete_smtp_config_response.get_status_code() == 204

    @needscredentials
    def test_delete_subscription(self):
        for id in [
            subscription_id,
            subscription_id1,
            subscription_id2,
            subscription_id4,
            subscription_id5,
            subscription_id6,
            subscription_id8,
            subscription_id9,
            subscription_id10,
            subscription_id11,
            subscription_id12,
            subscription_id13,
            subscription_id14,
            subscription_id15,
            subscription_id16,
            subscription_id17,
            subscription_id18,
            subscription_id19,
            subscription_id20,
            subscription_id21,
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
        for id in [topic_id, topic_id2, topic_id3, topic_id4]:
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
            destination_id4,
            destination_id5,
            destination_id6,
            destination_id8,
            destination_id9,
            destination_id10,
            destination_id11,
            destination_id12,
            destination_id13,
            destination_id14,
            destination_id15,
            destination_id16,
            destination_id17,
            destination_id18,
            destination_id19,
            destination_id20,
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
        for id in [
            template_invitation_id,
            template_notification_id,
            slack_template_id,
            webhook_template_id,
            pagerduty_template_id,
            event_streams_template_id,
            code_engine_app_template_id,
            code_engine_job_template_id,
        ]:
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
