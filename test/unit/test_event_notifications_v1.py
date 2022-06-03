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
Unit Tests for EventNotificationsV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import io
import json
import os
import pytest
import re
import requests
import responses
import tempfile
import urllib
from ibm_eventnotifications.event_notifications_v1 import *


_service = EventNotificationsV1(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://us-south.event-notifications.cloud.ibm.com/event-notifications'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


##############################################################################
# Start of Service: SendNotifications
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
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestSendNotifications():
    """
    Test Class for send_notifications
    """

    @responses.activate
    def test_send_notifications_all_params(self):
        """
        send_notifications()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/notifications')
        mock_response = '{"notification_id": "notification_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a NotificationCreate model
        notification_create_model = {}
        notification_create_model['data'] = {}
        notification_create_model['ibmenseverity'] = 'testString'
        notification_create_model['ibmenfcmbody'] = 'testString'
        notification_create_model['ibmenapnsbody'] = 'testString'
        notification_create_model['ibmensafaribody'] = 'testString'
        notification_create_model['ibmenpushto'] = '{"fcm_devices":["9c75975a-37d0-3898-905d-3b5ee0d7c172","C9CACDF5-6EBF-49E1-AD60-E25BA23E954C"],"apns_devices":["3423-37d0-3898-905d-42342","432423-6EBF-49E1-AD60-4234"],"user_ids":["user-1","user-2"],"tags":["tag-1","tag-2"],"platforms":["push_android","push_ios","push_chrome","push_firefox"]}'
        notification_create_model['ibmenapnsheaders'] = 'testString'
        notification_create_model['ibmendefaultshort'] = 'testString'
        notification_create_model['ibmendefaultlong'] = 'testString'
        notification_create_model['ibmenchromebody'] = 'testString'
        notification_create_model['ibmenfirefoxbody'] = 'testString'
        notification_create_model['ibmenchromeheaders'] = 'testString'
        notification_create_model['ibmenfirefoxheaders'] = 'testString'
        notification_create_model['ibmensourceid'] = 'testString'
        notification_create_model['datacontenttype'] = 'application/json'
        notification_create_model['subject'] = 'testString'
        notification_create_model['id'] = 'testString'
        notification_create_model['source'] = 'testString'
        notification_create_model['type'] = 'testString'
        notification_create_model['specversion'] = '1.0'
        notification_create_model['time'] = 'testString'
        notification_create_model['foo'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        body = notification_create_model
        ce_ibmenseverity = 'testString'
        ce_ibmendefaultshort = 'testString'
        ce_ibmendefaultlong = 'testString'
        ce_ibmenfcmbody = 'testString'
        ce_ibmenapnsbody = 'testString'
        ce_ibmensafaribody = 'testString'
        ce_ibmenpushto = '{"fcm_devices":["9c75975a-37d0-3898-905d-3b5ee0d7c172","C9CACDF5-6EBF-49E1-AD60-E25BA23E954C"],"apns_devices":["3423-37d0-3898-905d-42342","432423-6EBF-49E1-AD60-4234"],"user_ids":["user-1","user-2"],"tags":["tag-1","tag-2"],"platforms":["push_android","push_ios","push_chrome","push_firefox"]}'
        ce_ibmenapnsheaders = 'testString'
        ce_ibmenchromebody = 'testString'
        ce_ibmenfirefoxbody = 'testString'
        ce_ibmenchromeheaders = 'testString'
        ce_ibmenfirefoxheaders = 'testString'
        ce_ibmensourceid = 'testString'
        ce_id = 'testString'
        ce_source = 'testString'
        ce_type = 'testString'
        ce_specversion = '1.0'
        ce_time = 'testString'

        # Invoke method
        response = _service.send_notifications(
            instance_id,
            body=body,
            ce_ibmenseverity=ce_ibmenseverity,
            ce_ibmendefaultshort=ce_ibmendefaultshort,
            ce_ibmendefaultlong=ce_ibmendefaultlong,
            ce_ibmenfcmbody=ce_ibmenfcmbody,
            ce_ibmenapnsbody=ce_ibmenapnsbody,
            ce_ibmensafaribody=ce_ibmensafaribody,
            ce_ibmenpushto=ce_ibmenpushto,
            ce_ibmenapnsheaders=ce_ibmenapnsheaders,
            ce_ibmenchromebody=ce_ibmenchromebody,
            ce_ibmenfirefoxbody=ce_ibmenfirefoxbody,
            ce_ibmenchromeheaders=ce_ibmenchromeheaders,
            ce_ibmenfirefoxheaders=ce_ibmenfirefoxheaders,
            ce_ibmensourceid=ce_ibmensourceid,
            ce_id=ce_id,
            ce_source=ce_source,
            ce_type=ce_type,
            ce_specversion=ce_specversion,
            ce_time=ce_time,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_send_notifications_all_params_with_retries(self):
        # Enable retries and run test_send_notifications_all_params.
        _service.enable_retries()
        self.test_send_notifications_all_params()

        # Disable retries and run test_send_notifications_all_params.
        _service.disable_retries()
        self.test_send_notifications_all_params()

    @responses.activate
    def test_send_notifications_required_params(self):
        """
        test_send_notifications_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/notifications')
        mock_response = '{"notification_id": "notification_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.send_notifications(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_send_notifications_required_params_with_retries(self):
        # Enable retries and run test_send_notifications_required_params.
        _service.enable_retries()
        self.test_send_notifications_required_params()

        # Disable retries and run test_send_notifications_required_params.
        _service.disable_retries()
        self.test_send_notifications_required_params()

    @responses.activate
    def test_send_notifications_value_error(self):
        """
        test_send_notifications_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/notifications')
        mock_response = '{"notification_id": "notification_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.send_notifications(**req_copy)


    def test_send_notifications_value_error_with_retries(self):
        # Enable retries and run test_send_notifications_value_error.
        _service.enable_retries()
        self.test_send_notifications_value_error()

        # Disable retries and run test_send_notifications_value_error.
        _service.disable_retries()
        self.test_send_notifications_value_error()

class TestSendBulkNotifications():
    """
    Test Class for send_bulk_notifications
    """

    @responses.activate
    def test_send_bulk_notifications_all_params(self):
        """
        send_bulk_notifications()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/notifications/bulk')
        mock_response = '{"bulk_notification_id": "bulk_notification_id", "bulk_messages": ["anyValue"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a NotificationCreate model
        notification_create_model = {}
        notification_create_model['data'] = {}
        notification_create_model['ibmenseverity'] = 'testString'
        notification_create_model['ibmenfcmbody'] = 'testString'
        notification_create_model['ibmenapnsbody'] = 'testString'
        notification_create_model['ibmensafaribody'] = 'testString'
        notification_create_model['ibmenpushto'] = '{"fcm_devices":["9c75975a-37d0-3898-905d-3b5ee0d7c172","C9CACDF5-6EBF-49E1-AD60-E25BA23E954C"],"apns_devices":["3423-37d0-3898-905d-42342","432423-6EBF-49E1-AD60-4234"],"user_ids":["user-1","user-2"],"tags":["tag-1","tag-2"],"platforms":["push_android","push_ios","push_chrome","push_firefox"]}'
        notification_create_model['ibmenapnsheaders'] = 'testString'
        notification_create_model['ibmendefaultshort'] = 'testString'
        notification_create_model['ibmendefaultlong'] = 'testString'
        notification_create_model['ibmenchromebody'] = 'testString'
        notification_create_model['ibmenfirefoxbody'] = 'testString'
        notification_create_model['ibmenchromeheaders'] = 'testString'
        notification_create_model['ibmenfirefoxheaders'] = 'testString'
        notification_create_model['ibmensourceid'] = 'testString'
        notification_create_model['datacontenttype'] = 'application/json'
        notification_create_model['subject'] = 'testString'
        notification_create_model['id'] = 'testString'
        notification_create_model['source'] = 'testString'
        notification_create_model['type'] = 'testString'
        notification_create_model['specversion'] = '1.0'
        notification_create_model['time'] = 'testString'
        notification_create_model['foo'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        bulk_messages = [notification_create_model]

        # Invoke method
        response = _service.send_bulk_notifications(
            instance_id,
            bulk_messages=bulk_messages,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['bulk_messages'] == [notification_create_model]

    def test_send_bulk_notifications_all_params_with_retries(self):
        # Enable retries and run test_send_bulk_notifications_all_params.
        _service.enable_retries()
        self.test_send_bulk_notifications_all_params()

        # Disable retries and run test_send_bulk_notifications_all_params.
        _service.disable_retries()
        self.test_send_bulk_notifications_all_params()

    @responses.activate
    def test_send_bulk_notifications_required_params(self):
        """
        test_send_bulk_notifications_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/notifications/bulk')
        mock_response = '{"bulk_notification_id": "bulk_notification_id", "bulk_messages": ["anyValue"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.send_bulk_notifications(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_send_bulk_notifications_required_params_with_retries(self):
        # Enable retries and run test_send_bulk_notifications_required_params.
        _service.enable_retries()
        self.test_send_bulk_notifications_required_params()

        # Disable retries and run test_send_bulk_notifications_required_params.
        _service.disable_retries()
        self.test_send_bulk_notifications_required_params()

    @responses.activate
    def test_send_bulk_notifications_value_error(self):
        """
        test_send_bulk_notifications_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/notifications/bulk')
        mock_response = '{"bulk_notification_id": "bulk_notification_id", "bulk_messages": ["anyValue"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.send_bulk_notifications(**req_copy)


    def test_send_bulk_notifications_value_error_with_retries(self):
        # Enable retries and run test_send_bulk_notifications_value_error.
        _service.enable_retries()
        self.test_send_bulk_notifications_value_error()

        # Disable retries and run test_send_bulk_notifications_value_error.
        _service.disable_retries()
        self.test_send_bulk_notifications_value_error()

# endregion
##############################################################################
# End of Service: SendNotifications
##############################################################################

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
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestCreateSources():
    """
    Test Class for create_sources
    """

    @responses.activate
    def test_create_sources_all_params(self):
        """
        create_sources()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/sources')
        mock_response = '{"id": "id", "name": "name", "description": "description", "enabled": false, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        description = 'testString'
        enabled = True

        # Invoke method
        response = _service.create_sources(
            instance_id,
            name,
            description,
            enabled=enabled,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['enabled'] == True

    def test_create_sources_all_params_with_retries(self):
        # Enable retries and run test_create_sources_all_params.
        _service.enable_retries()
        self.test_create_sources_all_params()

        # Disable retries and run test_create_sources_all_params.
        _service.disable_retries()
        self.test_create_sources_all_params()

    @responses.activate
    def test_create_sources_value_error(self):
        """
        test_create_sources_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/sources')
        mock_response = '{"id": "id", "name": "name", "description": "description", "enabled": false, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        description = 'testString'
        enabled = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "name": name,
            "description": description,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_sources(**req_copy)


    def test_create_sources_value_error_with_retries(self):
        # Enable retries and run test_create_sources_value_error.
        _service.enable_retries()
        self.test_create_sources_value_error()

        # Disable retries and run test_create_sources_value_error.
        _service.disable_retries()
        self.test_create_sources_value_error()

class TestListSources():
    """
    Test Class for list_sources
    """

    @responses.activate
    def test_list_sources_all_params(self):
        """
        list_sources()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/sources')
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
        url = preprocess_url('/v1/instances/testString/sources')
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
        url = preprocess_url('/v1/instances/testString/sources')
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

    @responses.activate
    def test_get_source_all_params(self):
        """
        get_source()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/sources/testString')
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
        url = preprocess_url('/v1/instances/testString/sources/testString')
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

class TestDeleteSource():
    """
    Test Class for delete_source
    """

    @responses.activate
    def test_delete_source_all_params(self):
        """
        delete_source()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/sources/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_source(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_source_all_params_with_retries(self):
        # Enable retries and run test_delete_source_all_params.
        _service.enable_retries()
        self.test_delete_source_all_params()

        # Disable retries and run test_delete_source_all_params.
        _service.disable_retries()
        self.test_delete_source_all_params()

    @responses.activate
    def test_delete_source_value_error(self):
        """
        test_delete_source_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/sources/testString')
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
                _service.delete_source(**req_copy)


    def test_delete_source_value_error_with_retries(self):
        # Enable retries and run test_delete_source_value_error.
        _service.enable_retries()
        self.test_delete_source_value_error()

        # Disable retries and run test_delete_source_value_error.
        _service.disable_retries()
        self.test_delete_source_value_error()

class TestUpdateSource():
    """
    Test Class for update_source
    """

    @responses.activate
    def test_update_source_all_params(self):
        """
        update_source()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/sources/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "enabled": false, "type": "type", "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 11, "topic_names": ["topic_names"]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        enabled = True

        # Invoke method
        response = _service.update_source(
            instance_id,
            id,
            name=name,
            description=description,
            enabled=enabled,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['enabled'] == True

    def test_update_source_all_params_with_retries(self):
        # Enable retries and run test_update_source_all_params.
        _service.enable_retries()
        self.test_update_source_all_params()

        # Disable retries and run test_update_source_all_params.
        _service.disable_retries()
        self.test_update_source_all_params()

    @responses.activate
    def test_update_source_value_error(self):
        """
        test_update_source_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/sources/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "enabled": false, "type": "type", "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 11, "topic_names": ["topic_names"]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        enabled = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_source(**req_copy)


    def test_update_source_value_error_with_retries(self):
        # Enable retries and run test_update_source_value_error.
        _service.enable_retries()
        self.test_update_source_value_error()

        # Disable retries and run test_update_source_value_error.
        _service.disable_retries()
        self.test_update_source_value_error()

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
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestCreateTopic():
    """
    Test Class for create_topic
    """

    @responses.activate
    def test_create_topic_all_params(self):
        """
        create_topic()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/topics')
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
        url = preprocess_url('/v1/instances/testString/topics')
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

    @responses.activate
    def test_list_topics_all_params(self):
        """
        list_topics()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/topics')
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
        url = preprocess_url('/v1/instances/testString/topics')
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
        url = preprocess_url('/v1/instances/testString/topics')
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

    @responses.activate
    def test_get_topic_all_params(self):
        """
        get_topic()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/topics/testString')
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
        url = preprocess_url('/v1/instances/testString/topics/testString')
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
        url = preprocess_url('/v1/instances/testString/topics/testString')
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

    @responses.activate
    def test_replace_topic_all_params(self):
        """
        replace_topic()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/topics/testString')
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
        url = preprocess_url('/v1/instances/testString/topics/testString')
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

    @responses.activate
    def test_delete_topic_all_params(self):
        """
        delete_topic()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/topics/testString')
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
        url = preprocess_url('/v1/instances/testString/topics/testString')
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
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestCreateDestination():
    """
    Test Class for create_destination
    """

    @responses.activate
    def test_create_destination_all_params(self):
        """
        create_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations')
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
        certificate = io.BytesIO(b'This is a mock file.').getvalue()
        certificate_content_type = 'testString'
        icon_16x16 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_16x16_content_type = 'testString'
        icon_16x162x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_16x162x_content_type = 'testString'
        icon_32x32 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_32x32_content_type = 'testString'
        icon_32x322x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_32x322x_content_type = 'testString'
        icon_128x128 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_128x128_content_type = 'testString'
        icon_128x1282x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_128x1282x_content_type = 'testString'

        # Invoke method
        response = _service.create_destination(
            instance_id,
            name,
            type,
            description=description,
            config=config,
            certificate=certificate,
            certificate_content_type=certificate_content_type,
            icon_16x16=icon_16x16,
            icon_16x16_content_type=icon_16x16_content_type,
            icon_16x162x=icon_16x162x,
            icon_16x162x_content_type=icon_16x162x_content_type,
            icon_32x32=icon_32x32,
            icon_32x32_content_type=icon_32x32_content_type,
            icon_32x322x=icon_32x322x,
            icon_32x322x_content_type=icon_32x322x_content_type,
            icon_128x128=icon_128x128,
            icon_128x128_content_type=icon_128x128_content_type,
            icon_128x1282x=icon_128x1282x,
            icon_128x1282x_content_type=icon_128x1282x_content_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_destination_all_params_with_retries(self):
        # Enable retries and run test_create_destination_all_params.
        _service.enable_retries()
        self.test_create_destination_all_params()

        # Disable retries and run test_create_destination_all_params.
        _service.disable_retries()
        self.test_create_destination_all_params()

    @responses.activate
    def test_create_destination_required_params(self):
        """
        test_create_destination_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        type = 'webhook'

        # Invoke method
        response = _service.create_destination(
            instance_id,
            name,
            type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_create_destination_required_params_with_retries(self):
        # Enable retries and run test_create_destination_required_params.
        _service.enable_retries()
        self.test_create_destination_required_params()

        # Disable retries and run test_create_destination_required_params.
        _service.disable_retries()
        self.test_create_destination_required_params()

    @responses.activate
    def test_create_destination_value_error(self):
        """
        test_create_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        type = 'webhook'

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

    @responses.activate
    def test_list_destinations_all_params(self):
        """
        list_destinations()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations')
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
        url = preprocess_url('/v1/instances/testString/destinations')
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
        url = preprocess_url('/v1/instances/testString/destinations')
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

    @responses.activate
    def test_get_destination_all_params(self):
        """
        get_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString')
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
        url = preprocess_url('/v1/instances/testString/destinations/testString')
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

    @responses.activate
    def test_update_destination_all_params(self):
        """
        update_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString')
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
        certificate = io.BytesIO(b'This is a mock file.').getvalue()
        certificate_content_type = 'testString'
        icon_16x16 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_16x16_content_type = 'testString'
        icon_16x162x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_16x162x_content_type = 'testString'
        icon_32x32 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_32x32_content_type = 'testString'
        icon_32x322x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_32x322x_content_type = 'testString'
        icon_128x128 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_128x128_content_type = 'testString'
        icon_128x1282x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_128x1282x_content_type = 'testString'

        # Invoke method
        response = _service.update_destination(
            instance_id,
            id,
            name=name,
            description=description,
            config=config,
            certificate=certificate,
            certificate_content_type=certificate_content_type,
            icon_16x16=icon_16x16,
            icon_16x16_content_type=icon_16x16_content_type,
            icon_16x162x=icon_16x162x,
            icon_16x162x_content_type=icon_16x162x_content_type,
            icon_32x32=icon_32x32,
            icon_32x32_content_type=icon_32x32_content_type,
            icon_32x322x=icon_32x322x,
            icon_32x322x_content_type=icon_32x322x_content_type,
            icon_128x128=icon_128x128,
            icon_128x128_content_type=icon_128x128_content_type,
            icon_128x1282x=icon_128x1282x,
            icon_128x1282x_content_type=icon_128x1282x_content_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_destination_all_params_with_retries(self):
        # Enable retries and run test_update_destination_all_params.
        _service.enable_retries()
        self.test_update_destination_all_params()

        # Disable retries and run test_update_destination_all_params.
        _service.disable_retries()
        self.test_update_destination_all_params()

    @responses.activate
    def test_update_destination_required_params(self):
        """
        test_update_destination_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.update_destination(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_update_destination_required_params_with_retries(self):
        # Enable retries and run test_update_destination_required_params.
        _service.enable_retries()
        self.test_update_destination_required_params()

        # Disable retries and run test_update_destination_required_params.
        _service.disable_retries()
        self.test_update_destination_required_params()

    @responses.activate
    def test_update_destination_value_error(self):
        """
        test_update_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "config": {"params": {"url": "url", "verb": "get", "custom_headers": {"mapKey": "inner"}, "sensitive_headers": ["sensitive_headers"]}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(responses.PATCH,
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

    @responses.activate
    def test_delete_destination_all_params(self):
        """
        delete_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString')
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
        url = preprocess_url('/v1/instances/testString/destinations/testString')
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
# Start of Service: DestinationsPushDevices
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
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListDestinationDevices():
    """
    Test Class for list_destination_devices
    """

    @responses.activate
    def test_list_destination_devices_all_params(self):
        """
        list_destination_devices()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/devices')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "devices": [{"id": "id", "user_id": "user_id", "platform": "platform", "token": "token", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        limit = 1
        offset = 0
        search = 'testString'

        # Invoke method
        response = _service.list_destination_devices(
            instance_id,
            id,
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

    def test_list_destination_devices_all_params_with_retries(self):
        # Enable retries and run test_list_destination_devices_all_params.
        _service.enable_retries()
        self.test_list_destination_devices_all_params()

        # Disable retries and run test_list_destination_devices_all_params.
        _service.disable_retries()
        self.test_list_destination_devices_all_params()

    @responses.activate
    def test_list_destination_devices_required_params(self):
        """
        test_list_destination_devices_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/devices')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "devices": [{"id": "id", "user_id": "user_id", "platform": "platform", "token": "token", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.list_destination_devices(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_destination_devices_required_params_with_retries(self):
        # Enable retries and run test_list_destination_devices_required_params.
        _service.enable_retries()
        self.test_list_destination_devices_required_params()

        # Disable retries and run test_list_destination_devices_required_params.
        _service.disable_retries()
        self.test_list_destination_devices_required_params()

    @responses.activate
    def test_list_destination_devices_value_error(self):
        """
        test_list_destination_devices_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/devices')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "devices": [{"id": "id", "user_id": "user_id", "platform": "platform", "token": "token", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
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
                _service.list_destination_devices(**req_copy)


    def test_list_destination_devices_value_error_with_retries(self):
        # Enable retries and run test_list_destination_devices_value_error.
        _service.enable_retries()
        self.test_list_destination_devices_value_error()

        # Disable retries and run test_list_destination_devices_value_error.
        _service.disable_retries()
        self.test_list_destination_devices_value_error()

class TestGetDestinationDevicesReport():
    """
    Test Class for get_destination_devices_report
    """

    @responses.activate
    def test_get_destination_devices_report_all_params(self):
        """
        get_destination_devices_report()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/devices/report')
        mock_response = '{"android": 7, "ios": 3, "chrome": 6, "firefox": 7, "safari": 6, "chromeAppExt": 14, "all": 3}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        days = 1

        # Invoke method
        response = _service.get_destination_devices_report(
            instance_id,
            id,
            days=days,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'days={}'.format(days) in query_string

    def test_get_destination_devices_report_all_params_with_retries(self):
        # Enable retries and run test_get_destination_devices_report_all_params.
        _service.enable_retries()
        self.test_get_destination_devices_report_all_params()

        # Disable retries and run test_get_destination_devices_report_all_params.
        _service.disable_retries()
        self.test_get_destination_devices_report_all_params()

    @responses.activate
    def test_get_destination_devices_report_required_params(self):
        """
        test_get_destination_devices_report_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/devices/report')
        mock_response = '{"android": 7, "ios": 3, "chrome": 6, "firefox": 7, "safari": 6, "chromeAppExt": 14, "all": 3}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_destination_devices_report(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_destination_devices_report_required_params_with_retries(self):
        # Enable retries and run test_get_destination_devices_report_required_params.
        _service.enable_retries()
        self.test_get_destination_devices_report_required_params()

        # Disable retries and run test_get_destination_devices_report_required_params.
        _service.disable_retries()
        self.test_get_destination_devices_report_required_params()

    @responses.activate
    def test_get_destination_devices_report_value_error(self):
        """
        test_get_destination_devices_report_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/devices/report')
        mock_response = '{"android": 7, "ios": 3, "chrome": 6, "firefox": 7, "safari": 6, "chromeAppExt": 14, "all": 3}'
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
                _service.get_destination_devices_report(**req_copy)


    def test_get_destination_devices_report_value_error_with_retries(self):
        # Enable retries and run test_get_destination_devices_report_value_error.
        _service.enable_retries()
        self.test_get_destination_devices_report_value_error()

        # Disable retries and run test_get_destination_devices_report_value_error.
        _service.disable_retries()
        self.test_get_destination_devices_report_value_error()

# endregion
##############################################################################
# End of Service: DestinationsPushDevices
##############################################################################

##############################################################################
# Start of Service: DestinationTagsSubscriptions
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
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestListTagsSubscriptionsDevice():
    """
    Test Class for list_tags_subscriptions_device
    """

    @responses.activate
    def test_list_tags_subscriptions_device_all_params(self):
        """
        list_tags_subscriptions_device()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions/devices/testString')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "tag_subscriptions": [{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        device_id = 'testString'
        tag_name = 'testString'
        limit = 1
        offset = 0

        # Invoke method
        response = _service.list_tags_subscriptions_device(
            instance_id,
            id,
            device_id,
            tag_name=tag_name,
            limit=limit,
            offset=offset,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'tag_name={}'.format(tag_name) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string

    def test_list_tags_subscriptions_device_all_params_with_retries(self):
        # Enable retries and run test_list_tags_subscriptions_device_all_params.
        _service.enable_retries()
        self.test_list_tags_subscriptions_device_all_params()

        # Disable retries and run test_list_tags_subscriptions_device_all_params.
        _service.disable_retries()
        self.test_list_tags_subscriptions_device_all_params()

    @responses.activate
    def test_list_tags_subscriptions_device_required_params(self):
        """
        test_list_tags_subscriptions_device_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions/devices/testString')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "tag_subscriptions": [{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        device_id = 'testString'

        # Invoke method
        response = _service.list_tags_subscriptions_device(
            instance_id,
            id,
            device_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_tags_subscriptions_device_required_params_with_retries(self):
        # Enable retries and run test_list_tags_subscriptions_device_required_params.
        _service.enable_retries()
        self.test_list_tags_subscriptions_device_required_params()

        # Disable retries and run test_list_tags_subscriptions_device_required_params.
        _service.disable_retries()
        self.test_list_tags_subscriptions_device_required_params()

    @responses.activate
    def test_list_tags_subscriptions_device_value_error(self):
        """
        test_list_tags_subscriptions_device_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions/devices/testString')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "tag_subscriptions": [{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        device_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
            "device_id": device_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tags_subscriptions_device(**req_copy)


    def test_list_tags_subscriptions_device_value_error_with_retries(self):
        # Enable retries and run test_list_tags_subscriptions_device_value_error.
        _service.enable_retries()
        self.test_list_tags_subscriptions_device_value_error()

        # Disable retries and run test_list_tags_subscriptions_device_value_error.
        _service.disable_retries()
        self.test_list_tags_subscriptions_device_value_error()

class TestListTagsSubscription():
    """
    Test Class for list_tags_subscription
    """

    @responses.activate
    def test_list_tags_subscription_all_params(self):
        """
        list_tags_subscription()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "tag_subscriptions": [{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        device_id = 'testString'
        user_id = 'testString'
        tag_name = 'testString'
        limit = 1
        offset = 0
        search = 'testString'

        # Invoke method
        response = _service.list_tags_subscription(
            instance_id,
            id,
            device_id=device_id,
            user_id=user_id,
            tag_name=tag_name,
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
        assert 'device_id={}'.format(device_id) in query_string
        assert 'user_id={}'.format(user_id) in query_string
        assert 'tag_name={}'.format(tag_name) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'search={}'.format(search) in query_string

    def test_list_tags_subscription_all_params_with_retries(self):
        # Enable retries and run test_list_tags_subscription_all_params.
        _service.enable_retries()
        self.test_list_tags_subscription_all_params()

        # Disable retries and run test_list_tags_subscription_all_params.
        _service.disable_retries()
        self.test_list_tags_subscription_all_params()

    @responses.activate
    def test_list_tags_subscription_required_params(self):
        """
        test_list_tags_subscription_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "tag_subscriptions": [{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.list_tags_subscription(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_tags_subscription_required_params_with_retries(self):
        # Enable retries and run test_list_tags_subscription_required_params.
        _service.enable_retries()
        self.test_list_tags_subscription_required_params()

        # Disable retries and run test_list_tags_subscription_required_params.
        _service.disable_retries()
        self.test_list_tags_subscription_required_params()

    @responses.activate
    def test_list_tags_subscription_value_error(self):
        """
        test_list_tags_subscription_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "tag_subscriptions": [{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "updated_at": "2019-01-01T12:00:00.000Z"}]}'
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
                _service.list_tags_subscription(**req_copy)


    def test_list_tags_subscription_value_error_with_retries(self):
        # Enable retries and run test_list_tags_subscription_value_error.
        _service.enable_retries()
        self.test_list_tags_subscription_value_error()

        # Disable retries and run test_list_tags_subscription_value_error.
        _service.disable_retries()
        self.test_list_tags_subscription_value_error()

class TestCreateTagsSubscription():
    """
    Test Class for create_tags_subscription
    """

    @responses.activate
    def test_create_tags_subscription_all_params(self):
        """
        create_tags_subscription()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
        mock_response = '{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        device_id = 'testString'
        tag_name = 'testString'

        # Invoke method
        response = _service.create_tags_subscription(
            instance_id,
            id,
            device_id,
            tag_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['device_id'] == 'testString'
        assert req_body['tag_name'] == 'testString'

    def test_create_tags_subscription_all_params_with_retries(self):
        # Enable retries and run test_create_tags_subscription_all_params.
        _service.enable_retries()
        self.test_create_tags_subscription_all_params()

        # Disable retries and run test_create_tags_subscription_all_params.
        _service.disable_retries()
        self.test_create_tags_subscription_all_params()

    @responses.activate
    def test_create_tags_subscription_value_error(self):
        """
        test_create_tags_subscription_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
        mock_response = '{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        device_id = 'testString'
        tag_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
            "device_id": device_id,
            "tag_name": tag_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tags_subscription(**req_copy)


    def test_create_tags_subscription_value_error_with_retries(self):
        # Enable retries and run test_create_tags_subscription_value_error.
        _service.enable_retries()
        self.test_create_tags_subscription_value_error()

        # Disable retries and run test_create_tags_subscription_value_error.
        _service.disable_retries()
        self.test_create_tags_subscription_value_error()

class TestDeleteTagsSubscription():
    """
    Test Class for delete_tags_subscription
    """

    @responses.activate
    def test_delete_tags_subscription_all_params(self):
        """
        delete_tags_subscription()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        device_id = 'testString'
        tag_name = 'testString'

        # Invoke method
        response = _service.delete_tags_subscription(
            instance_id,
            id,
            device_id=device_id,
            tag_name=tag_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'device_id={}'.format(device_id) in query_string
        assert 'tag_name={}'.format(tag_name) in query_string

    def test_delete_tags_subscription_all_params_with_retries(self):
        # Enable retries and run test_delete_tags_subscription_all_params.
        _service.enable_retries()
        self.test_delete_tags_subscription_all_params()

        # Disable retries and run test_delete_tags_subscription_all_params.
        _service.disable_retries()
        self.test_delete_tags_subscription_all_params()

    @responses.activate
    def test_delete_tags_subscription_required_params(self):
        """
        test_delete_tags_subscription_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_tags_subscription(
            instance_id,
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_tags_subscription_required_params_with_retries(self):
        # Enable retries and run test_delete_tags_subscription_required_params.
        _service.enable_retries()
        self.test_delete_tags_subscription_required_params()

        # Disable retries and run test_delete_tags_subscription_required_params.
        _service.disable_retries()
        self.test_delete_tags_subscription_required_params()

    @responses.activate
    def test_delete_tags_subscription_value_error(self):
        """
        test_delete_tags_subscription_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
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
                _service.delete_tags_subscription(**req_copy)


    def test_delete_tags_subscription_value_error_with_retries(self):
        # Enable retries and run test_delete_tags_subscription_value_error.
        _service.enable_retries()
        self.test_delete_tags_subscription_value_error()

        # Disable retries and run test_delete_tags_subscription_value_error.
        _service.disable_retries()
        self.test_delete_tags_subscription_value_error()

# endregion
##############################################################################
# End of Service: DestinationTagsSubscriptions
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
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestCreateSubscription():
    """
    Test Class for create_subscription
    """

    @responses.activate
    def test_create_subscription_all_params(self):
        """
        create_subscription()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/subscriptions')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {}}'
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
        description = 'testString'
        attributes = subscription_create_attributes_model

        # Invoke method
        response = _service.create_subscription(
            instance_id,
            name,
            destination_id,
            topic_id,
            description=description,
            attributes=attributes,
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
        assert req_body['description'] == 'testString'
        assert req_body['attributes'] == subscription_create_attributes_model

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
        url = preprocess_url('/v1/instances/testString/subscriptions')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {}}'
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
        description = 'testString'
        attributes = subscription_create_attributes_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "name": name,
            "destination_id": destination_id,
            "topic_id": topic_id,
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

    @responses.activate
    def test_list_subscriptions_all_params(self):
        """
        list_subscriptions()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/subscriptions')
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
        url = preprocess_url('/v1/instances/testString/subscriptions')
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
        url = preprocess_url('/v1/instances/testString/subscriptions')
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

    @responses.activate
    def test_get_subscription_all_params(self):
        """
        get_subscription()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/subscriptions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {}}'
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
        url = preprocess_url('/v1/instances/testString/subscriptions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {}}'
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

    @responses.activate
    def test_delete_subscription_all_params(self):
        """
        delete_subscription()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/subscriptions/testString')
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
        url = preprocess_url('/v1/instances/testString/subscriptions/testString')
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

    @responses.activate
    def test_update_subscription_all_params(self):
        """
        update_subscription()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/subscriptions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {}}'
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
        url = preprocess_url('/v1/instances/testString/subscriptions/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {}}'
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
class TestModel_BulkNotificationResponse():
    """
    Test Class for BulkNotificationResponse
    """

    def test_bulk_notification_response_serialization(self):
        """
        Test serialization/deserialization for BulkNotificationResponse
        """

        # Construct a json representation of a BulkNotificationResponse model
        bulk_notification_response_model_json = {}
        bulk_notification_response_model_json['bulk_notification_id'] = 'testString'
        bulk_notification_response_model_json['bulk_messages'] = ['testString']

        # Construct a model instance of BulkNotificationResponse by calling from_dict on the json representation
        bulk_notification_response_model = BulkNotificationResponse.from_dict(bulk_notification_response_model_json)
        assert bulk_notification_response_model != False

        # Construct a model instance of BulkNotificationResponse by calling from_dict on the json representation
        bulk_notification_response_model_dict = BulkNotificationResponse.from_dict(bulk_notification_response_model_json).__dict__
        bulk_notification_response_model2 = BulkNotificationResponse(**bulk_notification_response_model_dict)

        # Verify the model instances are equivalent
        assert bulk_notification_response_model == bulk_notification_response_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_notification_response_model_json2 = bulk_notification_response_model.to_dict()
        assert bulk_notification_response_model_json2 == bulk_notification_response_model_json

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
        destination_model_json['updated_at'] = '2019-01-01T12:00:00Z'
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

class TestModel_DestinationDevicesList():
    """
    Test Class for DestinationDevicesList
    """

    def test_destination_devices_list_serialization(self):
        """
        Test serialization/deserialization for DestinationDevicesList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_devices_list_item_model = {} # DestinationDevicesListItem
        destination_devices_list_item_model['id'] = '11fe18ba-d0c8-4108-9f07-adsa'
        destination_devices_list_item_model['user_id'] = 'TestUserId'
        destination_devices_list_item_model['platform'] = 'A'
        destination_devices_list_item_model['token'] = '************'
        destination_devices_list_item_model['updated_at'] = '2021-09-05T00:25:19.599000Z'

        # Construct a json representation of a DestinationDevicesList model
        destination_devices_list_model_json = {}
        destination_devices_list_model_json['total_count'] = 38
        destination_devices_list_model_json['offset'] = 38
        destination_devices_list_model_json['limit'] = 38
        destination_devices_list_model_json['devices'] = [destination_devices_list_item_model]

        # Construct a model instance of DestinationDevicesList by calling from_dict on the json representation
        destination_devices_list_model = DestinationDevicesList.from_dict(destination_devices_list_model_json)
        assert destination_devices_list_model != False

        # Construct a model instance of DestinationDevicesList by calling from_dict on the json representation
        destination_devices_list_model_dict = DestinationDevicesList.from_dict(destination_devices_list_model_json).__dict__
        destination_devices_list_model2 = DestinationDevicesList(**destination_devices_list_model_dict)

        # Verify the model instances are equivalent
        assert destination_devices_list_model == destination_devices_list_model2

        # Convert model instance back to dict and verify no loss of data
        destination_devices_list_model_json2 = destination_devices_list_model.to_dict()
        assert destination_devices_list_model_json2 == destination_devices_list_model_json

class TestModel_DestinationDevicesListItem():
    """
    Test Class for DestinationDevicesListItem
    """

    def test_destination_devices_list_item_serialization(self):
        """
        Test serialization/deserialization for DestinationDevicesListItem
        """

        # Construct a json representation of a DestinationDevicesListItem model
        destination_devices_list_item_model_json = {}
        destination_devices_list_item_model_json['id'] = 'testString'
        destination_devices_list_item_model_json['user_id'] = 'testString'
        destination_devices_list_item_model_json['platform'] = 'testString'
        destination_devices_list_item_model_json['token'] = 'testString'
        destination_devices_list_item_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of DestinationDevicesListItem by calling from_dict on the json representation
        destination_devices_list_item_model = DestinationDevicesListItem.from_dict(destination_devices_list_item_model_json)
        assert destination_devices_list_item_model != False

        # Construct a model instance of DestinationDevicesListItem by calling from_dict on the json representation
        destination_devices_list_item_model_dict = DestinationDevicesListItem.from_dict(destination_devices_list_item_model_json).__dict__
        destination_devices_list_item_model2 = DestinationDevicesListItem(**destination_devices_list_item_model_dict)

        # Verify the model instances are equivalent
        assert destination_devices_list_item_model == destination_devices_list_item_model2

        # Convert model instance back to dict and verify no loss of data
        destination_devices_list_item_model_json2 = destination_devices_list_item_model.to_dict()
        assert destination_devices_list_item_model_json2 == destination_devices_list_item_model_json

class TestModel_DestinationDevicesReport():
    """
    Test Class for DestinationDevicesReport
    """

    def test_destination_devices_report_serialization(self):
        """
        Test serialization/deserialization for DestinationDevicesReport
        """

        # Construct a json representation of a DestinationDevicesReport model
        destination_devices_report_model_json = {}
        destination_devices_report_model_json['android'] = 26
        destination_devices_report_model_json['ios'] = 26
        destination_devices_report_model_json['chrome'] = 26
        destination_devices_report_model_json['firefox'] = 26
        destination_devices_report_model_json['safari'] = 26
        destination_devices_report_model_json['chromeAppExt'] = 26
        destination_devices_report_model_json['all'] = 26

        # Construct a model instance of DestinationDevicesReport by calling from_dict on the json representation
        destination_devices_report_model = DestinationDevicesReport.from_dict(destination_devices_report_model_json)
        assert destination_devices_report_model != False

        # Construct a model instance of DestinationDevicesReport by calling from_dict on the json representation
        destination_devices_report_model_dict = DestinationDevicesReport.from_dict(destination_devices_report_model_json).__dict__
        destination_devices_report_model2 = DestinationDevicesReport(**destination_devices_report_model_dict)

        # Verify the model instances are equivalent
        assert destination_devices_report_model == destination_devices_report_model2

        # Convert model instance back to dict and verify no loss of data
        destination_devices_report_model_json2 = destination_devices_report_model.to_dict()
        assert destination_devices_report_model_json2 == destination_devices_report_model_json

class TestModel_DestinationList():
    """
    Test Class for DestinationList
    """

    def test_destination_list_serialization(self):
        """
        Test serialization/deserialization for DestinationList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_list_item_model = {} # DestinationListItem
        destination_list_item_model['id'] = '11fe18ba-d0c8-4108-9f07-355e8052a813'
        destination_list_item_model['name'] = 'Slack Webhook'
        destination_list_item_model['description'] = 'This destination is for webhook purpose new'
        destination_list_item_model['type'] = 'webhook'
        destination_list_item_model['subscription_count'] = 2
        destination_list_item_model['subscription_names'] = ['Webhook Sub for new change']
        destination_list_item_model['updated_at'] = '2021-09-05T00:25:19.599000Z'

        # Construct a json representation of a DestinationList model
        destination_list_model_json = {}
        destination_list_model_json['total_count'] = 38
        destination_list_model_json['offset'] = 38
        destination_list_model_json['limit'] = 38
        destination_list_model_json['destinations'] = [destination_list_item_model]

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

class TestModel_DestinationListItem():
    """
    Test Class for DestinationListItem
    """

    def test_destination_list_item_serialization(self):
        """
        Test serialization/deserialization for DestinationListItem
        """

        # Construct a json representation of a DestinationListItem model
        destination_list_item_model_json = {}
        destination_list_item_model_json['id'] = 'testString'
        destination_list_item_model_json['name'] = 'testString'
        destination_list_item_model_json['description'] = 'testString'
        destination_list_item_model_json['type'] = 'webhook'
        destination_list_item_model_json['subscription_count'] = 38
        destination_list_item_model_json['subscription_names'] = ['testString']
        destination_list_item_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of DestinationListItem by calling from_dict on the json representation
        destination_list_item_model = DestinationListItem.from_dict(destination_list_item_model_json)
        assert destination_list_item_model != False

        # Construct a model instance of DestinationListItem by calling from_dict on the json representation
        destination_list_item_model_dict = DestinationListItem.from_dict(destination_list_item_model_json).__dict__
        destination_list_item_model2 = DestinationListItem(**destination_list_item_model_dict)

        # Verify the model instances are equivalent
        assert destination_list_item_model == destination_list_item_model2

        # Convert model instance back to dict and verify no loss of data
        destination_list_item_model_json2 = destination_list_item_model.to_dict()
        assert destination_list_item_model_json2 == destination_list_item_model_json

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
        destination_response_model_json['created_at'] = '2019-01-01T12:00:00Z'

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

class TestModel_DestinationTagsSubscriptionResponse():
    """
    Test Class for DestinationTagsSubscriptionResponse
    """

    def test_destination_tags_subscription_response_serialization(self):
        """
        Test serialization/deserialization for DestinationTagsSubscriptionResponse
        """

        # Construct a json representation of a DestinationTagsSubscriptionResponse model
        destination_tags_subscription_response_model_json = {}
        destination_tags_subscription_response_model_json['id'] = 'testString'
        destination_tags_subscription_response_model_json['device_id'] = 'testString'
        destination_tags_subscription_response_model_json['tag_name'] = 'testString'
        destination_tags_subscription_response_model_json['user_id'] = 'testString'
        destination_tags_subscription_response_model_json['created_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of DestinationTagsSubscriptionResponse by calling from_dict on the json representation
        destination_tags_subscription_response_model = DestinationTagsSubscriptionResponse.from_dict(destination_tags_subscription_response_model_json)
        assert destination_tags_subscription_response_model != False

        # Construct a model instance of DestinationTagsSubscriptionResponse by calling from_dict on the json representation
        destination_tags_subscription_response_model_dict = DestinationTagsSubscriptionResponse.from_dict(destination_tags_subscription_response_model_json).__dict__
        destination_tags_subscription_response_model2 = DestinationTagsSubscriptionResponse(**destination_tags_subscription_response_model_dict)

        # Verify the model instances are equivalent
        assert destination_tags_subscription_response_model == destination_tags_subscription_response_model2

        # Convert model instance back to dict and verify no loss of data
        destination_tags_subscription_response_model_json2 = destination_tags_subscription_response_model.to_dict()
        assert destination_tags_subscription_response_model_json2 == destination_tags_subscription_response_model_json

class TestModel_EmailUpdateAttributesTo():
    """
    Test Class for EmailUpdateAttributesTo
    """

    def test_email_update_attributes_to_serialization(self):
        """
        Test serialization/deserialization for EmailUpdateAttributesTo
        """

        # Construct a json representation of a EmailUpdateAttributesTo model
        email_update_attributes_to_model_json = {}
        email_update_attributes_to_model_json['add'] = ['testString']
        email_update_attributes_to_model_json['remove'] = ['testString']

        # Construct a model instance of EmailUpdateAttributesTo by calling from_dict on the json representation
        email_update_attributes_to_model = EmailUpdateAttributesTo.from_dict(email_update_attributes_to_model_json)
        assert email_update_attributes_to_model != False

        # Construct a model instance of EmailUpdateAttributesTo by calling from_dict on the json representation
        email_update_attributes_to_model_dict = EmailUpdateAttributesTo.from_dict(email_update_attributes_to_model_json).__dict__
        email_update_attributes_to_model2 = EmailUpdateAttributesTo(**email_update_attributes_to_model_dict)

        # Verify the model instances are equivalent
        assert email_update_attributes_to_model == email_update_attributes_to_model2

        # Convert model instance back to dict and verify no loss of data
        email_update_attributes_to_model_json2 = email_update_attributes_to_model.to_dict()
        assert email_update_attributes_to_model_json2 == email_update_attributes_to_model_json

class TestModel_EmailUpdateAttributesUnsubscribed():
    """
    Test Class for EmailUpdateAttributesUnsubscribed
    """

    def test_email_update_attributes_unsubscribed_serialization(self):
        """
        Test serialization/deserialization for EmailUpdateAttributesUnsubscribed
        """

        # Construct a json representation of a EmailUpdateAttributesUnsubscribed model
        email_update_attributes_unsubscribed_model_json = {}
        email_update_attributes_unsubscribed_model_json['remove'] = ['testString']

        # Construct a model instance of EmailUpdateAttributesUnsubscribed by calling from_dict on the json representation
        email_update_attributes_unsubscribed_model = EmailUpdateAttributesUnsubscribed.from_dict(email_update_attributes_unsubscribed_model_json)
        assert email_update_attributes_unsubscribed_model != False

        # Construct a model instance of EmailUpdateAttributesUnsubscribed by calling from_dict on the json representation
        email_update_attributes_unsubscribed_model_dict = EmailUpdateAttributesUnsubscribed.from_dict(email_update_attributes_unsubscribed_model_json).__dict__
        email_update_attributes_unsubscribed_model2 = EmailUpdateAttributesUnsubscribed(**email_update_attributes_unsubscribed_model_dict)

        # Verify the model instances are equivalent
        assert email_update_attributes_unsubscribed_model == email_update_attributes_unsubscribed_model2

        # Convert model instance back to dict and verify no loss of data
        email_update_attributes_unsubscribed_model_json2 = email_update_attributes_unsubscribed_model.to_dict()
        assert email_update_attributes_unsubscribed_model_json2 == email_update_attributes_unsubscribed_model_json

class TestModel_NotificationCreate():
    """
    Test Class for NotificationCreate
    """

    def test_notification_create_serialization(self):
        """
        Test serialization/deserialization for NotificationCreate
        """

        # Construct a json representation of a NotificationCreate model
        notification_create_model_json = {}
        notification_create_model_json['data'] = {}
        notification_create_model_json['ibmenseverity'] = 'testString'
        notification_create_model_json['ibmenfcmbody'] = 'testString'
        notification_create_model_json['ibmenapnsbody'] = 'testString'
        notification_create_model_json['ibmensafaribody'] = 'testString'
        notification_create_model_json['ibmenpushto'] = '{"fcm_devices":["9c75975a-37d0-3898-905d-3b5ee0d7c172","C9CACDF5-6EBF-49E1-AD60-E25BA23E954C"],"apns_devices":["3423-37d0-3898-905d-42342","432423-6EBF-49E1-AD60-4234"],"user_ids":["user-1","user-2"],"tags":["tag-1","tag-2"],"platforms":["push_android","push_ios","push_chrome","push_firefox"]}'
        notification_create_model_json['ibmenapnsheaders'] = 'testString'
        notification_create_model_json['ibmendefaultshort'] = 'testString'
        notification_create_model_json['ibmendefaultlong'] = 'testString'
        notification_create_model_json['ibmenchromebody'] = 'testString'
        notification_create_model_json['ibmenfirefoxbody'] = 'testString'
        notification_create_model_json['ibmenchromeheaders'] = 'testString'
        notification_create_model_json['ibmenfirefoxheaders'] = 'testString'
        notification_create_model_json['ibmensourceid'] = 'testString'
        notification_create_model_json['datacontenttype'] = 'application/json'
        notification_create_model_json['subject'] = 'testString'
        notification_create_model_json['id'] = 'testString'
        notification_create_model_json['source'] = 'testString'
        notification_create_model_json['type'] = 'testString'
        notification_create_model_json['specversion'] = '1.0'
        notification_create_model_json['time'] = 'testString'
        notification_create_model_json['foo'] = 'testString'

        # Construct a model instance of NotificationCreate by calling from_dict on the json representation
        notification_create_model = NotificationCreate.from_dict(notification_create_model_json)
        assert notification_create_model != False

        # Construct a model instance of NotificationCreate by calling from_dict on the json representation
        notification_create_model_dict = NotificationCreate.from_dict(notification_create_model_json).__dict__
        notification_create_model2 = NotificationCreate(**notification_create_model_dict)

        # Verify the model instances are equivalent
        assert notification_create_model == notification_create_model2

        # Convert model instance back to dict and verify no loss of data
        notification_create_model_json2 = notification_create_model.to_dict()
        assert notification_create_model_json2 == notification_create_model_json

        # Test get_properties and set_properties methods.
        notification_create_model.set_properties({})
        actual_dict = notification_create_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        notification_create_model.set_properties(expected_dict)
        actual_dict = notification_create_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_NotificationResponse():
    """
    Test Class for NotificationResponse
    """

    def test_notification_response_serialization(self):
        """
        Test serialization/deserialization for NotificationResponse
        """

        # Construct a json representation of a NotificationResponse model
        notification_response_model_json = {}
        notification_response_model_json['notification_id'] = 'testString'

        # Construct a model instance of NotificationResponse by calling from_dict on the json representation
        notification_response_model = NotificationResponse.from_dict(notification_response_model_json)
        assert notification_response_model != False

        # Construct a model instance of NotificationResponse by calling from_dict on the json representation
        notification_response_model_dict = NotificationResponse.from_dict(notification_response_model_json).__dict__
        notification_response_model2 = NotificationResponse(**notification_response_model_dict)

        # Verify the model instances are equivalent
        assert notification_response_model == notification_response_model2

        # Convert model instance back to dict and verify no loss of data
        notification_response_model_json2 = notification_response_model.to_dict()
        assert notification_response_model_json2 == notification_response_model_json

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
        source_model_json['updated_at'] = '2019-01-01T12:00:00Z'
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

        source_list_item_model = {} # SourceListItem
        source_list_item_model['id'] = '00bb34e5-b8c1-4159-af15-8bc6980c3ab2:api'
        source_list_item_model['name'] = 'CloudEvents Source'
        source_list_item_model['description'] = 'This source is related cloud events'
        source_list_item_model['type'] = 'api'
        source_list_item_model['enabled'] = True
        source_list_item_model['updated_at'] = '2021-08-19T05:30:03.696000Z'
        source_list_item_model['topic_count'] = 0

        # Construct a json representation of a SourceList model
        source_list_model_json = {}
        source_list_model_json['total_count'] = 0
        source_list_model_json['offset'] = 38
        source_list_model_json['limit'] = 38
        source_list_model_json['sources'] = [source_list_item_model]

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

class TestModel_SourceListItem():
    """
    Test Class for SourceListItem
    """

    def test_source_list_item_serialization(self):
        """
        Test serialization/deserialization for SourceListItem
        """

        # Construct a json representation of a SourceListItem model
        source_list_item_model_json = {}
        source_list_item_model_json['id'] = 'testString'
        source_list_item_model_json['name'] = 'testString'
        source_list_item_model_json['description'] = 'testString'
        source_list_item_model_json['type'] = 'testString'
        source_list_item_model_json['enabled'] = True
        source_list_item_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        source_list_item_model_json['topic_count'] = 0

        # Construct a model instance of SourceListItem by calling from_dict on the json representation
        source_list_item_model = SourceListItem.from_dict(source_list_item_model_json)
        assert source_list_item_model != False

        # Construct a model instance of SourceListItem by calling from_dict on the json representation
        source_list_item_model_dict = SourceListItem.from_dict(source_list_item_model_json).__dict__
        source_list_item_model2 = SourceListItem(**source_list_item_model_dict)

        # Verify the model instances are equivalent
        assert source_list_item_model == source_list_item_model2

        # Convert model instance back to dict and verify no loss of data
        source_list_item_model_json2 = source_list_item_model.to_dict()
        assert source_list_item_model_json2 == source_list_item_model_json

class TestModel_SourceResponse():
    """
    Test Class for SourceResponse
    """

    def test_source_response_serialization(self):
        """
        Test serialization/deserialization for SourceResponse
        """

        # Construct a json representation of a SourceResponse model
        source_response_model_json = {}
        source_response_model_json['id'] = 'testString'
        source_response_model_json['name'] = 'testString'
        source_response_model_json['description'] = 'testString'
        source_response_model_json['enabled'] = True
        source_response_model_json['created_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of SourceResponse by calling from_dict on the json representation
        source_response_model = SourceResponse.from_dict(source_response_model_json)
        assert source_response_model != False

        # Construct a model instance of SourceResponse by calling from_dict on the json representation
        source_response_model_dict = SourceResponse.from_dict(source_response_model_json).__dict__
        source_response_model2 = SourceResponse(**source_response_model_dict)

        # Verify the model instances are equivalent
        assert source_response_model == source_response_model2

        # Convert model instance back to dict and verify no loss of data
        source_response_model_json2 = source_response_model.to_dict()
        assert source_response_model_json2 == source_response_model_json

class TestModel_SourcesListItem():
    """
    Test Class for SourcesListItem
    """

    def test_sources_list_item_serialization(self):
        """
        Test serialization/deserialization for SourcesListItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_get_model = {} # RulesGet
        rules_get_model['enabled'] = True
        rules_get_model['event_type_filter'] = '$.*'
        rules_get_model['notification_filter'] = 'testString'
        rules_get_model['updated_at'] = 'testString'
        rules_get_model['id'] = 'testString'

        # Construct a json representation of a SourcesListItem model
        sources_list_item_model_json = {}
        sources_list_item_model_json['id'] = 'testString'
        sources_list_item_model_json['name'] = 'testString'
        sources_list_item_model_json['rules'] = [rules_get_model]

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

        subscription_attributes_model = {} # SubscriptionAttributesWebhookAttributesResponse
        subscription_attributes_model['signing_enabled'] = True
        subscription_attributes_model['add_notification_payload'] = True
        subscription_attributes_model['reply_to_mail'] = 'example@ibm.com'
        subscription_attributes_model['reply_to_name'] = 'USA news'
        subscription_attributes_model['from_name'] = 'IBM'
        subscription_attributes_model['to'] = '[{"email":"example1@gmail.com","time":"2021-11-26T12:36:27.693544+05:30"}]'
        subscription_attributes_model['unsubscribed'] = '[]'
        subscription_attributes_model['invited'] = '[]'

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
        subscription_list_item_model['updated_at'] = '2021-08-18T09:50:32.133000Z'

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
        subscription_list_item_model_json['updated_at'] = '2019-01-01T12:00:00Z'

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

class TestModel_TagsSubscriptionList():
    """
    Test Class for TagsSubscriptionList
    """

    def test_tags_subscription_list_serialization(self):
        """
        Test serialization/deserialization for TagsSubscriptionList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tags_subscription_list_item_model = {} # TagsSubscriptionListItem
        tags_subscription_list_item_model['id'] = 'nkjl-d0c8-4108-9f07-890'
        tags_subscription_list_item_model['device_id'] = '11fe18ba-d0c8-4108-9f07-355e8052a813'
        tags_subscription_list_item_model['tag_name'] = 'Slack_Webhook'
        tags_subscription_list_item_model['user_id'] = 'fcm_id_123'
        tags_subscription_list_item_model['updated_at'] = '2021-09-05T00:25:19.599000Z'

        # Construct a json representation of a TagsSubscriptionList model
        tags_subscription_list_model_json = {}
        tags_subscription_list_model_json['total_count'] = 38
        tags_subscription_list_model_json['offset'] = 38
        tags_subscription_list_model_json['limit'] = 38
        tags_subscription_list_model_json['tag_subscriptions'] = [tags_subscription_list_item_model]

        # Construct a model instance of TagsSubscriptionList by calling from_dict on the json representation
        tags_subscription_list_model = TagsSubscriptionList.from_dict(tags_subscription_list_model_json)
        assert tags_subscription_list_model != False

        # Construct a model instance of TagsSubscriptionList by calling from_dict on the json representation
        tags_subscription_list_model_dict = TagsSubscriptionList.from_dict(tags_subscription_list_model_json).__dict__
        tags_subscription_list_model2 = TagsSubscriptionList(**tags_subscription_list_model_dict)

        # Verify the model instances are equivalent
        assert tags_subscription_list_model == tags_subscription_list_model2

        # Convert model instance back to dict and verify no loss of data
        tags_subscription_list_model_json2 = tags_subscription_list_model.to_dict()
        assert tags_subscription_list_model_json2 == tags_subscription_list_model_json

class TestModel_TagsSubscriptionListItem():
    """
    Test Class for TagsSubscriptionListItem
    """

    def test_tags_subscription_list_item_serialization(self):
        """
        Test serialization/deserialization for TagsSubscriptionListItem
        """

        # Construct a json representation of a TagsSubscriptionListItem model
        tags_subscription_list_item_model_json = {}
        tags_subscription_list_item_model_json['id'] = 'testString'
        tags_subscription_list_item_model_json['device_id'] = 'testString'
        tags_subscription_list_item_model_json['tag_name'] = 'testString'
        tags_subscription_list_item_model_json['user_id'] = 'testString'
        tags_subscription_list_item_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of TagsSubscriptionListItem by calling from_dict on the json representation
        tags_subscription_list_item_model = TagsSubscriptionListItem.from_dict(tags_subscription_list_item_model_json)
        assert tags_subscription_list_item_model != False

        # Construct a model instance of TagsSubscriptionListItem by calling from_dict on the json representation
        tags_subscription_list_item_model_dict = TagsSubscriptionListItem.from_dict(tags_subscription_list_item_model_json).__dict__
        tags_subscription_list_item_model2 = TagsSubscriptionListItem(**tags_subscription_list_item_model_dict)

        # Verify the model instances are equivalent
        assert tags_subscription_list_item_model == tags_subscription_list_item_model2

        # Convert model instance back to dict and verify no loss of data
        tags_subscription_list_item_model_json2 = tags_subscription_list_item_model.to_dict()
        assert tags_subscription_list_item_model_json2 == tags_subscription_list_item_model_json

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

        sources_list_item_model = {} # SourcesListItem
        sources_list_item_model['id'] = '96dbf538-9fa7-4745-b9e4-32bb6f1dc47a:api'
        sources_list_item_model['name'] = 'Compliance source'
        sources_list_item_model['rules'] = [rules_get_model]

        subscription_list_item_model = {} # SubscriptionListItem
        subscription_list_item_model['id'] = '87bef75e-f826-4aa9-b64d-91af9be5e12b'
        subscription_list_item_model['name'] = 'SMS Subscription on new change'
        subscription_list_item_model['description'] = 'This subscription is to send events from SCC to EN Admins via sms'
        subscription_list_item_model['destination_id'] = 'ec28efee-2236-4c2d-8839-d34f697cfc69'
        subscription_list_item_model['destination_name'] = 'testString'
        subscription_list_item_model['destination_type'] = 'sms_ibm'
        subscription_list_item_model['topic_id'] = '7b23362d-6d48-47ef-847a-c8b291220306'
        subscription_list_item_model['topic_name'] = 'testString'
        subscription_list_item_model['updated_at'] = '2021-08-20T10:08:46.060000Z'

        # Construct a json representation of a Topic model
        topic_model_json = {}
        topic_model_json['id'] = 'testString'
        topic_model_json['description'] = 'testString'
        topic_model_json['name'] = 'testString'
        topic_model_json['updated_at'] = 'testString'
        topic_model_json['source_count'] = 38
        topic_model_json['sources'] = [sources_list_item_model]
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

class TestModel_DestinationConfigParamsChromeDestinationConfig():
    """
    Test Class for DestinationConfigParamsChromeDestinationConfig
    """

    def test_destination_config_params_chrome_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigParamsChromeDestinationConfig
        """

        # Construct a json representation of a DestinationConfigParamsChromeDestinationConfig model
        destination_config_params_chrome_destination_config_model_json = {}
        destination_config_params_chrome_destination_config_model_json['api_key'] = 'testString'
        destination_config_params_chrome_destination_config_model_json['website_url'] = 'testString'
        destination_config_params_chrome_destination_config_model_json['public_key'] = 'testString'

        # Construct a model instance of DestinationConfigParamsChromeDestinationConfig by calling from_dict on the json representation
        destination_config_params_chrome_destination_config_model = DestinationConfigParamsChromeDestinationConfig.from_dict(destination_config_params_chrome_destination_config_model_json)
        assert destination_config_params_chrome_destination_config_model != False

        # Construct a model instance of DestinationConfigParamsChromeDestinationConfig by calling from_dict on the json representation
        destination_config_params_chrome_destination_config_model_dict = DestinationConfigParamsChromeDestinationConfig.from_dict(destination_config_params_chrome_destination_config_model_json).__dict__
        destination_config_params_chrome_destination_config_model2 = DestinationConfigParamsChromeDestinationConfig(**destination_config_params_chrome_destination_config_model_dict)

        # Verify the model instances are equivalent
        assert destination_config_params_chrome_destination_config_model == destination_config_params_chrome_destination_config_model2

        # Convert model instance back to dict and verify no loss of data
        destination_config_params_chrome_destination_config_model_json2 = destination_config_params_chrome_destination_config_model.to_dict()
        assert destination_config_params_chrome_destination_config_model_json2 == destination_config_params_chrome_destination_config_model_json

class TestModel_DestinationConfigParamsFCMDestinationConfig():
    """
    Test Class for DestinationConfigParamsFCMDestinationConfig
    """

    def test_destination_config_params_fcm_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigParamsFCMDestinationConfig
        """

        # Construct a json representation of a DestinationConfigParamsFCMDestinationConfig model
        destination_config_params_fcm_destination_config_model_json = {}
        destination_config_params_fcm_destination_config_model_json['server_key'] = 'testString'
        destination_config_params_fcm_destination_config_model_json['sender_id'] = 'testString'

        # Construct a model instance of DestinationConfigParamsFCMDestinationConfig by calling from_dict on the json representation
        destination_config_params_fcm_destination_config_model = DestinationConfigParamsFCMDestinationConfig.from_dict(destination_config_params_fcm_destination_config_model_json)
        assert destination_config_params_fcm_destination_config_model != False

        # Construct a model instance of DestinationConfigParamsFCMDestinationConfig by calling from_dict on the json representation
        destination_config_params_fcm_destination_config_model_dict = DestinationConfigParamsFCMDestinationConfig.from_dict(destination_config_params_fcm_destination_config_model_json).__dict__
        destination_config_params_fcm_destination_config_model2 = DestinationConfigParamsFCMDestinationConfig(**destination_config_params_fcm_destination_config_model_dict)

        # Verify the model instances are equivalent
        assert destination_config_params_fcm_destination_config_model == destination_config_params_fcm_destination_config_model2

        # Convert model instance back to dict and verify no loss of data
        destination_config_params_fcm_destination_config_model_json2 = destination_config_params_fcm_destination_config_model.to_dict()
        assert destination_config_params_fcm_destination_config_model_json2 == destination_config_params_fcm_destination_config_model_json

class TestModel_DestinationConfigParamsFirefoxDestinationConfig():
    """
    Test Class for DestinationConfigParamsFirefoxDestinationConfig
    """

    def test_destination_config_params_firefox_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigParamsFirefoxDestinationConfig
        """

        # Construct a json representation of a DestinationConfigParamsFirefoxDestinationConfig model
        destination_config_params_firefox_destination_config_model_json = {}
        destination_config_params_firefox_destination_config_model_json['website_url'] = 'testString'
        destination_config_params_firefox_destination_config_model_json['public_key'] = 'testString'

        # Construct a model instance of DestinationConfigParamsFirefoxDestinationConfig by calling from_dict on the json representation
        destination_config_params_firefox_destination_config_model = DestinationConfigParamsFirefoxDestinationConfig.from_dict(destination_config_params_firefox_destination_config_model_json)
        assert destination_config_params_firefox_destination_config_model != False

        # Construct a model instance of DestinationConfigParamsFirefoxDestinationConfig by calling from_dict on the json representation
        destination_config_params_firefox_destination_config_model_dict = DestinationConfigParamsFirefoxDestinationConfig.from_dict(destination_config_params_firefox_destination_config_model_json).__dict__
        destination_config_params_firefox_destination_config_model2 = DestinationConfigParamsFirefoxDestinationConfig(**destination_config_params_firefox_destination_config_model_dict)

        # Verify the model instances are equivalent
        assert destination_config_params_firefox_destination_config_model == destination_config_params_firefox_destination_config_model2

        # Convert model instance back to dict and verify no loss of data
        destination_config_params_firefox_destination_config_model_json2 = destination_config_params_firefox_destination_config_model.to_dict()
        assert destination_config_params_firefox_destination_config_model_json2 == destination_config_params_firefox_destination_config_model_json

class TestModel_DestinationConfigParamsIOSDestinationConfig():
    """
    Test Class for DestinationConfigParamsIOSDestinationConfig
    """

    def test_destination_config_params_ios_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigParamsIOSDestinationConfig
        """

        # Construct a json representation of a DestinationConfigParamsIOSDestinationConfig model
        destination_config_params_ios_destination_config_model_json = {}
        destination_config_params_ios_destination_config_model_json['cert_type'] = 'p8'
        destination_config_params_ios_destination_config_model_json['is_sandbox'] = False
        destination_config_params_ios_destination_config_model_json['password'] = 'testString'
        destination_config_params_ios_destination_config_model_json['key_id'] = 'testString'
        destination_config_params_ios_destination_config_model_json['team_id'] = 'testString'
        destination_config_params_ios_destination_config_model_json['bundle_id'] = 'testString'

        # Construct a model instance of DestinationConfigParamsIOSDestinationConfig by calling from_dict on the json representation
        destination_config_params_ios_destination_config_model = DestinationConfigParamsIOSDestinationConfig.from_dict(destination_config_params_ios_destination_config_model_json)
        assert destination_config_params_ios_destination_config_model != False

        # Construct a model instance of DestinationConfigParamsIOSDestinationConfig by calling from_dict on the json representation
        destination_config_params_ios_destination_config_model_dict = DestinationConfigParamsIOSDestinationConfig.from_dict(destination_config_params_ios_destination_config_model_json).__dict__
        destination_config_params_ios_destination_config_model2 = DestinationConfigParamsIOSDestinationConfig(**destination_config_params_ios_destination_config_model_dict)

        # Verify the model instances are equivalent
        assert destination_config_params_ios_destination_config_model == destination_config_params_ios_destination_config_model2

        # Convert model instance back to dict and verify no loss of data
        destination_config_params_ios_destination_config_model_json2 = destination_config_params_ios_destination_config_model.to_dict()
        assert destination_config_params_ios_destination_config_model_json2 == destination_config_params_ios_destination_config_model_json

class TestModel_DestinationConfigParamsSafariDestinationConfig():
    """
    Test Class for DestinationConfigParamsSafariDestinationConfig
    """

    def test_destination_config_params_safari_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigParamsSafariDestinationConfig
        """

        # Construct a json representation of a DestinationConfigParamsSafariDestinationConfig model
        destination_config_params_safari_destination_config_model_json = {}
        destination_config_params_safari_destination_config_model_json['cert_type'] = 'p12'
        destination_config_params_safari_destination_config_model_json['password'] = 'testString'
        destination_config_params_safari_destination_config_model_json['website_url'] = 'testString'
        destination_config_params_safari_destination_config_model_json['website_name'] = 'testString'
        destination_config_params_safari_destination_config_model_json['url_format_string'] = 'testString'
        destination_config_params_safari_destination_config_model_json['website_push_id'] = 'testString'

        # Construct a model instance of DestinationConfigParamsSafariDestinationConfig by calling from_dict on the json representation
        destination_config_params_safari_destination_config_model = DestinationConfigParamsSafariDestinationConfig.from_dict(destination_config_params_safari_destination_config_model_json)
        assert destination_config_params_safari_destination_config_model != False

        # Construct a model instance of DestinationConfigParamsSafariDestinationConfig by calling from_dict on the json representation
        destination_config_params_safari_destination_config_model_dict = DestinationConfigParamsSafariDestinationConfig.from_dict(destination_config_params_safari_destination_config_model_json).__dict__
        destination_config_params_safari_destination_config_model2 = DestinationConfigParamsSafariDestinationConfig(**destination_config_params_safari_destination_config_model_dict)

        # Verify the model instances are equivalent
        assert destination_config_params_safari_destination_config_model == destination_config_params_safari_destination_config_model2

        # Convert model instance back to dict and verify no loss of data
        destination_config_params_safari_destination_config_model_json2 = destination_config_params_safari_destination_config_model.to_dict()
        assert destination_config_params_safari_destination_config_model_json2 == destination_config_params_safari_destination_config_model_json

class TestModel_DestinationConfigParamsSlackDestinationConfig():
    """
    Test Class for DestinationConfigParamsSlackDestinationConfig
    """

    def test_destination_config_params_slack_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigParamsSlackDestinationConfig
        """

        # Construct a json representation of a DestinationConfigParamsSlackDestinationConfig model
        destination_config_params_slack_destination_config_model_json = {}
        destination_config_params_slack_destination_config_model_json['url'] = 'testString'

        # Construct a model instance of DestinationConfigParamsSlackDestinationConfig by calling from_dict on the json representation
        destination_config_params_slack_destination_config_model = DestinationConfigParamsSlackDestinationConfig.from_dict(destination_config_params_slack_destination_config_model_json)
        assert destination_config_params_slack_destination_config_model != False

        # Construct a model instance of DestinationConfigParamsSlackDestinationConfig by calling from_dict on the json representation
        destination_config_params_slack_destination_config_model_dict = DestinationConfigParamsSlackDestinationConfig.from_dict(destination_config_params_slack_destination_config_model_json).__dict__
        destination_config_params_slack_destination_config_model2 = DestinationConfigParamsSlackDestinationConfig(**destination_config_params_slack_destination_config_model_dict)

        # Verify the model instances are equivalent
        assert destination_config_params_slack_destination_config_model == destination_config_params_slack_destination_config_model2

        # Convert model instance back to dict and verify no loss of data
        destination_config_params_slack_destination_config_model_json2 = destination_config_params_slack_destination_config_model.to_dict()
        assert destination_config_params_slack_destination_config_model_json2 == destination_config_params_slack_destination_config_model_json

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
        subscription_attributes_email_attributes_response_model_json['foo'] = 'testString'

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

        # Test get_properties and set_properties methods.
        subscription_attributes_email_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_email_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_email_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_email_attributes_response_model.get_properties()
        assert actual_dict == expected_dict

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
        subscription_attributes_sms_attributes_response_model_json['foo'] = 'testString'

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

        # Test get_properties and set_properties methods.
        subscription_attributes_sms_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_sms_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_sms_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_sms_attributes_response_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_SubscriptionAttributesSlackAttributesResponse():
    """
    Test Class for SubscriptionAttributesSlackAttributesResponse
    """

    def test_subscription_attributes_slack_attributes_response_serialization(self):
        """
        Test serialization/deserialization for SubscriptionAttributesSlackAttributesResponse
        """

        # Construct a json representation of a SubscriptionAttributesSlackAttributesResponse model
        subscription_attributes_slack_attributes_response_model_json = {}
        subscription_attributes_slack_attributes_response_model_json['attachment_color'] = 'testString'
        subscription_attributes_slack_attributes_response_model_json['foo'] = 'testString'

        # Construct a model instance of SubscriptionAttributesSlackAttributesResponse by calling from_dict on the json representation
        subscription_attributes_slack_attributes_response_model = SubscriptionAttributesSlackAttributesResponse.from_dict(subscription_attributes_slack_attributes_response_model_json)
        assert subscription_attributes_slack_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesSlackAttributesResponse by calling from_dict on the json representation
        subscription_attributes_slack_attributes_response_model_dict = SubscriptionAttributesSlackAttributesResponse.from_dict(subscription_attributes_slack_attributes_response_model_json).__dict__
        subscription_attributes_slack_attributes_response_model2 = SubscriptionAttributesSlackAttributesResponse(**subscription_attributes_slack_attributes_response_model_dict)

        # Verify the model instances are equivalent
        assert subscription_attributes_slack_attributes_response_model == subscription_attributes_slack_attributes_response_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_slack_attributes_response_model_json2 = subscription_attributes_slack_attributes_response_model.to_dict()
        assert subscription_attributes_slack_attributes_response_model_json2 == subscription_attributes_slack_attributes_response_model_json

        # Test get_properties and set_properties methods.
        subscription_attributes_slack_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_slack_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_slack_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_slack_attributes_response_model.get_properties()
        assert actual_dict == expected_dict

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
        subscription_attributes_webhook_attributes_response_model_json['foo'] = 'testString'

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

        # Test get_properties and set_properties methods.
        subscription_attributes_webhook_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_webhook_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_webhook_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_webhook_attributes_response_model.get_properties()
        assert actual_dict == expected_dict

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

class TestModel_SubscriptionCreateAttributesFCMAttributes():
    """
    Test Class for SubscriptionCreateAttributesFCMAttributes
    """

    def test_subscription_create_attributes_fcm_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesFCMAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesFCMAttributes model
        subscription_create_attributes_fcm_attributes_model_json = {}

        # Construct a model instance of SubscriptionCreateAttributesFCMAttributes by calling from_dict on the json representation
        subscription_create_attributes_fcm_attributes_model = SubscriptionCreateAttributesFCMAttributes.from_dict(subscription_create_attributes_fcm_attributes_model_json)
        assert subscription_create_attributes_fcm_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesFCMAttributes by calling from_dict on the json representation
        subscription_create_attributes_fcm_attributes_model_dict = SubscriptionCreateAttributesFCMAttributes.from_dict(subscription_create_attributes_fcm_attributes_model_json).__dict__
        subscription_create_attributes_fcm_attributes_model2 = SubscriptionCreateAttributesFCMAttributes(**subscription_create_attributes_fcm_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_create_attributes_fcm_attributes_model == subscription_create_attributes_fcm_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_fcm_attributes_model_json2 = subscription_create_attributes_fcm_attributes_model.to_dict()
        assert subscription_create_attributes_fcm_attributes_model_json2 == subscription_create_attributes_fcm_attributes_model_json

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

class TestModel_SubscriptionCreateAttributesSlackAttributes():
    """
    Test Class for SubscriptionCreateAttributesSlackAttributes
    """

    def test_subscription_create_attributes_slack_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesSlackAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesSlackAttributes model
        subscription_create_attributes_slack_attributes_model_json = {}
        subscription_create_attributes_slack_attributes_model_json['attachment_color'] = 'testString'

        # Construct a model instance of SubscriptionCreateAttributesSlackAttributes by calling from_dict on the json representation
        subscription_create_attributes_slack_attributes_model = SubscriptionCreateAttributesSlackAttributes.from_dict(subscription_create_attributes_slack_attributes_model_json)
        assert subscription_create_attributes_slack_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesSlackAttributes by calling from_dict on the json representation
        subscription_create_attributes_slack_attributes_model_dict = SubscriptionCreateAttributesSlackAttributes.from_dict(subscription_create_attributes_slack_attributes_model_json).__dict__
        subscription_create_attributes_slack_attributes_model2 = SubscriptionCreateAttributesSlackAttributes(**subscription_create_attributes_slack_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_create_attributes_slack_attributes_model == subscription_create_attributes_slack_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_slack_attributes_model_json2 = subscription_create_attributes_slack_attributes_model.to_dict()
        assert subscription_create_attributes_slack_attributes_model_json2 == subscription_create_attributes_slack_attributes_model_json

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

class TestModel_SubscriptionUpdateAttributesEmailUpdateAttributes():
    """
    Test Class for SubscriptionUpdateAttributesEmailUpdateAttributes
    """

    def test_subscription_update_attributes_email_update_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesEmailUpdateAttributes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        email_update_attributes_to_model = {} # EmailUpdateAttributesTo
        email_update_attributes_to_model['add'] = ['testString']
        email_update_attributes_to_model['remove'] = ['testString']

        email_update_attributes_unsubscribed_model = {} # EmailUpdateAttributesUnsubscribed
        email_update_attributes_unsubscribed_model['remove'] = ['testString']

        # Construct a json representation of a SubscriptionUpdateAttributesEmailUpdateAttributes model
        subscription_update_attributes_email_update_attributes_model_json = {}
        subscription_update_attributes_email_update_attributes_model_json['to'] = email_update_attributes_to_model
        subscription_update_attributes_email_update_attributes_model_json['add_notification_payload'] = False
        subscription_update_attributes_email_update_attributes_model_json['reply_to_mail'] = 'testString'
        subscription_update_attributes_email_update_attributes_model_json['reply_to_name'] = 'testString'
        subscription_update_attributes_email_update_attributes_model_json['from_name'] = 'testString'
        subscription_update_attributes_email_update_attributes_model_json['invited'] = ['testString']
        subscription_update_attributes_email_update_attributes_model_json['unsubscribed'] = email_update_attributes_unsubscribed_model

        # Construct a model instance of SubscriptionUpdateAttributesEmailUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_email_update_attributes_model = SubscriptionUpdateAttributesEmailUpdateAttributes.from_dict(subscription_update_attributes_email_update_attributes_model_json)
        assert subscription_update_attributes_email_update_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesEmailUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_email_update_attributes_model_dict = SubscriptionUpdateAttributesEmailUpdateAttributes.from_dict(subscription_update_attributes_email_update_attributes_model_json).__dict__
        subscription_update_attributes_email_update_attributes_model2 = SubscriptionUpdateAttributesEmailUpdateAttributes(**subscription_update_attributes_email_update_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_update_attributes_email_update_attributes_model == subscription_update_attributes_email_update_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_email_update_attributes_model_json2 = subscription_update_attributes_email_update_attributes_model.to_dict()
        assert subscription_update_attributes_email_update_attributes_model_json2 == subscription_update_attributes_email_update_attributes_model_json

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

class TestModel_SubscriptionUpdateAttributesSlackAttributes():
    """
    Test Class for SubscriptionUpdateAttributesSlackAttributes
    """

    def test_subscription_update_attributes_slack_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesSlackAttributes
        """

        # Construct a json representation of a SubscriptionUpdateAttributesSlackAttributes model
        subscription_update_attributes_slack_attributes_model_json = {}
        subscription_update_attributes_slack_attributes_model_json['attachment_color'] = 'testString'

        # Construct a model instance of SubscriptionUpdateAttributesSlackAttributes by calling from_dict on the json representation
        subscription_update_attributes_slack_attributes_model = SubscriptionUpdateAttributesSlackAttributes.from_dict(subscription_update_attributes_slack_attributes_model_json)
        assert subscription_update_attributes_slack_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesSlackAttributes by calling from_dict on the json representation
        subscription_update_attributes_slack_attributes_model_dict = SubscriptionUpdateAttributesSlackAttributes.from_dict(subscription_update_attributes_slack_attributes_model_json).__dict__
        subscription_update_attributes_slack_attributes_model2 = SubscriptionUpdateAttributesSlackAttributes(**subscription_update_attributes_slack_attributes_model_dict)

        # Verify the model instances are equivalent
        assert subscription_update_attributes_slack_attributes_model == subscription_update_attributes_slack_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_slack_attributes_model_json2 = subscription_update_attributes_slack_attributes_model.to_dict()
        assert subscription_update_attributes_slack_attributes_model_json2 == subscription_update_attributes_slack_attributes_model_json

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
