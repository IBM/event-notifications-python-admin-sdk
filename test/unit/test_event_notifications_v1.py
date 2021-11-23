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
Unit Tests for EventNotificationsV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import requests
import responses
import urllib
from ibm_eventnotifications.event_notifications_v1 import *


_service = EventNotificationsV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://us-south.event-notifications.cloud.ibm.com/event-notifications'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Sources
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = EventNotificationsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EventNotificationsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EventNotificationsV1.new_instance(
            )

class TestListSources():
    """
    Test Class for list_sources
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_sources_all_params(self):
        """
        list_sources()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/sources')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "sources": [{"id": "id", "name": "name", "description": "description", "type": "type", "enabled": false, "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 0}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        limit = 1
        offset = 0
        search = 'testString'

        # Invoke method
        response = _service.list_sources(
            instance_id,
            limit=limit,
            offset=offset,
            search=search,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'search={}'.format(search) in query_string

    def test_list_sources_all_params_with_retries(self):
        # Enable retries and run test_list_sources_all_params.
        _service.enable_retries()
        self.test_list_sources_all_params()

        # Disable retries and run test_list_sources_all_params.
        _service.disable_retries()
        self.test_list_sources_all_params()

    @responses.activate
    def test_list_sources_required_params(self):
        """
        test_list_sources_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/sources')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "sources": [{"id": "id", "name": "name", "description": "description", "type": "type", "enabled": false, "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 0}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_sources(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_sources_required_params_with_retries(self):
        # Enable retries and run test_list_sources_required_params.
        _service.enable_retries()
        self.test_list_sources_required_params()

        # Disable retries and run test_list_sources_required_params.
        _service.disable_retries()
        self.test_list_sources_required_params()

    @responses.activate
    def test_list_sources_value_error(self):
        """
        test_list_sources_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/sources')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "sources": [{"id": "id", "name": "name", "description": "description", "type": "type", "enabled": false, "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 0}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_sources(**req_copy)


    def test_list_sources_value_error_with_retries(self):
        # Enable retries and run test_list_sources_value_error.
        _service.enable_retries()
        self.test_list_sources_value_error()

        # Disable retries and run test_list_sources_value_error.
        _service.disable_retries()
        self.test_list_sources_value_error()

class TestGetSource():
    """
    Test Class for get_source
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_source_all_params(self):
        """
        get_source()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/sources/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "enabled": false, "type": "type", "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 11, "topic_names": ["topic_names"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_source(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_source_all_params_with_retries(self):
        # Enable retries and run test_get_source_all_params.
        _service.enable_retries()
        self.test_get_source_all_params()

        # Disable retries and run test_get_source_all_params.
        _service.disable_retries()
        self.test_get_source_all_params()

    @responses.activate
    def test_get_source_value_error(self):
        """
        test_get_source_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/sources/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "enabled": false, "type": "type", "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 11, "topic_names": ["topic_names"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_source(**req_copy)


    def test_get_source_value_error_with_retries(self):
        # Enable retries and run test_get_source_value_error.
        _service.enable_retries()
        self.test_get_source_value_error()

        # Disable retries and run test_get_source_value_error.
        _service.disable_retries()
        self.test_get_source_value_error()

# endregion
##############################################################################
# End of Service: Sources
##############################################################################

##############################################################################
# Start of Service: Topics
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = EventNotificationsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EventNotificationsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EventNotificationsV1.new_instance(
            )

class TestCreateTopic():
    """
    Test Class for create_topic
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_topic_all_params(self):
        """
        create_topic()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "created_at"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Rules model
        rules_model = {}
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.notification_event_info.event_type == \'cert_manager\''
        rules_model['notification_filter'] = '$.notification.findings[0].severity == \'MODERATE\''

        # Construct a dict representation of a TopicUpdateSourcesItem model
        topic_update_sources_item_model = {}
        topic_update_sources_item_model['id'] = 'e7c3b3ee-78d9-4e02-95c3-c001a05e6ea5:api'
        topic_update_sources_item_model['rules'] = [rules_model]

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        description = 'testString'
        sources = [topic_update_sources_item_model]

        # Invoke method
        response = _service.create_topic(
            instance_id,
            name,
            description=description,
            sources=sources,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['sources'] == [topic_update_sources_item_model]

    def test_create_topic_all_params_with_retries(self):
        # Enable retries and run test_create_topic_all_params.
        _service.enable_retries()
        self.test_create_topic_all_params()

        # Disable retries and run test_create_topic_all_params.
        _service.disable_retries()
        self.test_create_topic_all_params()

    @responses.activate
    def test_create_topic_value_error(self):
        """
        test_create_topic_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics')
        mock_response = '{"id": "id", "name": "name", "description": "description", "created_at": "created_at"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Rules model
        rules_model = {}
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.notification_event_info.event_type == \'cert_manager\''
        rules_model['notification_filter'] = '$.notification.findings[0].severity == \'MODERATE\''

        # Construct a dict representation of a TopicUpdateSourcesItem model
        topic_update_sources_item_model = {}
        topic_update_sources_item_model['id'] = 'e7c3b3ee-78d9-4e02-95c3-c001a05e6ea5:api'
        topic_update_sources_item_model['rules'] = [rules_model]

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        description = 'testString'
        sources = [topic_update_sources_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_topic(**req_copy)


    def test_create_topic_value_error_with_retries(self):
        # Enable retries and run test_create_topic_value_error.
        _service.enable_retries()
        self.test_create_topic_value_error()

        # Disable retries and run test_create_topic_value_error.
        _service.disable_retries()
        self.test_create_topic_value_error()

class TestListTopics():
    """
    Test Class for list_topics
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_topics_all_params(self):
        """
        list_topics()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "topics": [{"id": "id", "name": "name", "description": "description", "source_count": 0, "sources_names": ["sources_names"], "subscription_count": 0}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        limit = 1
        offset = 0
        search = 'testString'

        # Invoke method
        response = _service.list_topics(
            instance_id,
            limit=limit,
            offset=offset,
            search=search,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'search={}'.format(search) in query_string

    def test_list_topics_all_params_with_retries(self):
        # Enable retries and run test_list_topics_all_params.
        _service.enable_retries()
        self.test_list_topics_all_params()

        # Disable retries and run test_list_topics_all_params.
        _service.disable_retries()
        self.test_list_topics_all_params()

    @responses.activate
    def test_list_topics_required_params(self):
        """
        test_list_topics_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "topics": [{"id": "id", "name": "name", "description": "description", "source_count": 0, "sources_names": ["sources_names"], "subscription_count": 0}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_topics(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_topics_required_params_with_retries(self):
        # Enable retries and run test_list_topics_required_params.
        _service.enable_retries()
        self.test_list_topics_required_params()

        # Disable retries and run test_list_topics_required_params.
        _service.disable_retries()
        self.test_list_topics_required_params()

    @responses.activate
    def test_list_topics_value_error(self):
        """
        test_list_topics_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "topics": [{"id": "id", "name": "name", "description": "description", "source_count": 0, "sources_names": ["sources_names"], "subscription_count": 0}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_topics(**req_copy)


    def test_list_topics_value_error_with_retries(self):
        # Enable retries and run test_list_topics_value_error.
        _service.enable_retries()
        self.test_list_topics_value_error()

        # Disable retries and run test_list_topics_value_error.
        _service.disable_retries()
        self.test_list_topics_value_error()

class TestGetTopic():
    """
    Test Class for get_topic
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_topic_all_params(self):
        """
        get_topic()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics/testString')
        mock_response = '{"id": "id", "description": "description", "name": "name", "updated_at": "updated_at", "source_count": 12, "sources": [{"id": "id", "name": "name", "rules": [{"enabled": false, "event_type_filter": "$.*", "notification_filter": "notification_filter", "updated_at": "updated_at", "id": "id"}]}], "subscription_count": 18, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        include = 'testString'

        # Invoke method
        response = _service.get_topic(
            instance_id,
            id,
            include=include,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include={}'.format(include) in query_string

    def test_get_topic_all_params_with_retries(self):
        # Enable retries and run test_get_topic_all_params.
        _service.enable_retries()
        self.test_get_topic_all_params()

        # Disable retries and run test_get_topic_all_params.
        _service.disable_retries()
        self.test_get_topic_all_params()

    @responses.activate
    def test_get_topic_required_params(self):
        """
        test_get_topic_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics/testString')
        mock_response = '{"id": "id", "description": "description", "name": "name", "updated_at": "updated_at", "source_count": 12, "sources": [{"id": "id", "name": "name", "rules": [{"enabled": false, "event_type_filter": "$.*", "notification_filter": "notification_filter", "updated_at": "updated_at", "id": "id"}]}], "subscription_count": 18, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_topic(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_topic_required_params_with_retries(self):
        # Enable retries and run test_get_topic_required_params.
        _service.enable_retries()
        self.test_get_topic_required_params()

        # Disable retries and run test_get_topic_required_params.
        _service.disable_retries()
        self.test_get_topic_required_params()

    @responses.activate
    def test_get_topic_value_error(self):
        """
        test_get_topic_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics/testString')
        mock_response = '{"id": "id", "description": "description", "name": "name", "updated_at": "updated_at", "source_count": 12, "sources": [{"id": "id", "name": "name", "rules": [{"enabled": false, "event_type_filter": "$.*", "notification_filter": "notification_filter", "updated_at": "updated_at", "id": "id"}]}], "subscription_count": 18, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_topic(**req_copy)


    def test_get_topic_value_error_with_retries(self):
        # Enable retries and run test_get_topic_value_error.
        _service.enable_retries()
        self.test_get_topic_value_error()

        # Disable retries and run test_get_topic_value_error.
        _service.disable_retries()
        self.test_get_topic_value_error()

class TestReplaceTopic():
    """
    Test Class for replace_topic
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_replace_topic_all_params(self):
        """
        replace_topic()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics/testString')
        mock_response = '{"id": "id", "description": "description", "name": "name", "updated_at": "updated_at", "source_count": 12, "sources": [{"id": "id", "name": "name", "rules": [{"enabled": false, "event_type_filter": "$.*", "notification_filter": "notification_filter", "updated_at": "updated_at", "id": "id"}]}], "subscription_count": 18, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Rules model
        rules_model = {}
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.notification_event_info.event_type == \'cert_manager\''
        rules_model['notification_filter'] = '$.notification.findings[0].severity == \'MODERATE\''

        # Construct a dict representation of a TopicUpdateSourcesItem model
        topic_update_sources_item_model = {}
        topic_update_sources_item_model['id'] = 'e7c3b3ee-78d9-4e02-95c3-c001a05e6ea5:api'
        topic_update_sources_item_model['rules'] = [rules_model]

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        sources = [topic_update_sources_item_model]

        # Invoke method
        response = _service.replace_topic(
            instance_id,
            id,
            name=name,
            description=description,
            sources=sources,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['sources'] == [topic_update_sources_item_model]

    def test_replace_topic_all_params_with_retries(self):
        # Enable retries and run test_replace_topic_all_params.
        _service.enable_retries()
        self.test_replace_topic_all_params()

        # Disable retries and run test_replace_topic_all_params.
        _service.disable_retries()
        self.test_replace_topic_all_params()

    @responses.activate
    def test_replace_topic_value_error(self):
        """
        test_replace_topic_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics/testString')
        mock_response = '{"id": "id", "description": "description", "name": "name", "updated_at": "updated_at", "source_count": 12, "sources": [{"id": "id", "name": "name", "rules": [{"enabled": false, "event_type_filter": "$.*", "notification_filter": "notification_filter", "updated_at": "updated_at", "id": "id"}]}], "subscription_count": 18, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Rules model
        rules_model = {}
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.notification_event_info.event_type == \'cert_manager\''
        rules_model['notification_filter'] = '$.notification.findings[0].severity == \'MODERATE\''

        # Construct a dict representation of a TopicUpdateSourcesItem model
        topic_update_sources_item_model = {}
        topic_update_sources_item_model['id'] = 'e7c3b3ee-78d9-4e02-95c3-c001a05e6ea5:api'
        topic_update_sources_item_model['rules'] = [rules_model]

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        sources = [topic_update_sources_item_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_topic(**req_copy)


    def test_replace_topic_value_error_with_retries(self):
        # Enable retries and run test_replace_topic_value_error.
        _service.enable_retries()
        self.test_replace_topic_value_error()

        # Disable retries and run test_replace_topic_value_error.
        _service.disable_retries()
        self.test_replace_topic_value_error()

class TestDeleteTopic():
    """
    Test Class for delete_topic
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_topic_all_params(self):
        """
        delete_topic()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_topic(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_topic_all_params_with_retries(self):
        # Enable retries and run test_delete_topic_all_params.
        _service.enable_retries()
        self.test_delete_topic_all_params()

        # Disable retries and run test_delete_topic_all_params.
        _service.disable_retries()
        self.test_delete_topic_all_params()

    @responses.activate
    def test_delete_topic_value_error(self):
        """
        test_delete_topic_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/topics/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_topic(**req_copy)


    def test_delete_topic_value_error_with_retries(self):
        # Enable retries and run test_delete_topic_value_error.
        _service.enable_retries()
        self.test_delete_topic_value_error()

        # Disable retries and run test_delete_topic_value_error.
        _service.disable_retries()
        self.test_delete_topic_value_error()

# endregion
##############################################################################
# End of Service: Topics
##############################################################################

##############################################################################
# Start of Service: Destinations
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = EventNotificationsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EventNotificationsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EventNotificationsV1.new_instance(
            )

class TestCreateDestination():
    """
    Test Class for create_destination
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_destination_all_params(self):
        """
        create_destination()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
        destination_config_params_model = {}
        destination_config_params_model['url'] = 'testString'
        destination_config_params_model['verb'] = 'get'
        destination_config_params_model['custom_headers'] = {}
        destination_config_params_model['sensitive_headers'] = ['testString']

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {}
        destination_config_model['params'] = destination_config_params_model

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        type = 'webhook'
        description = 'testString'
        config = destination_config_model

        # Invoke method
        response = _service.create_destination(
            instance_id,
            name,
            type,
            description=description,
            config=config,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['type'] == 'webhook'
        assert req_body['description'] == 'testString'
        assert req_body['config'] == destination_config_model

    def test_create_destination_all_params_with_retries(self):
        # Enable retries and run test_create_destination_all_params.
        _service.enable_retries()
        self.test_create_destination_all_params()

        # Disable retries and run test_create_destination_all_params.
        _service.disable_retries()
        self.test_create_destination_all_params()

    @responses.activate
    def test_create_destination_value_error(self):
        """
        test_create_destination_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
        destination_config_params_model = {}
        destination_config_params_model['url'] = 'testString'
        destination_config_params_model['verb'] = 'get'
        destination_config_params_model['custom_headers'] = {}
        destination_config_params_model['sensitive_headers'] = ['testString']

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {}
        destination_config_model['params'] = destination_config_params_model

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        type = 'webhook'
        description = 'testString'
        config = destination_config_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "name": name,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_destination(**req_copy)


    def test_create_destination_value_error_with_retries(self):
        # Enable retries and run test_create_destination_value_error.
        _service.enable_retries()
        self.test_create_destination_value_error()

        # Disable retries and run test_create_destination_value_error.
        _service.disable_retries()
        self.test_create_destination_value_error()

class TestListDestinations():
    """
    Test Class for list_destinations
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_destinations_all_params(self):
        """
        list_destinations()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "destinations": [{"id": "id", "name": "name", "description": "description", "type": "webhook", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        limit = 1
        offset = 0
        search = 'testString'

        # Invoke method
        response = _service.list_destinations(
            instance_id,
            limit=limit,
            offset=offset,
            search=search,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'search={}'.format(search) in query_string

    def test_list_destinations_all_params_with_retries(self):
        # Enable retries and run test_list_destinations_all_params.
        _service.enable_retries()
        self.test_list_destinations_all_params()

        # Disable retries and run test_list_destinations_all_params.
        _service.disable_retries()
        self.test_list_destinations_all_params()

    @responses.activate
    def test_list_destinations_required_params(self):
        """
        test_list_destinations_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "destinations": [{"id": "id", "name": "name", "description": "description", "type": "webhook", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_destinations(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_destinations_required_params_with_retries(self):
        # Enable retries and run test_list_destinations_required_params.
        _service.enable_retries()
        self.test_list_destinations_required_params()

        # Disable retries and run test_list_destinations_required_params.
        _service.disable_retries()
        self.test_list_destinations_required_params()

    @responses.activate
    def test_list_destinations_value_error(self):
        """
        test_list_destinations_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "destinations": [{"id": "id", "name": "name", "description": "description", "type": "webhook", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_destinations(**req_copy)


    def test_list_destinations_value_error_with_retries(self):
        # Enable retries and run test_list_destinations_value_error.
        _service.enable_retries()
        self.test_list_destinations_value_error()

        # Disable retries and run test_list_destinations_value_error.
        _service.disable_retries()
        self.test_list_destinations_value_error()

class TestGetDestination():
    """
    Test Class for get_destination
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_destination_all_params(self):
        """
        get_destination()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_destination(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_destination_all_params_with_retries(self):
        # Enable retries and run test_get_destination_all_params.
        _service.enable_retries()
        self.test_get_destination_all_params()

        # Disable retries and run test_get_destination_all_params.
        _service.disable_retries()
        self.test_get_destination_all_params()

    @responses.activate
    def test_get_destination_value_error(self):
        """
        test_get_destination_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_destination(**req_copy)


    def test_get_destination_value_error_with_retries(self):
        # Enable retries and run test_get_destination_value_error.
        _service.enable_retries()
        self.test_get_destination_value_error()

        # Disable retries and run test_get_destination_value_error.
        _service.disable_retries()
        self.test_get_destination_value_error()

class TestUpdateDestination():
    """
    Test Class for update_destination
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_destination_all_params(self):
        """
        update_destination()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
        destination_config_params_model = {}
        destination_config_params_model['url'] = 'testString'
        destination_config_params_model['verb'] = 'get'
        destination_config_params_model['custom_headers'] = {}
        destination_config_params_model['sensitive_headers'] = ['testString']

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {}
        destination_config_model['params'] = destination_config_params_model

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        config = destination_config_model

        # Invoke method
        response = _service.update_destination(
            instance_id,
            id,
            name=name,
            description=description,
            config=config,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['config'] == destination_config_model

    def test_update_destination_all_params_with_retries(self):
        # Enable retries and run test_update_destination_all_params.
        _service.enable_retries()
        self.test_update_destination_all_params()

        # Disable retries and run test_update_destination_all_params.
        _service.disable_retries()
        self.test_update_destination_all_params()

    @responses.activate
    def test_update_destination_value_error(self):
        """
        test_update_destination_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
        destination_config_params_model = {}
        destination_config_params_model['url'] = 'testString'
        destination_config_params_model['verb'] = 'get'
        destination_config_params_model['custom_headers'] = {}
        destination_config_params_model['sensitive_headers'] = ['testString']

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {}
        destination_config_model['params'] = destination_config_params_model

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        config = destination_config_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_destination(**req_copy)


    def test_update_destination_value_error_with_retries(self):
        # Enable retries and run test_update_destination_value_error.
        _service.enable_retries()
        self.test_update_destination_value_error()

        # Disable retries and run test_update_destination_value_error.
        _service.disable_retries()
        self.test_update_destination_value_error()

class TestDeleteDestination():
    """
    Test Class for delete_destination
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_destination_all_params(self):
        """
        delete_destination()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_destination(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_destination_all_params_with_retries(self):
        # Enable retries and run test_delete_destination_all_params.
        _service.enable_retries()
        self.test_delete_destination_all_params()

        # Disable retries and run test_delete_destination_all_params.
        _service.disable_retries()
        self.test_delete_destination_all_params()

    @responses.activate
    def test_delete_destination_value_error(self):
        """
        test_delete_destination_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/destinations/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_destination(**req_copy)


    def test_delete_destination_value_error_with_retries(self):
        # Enable retries and run test_delete_destination_value_error.
        _service.enable_retries()
        self.test_delete_destination_value_error()

        # Disable retries and run test_delete_destination_value_error.
        _service.disable_retries()
        self.test_delete_destination_value_error()

# endregion
##############################################################################
# End of Service: Destinations
##############################################################################

##############################################################################
# Start of Service: Subscriptions
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = EventNotificationsV1.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, EventNotificationsV1)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = EventNotificationsV1.new_instance(
            )

class TestCreateSubscription():
    """
    Test Class for create_subscription
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_subscription_all_params(self):
        """
        create_subscription()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"to": ["to"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a SubscriptionCreateAttributesSMSAttributes model
        subscription_create_attributes_model = {}
        subscription_create_attributes_model['to'] = ['testString']

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        destination_id = 'testString'
        topic_id = 'testString'
        attributes = subscription_create_attributes_model
        description = 'testString'

        # Invoke method
        response = _service.create_subscription(
            instance_id,
            name,
            destination_id,
            topic_id,
            attributes,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['destination_id'] == 'testString'
        assert req_body['topic_id'] == 'testString'
        assert req_body['attributes'] == subscription_create_attributes_model
        assert req_body['description'] == 'testString'

    def test_create_subscription_all_params_with_retries(self):
        # Enable retries and run test_create_subscription_all_params.
        _service.enable_retries()
        self.test_create_subscription_all_params()

        # Disable retries and run test_create_subscription_all_params.
        _service.disable_retries()
        self.test_create_subscription_all_params()

    @responses.activate
    def test_create_subscription_value_error(self):
        """
        test_create_subscription_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"to": ["to"]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a SubscriptionCreateAttributesSMSAttributes model
        subscription_create_attributes_model = {}
        subscription_create_attributes_model['to'] = ['testString']

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        destination_id = 'testString'
        topic_id = 'testString'
        attributes = subscription_create_attributes_model
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "name": name,
            "destination_id": destination_id,
            "topic_id": topic_id,
            "attributes": attributes,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_subscription(**req_copy)


    def test_create_subscription_value_error_with_retries(self):
        # Enable retries and run test_create_subscription_value_error.
        _service.enable_retries()
        self.test_create_subscription_value_error()

        # Disable retries and run test_create_subscription_value_error.
        _service.disable_retries()
        self.test_create_subscription_value_error()

class TestListSubscriptions():
    """
    Test Class for list_subscriptions
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_subscriptions_all_params(self):
        """
        list_subscriptions()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        offset = 0
        limit = 1
        search = 'testString'

        # Invoke method
        response = _service.list_subscriptions(
            instance_id,
            offset=offset,
            limit=limit,
            search=search,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'search={}'.format(search) in query_string

    def test_list_subscriptions_all_params_with_retries(self):
        # Enable retries and run test_list_subscriptions_all_params.
        _service.enable_retries()
        self.test_list_subscriptions_all_params()

        # Disable retries and run test_list_subscriptions_all_params.
        _service.disable_retries()
        self.test_list_subscriptions_all_params()

    @responses.activate
    def test_list_subscriptions_required_params(self):
        """
        test_list_subscriptions_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_subscriptions(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_subscriptions_required_params_with_retries(self):
        # Enable retries and run test_list_subscriptions_required_params.
        _service.enable_retries()
        self.test_list_subscriptions_required_params()

        # Disable retries and run test_list_subscriptions_required_params.
        _service.disable_retries()
        self.test_list_subscriptions_required_params()

    @responses.activate
    def test_list_subscriptions_value_error(self):
        """
        test_list_subscriptions_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_subscriptions(**req_copy)


    def test_list_subscriptions_value_error_with_retries(self):
        # Enable retries and run test_list_subscriptions_value_error.
        _service.enable_retries()
        self.test_list_subscriptions_value_error()

        # Disable retries and run test_list_subscriptions_value_error.
        _service.disable_retries()
        self.test_list_subscriptions_value_error()

class TestGetSubscription():
    """
    Test Class for get_subscription
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_subscription_all_params(self):
        """
        get_subscription()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"to": ["to"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_subscription(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_subscription_all_params_with_retries(self):
        # Enable retries and run test_get_subscription_all_params.
        _service.enable_retries()
        self.test_get_subscription_all_params()

        # Disable retries and run test_get_subscription_all_params.
        _service.disable_retries()
        self.test_get_subscription_all_params()

    @responses.activate
    def test_get_subscription_value_error(self):
        """
        test_get_subscription_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"to": ["to"]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_subscription(**req_copy)


    def test_get_subscription_value_error_with_retries(self):
        # Enable retries and run test_get_subscription_value_error.
        _service.enable_retries()
        self.test_get_subscription_value_error()

        # Disable retries and run test_get_subscription_value_error.
        _service.disable_retries()
        self.test_get_subscription_value_error()

class TestDeleteSubscription():
    """
    Test Class for delete_subscription
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_subscription_all_params(self):
        """
        delete_subscription()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_subscription(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_subscription_all_params_with_retries(self):
        # Enable retries and run test_delete_subscription_all_params.
        _service.enable_retries()
        self.test_delete_subscription_all_params()

        # Disable retries and run test_delete_subscription_all_params.
        _service.disable_retries()
        self.test_delete_subscription_all_params()

    @responses.activate
    def test_delete_subscription_value_error(self):
        """
        test_delete_subscription_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_subscription(**req_copy)


    def test_delete_subscription_value_error_with_retries(self):
        # Enable retries and run test_delete_subscription_value_error.
        _service.enable_retries()
        self.test_delete_subscription_value_error()

        # Disable retries and run test_delete_subscription_value_error.
        _service.disable_retries()
        self.test_delete_subscription_value_error()

class TestUpdateSubscription():
    """
    Test Class for update_subscription
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_subscription_all_params(self):
        """
        update_subscription()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"to": ["to"]}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SubscriptionUpdateAttributesSMSAttributes model
        subscription_update_attributes_model = {}
        subscription_update_attributes_model['to'] = ['testString']

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        attributes = subscription_update_attributes_model

        # Invoke method
        response = _service.update_subscription(
            instance_id,
            id,
            name=name,
            description=description,
            attributes=attributes,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['attributes'] == subscription_update_attributes_model

    def test_update_subscription_all_params_with_retries(self):
        # Enable retries and run test_update_subscription_all_params.
        _service.enable_retries()
        self.test_update_subscription_all_params()

        # Disable retries and run test_update_subscription_all_params.
        _service.disable_retries()
        self.test_update_subscription_all_params()

    @responses.activate
    def test_update_subscription_value_error(self):
        """
        test_update_subscription_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/instances/testString/subscriptions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"to": ["to"]}}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a SubscriptionUpdateAttributesSMSAttributes model
        subscription_update_attributes_model = {}
        subscription_update_attributes_model['to'] = ['testString']

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        attributes = subscription_update_attributes_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_subscription(**req_copy)


    def test_update_subscription_value_error_with_retries(self):
        # Enable retries and run test_update_subscription_value_error.
        _service.enable_retries()
        self.test_update_subscription_value_error()

        # Disable retries and run test_update_subscription_value_error.
        _service.disable_retries()
        self.test_update_subscription_value_error()

# endregion
##############################################################################
# End of Service: Subscriptions
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Destination():
    """
    Test Class for Destination
    """

    def test_destination_serialization(self):
        """
        Test serialization/deserialization for Destination
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_config_params_model = {} # DestinationConfigParamsWebhookDestinationConfig
        destination_config_params_model['url'] = 'https://cloud.ibm.com/nhwebhook/sendwebhook'
        destination_config_params_model['verb'] = 'post'
        destination_config_params_model['custom_headers'] = {}
        destination_config_params_model['sensitive_headers'] = ['authorization']

        destination_config_model = {} # DestinationConfig
        destination_config_model['params'] = destination_config_params_model

        # Construct a json representation of a Destination model
        destination_model_json = {}
        destination_model_json['id'] = 'testString'
        destination_model_json['name'] = 'testString'
        destination_model_json['description'] = 'testString'
        destination_model_json['type'] = 'webhook'
        destination_model_json['config'] = destination_config_model
        destination_model_json['updated_at'] = "2019-01-01T12:00:00Z"
        destination_model_json['subscription_count'] = 0
        destination_model_json['subscription_names'] = ['testString']

        # Construct a model instance of Destination by calling from_dict on the json representation
        destination_model = Destination.from_dict(destination_model_json)
        assert destination_model != False

        # Construct a model instance of Destination by calling from_dict on the json representation
        destination_model_dict = Destination.from_dict(destination_model_json).__dict__
        destination_model2 = Destination(**destination_model_dict)

        # Verify the model instances are equivalent
        assert destination_model == destination_model2

        # Convert model instance back to dict and verify no loss of data
        destination_model_json2 = destination_model.to_dict()
        assert destination_model_json2 == destination_model_json

class TestModel_DestinationConfig():
    """
    Test Class for DestinationConfig
    """

    def test_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfig
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_config_params_model = {} # DestinationConfigParamsWebhookDestinationConfig
        destination_config_params_model['url'] = 'https://1ea472c0.us-south.apigw.appdomain.cloud/nhwebhook/sendwebhook'
        destination_config_params_model['verb'] = 'post'
        destination_config_params_model['custom_headers'] = {}
        destination_config_params_model['sensitive_headers'] = ['authorization']

        # Construct a json representation of a DestinationConfig model
        destination_config_model_json = {}
        destination_config_model_json['params'] = destination_config_params_model

        # Construct a model instance of DestinationConfig by calling from_dict on the json representation
        destination_config_model = DestinationConfig.from_dict(destination_config_model_json)
        assert destination_config_model != False

        # Construct a model instance of DestinationConfig by calling from_dict on the json representation
        destination_config_model_dict = DestinationConfig.from_dict(destination_config_model_json).__dict__
        destination_config_model2 = DestinationConfig(**destination_config_model_dict)

        # Verify the model instances are equivalent
        assert destination_config_model == destination_config_model2

        # Convert model instance back to dict and verify no loss of data
        destination_config_model_json2 = destination_config_model.to_dict()
        assert destination_config_model_json2 == destination_config_model_json

class TestModel_DestinationLisItem():
    """
    Test Class for DestinationLisItem
    """

    def test_destination_lis_item_serialization(self):
        """
        Test serialization/deserialization for DestinationLisItem
        """

        # Construct a json representation of a DestinationLisItem model
        destination_lis_item_model_json = {}
        destination_lis_item_model_json['id'] = 'testString'
        destination_lis_item_model_json['name'] = 'testString'
        destination_lis_item_model_json['description'] = 'testString'
        destination_lis_item_model_json['type'] = 'webhook'
        destination_lis_item_model_json['subscription_count'] = 38
        destination_lis_item_model_json['subscription_names'] = ['testString']
        destination_lis_item_model_json['updated_at'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of DestinationLisItem by calling from_dict on the json representation
        destination_lis_item_model = DestinationLisItem.from_dict(destination_lis_item_model_json)
        assert destination_lis_item_model != False

        # Construct a model instance of DestinationLisItem by calling from_dict on the json representation
        destination_lis_item_model_dict = DestinationLisItem.from_dict(destination_lis_item_model_json).__dict__
        destination_lis_item_model2 = DestinationLisItem(**destination_lis_item_model_dict)

        # Verify the model instances are equivalent
        assert destination_lis_item_model == destination_lis_item_model2

        # Convert model instance back to dict and verify no loss of data
        destination_lis_item_model_json2 = destination_lis_item_model.to_dict()
        assert destination_lis_item_model_json2 == destination_lis_item_model_json

class TestModel_DestinationList():
    """
    Test Class for DestinationList
    """

    def test_destination_list_serialization(self):
        """
        Test serialization/deserialization for DestinationList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_lis_item_model = {} # DestinationLisItem
        destination_lis_item_model['id'] = '11fe18ba-d0c8-4108-9f07-355e8052a813'
        destination_lis_item_model['name'] = 'Slack Webhook'
        destination_lis_item_model['description'] = 'This destination is for webhook purpose new'
        destination_lis_item_model['type'] = 'webhook'
        destination_lis_item_model['subscription_count'] = 2
        destination_lis_item_model['subscription_names'] = ['Webhook Sub for new change']
        destination_lis_item_model['updated_at'] = "2021-09-05T00:25:19.599000Z"

        # Construct a json representation of a DestinationList model
        destination_list_model_json = {}
        destination_list_model_json['total_count'] = 38
        destination_list_model_json['offset'] = 38
        destination_list_model_json['limit'] = 38
        destination_list_model_json['destinations'] = [destination_lis_item_model]

        # Construct a model instance of DestinationList by calling from_dict on the json representation
        destination_list_model = DestinationList.from_dict(destination_list_model_json)
        assert destination_list_model != False

        # Construct a model instance of DestinationList by calling from_dict on the json representation
        destination_list_model_dict = DestinationList.from_dict(destination_list_model_json).__dict__
        destination_list_model2 = DestinationList(**destination_list_model_dict)

        # Verify the model instances are equivalent
        assert destination_list_model == destination_list_model2

        # Convert model instance back to dict and verify no loss of data
        destination_list_model_json2 = destination_list_model.to_dict()
        assert destination_list_model_json2 == destination_list_model_json

class TestModel_DestinationResponse():
    """
    Test Class for DestinationResponse
    """

    def test_destination_response_serialization(self):
        """
        Test serialization/deserialization for DestinationResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_config_params_model = {} # DestinationConfigParamsWebhookDestinationConfig
        destination_config_params_model['url'] = 'https://cloud.ibm.com/nhwebhook/sendwebhook'
        destination_config_params_model['verb'] = 'post'
        destination_config_params_model['custom_headers'] = {}
        destination_config_params_model['sensitive_headers'] = ['authorization']

        destination_config_model = {} # DestinationConfig
        destination_config_model['params'] = destination_config_params_model

        # Construct a json representation of a DestinationResponse model
        destination_response_model_json = {}
        destination_response_model_json['id'] = 'testString'
        destination_response_model_json['name'] = 'testString'
        destination_response_model_json['description'] = 'testString'
        destination_response_model_json['type'] = 'webhook'
        destination_response_model_json['config'] = destination_config_model
        destination_response_model_json['created_at'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of DestinationResponse by calling from_dict on the json representation
        destination_response_model = DestinationResponse.from_dict(destination_response_model_json)
        assert destination_response_model != False

        # Construct a model instance of DestinationResponse by calling from_dict on the json representation
        destination_response_model_dict = DestinationResponse.from_dict(destination_response_model_json).__dict__
        destination_response_model2 = DestinationResponse(**destination_response_model_dict)

        # Verify the model instances are equivalent
        assert destination_response_model == destination_response_model2

        # Convert model instance back to dict and verify no loss of data
        destination_response_model_json2 = destination_response_model.to_dict()
        assert destination_response_model_json2 == destination_response_model_json

class TestModel_Rules():
    """
    Test Class for Rules
    """

    def test_rules_serialization(self):
        """
        Test serialization/deserialization for Rules
        """

        # Construct a json representation of a Rules model
        rules_model_json = {}
        rules_model_json['enabled'] = True
        rules_model_json['event_type_filter'] = '$.*'
        rules_model_json['notification_filter'] = 'testString'

        # Construct a model instance of Rules by calling from_dict on the json representation
        rules_model = Rules.from_dict(rules_model_json)
        assert rules_model != False

        # Construct a model instance of Rules by calling from_dict on the json representation
        rules_model_dict = Rules.from_dict(rules_model_json).__dict__
        rules_model2 = Rules(**rules_model_dict)

        # Verify the model instances are equivalent
        assert rules_model == rules_model2

        # Convert model instance back to dict and verify no loss of data
        rules_model_json2 = rules_model.to_dict()
        assert rules_model_json2 == rules_model_json

class TestModel_RulesGet():
    """
    Test Class for RulesGet
    """

    def test_rules_get_serialization(self):
        """
        Test serialization/deserialization for RulesGet
        """

        # Construct a json representation of a RulesGet model
        rules_get_model_json = {}
        rules_get_model_json['enabled'] = True
        rules_get_model_json['event_type_filter'] = '$.*'
        rules_get_model_json['notification_filter'] = 'testString'
        rules_get_model_json['updated_at'] = 'testString'
        rules_get_model_json['id'] = 'testString'

        # Construct a model instance of RulesGet by calling from_dict on the json representation
        rules_get_model = RulesGet.from_dict(rules_get_model_json)
        assert rules_get_model != False

        # Construct a model instance of RulesGet by calling from_dict on the json representation
        rules_get_model_dict = RulesGet.from_dict(rules_get_model_json).__dict__
        rules_get_model2 = RulesGet(**rules_get_model_dict)

        # Verify the model instances are equivalent
        assert rules_get_model == rules_get_model2

        # Convert model instance back to dict and verify no loss of data
        rules_get_model_json2 = rules_get_model.to_dict()
        assert rules_get_model_json2 == rules_get_model_json

class TestModel_Source():
    """
    Test Class for Source
    """

    def test_source_serialization(self):
        """
        Test serialization/deserialization for Source
        """

        # Construct a json representation of a Source model
        source_model_json = {}
        source_model_json['id'] = 'testString'
        source_model_json['name'] = 'testString'
        source_model_json['description'] = 'testString'
        source_model_json['enabled'] = True
        source_model_json['type'] = 'testString'
        source_model_json['updated_at'] = "2019-01-01T12:00:00Z"
        source_model_json['topic_count'] = 38
        source_model_json['topic_names'] = ['testString']

        # Construct a model instance of Source by calling from_dict on the json representation
        source_model = Source.from_dict(source_model_json)
        assert source_model != False

        # Construct a model instance of Source by calling from_dict on the json representation
        source_model_dict = Source.from_dict(source_model_json).__dict__
        source_model2 = Source(**source_model_dict)

        # Verify the model instances are equivalent
        assert source_model == source_model2

        # Convert model instance back to dict and verify no loss of data
        source_model_json2 = source_model.to_dict()
        assert source_model_json2 == source_model_json

class TestModel_SourceList():
    """
    Test Class for SourceList
    """

    def test_source_list_serialization(self):
        """
        Test serialization/deserialization for SourceList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        sources_list_item_model = {} # SourcesListItem
        sources_list_item_model['id'] = '00bb34e5-b8c1-4159-af15-8bc6980c3ab2:api'
        sources_list_item_model['name'] = 'CloudEvents Source'
        sources_list_item_model['description'] = 'This source is related cloud events'
        sources_list_item_model['type'] = 'api'
        sources_list_item_model['enabled'] = True
        sources_list_item_model['updated_at'] = "2021-08-19T05:30:03.696000Z"
        sources_list_item_model['topic_count'] = 0

        # Construct a json representation of a SourceList model
        source_list_model_json = {}
        source_list_model_json['total_count'] = 0
        source_list_model_json['offset'] = 38
        source_list_model_json['limit'] = 38
        source_list_model_json['sources'] = [sources_list_item_model]

        # Construct a model instance of SourceList by calling from_dict on the json representation
        source_list_model = SourceList.from_dict(source_list_model_json)
        assert source_list_model != False

        # Construct a model instance of SourceList by calling from_dict on the json representation
        source_list_model_dict = SourceList.from_dict(source_list_model_json).__dict__
        source_list_model2 = SourceList(**source_list_model_dict)

        # Verify the model instances are equivalent
        assert source_list_model == source_list_model2

        # Convert model instance back to dict and verify no loss of data
        source_list_model_json2 = source_list_model.to_dict()
        assert source_list_model_json2 == source_list_model_json

class TestModel_SourcesListItem():
    """
    Test Class for SourcesListItem
    """

    def test_sources_list_item_serialization(self):
        """
        Test serialization/deserialization for SourcesListItem
        """

        # Construct a json representation of a SourcesListItem model
        sources_list_item_model_json = {}
        sources_list_item_model_json['id'] = 'testString'
        sources_list_item_model_json['name'] = 'testString'
        sources_list_item_model_json['description'] = 'testString'
        sources_list_item_model_json['type'] = 'testString'
        sources_list_item_model_json['enabled'] = True
        sources_list_item_model_json['updated_at'] = "2019-01-01T12:00:00Z"
        sources_list_item_model_json['topic_count'] = 0

        # Construct a model instance of SourcesListItem by calling from_dict on the json representation
        sources_list_item_model = SourcesListItem.from_dict(sources_list_item_model_json)
        assert sources_list_item_model != False

        # Construct a model instance of SourcesListItem by calling from_dict on the json representation
        sources_list_item_model_dict = SourcesListItem.from_dict(sources_list_item_model_json).__dict__
        sources_list_item_model2 = SourcesListItem(**sources_list_item_model_dict)

        # Verify the model instances are equivalent
        assert sources_list_item_model == sources_list_item_model2

        # Convert model instance back to dict and verify no loss of data
        sources_list_item_model_json2 = sources_list_item_model.to_dict()
        assert sources_list_item_model_json2 == sources_list_item_model_json

class TestModel_Subscription():
    """
    Test Class for Subscription
    """

    def test_subscription_serialization(self):
        """
        Test serialization/deserialization for Subscription
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subscription_attributes_model = {} # SubscriptionAttributesEmailAttributesResponse
        subscription_attributes_model['to'] = ['example1@gmail.com', 'example2@gmail.com.com']
        subscription_attributes_model['add_notification_payload'] = True
        subscription_attributes_model['reply_to_mail'] = 'example@ibm.com'
        subscription_attributes_model['reply_to_name'] = 'USA news'
        subscription_attributes_model['from_name'] = 'IBM'

        # Construct a json representation of a Subscription model
        subscription_model_json = {}
        subscription_model_json['id'] = 'testString'
        subscription_model_json['name'] = 'testString'
        subscription_model_json['description'] = 'testString'
        subscription_model_json['updated_at'] = 'testString'
        subscription_model_json['from'] = 'testString'
        subscription_model_json['destination_type'] = 'sms_ibm'
        subscription_model_json['destination_id'] = 'testString'
        subscription_model_json['destination_name'] = 'testString'
        subscription_model_json['topic_id'] = 'testString'
        subscription_model_json['topic_name'] = 'testString'
        subscription_model_json['attributes'] = subscription_attributes_model
        subscription_model_json['foo'] = 'testString'

        # Construct a model instance of Subscription by calling from_dict on the json representation
        subscription_model = Subscription.from_dict(subscription_model_json)
        assert subscription_model != False

        # Construct a model instance of Subscription by calling from_dict on the json representation
        subscription_model_dict = Subscription.from_dict(subscription_model_json).__dict__
        subscription_model2 = Subscription(**subscription_model_dict)

        # Verify the model instances are equivalent
        assert subscription_model == subscription_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_model_json2 = subscription_model.to_dict()
        assert subscription_model_json2 == subscription_model_json

        # Test get_properties and set_properties methods.
        subscription_model.set_properties({})
        actual_dict = subscription_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_model.set_properties(expected_dict)
        actual_dict = subscription_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_SubscriptionList():
    """
    Test Class for SubscriptionList
    """

    def test_subscription_list_serialization(self):
        """
        Test serialization/deserialization for SubscriptionList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subscription_list_item_model = {} # SubscriptionListItem
        subscription_list_item_model['id'] = '60502ac0-5748-40b1-84b8-938b77f1c8d1'
        subscription_list_item_model['name'] = 'Test subscription'
        subscription_list_item_model['description'] = 'Developers of EN'
        subscription_list_item_model['destination_id'] = 'b5cb3f03-ff12-42f3-9fae-37ee27f2a81a'
        subscription_list_item_model['destination_name'] = 'Developers Email destination'
        subscription_list_item_model['destination_type'] = 'smtp_ibm'
        subscription_list_item_model['topic_id'] = '33d2b8d5-8ab8-46c7-97b9-c508afbf0701'
        subscription_list_item_model['topic_name'] = 'Developers topic'
        subscription_list_item_model['updated_at'] = "2021-08-18T09:50:32.133000Z"

        # Construct a json representation of a SubscriptionList model
        subscription_list_model_json = {}
        subscription_list_model_json['total_count'] = 0
        subscription_list_model_json['offset'] = 38
        subscription_list_model_json['limit'] = 38
        subscription_list_model_json['subscriptions'] = [subscription_list_item_model]

        # Construct a model instance of SubscriptionList by calling from_dict on the json representation
        subscription_list_model = SubscriptionList.from_dict(subscription_list_model_json)
        assert subscription_list_model != False

        # Construct a model instance of SubscriptionList by calling from_dict on the json representation
        subscription_list_model_dict = SubscriptionList.from_dict(subscription_list_model_json).__dict__
        subscription_list_model2 = SubscriptionList(**subscription_list_model_dict)

        # Verify the model instances are equivalent
        assert subscription_list_model == subscription_list_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_list_model_json2 = subscription_list_model.to_dict()
        assert subscription_list_model_json2 == subscription_list_model_json

class TestModel_SubscriptionListItem():
    """
    Test Class for SubscriptionListItem
    """

    def test_subscription_list_item_serialization(self):
        """
        Test serialization/deserialization for SubscriptionListItem
        """

        # Construct a json representation of a SubscriptionListItem model
        subscription_list_item_model_json = {}
        subscription_list_item_model_json['id'] = 'testString'
        subscription_list_item_model_json['name'] = 'testString'
        subscription_list_item_model_json['description'] = 'testString'
        subscription_list_item_model_json['destination_id'] = 'testString'
        subscription_list_item_model_json['destination_name'] = 'testString'
        subscription_list_item_model_json['destination_type'] = 'sms_ibm'
        subscription_list_item_model_json['topic_id'] = 'testString'
        subscription_list_item_model_json['topic_name'] = 'testString'
        subscription_list_item_model_json['updated_at'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of SubscriptionListItem by calling from_dict on the json representation
        subscription_list_item_model = SubscriptionListItem.from_dict(subscription_list_item_model_json)
        assert subscription_list_item_model != False

        # Construct a model instance of SubscriptionListItem by calling from_dict on the json representation
        subscription_list_item_model_dict = SubscriptionListItem.from_dict(subscription_list_item_model_json).__dict__
        subscription_list_item_model2 = SubscriptionListItem(**subscription_list_item_model_dict)

        # Verify the model instances are equivalent
        assert subscription_list_item_model == subscription_list_item_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_list_item_model_json2 = subscription_list_item_model.to_dict()
        assert subscription_list_item_model_json2 == subscription_list_item_model_json

class TestModel_Topic():
    """
    Test Class for Topic
    """

    def test_topic_serialization(self):
        """
        Test serialization/deserialization for Topic
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_get_model = {} # RulesGet
        rules_get_model['enabled'] = True
        rules_get_model['event_type_filter'] = '$.notification_event_info.event_type == \'test\''
        rules_get_model['notification_filter'] = '$.notification.findings[0].severity == \'LOW\''
        rules_get_model['updated_at'] = '2021-09-08T13:25:20.523533Z'
        rules_get_model['id'] = '218f4e30-9af2-4f70-b38b-738f923b0c4b'

        topic_sources_item_model = {} # TopicSourcesItem
        topic_sources_item_model['id'] = '96dbf538-9fa7-4745-b9e4-32bb6f1dc47a:api'
        topic_sources_item_model['name'] = 'Compliance source'
        topic_sources_item_model['rules'] = [rules_get_model]

        subscription_list_item_model = {} # SubscriptionListItem
        subscription_list_item_model['id'] = '87bef75e-f826-4aa9-b64d-91af9be5e12b'
        subscription_list_item_model['name'] = 'SMS Subscription on new change'
        subscription_list_item_model['description'] = 'This subscription is to send events from SCC to EN Admins via sms'
        subscription_list_item_model['destination_id'] = 'ec28efee-2236-4c2d-8839-d34f697cfc69'
        subscription_list_item_model['destination_name'] = 'testString'
        subscription_list_item_model['destination_type'] = 'sms_ibm'
        subscription_list_item_model['topic_id'] = '7b23362d-6d48-47ef-847a-c8b291220306'
        subscription_list_item_model['topic_name'] = 'testString'
        subscription_list_item_model['updated_at'] = "2021-08-20T10:08:46.060000Z"

        # Construct a json representation of a Topic model
        topic_model_json = {}
        topic_model_json['id'] = 'testString'
        topic_model_json['description'] = 'testString'
        topic_model_json['name'] = 'testString'
        topic_model_json['updated_at'] = 'testString'
        topic_model_json['source_count'] = 38
        topic_model_json['sources'] = [topic_sources_item_model]
        topic_model_json['subscription_count'] = 38
        topic_model_json['subscriptions'] = [subscription_list_item_model]

        # Construct a model instance of Topic by calling from_dict on the json representation
        topic_model = Topic.from_dict(topic_model_json)
        assert topic_model != False

        # Construct a model instance of Topic by calling from_dict on the json representation
        topic_model_dict = Topic.from_dict(topic_model_json).__dict__
        topic_model2 = Topic(**topic_model_dict)

        # Verify the model instances are equivalent
        assert topic_model == topic_model2

        # Convert model instance back to dict and verify no loss of data
        topic_model_json2 = topic_model.to_dict()
        assert topic_model_json2 == topic_model_json

class TestModel_TopicList():
    """
    Test Class for TopicList
    """

    def test_topic_list_serialization(self):
        """
        Test serialization/deserialization for TopicList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        topics_list_item_model = {} # TopicsListItem
        topics_list_item_model['id'] = '33d2b8d5-8ab8-46c7-97b9-c508afbf0701'
        topics_list_item_model['name'] = 'Developers topic'
        topics_list_item_model['description'] = 'To send events to all EN developers'
        topics_list_item_model['source_count'] = 2
        topics_list_item_model['sources_names'] = ['Push Source', 'Custom source']
        topics_list_item_model['subscription_count'] = 3

        # Construct a json representation of a TopicList model
        topic_list_model_json = {}
        topic_list_model_json['total_count'] = 0
        topic_list_model_json['offset'] = 38
        topic_list_model_json['limit'] = 38
        topic_list_model_json['topics'] = [topics_list_item_model]

        # Construct a model instance of TopicList by calling from_dict on the json representation
        topic_list_model = TopicList.from_dict(topic_list_model_json)
        assert topic_list_model != False

        # Construct a model instance of TopicList by calling from_dict on the json representation
        topic_list_model_dict = TopicList.from_dict(topic_list_model_json).__dict__
        topic_list_model2 = TopicList(**topic_list_model_dict)

        # Verify the model instances are equivalent
        assert topic_list_model == topic_list_model2

        # Convert model instance back to dict and verify no loss of data
        topic_list_model_json2 = topic_list_model.to_dict()
        assert topic_list_model_json2 == topic_list_model_json

class TestModel_TopicResponse():
    """
    Test Class for TopicResponse
    """

    def test_topic_response_serialization(self):
        """
        Test serialization/deserialization for TopicResponse
        """

        # Construct a json representation of a TopicResponse model
        topic_response_model_json = {}
        topic_response_model_json['id'] = 'testString'
        topic_response_model_json['name'] = 'testString'
        topic_response_model_json['description'] = 'testString'
        topic_response_model_json['created_at'] = 'testString'

        # Construct a model instance of TopicResponse by calling from_dict on the json representation
        topic_response_model = TopicResponse.from_dict(topic_response_model_json)
        assert topic_response_model != False

        # Construct a model instance of TopicResponse by calling from_dict on the json representation
        topic_response_model_dict = TopicResponse.from_dict(topic_response_model_json).__dict__
        topic_response_model2 = TopicResponse(**topic_response_model_dict)

        # Verify the model instances are equivalent
        assert topic_response_model == topic_response_model2

        # Convert model instance back to dict and verify no loss of data
        topic_response_model_json2 = topic_response_model.to_dict()
        assert topic_response_model_json2 == topic_response_model_json

class TestModel_TopicSourcesItem():
    """
    Test Class for TopicSourcesItem
    """

    def test_topic_sources_item_serialization(self):
        """
        Test serialization/deserialization for TopicSourcesItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_get_model = {} # RulesGet
        rules_get_model['enabled'] = True
        rules_get_model['event_type_filter'] = '$.*'
        rules_get_model['notification_filter'] = 'testString'
        rules_get_model['updated_at'] = 'testString'
        rules_get_model['id'] = 'testString'

        # Construct a json representation of a TopicSourcesItem model
        topic_sources_item_model_json = {}
        topic_sources_item_model_json['id'] = 'testString'
        topic_sources_item_model_json['name'] = 'testString'
        topic_sources_item_model_json['rules'] = [rules_get_model]

        # Construct a model instance of TopicSourcesItem by calling from_dict on the json representation
        topic_sources_item_model = TopicSourcesItem.from_dict(topic_sources_item_model_json)
        assert topic_sources_item_model != False

        # Construct a model instance of TopicSourcesItem by calling from_dict on the json representation
        topic_sources_item_model_dict = TopicSourcesItem.from_dict(topic_sources_item_model_json).__dict__
        topic_sources_item_model2 = TopicSourcesItem(**topic_sources_item_model_dict)

        # Verify the model instances are equivalent
        assert topic_sources_item_model == topic_sources_item_model2

        # Convert model instance back to dict and verify no loss of data
        topic_sources_item_model_json2 = topic_sources_item_model.to_dict()
        assert topic_sources_item_model_json2 == topic_sources_item_model_json

class TestModel_TopicUpdateSourcesItem():
    """
    Test Class for TopicUpdateSourcesItem
    """

    def test_topic_update_sources_item_serialization(self):
        """
        Test serialization/deserialization for TopicUpdateSourcesItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_model = {} # Rules
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.*'
        rules_model['notification_filter'] = 'testString'

        # Construct a json representation of a TopicUpdateSourcesItem model
        topic_update_sources_item_model_json = {}
        topic_update_sources_item_model_json['id'] = 'testString'
        topic_update_sources_item_model_json['rules'] = [rules_model]

        # Construct a model instance of TopicUpdateSourcesItem by calling from_dict on the json representation
        topic_update_sources_item_model = TopicUpdateSourcesItem.from_dict(topic_update_sources_item_model_json)
        assert topic_update_sources_item_model != False

        # Construct a model instance of TopicUpdateSourcesItem by calling from_dict on the json representation
        topic_update_sources_item_model_dict = TopicUpdateSourcesItem.from_dict(topic_update_sources_item_model_json).__dict__
        topic_update_sources_item_model2 = TopicUpdateSourcesItem(**topic_update_sources_item_model_dict)

        # Verify the model instances are equivalent
        assert topic_update_sources_item_model == topic_update_sources_item_model2

        # Convert model instance back to dict and verify no loss of data
        topic_update_sources_item_model_json2 = topic_update_sources_item_model.to_dict()
        assert topic_update_sources_item_model_json2 == topic_update_sources_item_model_json

class TestModel_TopicsListItem():
    """
    Test Class for TopicsListItem
    """

    def test_topics_list_item_serialization(self):
        """
        Test serialization/deserialization for TopicsListItem
        """

        # Construct a json representation of a TopicsListItem model
        topics_list_item_model_json = {}
        topics_list_item_model_json['id'] = 'testString'
        topics_list_item_model_json['name'] = 'testString'
        topics_list_item_model_json['description'] = 'testString'
        topics_list_item_model_json['source_count'] = 0
        topics_list_item_model_json['sources_names'] = ['testString']
        topics_list_item_model_json['subscription_count'] = 0

        # Construct a model instance of TopicsListItem by calling from_dict on the json representation
        topics_list_item_model = TopicsListItem.from_dict(topics_list_item_model_json)
        assert topics_list_item_model != False

        # Construct a model instance of TopicsListItem by calling from_dict on the json representation
        topics_list_item_model_dict = TopicsListItem.from_dict(topics_list_item_model_json).__dict__
        topics_list_item_model2 = TopicsListItem(**topics_list_item_model_dict)

        # Verify the model instances are equivalent
        assert topics_list_item_model == topics_list_item_model2

        # Convert model instance back to dict and verify no loss of data
        topics_list_item_model_json2 = topics_list_item_model.to_dict()
        assert topics_list_item_model_json2 == topics_list_item_model_json

class TestModel_DestinationConfigParamsWebhookDestinationConfig():
    """
    Test Class for DestinationConfigParamsWebhookDestinationConfig
    """

    def test_destination_config_params_webhook_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigParamsWebhookDestinationConfig
        """

        # Construct a json representation of a DestinationConfigParamsWebhookDestinationConfig model
        destination_config_params_webhook_destination_config_model_json = {}
        destination_config_params_webhook_destination_config_model_json['url'] = 'testString'
        destination_config_params_webhook_destination_config_model_json['verb'] = 'get'
        destination_config_params_webhook_destination_config_model_json['custom_headers'] = {}
        destination_config_params_webhook_destination_config_model_json['sensitive_headers'] = ['testString']

        # Construct a model instance of DestinationConfigParamsWebhookDestinationConfig by calling from_dict on the json representation
        destination_config_params_webhook_destination_config_model = DestinationConfigParamsWebhookDestinationConfig.from_dict(destination_config_params_webhook_destination_config_model_json)
        assert destination_config_params_webhook_destination_config_model != False

        # Construct a model instance of DestinationConfigParamsWebhookDestinationConfig by calling from_dict on the json representation
        destination_config_params_webhook_destination_config_model_dict = DestinationConfigParamsWebhookDestinationConfig.from_dict(destination_config_params_webhook_destination_config_model_json).__dict__
        destination_config_params_webhook_destination_config_model2 = DestinationConfigParamsWebhookDestinationConfig(**destination_config_params_webhook_destination_config_model_dict)

        # Verify the model instances are equivalent
        assert destination_config_params_webhook_destination_config_model == destination_config_params_webhook_destination_config_model2

        # Convert model instance back to dict and verify no loss of data
        destination_config_params_webhook_destination_config_model_json2 = destination_config_params_webhook_destination_config_model.to_dict()
        assert destination_config_params_webhook_destination_config_model_json2 == destination_config_params_webhook_destination_config_model_json

class TestModel_SubscriptionAttributesEmailAttributesResponse():
    """
    Test Class for SubscriptionAttributesEmailAttributesResponse
    """

    def test_subscription_attributes_email_attributes_response_serialization(self):
        """
        Test serialization/deserialization for SubscriptionAttributesEmailAttributesResponse
        """

        # Construct a json representation of a SubscriptionAttributesEmailAttributesResponse model
        subscription_attributes_email_attributes_response_model_json = {}
        subscription_attributes_email_attributes_response_model_json['to'] = ['testString']
        subscription_attributes_email_attributes_response_model_json['add_notification_payload'] = False
        subscription_attributes_email_attributes_response_model_json['reply_to_mail'] = 'testString'
        subscription_attributes_email_attributes_response_model_json['reply_to_name'] = 'testString'
        subscription_attributes_email_attributes_response_model_json['from_name'] = 'testString'

        # Construct a model instance of SubscriptionAttributesEmailAttributesResponse by calling from_dict on the json representation
        subscription_attributes_email_attributes_response_model = SubscriptionAttributesEmailAttributesResponse.from_dict(subscription_attributes_email_attributes_response_model_json)
        assert subscription_attributes_email_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesEmailAttributesResponse by calling from_dict on the json representation
        subscription_attributes_email_attributes_response_model_dict = SubscriptionAttributesEmailAttributesResponse.from_dict(subscription_attributes_email_attributes_response_model_json).__dict__
        subscription_attributes_email_attributes_response_model2 = SubscriptionAttributesEmailAttributesResponse(**subscription_attributes_email_attributes_response_model_dict)

        # Verify the model instances are equivalent
        assert subscription_attributes_email_attributes_response_model == subscription_attributes_email_attributes_response_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_email_attributes_response_model_json2 = subscription_attributes_email_attributes_response_model.to_dict()
        assert subscription_attributes_email_attributes_response_model_json2 == subscription_attributes_email_attributes_response_model_json

class TestModel_SubscriptionAttributesSMSAttributesResponse():
    """
    Test Class for SubscriptionAttributesSMSAttributesResponse
    """

    def test_subscription_attributes_sms_attributes_response_serialization(self):
        """
        Test serialization/deserialization for SubscriptionAttributesSMSAttributesResponse
        """

        # Construct a json representation of a SubscriptionAttributesSMSAttributesResponse model
        subscription_attributes_sms_attributes_response_model_json = {}
        subscription_attributes_sms_attributes_response_model_json['to'] = ['testString']

        # Construct a model instance of SubscriptionAttributesSMSAttributesResponse by calling from_dict on the json representation
        subscription_attributes_sms_attributes_response_model = SubscriptionAttributesSMSAttributesResponse.from_dict(subscription_attributes_sms_attributes_response_model_json)
        assert subscription_attributes_sms_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesSMSAttributesResponse by calling from_dict on the json representation
        subscription_attributes_sms_attributes_response_model_dict = SubscriptionAttributesSMSAttributesResponse.from_dict(subscription_attributes_sms_attributes_response_model_json).__dict__
        subscription_attributes_sms_attributes_response_model2 = SubscriptionAttributesSMSAttributesResponse(**subscription_attributes_sms_attributes_response_model_dict)

        # Verify the model instances are equivalent
        assert subscription_attributes_sms_attributes_response_model == subscription_attributes_sms_attributes_response_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_sms_attributes_response_model_json2 = subscription_attributes_sms_attributes_response_model.to_dict()
        assert subscription_attributes_sms_attributes_response_model_json2 == subscription_attributes_sms_attributes_response_model_json

class TestModel_SubscriptionAttributesWebhookAttributesResponse():
    """
    Test Class for SubscriptionAttributesWebhookAttributesResponse
    """

    def test_subscription_attributes_webhook_attributes_response_serialization(self):
        """
        Test serialization/deserialization for SubscriptionAttributesWebhookAttributesResponse
        """

        # Construct a json representation of a SubscriptionAttributesWebhookAttributesResponse model
        subscription_attributes_webhook_attributes_response_model_json = {}
        subscription_attributes_webhook_attributes_response_model_json['signing_enabled'] = True
        subscription_attributes_webhook_attributes_response_model_json['add_notification_payload'] = True

        # Construct a model instance of SubscriptionAttributesWebhookAttributesResponse by calling from_dict on the json representation
        subscription_attributes_webhook_attributes_response_model = SubscriptionAttributesWebhookAttributesResponse.from_dict(subscription_attributes_webhook_attributes_response_model_json)
        assert subscription_attributes_webhook_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesWebhookAttributesResponse by calling from_dict on the json representation
        subscription_attributes_webhook_attributes_response_model_dict = SubscriptionAttributesWebhookAttributesResponse.from_dict(subscription_attributes_webhook_attributes_response_model_json).__dict__
        subscription_attributes_webhook_attributes_response_model2 = SubscriptionAttributesWebhookAttributesResponse(**subscription_attributes_webhook_attributes_response_model_dict)

        # Verify the model instances are equivalent
        assert subscription_attributes_webhook_attributes_response_model == subscription_attributes_webhook_attributes_response_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_webhook_attributes_response_model_json2 = subscription_attributes_webhook_attributes_response_model.to_dict()
        assert subscription_attributes_webhook_attributes_response_model_json2 == subscription_attributes_webhook_attributes_response_model_json

class TestModel_SubscriptionCreateAttributesEmailAttributes():
    """
    Test Class for SubscriptionCreateAttributesEmailAttributes
    """

    def test_subscription_create_attributes_email_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesEmailAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesEmailAttributes model
        subscription_create_attributes_email_attributes_model_json = {}
        subscription_create_attributes_email_attributes_model_json['to'] = ['testString']
        subscription_create_attributes_email_attributes_model_json['add_notification_payload'] = False
        subscription_create_attributes_email_attributes_model_json['reply_to_mail'] = 'testString'
        subscription_create_attributes_email_attributes_model_json['reply_to_name'] = 'testString'
        subscription_create_attributes_email_attributes_model_json['from_name'] = 'testString'

        # Construct a model instance of SubscriptionCreateAttributesEmailAttributes by calling from_dict on the json representation
        subscription_create_attributes_email_attributes_model = SubscriptionCreateAttributesEmailAttributes.from_dict(subscription_create_attributes_email_attributes_model_json)
        assert subscription_create_attributes_email_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesEmailAttributes by calling from_dict on the json representation
        subscription_create_attributes_email_attributes_model_dict = SubscriptionCreateAttributesEmailAttributes.from_dict(subscription_create_attributes_email_attributes_model_json).__dict__
        subscription_create_attributes_email_attributes_model2 = SubscriptionCreateAttributesEmailAttributes(**subscription_create_attributes_email_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_create_attributes_email_attributes_model == subscription_create_attributes_email_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_email_attributes_model_json2 = subscription_create_attributes_email_attributes_model.to_dict()
        assert subscription_create_attributes_email_attributes_model_json2 == subscription_create_attributes_email_attributes_model_json

class TestModel_SubscriptionCreateAttributesSMSAttributes():
    """
    Test Class for SubscriptionCreateAttributesSMSAttributes
    """

    def test_subscription_create_attributes_sms_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesSMSAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesSMSAttributes model
        subscription_create_attributes_sms_attributes_model_json = {}
        subscription_create_attributes_sms_attributes_model_json['to'] = ['testString']

        # Construct a model instance of SubscriptionCreateAttributesSMSAttributes by calling from_dict on the json representation
        subscription_create_attributes_sms_attributes_model = SubscriptionCreateAttributesSMSAttributes.from_dict(subscription_create_attributes_sms_attributes_model_json)
        assert subscription_create_attributes_sms_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesSMSAttributes by calling from_dict on the json representation
        subscription_create_attributes_sms_attributes_model_dict = SubscriptionCreateAttributesSMSAttributes.from_dict(subscription_create_attributes_sms_attributes_model_json).__dict__
        subscription_create_attributes_sms_attributes_model2 = SubscriptionCreateAttributesSMSAttributes(**subscription_create_attributes_sms_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_create_attributes_sms_attributes_model == subscription_create_attributes_sms_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_sms_attributes_model_json2 = subscription_create_attributes_sms_attributes_model.to_dict()
        assert subscription_create_attributes_sms_attributes_model_json2 == subscription_create_attributes_sms_attributes_model_json

class TestModel_SubscriptionCreateAttributesWebhookAttributes():
    """
    Test Class for SubscriptionCreateAttributesWebhookAttributes
    """

    def test_subscription_create_attributes_webhook_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesWebhookAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesWebhookAttributes model
        subscription_create_attributes_webhook_attributes_model_json = {}
        subscription_create_attributes_webhook_attributes_model_json['signing_enabled'] = True

        # Construct a model instance of SubscriptionCreateAttributesWebhookAttributes by calling from_dict on the json representation
        subscription_create_attributes_webhook_attributes_model = SubscriptionCreateAttributesWebhookAttributes.from_dict(subscription_create_attributes_webhook_attributes_model_json)
        assert subscription_create_attributes_webhook_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesWebhookAttributes by calling from_dict on the json representation
        subscription_create_attributes_webhook_attributes_model_dict = SubscriptionCreateAttributesWebhookAttributes.from_dict(subscription_create_attributes_webhook_attributes_model_json).__dict__
        subscription_create_attributes_webhook_attributes_model2 = SubscriptionCreateAttributesWebhookAttributes(**subscription_create_attributes_webhook_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_create_attributes_webhook_attributes_model == subscription_create_attributes_webhook_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_webhook_attributes_model_json2 = subscription_create_attributes_webhook_attributes_model.to_dict()
        assert subscription_create_attributes_webhook_attributes_model_json2 == subscription_create_attributes_webhook_attributes_model_json

class TestModel_SubscriptionUpdateAttributesEmailAttributes():
    """
    Test Class for SubscriptionUpdateAttributesEmailAttributes
    """

    def test_subscription_update_attributes_email_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesEmailAttributes
        """

        # Construct a json representation of a SubscriptionUpdateAttributesEmailAttributes model
        subscription_update_attributes_email_attributes_model_json = {}
        subscription_update_attributes_email_attributes_model_json['to'] = ['testString']
        subscription_update_attributes_email_attributes_model_json['add_notification_payload'] = False
        subscription_update_attributes_email_attributes_model_json['reply_to_mail'] = 'testString'
        subscription_update_attributes_email_attributes_model_json['reply_to_name'] = 'testString'
        subscription_update_attributes_email_attributes_model_json['from_name'] = 'testString'

        # Construct a model instance of SubscriptionUpdateAttributesEmailAttributes by calling from_dict on the json representation
        subscription_update_attributes_email_attributes_model = SubscriptionUpdateAttributesEmailAttributes.from_dict(subscription_update_attributes_email_attributes_model_json)
        assert subscription_update_attributes_email_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesEmailAttributes by calling from_dict on the json representation
        subscription_update_attributes_email_attributes_model_dict = SubscriptionUpdateAttributesEmailAttributes.from_dict(subscription_update_attributes_email_attributes_model_json).__dict__
        subscription_update_attributes_email_attributes_model2 = SubscriptionUpdateAttributesEmailAttributes(**subscription_update_attributes_email_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_update_attributes_email_attributes_model == subscription_update_attributes_email_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_email_attributes_model_json2 = subscription_update_attributes_email_attributes_model.to_dict()
        assert subscription_update_attributes_email_attributes_model_json2 == subscription_update_attributes_email_attributes_model_json

class TestModel_SubscriptionUpdateAttributesSMSAttributes():
    """
    Test Class for SubscriptionUpdateAttributesSMSAttributes
    """

    def test_subscription_update_attributes_sms_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesSMSAttributes
        """

        # Construct a json representation of a SubscriptionUpdateAttributesSMSAttributes model
        subscription_update_attributes_sms_attributes_model_json = {}
        subscription_update_attributes_sms_attributes_model_json['to'] = ['testString']

        # Construct a model instance of SubscriptionUpdateAttributesSMSAttributes by calling from_dict on the json representation
        subscription_update_attributes_sms_attributes_model = SubscriptionUpdateAttributesSMSAttributes.from_dict(subscription_update_attributes_sms_attributes_model_json)
        assert subscription_update_attributes_sms_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesSMSAttributes by calling from_dict on the json representation
        subscription_update_attributes_sms_attributes_model_dict = SubscriptionUpdateAttributesSMSAttributes.from_dict(subscription_update_attributes_sms_attributes_model_json).__dict__
        subscription_update_attributes_sms_attributes_model2 = SubscriptionUpdateAttributesSMSAttributes(**subscription_update_attributes_sms_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_update_attributes_sms_attributes_model == subscription_update_attributes_sms_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_sms_attributes_model_json2 = subscription_update_attributes_sms_attributes_model.to_dict()
        assert subscription_update_attributes_sms_attributes_model_json2 == subscription_update_attributes_sms_attributes_model_json

class TestModel_SubscriptionUpdateAttributesWebhookAttributes():
    """
    Test Class for SubscriptionUpdateAttributesWebhookAttributes
    """

    def test_subscription_update_attributes_webhook_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesWebhookAttributes
        """

        # Construct a json representation of a SubscriptionUpdateAttributesWebhookAttributes model
        subscription_update_attributes_webhook_attributes_model_json = {}
        subscription_update_attributes_webhook_attributes_model_json['signing_enabled'] = True

        # Construct a model instance of SubscriptionUpdateAttributesWebhookAttributes by calling from_dict on the json representation
        subscription_update_attributes_webhook_attributes_model = SubscriptionUpdateAttributesWebhookAttributes.from_dict(subscription_update_attributes_webhook_attributes_model_json)
        assert subscription_update_attributes_webhook_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesWebhookAttributes by calling from_dict on the json representation
        subscription_update_attributes_webhook_attributes_model_dict = SubscriptionUpdateAttributesWebhookAttributes.from_dict(subscription_update_attributes_webhook_attributes_model_json).__dict__
        subscription_update_attributes_webhook_attributes_model2 = SubscriptionUpdateAttributesWebhookAttributes(**subscription_update_attributes_webhook_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_update_attributes_webhook_attributes_model == subscription_update_attributes_webhook_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_webhook_attributes_model_json2 = subscription_update_attributes_webhook_attributes_model.to_dict()
        assert subscription_update_attributes_webhook_attributes_model_json2 == subscription_update_attributes_webhook_attributes_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
