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
config_file = "../event_notifications_v1.env"

event_notifications_service = None

config = None

# EN config values
instance_id = ""
search = ""
topic_name = "Admin Topic Compliance"
source_id = ""
topic_id = ""
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
destination_id17 = ""
destination_id18 = ""
safariCertificatePath = ""
subscription_id = ""
subscription_id1 = ""
subscription_id2 = ""
subscription_id3 = ""
subscription_id4 = ""
subscription_id5 = ""
subscription_id6 = ""
subscription_id7 = ""
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
slack_template_id = ""
template_body = ""
slack_template_body = ""
cos_instance_crn = ""
cos_integration_id = ""
code_engine_project_CRN = ""
smtp_user_id = ""
smtp_config_id = ""
slack_token = ""


##############################################################################
# Start of Examples for Service: EventNotificationsV1
##############################################################################
# region
class TestEventNotificationsV1Examples:
    """
    Example Test Class for EventNotificationsV1
    """

    @classmethod
    def setup_class(cls):
        global instance_id, fcmServerKey, fcmSenderId, safariCertificatePath, fcm_project_id, fcm_private_key, fcm_client_email, code_engine_URL, huawei_client_id, huawei_client_secret, cos_instance_id, cos_end_point, cos_bucket_name, cos_instance_crn, template_body, code_engine_project_CRN, slack_template_body, slack_token
        global event_notifications_service
        if os.path.exists(config_file):
            os.environ["IBM_CREDENTIALS_FILE"] = config_file

            # begin-common

            event_notifications_service = EventNotificationsV1.new_instance()

            # end-common
            assert event_notifications_service is not None

            # Load the configuration
            global config
            config = read_external_sources(EventNotificationsV1.DEFAULT_SERVICE_NAME)

            instance_id = config["GUID"]
            fcmServerKey = config["FCM_KEY"]
            fcmSenderId = config["FCM_ID"]
            safariCertificatePath = config["SAFARI_CERTIFICATE"]
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
            template_body = cls.config["TEMPLATE_BODY"]
            slack_template_body = cls.config["SLACK_TEMPLATE_BODY"]
            code_engine_project_CRN = cls.config["CODE_ENGINE_PROJECT_CRN"]
            slack_token = cls.config["SLACK_TOKEN"]
            assert instance_id is not None
            assert fcmServerKey is not None
            assert fcmSenderId is not None
            assert snow_client_id is not None
            assert snow_client_secret is not None
            assert snow_user_name is not None
            assert snow_password is not None
            assert snow_instance_name is not None
            assert cos_end_point is not None
            assert cos_instance_id is not None
            assert cos_bucket_name is not None
            assert template_body is not None
            assert cos_instance_crn is not None
            assert code_engine_project_CRN is not None
            assert slack_token is not None

        print("Setup complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...",
    )

    @needscredentials
    def test_create_sources_example(self):
        """
        create_sources request example
        """
        global source_id
        try:
            print("\ncreate_sources() result:")
            # begin-create_sources

            source_response = event_notifications_service.create_sources(
                instance_id,
                name="Event Notification Create Source Acme",
                description="This source is used for Acme Bank",
                enabled=False,
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
            print("\nlist_sources() result:")
            # begin-list_sources

            source_list = event_notifications_service.list_sources(instance_id).get_result()

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
            print("\nget_source() result:")
            # begin-get_source

            source = event_notifications_service.get_source(instance_id, id=source_id).get_result()

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
            print("\nupdate_source() result:")
            # begin-update_source

            source = event_notifications_service.update_source(
                instance_id,
                id=source_id,
                name="Event Notification update Source Acme",
                description="This source is used for updated Acme Bank",
                enabled=True,
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
            print("\ncreate_topic() result:")
            # begin-create_topic

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

            topic = event_notifications_service.create_topic(
                instance_id,
                name=topic_name,
                description="This topic is used for routing all compliance related notifications to the appropriate destinations",
                sources=[topic_update_sources_item_model],
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
            print("\nlist_topics() result:")
            # begin-list_topics

            topic_list = event_notifications_service.list_topics(instance_id).get_result()

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
            print("\nget_topic() result:")
            # begin-get_topic

            topic = event_notifications_service.get_topic(instance_id, id=topic_id).get_result()

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
            print("\nreplace_topic() result:")
            # begin-replace_topic

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
            name = "Updated Admin Topic Compliance"
            topic = event_notifications_service.replace_topic(
                instance_id,
                id=topic_id,
                name=name,
                description=description,
                sources=[topic_update_sources_item_model],
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
        global destination_id, destination_id3, destination_id4, destination_id5, destination_id6, destination_id7, destination_id8, destination_id9, destination_id10, destination_id11, destination_id12, destination_id13, destination_id14, destination_id15, destination_id16, destination_id17, destination_id18
        try:
            print("\ncreate_destination() result:")
            # begin-create_destination

            destination_config_params_model = {
                "server_key": fcmServerKey,
                "sender_id": fcmSenderId,
                "pre_prod": False,
            }

            destination_config_model = {
                "params": destination_config_params_model,
            }
            name = "FCM_destination"
            typeVal = "push_android"
            description = "FCM Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeVal,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            destination = DestinationResponse.from_dict(destination)
            destination_id = destination.id

            # Webhook
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

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            destination = DestinationResponse.from_dict(destination)
            destination_id3 = destination.id

            # slack
            slack_config_params = {
                "url": "https://api.slack.com/myslack",
                "token": slack_token,
            }

            destination_config_model = {
                "params": slack_config_params,
            }

            name = "Slack_destination"
            typeval = "slack"
            description = "Slack Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()
            print(json.dumps(destination, indent=2))

            destination = DestinationResponse.from_dict(destination)
            destination_id4 = destination.id

            # Safari
            safari_config_params = {
                "cert_type": "p12",
                "password": "password",
                "website_url": "https://ensafaripush.mybluemix.net",
                "website_name": "NodeJS Starter Application",
                "url_format_string": "https://ensafaripush.mybluemix.net/%@/?flight=%@",
                "website_push_id": "web.net.mybluemix.ensafaripush",
                "pre_prod": False,
            }

            destination_config_model = {
                "params": safari_config_params,
            }

            name = "Safari_destination"
            typeVal = "push_safari"
            description = "Safari Destination"

            certificatefile = open(safariCertificatePath, "rb")
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
                "url": "https://teams.microsoft.com",
            }

            destination_config_model = {
                "params": msteams_config_params,
            }

            name = "MSTeams_destination"
            typeval = "msteams"
            description = "MSteams Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()
            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id6 = destination.id

            # cloud functions
            cf_config_params = {
                "url": "https://www.ibmcfendpoint.com/",
                "api_key": "apikey",
            }

            destination_config_model = {
                "params": cf_config_params,
            }
            name = "Cloud_Functions_destination"
            typeVal = "ibmcf"
            description = "This is a Cloud Functions Destination for actions"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeVal,
                description=description,
                config=destination_config_model,
            ).get_result()
            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id7 = destination.id

            # chrome
            chrome_config_params = {
                "website_url": "https://www.ibmcfendpoint.com/",
                "api_key": "apikey",
            }

            destination_config_model = {
                "params": chrome_config_params,
            }
            name = "Chrome_destination"
            typeval = "push_chrome"
            description = "This is a Chrome Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()
            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id8 = destination.id

            # Firefox
            fire_config_params = {"website_url": "https://cloud.ibm.com"}

            destination_config_model = {
                "params": fire_config_params,
            }
            name = "Firefox_destination"
            typeval = "push_firefox"
            description = "This is a Firefox Destination"

            destination = event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id9 = destination.id

            pd_config_params = {
                "api_key": "insert API Key here",
                "routing_key": "insert Routing Key here",
            }

            destination_config_model = {
                "params": pd_config_params,
            }
            name = "Pager_Duty_destination"
            typeval = "pagerduty"
            description = "This is a PagerDuty Destination"

            destination = event_notifications_service.event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()

            destination = DestinationResponse.from_dict(destination)

            print(json.dumps(destination, indent=2))
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

            destination = self.event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()

            destination = DestinationResponse.from_dict(destination)
            print(json.dumps(destination, indent=2))
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

            destination = DestinationResponse.from_dict(destination_response)

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

            destination = self.event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
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

            destination = self.event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
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

            destination = self.event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
            destination_id15 = destination.id

            destination_config_model = {
                "params": {
                    "domain": "abc.event-notifications.test.cloud.ibm.com",
                }
            }

            name = "custom_email_destination"
            typeval = "smtp_custom"
            description = "Custom Email Destination"

            destination = self.event_notifications_service.create_destination(
                instance_id,
                name,
                type=typeval,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))
            destination = DestinationResponse.from_dict(destination)
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

            destination_response = create_destination_response.get_result()
            destination_id17 = destination_response.get('id')

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

            destination_response = create_destination_response.get_result()
            destination_id18 = destination_response.get('id')

            # end-create_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_destination_example(self):
        """
        test_destination request example
        """
        # begin-test_destination
        try:
            test_destination_response = event_notifications_service.test_destination(instance_id, id=destination_id4)

        except ApiException as e:
            pytest.fail(str(e))
        # end-test_destination

    @needscredentials
    def test_create_template_example(self):
        """
        create_template request example
        """
        global template_notification_id, template_invitation_id, slack_template_id
        try:
            print("\ncreate_template() result:")
            # begin-create_template
            template_config_model_json = {
                'body': template_body,
                'subject': 'Hi this is invitation for invitation message',
            }

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
            ).get_result()

            print(json.dumps(create_template_response, indent=2))
            template = TemplateResponse.from_dict(create_template_response)
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
            ).get_result()

            print(json.dumps(create_template_response, indent=2))
            template = TemplateResponse.from_dict(create_template_response)
            template_notification_id = template.id

            slack_template_config_model_json = {'body': slack_template_body}

            slack_template_config_model = TemplateConfigOneOfSlackTemplateConfig.from_dict(
                slack_template_config_model_json
            )

            name = "template_slack"
            typeval = "slack.notification"
            description = "slack template"

            create_template_response = self.event_notifications_service.create_template(
                instance_id,
                name,
                type=typeval,
                params=slack_template_config_model,
                description=description,
            ).get_result()

            print(json.dumps(create_template_response, indent=2))
            template = TemplateResponse.from_dict(create_template_response)
            slack_template_id = template.id
            # end-create_template

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_templates(self):
        """
        list_templates request example
        """
        more_results = True
        limit = 1
        offset = 0

        while more_results:
            print("\nlist_templates() result:")
            # begin-list_templates
            list_templates_response = self.event_notifications_service.list_templates(
                instance_id, limit=limit, offset=offset, search=search
            )

            templates_list = list_templates_response.get_result()
            # end-list_templates
            assert list_templates_response.get_status_code() == 200
            assert templates_list is not None

            templates = TemplateList.from_dict(templates_list)
            assert templates is not None

            if templates.total_count <= offset:
                more_results = False
            offset += 1

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
            print("\nlist_destinations() result:")
            # begin-list_destinations

            destination_list = event_notifications_service.list_destinations(instance_id).get_result()

            # end-list_destinations
            print(json.dumps(destination_list, indent=2))

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
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_destination_example(self):
        """
        get_destination request example
        """
        try:
            print("\nget_destination() result:")
            # begin-get_destination

            destination = event_notifications_service.get_destination(instance_id, id=destination_id).get_result()

            print(json.dumps(destination, indent=2))

            # end-get_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_template(self):
        """
        get_template request example
        """
        print("\nget_destination() result:")
        # begin-get_template
        get_template_response = event_notifications_service.get_template(
            instance_id, id=template_invitation_id
        ).get_result()

        print(json.dumps(get_template_response, indent=2))
        # end-get_template

    @needscredentials
    def test_update_destination_example(self):
        """
        update_destination request example
        """
        try:
            print("\nupdate_destination() result:")
            # begin-update_destination

            # FCM
            destination_config_params_model = {
                "server_key": fcmServerKey,
                "sender_id": fcmSenderId,
            }

            destination_config_model = {
                "params": destination_config_params_model,
            }
            name = "Admin FCM Compliance"
            description = "This destination is for creating admin FCM to receive compliance notifications"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            # webhook
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
            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id3,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            # Slack
            slack_config_params = {
                "url": "https://api.slack.com/myslack",
                "token": slack_token,
            }

            destination_config_model = {
                "params": slack_config_params,
            }

            name = "Slack_destination_update"
            description = "Slack Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id4,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            # Safari
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
            update_destination_response = event_notifications_service.update_destination(
                instance_id,
                id=destination_id5,
                name=name,
                description=description,
                config=safari_destination_config_model,
                certificate=certificatefile,
            ).get_result()

            print(json.dumps(update_destination_response, indent=2))

            # MSTeams
            msteams_config_params = {
                "url": "https://teams.microsoft.com",
            }

            destination_config_model = {
                "params": msteams_config_params,
            }

            name = "MSTeams_destination_update"
            description = "MSteams Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id6,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            # Cloud Functions
            destination_config_params_model = {
                "url": "https://www.ibmcfendpoint.com/",
                "api_key": "apikey",
            }

            destination_config_model = {
                "params": destination_config_params_model,
            }
            name = "Cloud_Functions_dest"
            description = "This is a Cloud Functions Destination"

            update_destination_response = event_notifications_service.update_destination(
                instance_id,
                id=destination_id7,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(update_destination_response, indent=2))

            # Chrome
            chrome_config_params = {
                "website_url": "https://www.ibmcfendpoint.com/",
                "api_key": "apikey",
            }

            destination_config_model = {
                "params": chrome_config_params,
            }
            name = "Chrome_destination_update"
            description = "This is a Chrome Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id8,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            # Firefox
            fire_config_params = {"website_url": "https://cloud.ibm.com"}

            destination_config_model = {
                "params": fire_config_params,
            }
            name = "Firefox_destination_update"
            description = "This is a Firefox Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id9,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            pd_config_params = {
                "api_key": "insert API Key here",
                "routing_key": "insert Routing Key here",
            }

            destination_config_model = {
                "params": pd_config_params,
            }
            name = "PagerDuty_destination_update"
            description = "This is a PagerDuty Destination update"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id10,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

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

            destination = self.event_notifications_service.update_destination(
                instance_id,
                id=destination_id11,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            # FCM
            destination_config_params_model = {
                "project_id": fcm_project_id,
                "private_key": fcm_private_key,
                "client_email": fcm_client_email,
            }

            destination_config_model = {
                "params": destination_config_params_model,
            }
            name = "Admin FCM Compliance"
            description = "This destination is for creating admin FCM to receive compliance notifications"

            destination = event_notifications_service.update_destination(
                instance_id,
                id=destination_id12,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

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
            destination = self.event_notifications_service.update_destination(
                instance_id,
                id=destination_id13,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            destination_config_model = {
                "params": {
                    "bucket_name": cos_bucket_name,
                    "instance_id": cos_instance_id,
                    "endpoint": cos_end_point,
                }
            }

            name = "COS_destination_update"
            description = "COS Destination update"

            destination = self.event_notifications_service.update_destination(
                instance_id,
                id=destination_id14,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            destination_config_model = {
                "params": {
                    "client_id": huawei_client_id,
                    "client_secret": huawei_client_secret,
                    "pre_prod": False,
                }
            }

            name = "Huawei_destination_update"
            description = "Huawei Destination update"

            destination = self.event_notifications_service.update_destination(
                instance_id,
                id=destination_id15,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            destination_config_model = {"params": {"domain": "abc.event-notifications.test.cloud.ibm.com"}}

            name = "Custom_Email_destination_update"
            description = "Custom Email Destination update"

            destination = self.event_notifications_service.update_destination(
                instance_id,
                id=destination_id16,
                name=name,
                description=description,
                config=destination_config_model,
            ).get_result()

            print(json.dumps(destination, indent=2))

            verification_response = self.event_notifications_service.update_verify_destination(
                instance_id,
                id=destination_id16,
                type="spf/dkim",
            ).get_result()

            print(json.dumps(verification_response, indent=2))

            name = "Custom_SMS_destination_update"
            description = "Custom SMS Destination update"

            destination = self.event_notifications_service.update_destination(
                instance_id,
                id=destination_id17,
                name=name,
                description=description,
            ).get_result()

            print(json.dumps(destination, indent=2))

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
            ).get_result()

            print(json.dumps(destination, indent=2))

            # end-update_destination

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_template_example(self):
        """
        update_template request example
        """
        global template_notification_id, template_invitation_id
        try:
            print("\nupdate_template() result:")
            # begin-replace_template

            template_config_model = {
                "body": template_body,
                "subject": "Hi this is invitation for invitation message",
            }

            template_name = "template_invitation"
            typeval = "smtp_custom.invitation"
            description = "invitation template"

            replace_template_response = self.event_notifications_service.replace_template(
                instance_id,
                id=template_invitation_id,
                name=template_name,
                type=typeval,
                description=description,
                params=template_config_model,
            ).get_result()

            print(json.dumps(replace_template_response, indent=2))

            template_name = "template_notification"
            typeval = "smtp_custom.notification"
            description = "notification template"

            replace_template_response = self.event_notifications_service.replace_template(
                instance_id,
                id=template_notification_id,
                name=template_name,
                type=typeval,
                description=description,
                params=template_config_model,
            ).get_result()

            print(json.dumps(replace_template_response, indent=2))

            slack_template_config_model_json = {'body': slack_template_body}

            slack_template_config_model = TemplateConfigOneOfSlackTemplateConfig.from_dict(
                slack_template_config_model_json
            )

            name = "template_slack"
            typeval = "slack.notification"
            description = "slack template"

            replace_template_response = self.event_notifications_service.replace_template(
                instance_id,
                name,
                type=typeval,
                params=slack_template_config_model,
                description=description,
            ).get_result()

            print(json.dumps(replace_template_response, indent=2))

            # end-replace_template
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_subscription_example(self):
        """
        create_subscription request example
        """
        global subscription_id, subscription_id1, subscription_id2, subscription_id3, subscription_id4, subscription_id5, subscription_id6, subscription_id7
        try:
            print("\ncreate_subscription() result:")
            # begin-create_subscription

            # FCM
            name = "FCM subscription"
            description = "Subscription for the FCM"
            subscription = event_notifications_service.create_subscription(
                instance_id, name, destination_id, topic_id, description=description
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id = subscription.get("id")

            subscription_create_attributes_model = {
                "invited": ["+12064512559", "+12064512559"],
            }

            name = "subscription_sms"
            description = "Subscription for sms"
            subscription = event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id=destination_id1,
                topic_id=topic_id,
                attributes=subscription_create_attributes_model,
                description=description,
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id1 = subscription.get("id")

            # Email
            subscription_create_attributes_model = {
                "invited": ["tester1@gmail.com", "tester3@ibm.com"],
                "add_notification_payload": True,
                "reply_to_mail": "reply_to_mail@us.com",
                "reply_to_name": "US News",
                "from_name": "IBM",
            }

            name = "subscription_email"
            description = "Subscription for email"
            subscription = event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id=destination_id2,
                topic_id=topic_id,
                attributes=subscription_create_attributes_model,
                description=description,
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id2 = subscription.get("id")

            # webhook
            subscription_create_attributes_model = {
                "signing_enabled": False,
            }

            name = "subscription_web"
            description = "Subscription for web"
            subscription = event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id3,
                topic_id,
                attributes=subscription_create_attributes_model,
                description=description,
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id3 = subscription.get("id")

            name = "ServiceNow subscription"
            description = "Subscription for the ServiceNow"

            subscription_create_attributes_model = {
                "assigned_to": "user",
                "assignment_group": "group",
            }

            subscription = self.event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id=destination_id11,
                topic_id=topic_id,
                description=description,
                attributes=subscription_create_attributes_model,
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id4 = subscription.get("id")

            name = "slack subscription"
            description = "Subscription for the slack"

            subscription_create_attributes_model_json = {
                'attachment_color': '#0000FF',
                'template_id_notification': slack_template_id,
                'to': [""],
            }

            subscription_create_attributes_model = SubscriptionCreateAttributesSlackAttributes.from_dict(
                subscription_create_attributes_model_json
            )

            subscription = self.event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id=destination_id4,
                topic_id=topic_id,
                description=description,
                attributes=subscription_create_attributes_model,
            ).get_result()

            print(json.dumps(subscription, indent=2))

            subscription_id5 = subscription.get("id")

            subscription_create_attributes_model = {
                "invited": ["abc@gmail.com", "tester3@ibm.com"],
                "add_notification_payload": True,
                "reply_to_mail": "reply_to_mail@us.com",
                "reply_to_name": "US News",
                "from_name": "IBM",
                "from_email": "test@abc.event-notifications.test.cloud.ibm.com",
                "template_id_invitation": template_invitation_id,
                "template_id_notification": template_notification_id,
            }

            name = "subscription_custom_email"
            description = "Subscription for custom email"
            subscription = self.event_notifications_service.create_subscription(
                instance_id,
                name,
                destination_id=destination_id16,
                topic_id=topic_id,
                attributes=subscription_create_attributes_model,
                description=description,
            ).get_result()

            print(json.dumps(subscription, indent=2))
            subscription_id6 = subscription.get("id")

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
            ).get_result()

            print(json.dumps(create_subscription_response, indent=2))
            subscription_id7 = create_subscription_response.get("id")

        except ApiException as e:
            pytest.fail(str(e))

        # end-create_subscription

    @needscredentials
    def test_list_subscriptions_example(self):
        """
        list_subscriptions request example
        """
        try:
            print("\nlist_subscriptions() result:")
            # begin-list_subscriptions

            subscription_list = event_notifications_service.list_subscriptions(instance_id).get_result()

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
            print("\nget_subscription() result:")
            # begin-get_subscription

            subscription = event_notifications_service.get_subscription(instance_id, id=subscription_id).get_result()

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
            print("\nupdate_subscription() result:")
            # begin-update_subscription

            # FCM
            name = "Update_FCM_subscription"
            description = "Update FCM subscription"
            subscription = event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id,
                name=name,
                description=description,
            ).get_result()

            print(json.dumps(subscription, indent=2))

            # SMS
            sms_update_attributes_invite_model = {"add": ["+12064512559"]}

            sms_update_attributes_toremove_model = {"remove": ["+12064512559"]}

            subscription_update_attributes_model = {
                "invited": sms_update_attributes_invite_model,
                "subscribed": sms_update_attributes_toremove_model,
                "unsubscribed": sms_update_attributes_toremove_model,
            }

            name = "subscription_sms update"
            description = "Subscription for sms updated"
            subscription = self.event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id1,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model,
            ).get_result()
            print(json.dumps(subscription, indent=2))

            # Email
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
                "signing_enabled": True,
            }

            name = "Webhook_sub_updated"
            description = "Update Webhook subscription"
            update_subscription_response = event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id3,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model,
            )

            subscription_response = update_subscription_response.get_result()
            print(json.dumps(subscription_response, indent=2))

            subscription_update_attributes_model = {
                "assigned_to": "user",
                "assignment_group": "group",
            }

            name = "ServiceNow update"
            description = "Subscription for ServiceNow updated"
            update_subscription_response = self.event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id4,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model,
            )

            subscription_response = update_subscription_response.get_result()
            print(json.dumps(subscription_response, indent=2))

            name = "Slack update"
            description = "Subscription for slack updated"
            subscription_update_attributes_model_json = {
                'attachment_color': '#0000FF',
                'template_id_notification': slack_template_id,
                'to': [""],
            }
            subscription_update_attributes_model = SubscriptionUpdateAttributesSlackAttributes.from_dict(
                subscription_update_attributes_model_json
            )
            update_subscription_response = self.event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id5,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model,
            )

            subscription_response = update_subscription_response.get_result()
            print(json.dumps(subscription_response, indent=2))

            custom_email_update_attributes_invite_model = {"add": ["tester4@ibm.com", "abc@gmail.com"]}

            custom_email_update_attributes_to_remove_model = {"remove": ["tester3@ibm.com"]}

            subscription_update_attributes_model = {
                "invited": custom_email_update_attributes_invite_model,
                "add_notification_payload": True,
                "reply_to_mail": "reply_to_mail@us.com",
                "reply_to_name": "US News",
                "from_name": "IBM",
                "from_email": "test@abc.event-notifications.test.cloud.ibm.com",
                "subscribed": custom_email_update_attributes_to_remove_model,
                "unsubscribed": custom_email_update_attributes_to_remove_model,
                "template_id_invitation": template_invitation_id,
                "template_id_notification": template_notification_id,
            }

            name = "subscription_custom_email update"
            description = "Subscription for custom email updated"
            update_subscription_response = self.event_notifications_service.update_subscription(
                instance_id,
                id=subscription_id6,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model,
            )

            subscription_response = update_subscription_response.get_result()
            print(json.dumps(subscription_response, indent=2))

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
                id=subscription_id7,
                name=name,
                description=description,
                attributes=subscription_update_attributes_model,
            )

            subscription_response = update_subscription_response.get_result()
            print(json.dumps(subscription_response, indent=2))

            # end-update_subscription
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_enabled_countries(self):
        # begin-get_enabled_countries
        try:
            get_enabled_countries_response = self.event_notifications_service.get_enabled_countries(
                instance_id, id=destination_id17
            )
            enabled_countries_response = get_enabled_countries_response.get_result()
            print(json.dumps(enabled_countries_response, indent=2))
        except ApiException as e:
            pytest.fail(str(e))
        # end-get_enabled_countries

    @needscredentials
    def test_send_notifications_example(self):
        """
        send_notifications request example
        """
        try:
            print("\nsend_notifications() result:")

            notification_id = "1234-1234-sdfs-234"
            notification_severity = "MEDIUM"
            type_value = "com.acme.offer:new"
            date = "2019-01-01T12:00:00.000Z"
            notifications_source = "1234-1234-sdfs-234:test"
            # begin-send_notifications

            notification_devices_model = {
                "platforms": [
                    "push_huawei",
                    "push_android",
                    "push_ios",
                    "push_chrome",
                    "push_firefox",
                ]
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

            notification_huawei_body_model = {
                "message": notification_huawei_body_message_data_model,
            }

            message_apns_headers = {
                "apns-collapse-id": "123",
            }

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
            smsto = '["+911234567890", "+911224567890"]'
            templates = '["149b0e11-8a7c-4fda-a847-5d79e01b71dc"]'

            notification_create_model = {
                "ibmenseverity": notification_severity,
                "ibmenfcmbody": json.dumps(notification_fcm_body_model),
                "ibmenpushto": json.dumps(notification_devices_model),
                "ibmenapnsbody": json.dumps(notification_apns_body_model),
                "ibmenhuaweibody": json.dumps(notification_huawei_body_model),
                "ibmensourceid": source_id,
                "ibmendefaultshort": "teststring",
                "ibmendefaultlong": "teststring",
                "ibmensafaribody": json.dumps(notificationSafariBodymodel),
                "ibmenhtmlbody": htmlbody,
                "ibmensubject": "Findings on IBM Cloud Security Advisor",
                "ibmenmailto": mailto,
                "ibmensmsto": smsto,
                "ibmentemplates": templates,
                "id": notification_id,
                "source": notifications_source,
                "type": type_value,
                "specversion": "1.0",
                "time": "2019-01-01T12:00:00.000Z",
            }

            send_notifications_response = event_notifications_service.send_notifications(
                instance_id, body=notification_create_model
            ).get_result()

            print(json.dumps(send_notifications_response, indent=2))

            # end-send_notifications

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_smtp_configuration_example(self):
        global template_notification_id, template_invitation_id, slack_template_id
        try:
            print("\ncreate_smtp_configuration() result:")
            # begin-create_smtp_configuration
            global smtp_config_id
            name = "SMTP configuration"
            domain = "mailx.event-notifications.test.cloud.ibm.com"
            description = "SMTP description"

            create_smtp_config_response = self.event_notifications_service.create_smtp_configuration(
                instance_id, name, domain, description=description
            )

            smtp_response = create_smtp_config_response.get_result()
            print(json.dumps(create_smtp_config_response, indent=2))
            smtp_config = SMTPCreateResponse.from_dict(smtp_response)
            smtp_config_id = smtp_config.id
            # end-create_smtp_configuration

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_verify_smtp_example(self):
        try:
            print("\nverify_smtp() result:")
            # begin-update_verify_smtp
            update_verify_smtp_response = self.event_notifications_service.update_verify_smtp(
                instance_id, type="dkim,spf,en_authorization", id=smtp_config_id
            )

            verify_response = update_verify_smtp_response.get_result()
            print(json.dumps(verify_response, indent=2))
            # end-update_verify_smtp

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_smtp_allowed_ips_example(self):
        try:
            print("\n test_update_smtp_allowed_ips_example() result:")
            # begin-update_smtp_allowed_ips
            subnets = ['192.168.1.64']
            update_smtp_allowed_ip_response = self.event_notifications_service.update_smtp_allowed_ips(
                instance_id, id=smtp_config_id, subnets=subnets
            )

            allowed_ip_response = update_smtp_allowed_ip_response.get_result()
            print(json.dumps(allowed_ip_response, indent=2))
            # end-update_smtp_allowed_ips

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_smtp_user_example(self):
        global smtp_user_id
        try:
            print("\n test_create_smtp_user_example() result:")
            # begin-create_smtp_user
            global smtp_user_id
            description = 'SMTP user description'
            create_smtp_user_response = self.event_notifications_service.create_smtp_user(
                instance_id, id=smtp_config_id, description=description
            )

            create_user_response = create_smtp_user_response.get_result()
            print(json.dumps(create_user_response, indent=2))
            smtp_user = SMTPUserResponse.from_dict(create_user_response)
            smtp_user_id = smtp_user.id
            # end-create_smtp_user

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_smtp_configurations_example(self):
        try:
            print("\n test_list_smtp_configurations_example() result:")
            # begin-list_smtp_configurations
            limit = 1
            offset = 0
            list_smtp_config_response = self.event_notifications_service.list_smtp_configurations(
                instance_id,
                limit=limit,
                offset=offset,
                search=search,
            )

            list_smtp_config_response = list_smtp_config_response.get_result()
            print(json.dumps(list_smtp_config_response, indent=2))
            # end-list_smtp_configurations

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_smtp_users_example(self):
        try:
            print("\n test_list_smtp_users_example() result:")
            # begin-list_smtp_users
            limit = 1
            offset = 0
            list_smtp_user_response = self.event_notifications_service.list_smtp_users(
                instance_id,
                id=smtp_config_id,
                limit=limit,
                offset=offset,
                search=search,
            )

            list_smtp_user_response = list_smtp_user_response.get_result()
            print(json.dumps(list_smtp_user_response, indent=2))
            # end-list_smtp_users

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_smtp_configuration_example(self):
        try:
            print("\n test_get_smtp_configuration_example() result:")
            # begin-get_smtp_configuration
            get_smtp_config_response = self.event_notifications_service.get_smtp_configuration(
                instance_id,
                id=smtp_config_id,
            )

            get_smtp_config_response = get_smtp_config_response.get_result()
            print(json.dumps(get_smtp_config_response, indent=2))
            # end-get_smtp_configuration

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_smtp_allowed_ip_example(self):
        try:
            print("\n test_get_smtp_allowed_ip_example() result:")
            # begin-get_smtp_allowed_ips
            get_smtp_allowed_ip_response = self.event_notifications_service.get_smtp_allowed_ips(
                instance_id,
                id=smtp_config_id,
            )

            get_smtp_allowed_ip_response = get_smtp_allowed_ip_response.get_result()
            print(json.dumps(get_smtp_allowed_ip_response, indent=2))
            # end-get_smtp_allowed_ips

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_smtp_user_example(self):
        try:
            print("\n test_get_smtp_user_example() result:")
            # begin-get_smtp_user
            get_smtp_user_response = self.event_notifications_service.get_smtp_user(
                instance_id, id=smtp_config_id, user_id=smtp_user_id
            )

            get_smtp_user_response = get_smtp_user_response.get_result()
            print(json.dumps(get_smtp_user_response, indent=2))
            # end-get_smtp_user

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_smtp_configuration_example(self):
        try:
            print("\n test_update_smtp_configuration_example() result:")
            # begin-update_smtp_configuration
            name = 'SMTP configuration update'
            description = 'SMTP configuration description update'
            update_smtp_config_response = self.event_notifications_service.update_smtp_configuration(
                instance_id,
                id=smtp_config_id,
                name=name,
                description=description,
            )

            update_smtp_config_response = update_smtp_config_response.get_result()
            print(json.dumps(update_smtp_config_response, indent=2))
            # end-update_smtp_configuration

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_smtp_user_example(self):
        try:
            print("\n test_update_smtp_user_example() result:")
            # begin-update_smtp_user
            description = 'SMTP user description update'
            update_smtp_user_response = self.event_notifications_service.update_smtp_user(
                instance_id,
                id=smtp_config_id,
                user_id=smtp_user_id,
                description=description,
            )

            update_smtp_user_response = update_smtp_user_response.get_result()
            print(json.dumps(update_smtp_user_response, indent=2))
            # end-update_smtp_user

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_smtp_user_example(self):
        try:
            print("\n test_delete_smtp_user_example() result:")
            # begin-delete_smtp_user
            delete_smtp_user_response = self.event_notifications_service.delete_smtp_user(
                instance_id, id=smtp_config_id, user_id=smtp_user_id
            )

            print(json.dumps(delete_smtp_user_response, indent=2))
            # end-delete_smtp_user

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_smtp_configuration_example(self):
        try:
            print("\n test_delete_smtp_configuration_example() result:")
            # begin-delete_smtp_configuration
            delete_smtp_config_response = self.event_notifications_service.delete_smtp_configuration(
                instance_id, id=smtp_config_id
            )

            print(json.dumps(delete_smtp_config_response, indent=2))
            # end-delete_smtp_configuration

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_subscription_example(self):
        """
        delete_subscription request example
        """
        try:
            # begin-delete_subscription

            response = event_notifications_service.delete_subscription(instance_id, id=subscription_id)
            # end-delete_subscription
            print(
                "\ndelete_subscription() response status code: ",
                response.get_status_code(),
            )

            for id in [
                subscription_id1,
                subscription_id2,
                subscription_id3,
                subscription_id4,
                subscription_id5,
                subscription_id6,
                subscription_id7,
            ]:
                delete_subscription_response = event_notifications_service.delete_subscription(instance_id, id)
            print(
                "\ndelete_subscription() response status code: ",
                delete_subscription_response.get_status_code(),
            )

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_topic_example(self):
        """
        delete_topic request example
        """
        try:
            # begin-delete_topic

            response = event_notifications_service.delete_topic(instance_id, id=topic_id)

            # end-delete_topic
            print("\ndelete_topic() response status code: ", response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_destination_example(self):
        """
        delete_destination request example
        """
        try:
            # begin-delete_destination

            response = event_notifications_service.delete_destination(instance_id, id=destination_id)

            # end-delete_destination
            print(
                "\ndelete_destination() response status code: ",
                response.get_status_code(),
            )

            for id in [
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
                destination_id17,
                destination_id18,
            ]:
                delete_destination_response = event_notifications_service.delete_destination(instance_id, id)
            print(
                "\ndelete_destination() response status code: ",
                delete_destination_response.get_status_code(),
            )

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_template_example(self):
        """
        delete_template request example
        """
        for id in [template_invitation_id, template_notification_id, slack_template_id]:
            # begin-delete_template
            delete_template_response = event_notifications_service.delete_template(instance_id, id).get_result()
            # end-delete_template
        print(
            "\ndelete_template() response status code: ",
            delete_template_response.get_status_code(),
        )

    @needscredentials
    def test_delete_source_example(self):
        """
        delete_source request example
        """
        try:
            # begin-delete_source

            response = event_notifications_service.delete_source(instance_id, id=source_id)

            # end-delete_source
            print("\ndelete_source() response status code: ", response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_integration(self):
        global cos_integration_id
        try:
            # begin-create_integration
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
            # end-create_integration

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_integrations_example(self):
        global integration_id
        try:
            # begin-list_integrations

            list_integrations_response = event_notifications_service.list_integrations(
                instance_id, limit=1, offset=0, search=search
            )

            integration_response = list_integrations_response.get_result()
            integrations = integration_response.get("integrations")
            integration_id = integrations[0].get("id")
            # end-list_integrations
            print(
                "\nlist_integrations() response status code: ",
                list_integrations_response.get_status_code(),
            )

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_integration_example(self):
        try:
            # begin-get_integration
            get_integration_response = event_notifications_service.get_integration(instance_id, id=integration_id)

            # end-get_integration
            print(
                "\nget_integration() response status code: ",
                get_integration_response.get_status_code(),
            )

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_integration_example(self):
        try:
            # begin-replace_integration

            integration_metadata = {
                "endpoint": "https://private.us-south.kms.cloud.ibm.com",
                "crn": "insert crn",
                "root_key_id": "insert root key id",
            }

            replace_integration_response = event_notifications_service.replace_integration(
                instance_id,
                type="kms/hs-crypto",
                id=integration_id,
                metadata=integration_metadata,
            )

            print(
                "\nupdate_integration() response status code: ",
                replace_integration_response.get_status_code(),
            )

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
            print(
                "\nupdate_integration() response status code: ",
                replace_integration_response.get_status_code(),
            )
            # end-replace_integration

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: EventNotificationsV1
##############################################################################
