# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2024.
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


_service = EventNotificationsV1(authenticator=NoAuthAuthenticator())

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
# Start of Service: Metrics
##############################################################################
# region


class TestNewInstance:
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


class TestGetMetrics:
    """
    Test Class for get_metrics
    """

    @responses.activate
    def test_get_metrics_all_params(self):
        """
        get_metrics()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/metrics')
        mock_response = '{"metrics": [{"key": "bounced", "doc_count": 9, "histogram": {"buckets": [{"doc_count": 9, "key_as_string": "2019-01-01T12:00:00.000Z"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        destination_type = 'smtp_custom'
        gte = 'testString'
        lte = 'testString'
        id = 'testString'
        email_to = 'testString'
        notification_id = 'testString'
        subject = 'testString'

        # Invoke method
        response = _service.get_metrics(
            instance_id,
            destination_type,
            gte,
            lte,
            id=id,
            email_to=email_to,
            notification_id=notification_id,
            subject=subject,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'destination_type={}'.format(destination_type) in query_string
        assert 'gte={}'.format(gte) in query_string
        assert 'lte={}'.format(lte) in query_string
        assert 'id={}'.format(id) in query_string
        assert 'email_to={}'.format(email_to) in query_string
        assert 'notification_id={}'.format(notification_id) in query_string
        assert 'subject={}'.format(subject) in query_string

    def test_get_metrics_all_params_with_retries(self):
        # Enable retries and run test_get_metrics_all_params.
        _service.enable_retries()
        self.test_get_metrics_all_params()

        # Disable retries and run test_get_metrics_all_params.
        _service.disable_retries()
        self.test_get_metrics_all_params()

    @responses.activate
    def test_get_metrics_required_params(self):
        """
        test_get_metrics_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/metrics')
        mock_response = '{"metrics": [{"key": "bounced", "doc_count": 9, "histogram": {"buckets": [{"doc_count": 9, "key_as_string": "2019-01-01T12:00:00.000Z"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        destination_type = 'smtp_custom'
        gte = 'testString'
        lte = 'testString'

        # Invoke method
        response = _service.get_metrics(
            instance_id,
            destination_type,
            gte,
            lte,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'destination_type={}'.format(destination_type) in query_string
        assert 'gte={}'.format(gte) in query_string
        assert 'lte={}'.format(lte) in query_string

    def test_get_metrics_required_params_with_retries(self):
        # Enable retries and run test_get_metrics_required_params.
        _service.enable_retries()
        self.test_get_metrics_required_params()

        # Disable retries and run test_get_metrics_required_params.
        _service.disable_retries()
        self.test_get_metrics_required_params()

    @responses.activate
    def test_get_metrics_value_error(self):
        """
        test_get_metrics_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/metrics')
        mock_response = '{"metrics": [{"key": "bounced", "doc_count": 9, "histogram": {"buckets": [{"doc_count": 9, "key_as_string": "2019-01-01T12:00:00.000Z"}]}}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        destination_type = 'smtp_custom'
        gte = 'testString'
        lte = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "destination_type": destination_type,
            "gte": gte,
            "lte": lte,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_metrics(**req_copy)

    def test_get_metrics_value_error_with_retries(self):
        # Enable retries and run test_get_metrics_value_error.
        _service.enable_retries()
        self.test_get_metrics_value_error()

        # Disable retries and run test_get_metrics_value_error.
        _service.disable_retries()
        self.test_get_metrics_value_error()


# endregion
##############################################################################
# End of Service: Metrics
##############################################################################

##############################################################################
# Start of Service: SendNotifications
##############################################################################
# region


class TestNewInstance:
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


class TestSendNotifications:
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Construct a dict representation of a NotificationCreate model
        notification_create_model = {}
        notification_create_model['specversion'] = '1.0'
        notification_create_model['time'] = '2019-01-01T12:00:00Z'
        notification_create_model['id'] = 'testString'
        notification_create_model['source'] = 'testString'
        notification_create_model['type'] = 'testString'
        notification_create_model['ibmenseverity'] = 'testString'
        notification_create_model['ibmensourceid'] = 'testString'
        notification_create_model['ibmendefaultshort'] = 'testString'
        notification_create_model['ibmendefaultlong'] = 'testString'
        notification_create_model['ibmensubject'] = 'testString'
        notification_create_model['ibmentemplates'] = 'testString'
        notification_create_model['ibmenmailto'] = 'testString'
        notification_create_model['ibmensmsto'] = 'testString'
        notification_create_model['ibmenhtmlbody'] = 'testString'
        notification_create_model['subject'] = 'testString'
        notification_create_model['ibmenmms'] = 'testString'
        notification_create_model['data'] = {'foo': 'bar'}
        notification_create_model['datacontenttype'] = 'application/json'
        notification_create_model['ibmenpushto'] = '{"platforms":["push_android"]}'
        notification_create_model['ibmenfcmbody'] = 'testString'
        notification_create_model['ibmenapnsbody'] = 'testString'
        notification_create_model['ibmenapnsheaders'] = 'testString'
        notification_create_model['ibmenchromebody'] = 'testString'
        notification_create_model['ibmenchromeheaders'] = '{"TTL":3600,"Topic":"test","Urgency":"high"}'
        notification_create_model['ibmenfirefoxbody'] = 'testString'
        notification_create_model['ibmenfirefoxheaders'] = '{"TTL":3600,"Topic":"test","Urgency":"high"}'
        notification_create_model['ibmenhuaweibody'] = 'testString'
        notification_create_model['ibmensafaribody'] = 'testString'
        notification_create_model['foo'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        body = notification_create_model

        # Invoke method
        response = _service.send_notifications(
            instance_id,
            body=body,
            headers={},
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.send_notifications(
            instance_id,
            headers={},
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=202,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.send_notifications(**req_copy)

    def test_send_notifications_value_error_with_retries(self):
        # Enable retries and run test_send_notifications_value_error.
        _service.enable_retries()
        self.test_send_notifications_value_error()

        # Disable retries and run test_send_notifications_value_error.
        _service.disable_retries()
        self.test_send_notifications_value_error()


# endregion
##############################################################################
# End of Service: SendNotifications
##############################################################################

##############################################################################
# Start of Service: Sources
##############################################################################
# region


class TestNewInstance:
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


class TestCreateSources:
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            headers={},
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_sources(**req_copy)

    def test_create_sources_value_error_with_retries(self):
        # Enable retries and run test_create_sources_value_error.
        _service.enable_retries()
        self.test_create_sources_value_error()

        # Disable retries and run test_create_sources_value_error.
        _service.disable_retries()
        self.test_create_sources_value_error()


class TestListSources:
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
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "sources": [{"id": "id", "name": "name", "description": "description", "type": "type", "enabled": false, "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 0}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "sources": [{"id": "id", "name": "name", "description": "description", "type": "type", "enabled": false, "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 0}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_sources(
            instance_id,
            headers={},
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
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "sources": [{"id": "id", "name": "name", "description": "description", "type": "type", "enabled": false, "updated_at": "2019-01-01T12:00:00.000Z", "topic_count": 0}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_sources(**req_copy)

    def test_list_sources_value_error_with_retries(self):
        # Enable retries and run test_list_sources_value_error.
        _service.enable_retries()
        self.test_list_sources_value_error()

        # Disable retries and run test_list_sources_value_error.
        _service.disable_retries()
        self.test_list_sources_value_error()

    @responses.activate
    def test_list_sources_with_pager_get_next(self):
        """
        test_list_sources_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/sources')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"sources":[{"id":"id","name":"name","description":"description","type":"type","enabled":false,"updated_at":"2019-01-01T12:00:00.000Z","topic_count":0}],"total_count":2,"limit":1}'
        mock_response2 = '{"sources":[{"id":"id","name":"name","description":"description","type":"type","enabled":false,"updated_at":"2019-01-01T12:00:00.000Z","topic_count":0}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = SourcesPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_sources_with_pager_get_all(self):
        """
        test_list_sources_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/sources')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"sources":[{"id":"id","name":"name","description":"description","type":"type","enabled":false,"updated_at":"2019-01-01T12:00:00.000Z","topic_count":0}],"total_count":2,"limit":1}'
        mock_response2 = '{"sources":[{"id":"id","name":"name","description":"description","type":"type","enabled":false,"updated_at":"2019-01-01T12:00:00.000Z","topic_count":0}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = SourcesPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetSource:
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
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_source(
            instance_id,
            id,
            headers={},
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
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_source(**req_copy)

    def test_get_source_value_error_with_retries(self):
        # Enable retries and run test_get_source_value_error.
        _service.enable_retries()
        self.test_get_source_value_error()

        # Disable retries and run test_get_source_value_error.
        _service.disable_retries()
        self.test_get_source_value_error()


class TestDeleteSource:
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_source(
            instance_id,
            id,
            headers={},
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_source(**req_copy)

    def test_delete_source_value_error_with_retries(self):
        # Enable retries and run test_delete_source_value_error.
        _service.enable_retries()
        self.test_delete_source_value_error()

        # Disable retries and run test_delete_source_value_error.
        _service.disable_retries()
        self.test_delete_source_value_error()


class TestUpdateSource:
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
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
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
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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


class TestNewInstance:
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


class TestCreateTopic:
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Rules model
        rules_model = {}
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.notification_event_info.event_type == \'cert_manager\''
        rules_model['notification_filter'] = '$.notification.findings[0].severity == \'MODERATE\''

        # Construct a dict representation of a SourcesItems model
        sources_items_model = {}
        sources_items_model['id'] = 'e7c3b3ee-78d9-4e02-95c3-c001a05e6ea5:api'
        sources_items_model['rules'] = [rules_model]

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        description = 'testString'
        sources = [sources_items_model]

        # Invoke method
        response = _service.create_topic(
            instance_id,
            name,
            description=description,
            sources=sources,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['sources'] == [sources_items_model]

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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a Rules model
        rules_model = {}
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.notification_event_info.event_type == \'cert_manager\''
        rules_model['notification_filter'] = '$.notification.findings[0].severity == \'MODERATE\''

        # Construct a dict representation of a SourcesItems model
        sources_items_model = {}
        sources_items_model['id'] = 'e7c3b3ee-78d9-4e02-95c3-c001a05e6ea5:api'
        sources_items_model['rules'] = [rules_model]

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        description = 'testString'
        sources = [sources_items_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_topic(**req_copy)

    def test_create_topic_value_error_with_retries(self):
        # Enable retries and run test_create_topic_value_error.
        _service.enable_retries()
        self.test_create_topic_value_error()

        # Disable retries and run test_create_topic_value_error.
        _service.disable_retries()
        self.test_create_topic_value_error()


class TestListTopics:
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
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "topics": [{"id": "id", "name": "name", "description": "description", "source_count": 0, "sources_names": ["sources_names"], "subscription_count": 0}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "topics": [{"id": "id", "name": "name", "description": "description", "source_count": 0, "sources_names": ["sources_names"], "subscription_count": 0}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_topics(
            instance_id,
            headers={},
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
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "topics": [{"id": "id", "name": "name", "description": "description", "source_count": 0, "sources_names": ["sources_names"], "subscription_count": 0}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_topics(**req_copy)

    def test_list_topics_value_error_with_retries(self):
        # Enable retries and run test_list_topics_value_error.
        _service.enable_retries()
        self.test_list_topics_value_error()

        # Disable retries and run test_list_topics_value_error.
        _service.disable_retries()
        self.test_list_topics_value_error()

    @responses.activate
    def test_list_topics_with_pager_get_next(self):
        """
        test_list_topics_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/topics')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"topics":[{"id":"id","name":"name","description":"description","source_count":0,"sources_names":["sources_names"],"subscription_count":0}],"limit":1}'
        mock_response2 = '{"total_count":2,"topics":[{"id":"id","name":"name","description":"description","source_count":0,"sources_names":["sources_names"],"subscription_count":0}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = TopicsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_topics_with_pager_get_all(self):
        """
        test_list_topics_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/topics')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"topics":[{"id":"id","name":"name","description":"description","source_count":0,"sources_names":["sources_names"],"subscription_count":0}],"limit":1}'
        mock_response2 = '{"total_count":2,"topics":[{"id":"id","name":"name","description":"description","source_count":0,"sources_names":["sources_names"],"subscription_count":0}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = TopicsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetTopic:
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
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        include = 'testString'

        # Invoke method
        response = _service.get_topic(
            instance_id,
            id,
            include=include,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_topic(
            instance_id,
            id,
            headers={},
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
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_topic(**req_copy)

    def test_get_topic_value_error_with_retries(self):
        # Enable retries and run test_get_topic_value_error.
        _service.enable_retries()
        self.test_get_topic_value_error()

        # Disable retries and run test_get_topic_value_error.
        _service.disable_retries()
        self.test_get_topic_value_error()


class TestReplaceTopic:
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
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Rules model
        rules_model = {}
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.notification_event_info.event_type == \'cert_manager\''
        rules_model['notification_filter'] = '$.notification.findings[0].severity == \'MODERATE\''

        # Construct a dict representation of a SourcesItems model
        sources_items_model = {}
        sources_items_model['id'] = 'e7c3b3ee-78d9-4e02-95c3-c001a05e6ea5:api'
        sources_items_model['rules'] = [rules_model]

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        sources = [sources_items_model]

        # Invoke method
        response = _service.replace_topic(
            instance_id,
            id,
            name=name,
            description=description,
            sources=sources,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['sources'] == [sources_items_model]

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
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a Rules model
        rules_model = {}
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.notification_event_info.event_type == \'cert_manager\''
        rules_model['notification_filter'] = '$.notification.findings[0].severity == \'MODERATE\''

        # Construct a dict representation of a SourcesItems model
        sources_items_model = {}
        sources_items_model['id'] = 'e7c3b3ee-78d9-4e02-95c3-c001a05e6ea5:api'
        sources_items_model['rules'] = [rules_model]

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        sources = [sources_items_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_topic(**req_copy)

    def test_replace_topic_value_error_with_retries(self):
        # Enable retries and run test_replace_topic_value_error.
        _service.enable_retries()
        self.test_replace_topic_value_error()

        # Disable retries and run test_replace_topic_value_error.
        _service.disable_retries()
        self.test_replace_topic_value_error()


class TestDeleteTopic:
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_topic(
            instance_id,
            id,
            headers={},
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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
# Start of Service: Templates
##############################################################################
# region


class TestNewInstance:
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


class TestCreateTemplate:
    """
    Test Class for create_template
    """

    @responses.activate
    def test_create_template_all_params(self):
        """
        create_template()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "type", "params": {"body": "body", "subject": "subject"}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a TemplateConfigOneOfEmailTemplateConfig model
        template_config_one_of_model = {}
        template_config_one_of_model['body'] = 'testString'
        template_config_one_of_model['subject'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        type = 'testString'
        params = template_config_one_of_model
        description = 'testString'

        # Invoke method
        response = _service.create_template(
            instance_id,
            name,
            type,
            params,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['type'] == 'testString'
        assert req_body['params'] == template_config_one_of_model
        assert req_body['description'] == 'testString'

    def test_create_template_all_params_with_retries(self):
        # Enable retries and run test_create_template_all_params.
        _service.enable_retries()
        self.test_create_template_all_params()

        # Disable retries and run test_create_template_all_params.
        _service.disable_retries()
        self.test_create_template_all_params()

    @responses.activate
    def test_create_template_value_error(self):
        """
        test_create_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "type", "params": {"body": "body", "subject": "subject"}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a TemplateConfigOneOfEmailTemplateConfig model
        template_config_one_of_model = {}
        template_config_one_of_model['body'] = 'testString'
        template_config_one_of_model['subject'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        type = 'testString'
        params = template_config_one_of_model
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "name": name,
            "type": type,
            "params": params,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_template(**req_copy)

    def test_create_template_value_error_with_retries(self):
        # Enable retries and run test_create_template_value_error.
        _service.enable_retries()
        self.test_create_template_value_error()

        # Disable retries and run test_create_template_value_error.
        _service.disable_retries()
        self.test_create_template_value_error()


class TestListTemplates:
    """
    Test Class for list_templates
    """

    @responses.activate
    def test_list_templates_all_params(self):
        """
        list_templates()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "templates": [{"id": "id", "name": "name", "description": "description", "type": "type", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        limit = 1
        offset = 0
        search = 'testString'

        # Invoke method
        response = _service.list_templates(
            instance_id,
            limit=limit,
            offset=offset,
            search=search,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'search={}'.format(search) in query_string

    def test_list_templates_all_params_with_retries(self):
        # Enable retries and run test_list_templates_all_params.
        _service.enable_retries()
        self.test_list_templates_all_params()

        # Disable retries and run test_list_templates_all_params.
        _service.disable_retries()
        self.test_list_templates_all_params()

    @responses.activate
    def test_list_templates_required_params(self):
        """
        test_list_templates_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "templates": [{"id": "id", "name": "name", "description": "description", "type": "type", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_templates(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_templates_required_params_with_retries(self):
        # Enable retries and run test_list_templates_required_params.
        _service.enable_retries()
        self.test_list_templates_required_params()

        # Disable retries and run test_list_templates_required_params.
        _service.disable_retries()
        self.test_list_templates_required_params()

    @responses.activate
    def test_list_templates_value_error(self):
        """
        test_list_templates_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "templates": [{"id": "id", "name": "name", "description": "description", "type": "type", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_templates(**req_copy)

    def test_list_templates_value_error_with_retries(self):
        # Enable retries and run test_list_templates_value_error.
        _service.enable_retries()
        self.test_list_templates_value_error()

        # Disable retries and run test_list_templates_value_error.
        _service.disable_retries()
        self.test_list_templates_value_error()

    @responses.activate
    def test_list_templates_with_pager_get_next(self):
        """
        test_list_templates_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/templates')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"templates":[{"id":"id","name":"name","description":"description","type":"type","subscription_count":18,"subscription_names":["subscription_names"],"updated_at":"2019-01-01T12:00:00.000Z"}],"limit":1}'
        mock_response2 = '{"total_count":2,"templates":[{"id":"id","name":"name","description":"description","type":"type","subscription_count":18,"subscription_names":["subscription_names"],"updated_at":"2019-01-01T12:00:00.000Z"}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = TemplatesPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_templates_with_pager_get_all(self):
        """
        test_list_templates_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/templates')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"templates":[{"id":"id","name":"name","description":"description","type":"type","subscription_count":18,"subscription_names":["subscription_names"],"updated_at":"2019-01-01T12:00:00.000Z"}],"limit":1}'
        mock_response2 = '{"total_count":2,"templates":[{"id":"id","name":"name","description":"description","type":"type","subscription_count":18,"subscription_names":["subscription_names"],"updated_at":"2019-01-01T12:00:00.000Z"}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = TemplatesPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetTemplate:
    """
    Test Class for get_template
    """

    @responses.activate
    def test_get_template_all_params(self):
        """
        get_template()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "type", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_template(
            instance_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_template_all_params_with_retries(self):
        # Enable retries and run test_get_template_all_params.
        _service.enable_retries()
        self.test_get_template_all_params()

        # Disable retries and run test_get_template_all_params.
        _service.disable_retries()
        self.test_get_template_all_params()

    @responses.activate
    def test_get_template_value_error(self):
        """
        test_get_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "type", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_template(**req_copy)

    def test_get_template_value_error_with_retries(self):
        # Enable retries and run test_get_template_value_error.
        _service.enable_retries()
        self.test_get_template_value_error()

        # Disable retries and run test_get_template_value_error.
        _service.disable_retries()
        self.test_get_template_value_error()


class TestReplaceTemplate:
    """
    Test Class for replace_template
    """

    @responses.activate
    def test_replace_template_all_params(self):
        """
        replace_template()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "type", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a TemplateConfigOneOfEmailTemplateConfig model
        template_config_one_of_model = {}
        template_config_one_of_model['body'] = 'testString'
        template_config_one_of_model['subject'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        type = 'testString'
        params = template_config_one_of_model

        # Invoke method
        response = _service.replace_template(
            instance_id,
            id,
            name=name,
            description=description,
            type=type,
            params=params,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['type'] == 'testString'
        assert req_body['params'] == template_config_one_of_model

    def test_replace_template_all_params_with_retries(self):
        # Enable retries and run test_replace_template_all_params.
        _service.enable_retries()
        self.test_replace_template_all_params()

        # Disable retries and run test_replace_template_all_params.
        _service.disable_retries()
        self.test_replace_template_all_params()

    @responses.activate
    def test_replace_template_value_error(self):
        """
        test_replace_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "type", "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a TemplateConfigOneOfEmailTemplateConfig model
        template_config_one_of_model = {}
        template_config_one_of_model['body'] = 'testString'
        template_config_one_of_model['subject'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        type = 'testString'
        params = template_config_one_of_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_template(**req_copy)

    def test_replace_template_value_error_with_retries(self):
        # Enable retries and run test_replace_template_value_error.
        _service.enable_retries()
        self.test_replace_template_value_error()

        # Disable retries and run test_replace_template_value_error.
        _service.disable_retries()
        self.test_replace_template_value_error()


class TestDeleteTemplate:
    """
    Test Class for delete_template
    """

    @responses.activate
    def test_delete_template_all_params(self):
        """
        delete_template()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_template(
            instance_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_template_all_params_with_retries(self):
        # Enable retries and run test_delete_template_all_params.
        _service.enable_retries()
        self.test_delete_template_all_params()

        # Disable retries and run test_delete_template_all_params.
        _service.disable_retries()
        self.test_delete_template_all_params()

    @responses.activate
    def test_delete_template_value_error(self):
        """
        test_delete_template_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/templates/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_template(**req_copy)

    def test_delete_template_value_error_with_retries(self):
        # Enable retries and run test_delete_template_value_error.
        _service.enable_retries()
        self.test_delete_template_value_error()

        # Disable retries and run test_delete_template_value_error.
        _service.disable_retries()
        self.test_delete_template_value_error()


# endregion
##############################################################################
# End of Service: Templates
##############################################################################

##############################################################################
# Start of Service: Destinations
##############################################################################
# region


class TestNewInstance:
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


class TestCreateDestination:
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "config": {"params": {"domain": "domain", "dkim": {"public_key": "public_key", "selector": "selector", "verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a DKIMAttributes model
        dkim_attributes_model = {}
        dkim_attributes_model['public_key'] = 'testString'
        dkim_attributes_model['selector'] = 'testString'
        dkim_attributes_model['verification'] = 'testString'

        # Construct a dict representation of a SPFAttributes model
        spf_attributes_model = {}
        spf_attributes_model['txt_name'] = 'testString'
        spf_attributes_model['txt_value'] = 'testString'
        spf_attributes_model['verification'] = 'testString'

        # Construct a dict representation of a DestinationConfigOneOfCustomDomainEmailDestinationConfig model
        destination_config_one_of_model = {}
        destination_config_one_of_model['domain'] = 'testString'
        destination_config_one_of_model['dkim'] = dkim_attributes_model
        destination_config_one_of_model['spf'] = spf_attributes_model

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {}
        destination_config_model['params'] = destination_config_one_of_model

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        type = 'webhook'
        description = 'testString'
        collect_failed_events = False
        config = destination_config_model
        certificate = io.BytesIO(b'This is a mock file.').getvalue()
        certificate_content_type = 'testString'
        icon_16x16 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_16x16_content_type = 'testString'
        icon_16x16_2x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_16x16_2x_content_type = 'testString'
        icon_32x32 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_32x32_content_type = 'testString'
        icon_32x32_2x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_32x32_2x_content_type = 'testString'
        icon_128x128 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_128x128_content_type = 'testString'
        icon_128x128_2x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_128x128_2x_content_type = 'testString'

        # Invoke method
        response = _service.create_destination(
            instance_id,
            name,
            type,
            description=description,
            collect_failed_events=collect_failed_events,
            config=config,
            certificate=certificate,
            certificate_content_type=certificate_content_type,
            icon_16x16=icon_16x16,
            icon_16x16_content_type=icon_16x16_content_type,
            icon_16x16_2x=icon_16x16_2x,
            icon_16x16_2x_content_type=icon_16x16_2x_content_type,
            icon_32x32=icon_32x32,
            icon_32x32_content_type=icon_32x32_content_type,
            icon_32x32_2x=icon_32x32_2x,
            icon_32x32_2x_content_type=icon_32x32_2x_content_type,
            icon_128x128=icon_128x128,
            icon_128x128_content_type=icon_128x128_content_type,
            icon_128x128_2x=icon_128x128_2x,
            icon_128x128_2x_content_type=icon_128x128_2x_content_type,
            headers={},
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "config": {"params": {"domain": "domain", "dkim": {"public_key": "public_key", "selector": "selector", "verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        type = 'webhook'

        # Invoke method
        response = _service.create_destination(
            instance_id,
            name,
            type,
            headers={},
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "config": {"params": {"domain": "domain", "dkim": {"public_key": "public_key", "selector": "selector", "verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_destination(**req_copy)

    def test_create_destination_value_error_with_retries(self):
        # Enable retries and run test_create_destination_value_error.
        _service.enable_retries()
        self.test_create_destination_value_error()

        # Disable retries and run test_create_destination_value_error.
        _service.disable_retries()
        self.test_create_destination_value_error()


class TestListDestinations:
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
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "destinations": [{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "destinations": [{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_destinations(
            instance_id,
            headers={},
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
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "destinations": [{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "subscription_count": 18, "subscription_names": ["subscription_names"], "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_destinations(**req_copy)

    def test_list_destinations_value_error_with_retries(self):
        # Enable retries and run test_list_destinations_value_error.
        _service.enable_retries()
        self.test_list_destinations_value_error()

        # Disable retries and run test_list_destinations_value_error.
        _service.disable_retries()
        self.test_list_destinations_value_error()

    @responses.activate
    def test_list_destinations_with_pager_get_next(self):
        """
        test_list_destinations_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/destinations')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"destinations":[{"id":"id","name":"name","description":"description","type":"webhook","collect_failed_events":false,"subscription_count":18,"subscription_names":["subscription_names"],"updated_at":"2019-01-01T12:00:00.000Z"}],"limit":1}'
        mock_response2 = '{"total_count":2,"destinations":[{"id":"id","name":"name","description":"description","type":"webhook","collect_failed_events":false,"subscription_count":18,"subscription_names":["subscription_names"],"updated_at":"2019-01-01T12:00:00.000Z"}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = DestinationsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_destinations_with_pager_get_all(self):
        """
        test_list_destinations_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/destinations')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"destinations":[{"id":"id","name":"name","description":"description","type":"webhook","collect_failed_events":false,"subscription_count":18,"subscription_names":["subscription_names"],"updated_at":"2019-01-01T12:00:00.000Z"}],"limit":1}'
        mock_response2 = '{"total_count":2,"destinations":[{"id":"id","name":"name","description":"description","type":"webhook","collect_failed_events":false,"subscription_count":18,"subscription_names":["subscription_names"],"updated_at":"2019-01-01T12:00:00.000Z"}],"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = DestinationsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetDestination:
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "config": {"params": {"domain": "domain", "dkim": {"public_key": "public_key", "selector": "selector", "verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_destination(
            instance_id,
            id,
            headers={},
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "config": {"params": {"domain": "domain", "dkim": {"public_key": "public_key", "selector": "selector", "verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_destination(**req_copy)

    def test_get_destination_value_error_with_retries(self):
        # Enable retries and run test_get_destination_value_error.
        _service.enable_retries()
        self.test_get_destination_value_error()

        # Disable retries and run test_get_destination_value_error.
        _service.disable_retries()
        self.test_get_destination_value_error()


class TestUpdateDestination:
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "config": {"params": {"domain": "domain", "dkim": {"public_key": "public_key", "selector": "selector", "verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a DKIMAttributes model
        dkim_attributes_model = {}
        dkim_attributes_model['public_key'] = 'testString'
        dkim_attributes_model['selector'] = 'testString'
        dkim_attributes_model['verification'] = 'testString'

        # Construct a dict representation of a SPFAttributes model
        spf_attributes_model = {}
        spf_attributes_model['txt_name'] = 'testString'
        spf_attributes_model['txt_value'] = 'testString'
        spf_attributes_model['verification'] = 'testString'

        # Construct a dict representation of a DestinationConfigOneOfCustomDomainEmailDestinationConfig model
        destination_config_one_of_model = {}
        destination_config_one_of_model['domain'] = 'testString'
        destination_config_one_of_model['dkim'] = dkim_attributes_model
        destination_config_one_of_model['spf'] = spf_attributes_model

        # Construct a dict representation of a DestinationConfig model
        destination_config_model = {}
        destination_config_model['params'] = destination_config_one_of_model

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'
        collect_failed_events = False
        config = destination_config_model
        certificate = io.BytesIO(b'This is a mock file.').getvalue()
        certificate_content_type = 'testString'
        icon_16x16 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_16x16_content_type = 'testString'
        icon_16x16_2x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_16x16_2x_content_type = 'testString'
        icon_32x32 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_32x32_content_type = 'testString'
        icon_32x32_2x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_32x32_2x_content_type = 'testString'
        icon_128x128 = io.BytesIO(b'This is a mock file.').getvalue()
        icon_128x128_content_type = 'testString'
        icon_128x128_2x = io.BytesIO(b'This is a mock file.').getvalue()
        icon_128x128_2x_content_type = 'testString'

        # Invoke method
        response = _service.update_destination(
            instance_id,
            id,
            name=name,
            description=description,
            collect_failed_events=collect_failed_events,
            config=config,
            certificate=certificate,
            certificate_content_type=certificate_content_type,
            icon_16x16=icon_16x16,
            icon_16x16_content_type=icon_16x16_content_type,
            icon_16x16_2x=icon_16x16_2x,
            icon_16x16_2x_content_type=icon_16x16_2x_content_type,
            icon_32x32=icon_32x32,
            icon_32x32_content_type=icon_32x32_content_type,
            icon_32x32_2x=icon_32x32_2x,
            icon_32x32_2x_content_type=icon_32x32_2x_content_type,
            icon_128x128=icon_128x128,
            icon_128x128_content_type=icon_128x128_content_type,
            icon_128x128_2x=icon_128x128_2x,
            icon_128x128_2x_content_type=icon_128x128_2x_content_type,
            headers={},
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "config": {"params": {"domain": "domain", "dkim": {"public_key": "public_key", "selector": "selector", "verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.update_destination(
            instance_id,
            id,
            headers={},
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "type": "webhook", "collect_failed_events": false, "config": {"params": {"domain": "domain", "dkim": {"public_key": "public_key", "selector": "selector", "verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}}, "updated_at": "2019-01-01T12:00:00.000Z", "subscription_count": 0, "subscription_names": ["subscription_names"]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_destination(**req_copy)

    def test_update_destination_value_error_with_retries(self):
        # Enable retries and run test_update_destination_value_error.
        _service.enable_retries()
        self.test_update_destination_value_error()

        # Disable retries and run test_update_destination_value_error.
        _service.disable_retries()
        self.test_update_destination_value_error()


class TestDeleteDestination:
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_destination(
            instance_id,
            id,
            headers={},
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_destination(**req_copy)

    def test_delete_destination_value_error_with_retries(self):
        # Enable retries and run test_delete_destination_value_error.
        _service.enable_retries()
        self.test_delete_destination_value_error()

        # Disable retries and run test_delete_destination_value_error.
        _service.disable_retries()
        self.test_delete_destination_value_error()


class TestGetEnabledCountries:
    """
    Test Class for get_enabled_countries
    """

    @responses.activate
    def test_get_enabled_countries_all_params(self):
        """
        get_enabled_countries()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/enabled_countries')
        mock_response = '{"status": "status", "enabled_countries": [{"number": "number", "country": ["country"]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_enabled_countries(
            instance_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_enabled_countries_all_params_with_retries(self):
        # Enable retries and run test_get_enabled_countries_all_params.
        _service.enable_retries()
        self.test_get_enabled_countries_all_params()

        # Disable retries and run test_get_enabled_countries_all_params.
        _service.disable_retries()
        self.test_get_enabled_countries_all_params()

    @responses.activate
    def test_get_enabled_countries_value_error(self):
        """
        test_get_enabled_countries_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/enabled_countries')
        mock_response = '{"status": "status", "enabled_countries": [{"number": "number", "country": ["country"]}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_enabled_countries(**req_copy)

    def test_get_enabled_countries_value_error_with_retries(self):
        # Enable retries and run test_get_enabled_countries_value_error.
        _service.enable_retries()
        self.test_get_enabled_countries_value_error()

        # Disable retries and run test_get_enabled_countries_value_error.
        _service.disable_retries()
        self.test_get_enabled_countries_value_error()


class TestTestDestination:
    """
    Test Class for test_destination
    """

    @responses.activate
    def test_test_destination_all_params(self):
        """
        test_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/test')
        mock_response = '{"status": "status"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.test_destination(
            instance_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201

    def test_test_destination_all_params_with_retries(self):
        # Enable retries and run test_test_destination_all_params.
        _service.enable_retries()
        self.test_test_destination_all_params()

        # Disable retries and run test_test_destination_all_params.
        _service.disable_retries()
        self.test_test_destination_all_params()

    @responses.activate
    def test_test_destination_value_error(self):
        """
        test_test_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/test')
        mock_response = '{"status": "status"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.test_destination(**req_copy)

    def test_test_destination_value_error_with_retries(self):
        # Enable retries and run test_test_destination_value_error.
        _service.enable_retries()
        self.test_test_destination_value_error()

        # Disable retries and run test_test_destination_value_error.
        _service.disable_retries()
        self.test_test_destination_value_error()


class TestUpdateVerifyDestination:
    """
    Test Class for update_verify_destination
    """

    @responses.activate
    def test_update_verify_destination_all_params(self):
        """
        update_verify_destination()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/verify')
        mock_response = '{"type": "type", "verification": "verification"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        type = 'testString'

        # Invoke method
        response = _service.update_verify_destination(
            instance_id,
            id,
            type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string

    def test_update_verify_destination_all_params_with_retries(self):
        # Enable retries and run test_update_verify_destination_all_params.
        _service.enable_retries()
        self.test_update_verify_destination_all_params()

        # Disable retries and run test_update_verify_destination_all_params.
        _service.disable_retries()
        self.test_update_verify_destination_all_params()

    @responses.activate
    def test_update_verify_destination_value_error(self):
        """
        test_update_verify_destination_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/destinations/testString/verify')
        mock_response = '{"type": "type", "verification": "verification"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        type = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_verify_destination(**req_copy)

    def test_update_verify_destination_value_error_with_retries(self):
        # Enable retries and run test_update_verify_destination_value_error.
        _service.enable_retries()
        self.test_update_verify_destination_value_error()

        # Disable retries and run test_update_verify_destination_value_error.
        _service.disable_retries()
        self.test_update_verify_destination_value_error()


# endregion
##############################################################################
# End of Service: Destinations
##############################################################################

##############################################################################
# Start of Service: PushDestinationAPIs
##############################################################################
# region


class TestNewInstance:
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


class TestCreateTagsSubscription:
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            headers={},
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
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tags_subscription(**req_copy)

    def test_create_tags_subscription_value_error_with_retries(self):
        # Enable retries and run test_create_tags_subscription_value_error.
        _service.enable_retries()
        self.test_create_tags_subscription_value_error()

        # Disable retries and run test_create_tags_subscription_value_error.
        _service.disable_retries()
        self.test_create_tags_subscription_value_error()


class TestListTagsSubscription:
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
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "tag_subscriptions": [{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "tag_subscriptions": [{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.list_tags_subscription(
            instance_id,
            id,
            headers={},
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
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "tag_subscriptions": [{"id": "id", "device_id": "device_id", "tag_name": "tag_name", "user_id": "user_id", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_tags_subscription(**req_copy)

    def test_list_tags_subscription_value_error_with_retries(self):
        # Enable retries and run test_list_tags_subscription_value_error.
        _service.enable_retries()
        self.test_list_tags_subscription_value_error()

        # Disable retries and run test_list_tags_subscription_value_error.
        _service.disable_retries()
        self.test_list_tags_subscription_value_error()

    @responses.activate
    def test_list_tags_subscription_with_pager_get_next(self):
        """
        test_list_tags_subscription_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"tag_subscriptions":[{"id":"id","device_id":"device_id","tag_name":"tag_name","user_id":"user_id","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"tag_subscriptions":[{"id":"id","device_id":"device_id","tag_name":"tag_name","user_id":"user_id","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = TagsSubscriptionPager(
            client=_service,
            instance_id='testString',
            id='testString',
            device_id='testString',
            user_id='testString',
            tag_name='testString',
            limit=10,
            search='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_tags_subscription_with_pager_get_all(self):
        """
        test_list_tags_subscription_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/destinations/testString/tag_subscriptions')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"tag_subscriptions":[{"id":"id","device_id":"device_id","tag_name":"tag_name","user_id":"user_id","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"tag_subscriptions":[{"id":"id","device_id":"device_id","tag_name":"tag_name","user_id":"user_id","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = TagsSubscriptionPager(
            client=_service,
            instance_id='testString',
            id='testString',
            device_id='testString',
            user_id='testString',
            tag_name='testString',
            limit=10,
            search='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestDeleteTagsSubscription:
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_tags_subscription(
            instance_id,
            id,
            headers={},
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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
# End of Service: PushDestinationAPIs
##############################################################################

##############################################################################
# Start of Service: Subscriptions
##############################################################################
# region


class TestNewInstance:
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


class TestCreateSubscription:
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"subscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "unsubscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "invited": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z", "expires_at": "2019-01-01T12:00:00.000Z"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SubscriptionCreateAttributesSMSAttributes model
        subscription_create_attributes_model = {}
        subscription_create_attributes_model['invited'] = ['testString']

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
            headers={},
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"subscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "unsubscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "invited": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z", "expires_at": "2019-01-01T12:00:00.000Z"}]}}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a SubscriptionCreateAttributesSMSAttributes model
        subscription_create_attributes_model = {}
        subscription_create_attributes_model['invited'] = ['testString']

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_subscription(**req_copy)

    def test_create_subscription_value_error_with_retries(self):
        # Enable retries and run test_create_subscription_value_error.
        _service.enable_retries()
        self.test_create_subscription_value_error()

        # Disable retries and run test_create_subscription_value_error.
        _service.disable_retries()
        self.test_create_subscription_value_error()


class TestListSubscriptions:
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
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

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
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
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
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_subscriptions(
            instance_id,
            headers={},
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
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "subscriptions": [{"id": "id", "name": "name", "description": "description", "destination_id": "destination_id", "destination_name": "destination_name", "destination_type": "sms_ibm", "topic_id": "topic_id", "topic_name": "topic_name", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_subscriptions(**req_copy)

    def test_list_subscriptions_value_error_with_retries(self):
        # Enable retries and run test_list_subscriptions_value_error.
        _service.enable_retries()
        self.test_list_subscriptions_value_error()

        # Disable retries and run test_list_subscriptions_value_error.
        _service.disable_retries()
        self.test_list_subscriptions_value_error()

    @responses.activate
    def test_list_subscriptions_with_pager_get_next(self):
        """
        test_list_subscriptions_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/subscriptions')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"subscriptions":[{"id":"id","name":"name","description":"description","destination_id":"destination_id","destination_name":"destination_name","destination_type":"sms_ibm","topic_id":"topic_id","topic_name":"topic_name","updated_at":"2019-01-01T12:00:00.000Z"}],"total_count":2,"limit":1}'
        mock_response2 = '{"subscriptions":[{"id":"id","name":"name","description":"description","destination_id":"destination_id","destination_name":"destination_name","destination_type":"sms_ibm","topic_id":"topic_id","topic_name":"topic_name","updated_at":"2019-01-01T12:00:00.000Z"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = SubscriptionsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_subscriptions_with_pager_get_all(self):
        """
        test_list_subscriptions_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/subscriptions')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"subscriptions":[{"id":"id","name":"name","description":"description","destination_id":"destination_id","destination_name":"destination_name","destination_type":"sms_ibm","topic_id":"topic_id","topic_name":"topic_name","updated_at":"2019-01-01T12:00:00.000Z"}],"total_count":2,"limit":1}'
        mock_response2 = '{"subscriptions":[{"id":"id","name":"name","description":"description","destination_id":"destination_id","destination_name":"destination_name","destination_type":"sms_ibm","topic_id":"topic_id","topic_name":"topic_name","updated_at":"2019-01-01T12:00:00.000Z"}],"total_count":2,"limit":1}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = SubscriptionsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetSubscription:
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"subscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "unsubscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "invited": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z", "expires_at": "2019-01-01T12:00:00.000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_subscription(
            instance_id,
            id,
            headers={},
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"subscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "unsubscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "invited": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z", "expires_at": "2019-01-01T12:00:00.000Z"}]}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_subscription(**req_copy)

    def test_get_subscription_value_error_with_retries(self):
        # Enable retries and run test_get_subscription_value_error.
        _service.enable_retries()
        self.test_get_subscription_value_error()

        # Disable retries and run test_get_subscription_value_error.
        _service.disable_retries()
        self.test_get_subscription_value_error()


class TestDeleteSubscription:
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_subscription(
            instance_id,
            id,
            headers={},
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
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_subscription(**req_copy)

    def test_delete_subscription_value_error_with_retries(self):
        # Enable retries and run test_delete_subscription_value_error.
        _service.enable_retries()
        self.test_delete_subscription_value_error()

        # Disable retries and run test_delete_subscription_value_error.
        _service.disable_retries()
        self.test_delete_subscription_value_error()


class TestUpdateSubscription:
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"subscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "unsubscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "invited": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z", "expires_at": "2019-01-01T12:00:00.000Z"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a UpdateAttributesInvited model
        update_attributes_invited_model = {}
        update_attributes_invited_model['add'] = ['testString']
        update_attributes_invited_model['remove'] = ['testString']

        # Construct a dict representation of a UpdateAttributesSubscribed model
        update_attributes_subscribed_model = {}
        update_attributes_subscribed_model['remove'] = ['testString']

        # Construct a dict representation of a UpdateAttributesUnsubscribed model
        update_attributes_unsubscribed_model = {}
        update_attributes_unsubscribed_model['remove'] = ['testString']

        # Construct a dict representation of a SubscriptionUpdateAttributesSMSUpdateAttributes model
        subscription_update_attributes_model = {}
        subscription_update_attributes_model['invited'] = update_attributes_invited_model
        subscription_update_attributes_model['subscribed'] = update_attributes_subscribed_model
        subscription_update_attributes_model['unsubscribed'] = update_attributes_unsubscribed_model

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
            headers={},
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
        mock_response = '{"id": "id", "name": "name", "description": "description", "updated_at": "updated_at", "from": "from_", "destination_type": "sms_ibm", "destination_id": "destination_id", "destination_name": "destination_name", "topic_id": "topic_id", "topic_name": "topic_name", "attributes": {"subscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "unsubscribed": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z"}], "invited": [{"phone_number": "phone_number", "updated_at": "2019-01-01T12:00:00.000Z", "expires_at": "2019-01-01T12:00:00.000Z"}]}}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a UpdateAttributesInvited model
        update_attributes_invited_model = {}
        update_attributes_invited_model['add'] = ['testString']
        update_attributes_invited_model['remove'] = ['testString']

        # Construct a dict representation of a UpdateAttributesSubscribed model
        update_attributes_subscribed_model = {}
        update_attributes_subscribed_model['remove'] = ['testString']

        # Construct a dict representation of a UpdateAttributesUnsubscribed model
        update_attributes_unsubscribed_model = {}
        update_attributes_unsubscribed_model['remove'] = ['testString']

        # Construct a dict representation of a SubscriptionUpdateAttributesSMSUpdateAttributes model
        subscription_update_attributes_model = {}
        subscription_update_attributes_model['invited'] = update_attributes_invited_model
        subscription_update_attributes_model['subscribed'] = update_attributes_subscribed_model
        subscription_update_attributes_model['unsubscribed'] = update_attributes_unsubscribed_model

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
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
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
# Start of Service: Integrations
##############################################################################
# region


class TestNewInstance:
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


class TestCreateIntegration:
    """
    Test Class for create_integration
    """

    @responses.activate
    def test_create_integration_all_params(self):
        """
        create_integration()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/integrations')
        mock_response = '{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "type": "type", "metadata": {"endpoint": "endpoint", "crn": "crn", "bucket_name": "bucket_name"}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a IntegrationCreateMetadata model
        integration_create_metadata_model = {}
        integration_create_metadata_model['endpoint'] = 'testString'
        integration_create_metadata_model['crn'] = 'testString'
        integration_create_metadata_model['bucket_name'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        type = 'collect_failed_events'
        metadata = integration_create_metadata_model

        # Invoke method
        response = _service.create_integration(
            instance_id,
            type,
            metadata,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'collect_failed_events'
        assert req_body['metadata'] == integration_create_metadata_model

    def test_create_integration_all_params_with_retries(self):
        # Enable retries and run test_create_integration_all_params.
        _service.enable_retries()
        self.test_create_integration_all_params()

        # Disable retries and run test_create_integration_all_params.
        _service.disable_retries()
        self.test_create_integration_all_params()

    @responses.activate
    def test_create_integration_value_error(self):
        """
        test_create_integration_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/integrations')
        mock_response = '{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "type": "type", "metadata": {"endpoint": "endpoint", "crn": "crn", "bucket_name": "bucket_name"}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Construct a dict representation of a IntegrationCreateMetadata model
        integration_create_metadata_model = {}
        integration_create_metadata_model['endpoint'] = 'testString'
        integration_create_metadata_model['crn'] = 'testString'
        integration_create_metadata_model['bucket_name'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        type = 'collect_failed_events'
        metadata = integration_create_metadata_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "type": type,
            "metadata": metadata,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_integration(**req_copy)

    def test_create_integration_value_error_with_retries(self):
        # Enable retries and run test_create_integration_value_error.
        _service.enable_retries()
        self.test_create_integration_value_error()

        # Disable retries and run test_create_integration_value_error.
        _service.disable_retries()
        self.test_create_integration_value_error()


class TestListIntegrations:
    """
    Test Class for list_integrations
    """

    @responses.activate
    def test_list_integrations_all_params(self):
        """
        list_integrations()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/integrations')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "integrations": [{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "type": "type", "metadata": {"endpoint": "endpoint", "crn": "crn", "root_key_id": "root_key_id", "bucket_name": "bucket_name"}, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        offset = 0
        limit = 1
        search = 'testString'

        # Invoke method
        response = _service.list_integrations(
            instance_id,
            offset=offset,
            limit=limit,
            search=search,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'offset={}'.format(offset) in query_string
        assert 'limit={}'.format(limit) in query_string
        assert 'search={}'.format(search) in query_string

    def test_list_integrations_all_params_with_retries(self):
        # Enable retries and run test_list_integrations_all_params.
        _service.enable_retries()
        self.test_list_integrations_all_params()

        # Disable retries and run test_list_integrations_all_params.
        _service.disable_retries()
        self.test_list_integrations_all_params()

    @responses.activate
    def test_list_integrations_required_params(self):
        """
        test_list_integrations_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/integrations')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "integrations": [{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "type": "type", "metadata": {"endpoint": "endpoint", "crn": "crn", "root_key_id": "root_key_id", "bucket_name": "bucket_name"}, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_integrations(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_integrations_required_params_with_retries(self):
        # Enable retries and run test_list_integrations_required_params.
        _service.enable_retries()
        self.test_list_integrations_required_params()

        # Disable retries and run test_list_integrations_required_params.
        _service.disable_retries()
        self.test_list_integrations_required_params()

    @responses.activate
    def test_list_integrations_value_error(self):
        """
        test_list_integrations_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/integrations')
        mock_response = '{"total_count": 0, "offset": 6, "limit": 5, "integrations": [{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "type": "type", "metadata": {"endpoint": "endpoint", "crn": "crn", "root_key_id": "root_key_id", "bucket_name": "bucket_name"}, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_integrations(**req_copy)

    def test_list_integrations_value_error_with_retries(self):
        # Enable retries and run test_list_integrations_value_error.
        _service.enable_retries()
        self.test_list_integrations_value_error()

        # Disable retries and run test_list_integrations_value_error.
        _service.disable_retries()
        self.test_list_integrations_value_error()

    @responses.activate
    def test_list_integrations_with_pager_get_next(self):
        """
        test_list_integrations_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/integrations')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"integrations":[{"id":"9fab83da-98cb-4f18-a7ba-b6f0435c9673","type":"type","metadata":{"endpoint":"endpoint","crn":"crn","root_key_id":"root_key_id","bucket_name":"bucket_name"},"created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"integrations":[{"id":"9fab83da-98cb-4f18-a7ba-b6f0435c9673","type":"type","metadata":{"endpoint":"endpoint","crn":"crn","root_key_id":"root_key_id","bucket_name":"bucket_name"},"created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = IntegrationsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_integrations_with_pager_get_all(self):
        """
        test_list_integrations_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/integrations')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"integrations":[{"id":"9fab83da-98cb-4f18-a7ba-b6f0435c9673","type":"type","metadata":{"endpoint":"endpoint","crn":"crn","root_key_id":"root_key_id","bucket_name":"bucket_name"},"created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"integrations":[{"id":"9fab83da-98cb-4f18-a7ba-b6f0435c9673","type":"type","metadata":{"endpoint":"endpoint","crn":"crn","root_key_id":"root_key_id","bucket_name":"bucket_name"},"created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = IntegrationsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetIntegration:
    """
    Test Class for get_integration
    """

    @responses.activate
    def test_get_integration_all_params(self):
        """
        get_integration()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/integrations/testString')
        mock_response = '{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "type": "type", "metadata": {"endpoint": "endpoint", "crn": "crn", "root_key_id": "root_key_id", "bucket_name": "bucket_name"}, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_integration(
            instance_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_integration_all_params_with_retries(self):
        # Enable retries and run test_get_integration_all_params.
        _service.enable_retries()
        self.test_get_integration_all_params()

        # Disable retries and run test_get_integration_all_params.
        _service.disable_retries()
        self.test_get_integration_all_params()

    @responses.activate
    def test_get_integration_value_error(self):
        """
        test_get_integration_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/integrations/testString')
        mock_response = '{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "type": "type", "metadata": {"endpoint": "endpoint", "crn": "crn", "root_key_id": "root_key_id", "bucket_name": "bucket_name"}, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_integration(**req_copy)

    def test_get_integration_value_error_with_retries(self):
        # Enable retries and run test_get_integration_value_error.
        _service.enable_retries()
        self.test_get_integration_value_error()

        # Disable retries and run test_get_integration_value_error.
        _service.disable_retries()
        self.test_get_integration_value_error()


class TestReplaceIntegration:
    """
    Test Class for replace_integration
    """

    @responses.activate
    def test_replace_integration_all_params(self):
        """
        replace_integration()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/integrations/testString')
        mock_response = '{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "type": "type", "metadata": {"endpoint": "endpoint", "crn": "crn", "root_key_id": "root_key_id", "bucket_name": "bucket_name"}, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a IntegrationMetadata model
        integration_metadata_model = {}
        integration_metadata_model['endpoint'] = 'testString'
        integration_metadata_model['crn'] = 'testString'
        integration_metadata_model['root_key_id'] = 'testString'
        integration_metadata_model['bucket_name'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        type = 'testString'
        metadata = integration_metadata_model

        # Invoke method
        response = _service.replace_integration(
            instance_id,
            id,
            type,
            metadata,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'testString'
        assert req_body['metadata'] == integration_metadata_model

    def test_replace_integration_all_params_with_retries(self):
        # Enable retries and run test_replace_integration_all_params.
        _service.enable_retries()
        self.test_replace_integration_all_params()

        # Disable retries and run test_replace_integration_all_params.
        _service.disable_retries()
        self.test_replace_integration_all_params()

    @responses.activate
    def test_replace_integration_value_error(self):
        """
        test_replace_integration_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/integrations/testString')
        mock_response = '{"id": "9fab83da-98cb-4f18-a7ba-b6f0435c9673", "type": "type", "metadata": {"endpoint": "endpoint", "crn": "crn", "root_key_id": "root_key_id", "bucket_name": "bucket_name"}, "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PUT,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Construct a dict representation of a IntegrationMetadata model
        integration_metadata_model = {}
        integration_metadata_model['endpoint'] = 'testString'
        integration_metadata_model['crn'] = 'testString'
        integration_metadata_model['root_key_id'] = 'testString'
        integration_metadata_model['bucket_name'] = 'testString'

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        type = 'testString'
        metadata = integration_metadata_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
            "type": type,
            "metadata": metadata,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.replace_integration(**req_copy)

    def test_replace_integration_value_error_with_retries(self):
        # Enable retries and run test_replace_integration_value_error.
        _service.enable_retries()
        self.test_replace_integration_value_error()

        # Disable retries and run test_replace_integration_value_error.
        _service.disable_retries()
        self.test_replace_integration_value_error()


# endregion
##############################################################################
# End of Service: Integrations
##############################################################################

##############################################################################
# Start of Service: SMTPConfigurations
##############################################################################
# region


class TestNewInstance:
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


class TestCreateSmtpConfiguration:
    """
    Test Class for create_smtp_configuration
    """

    @responses.activate
    def test_create_smtp_configuration_all_params(self):
        """
        create_smtp_configuration()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config')
        mock_response = '{"id": "id", "name": "name", "description": "description", "domain": "domain", "config": {"dkim": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}, "en_authorization": {"verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        domain = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.create_smtp_configuration(
            instance_id,
            name,
            domain,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['domain'] == 'testString'
        assert req_body['description'] == 'testString'

    def test_create_smtp_configuration_all_params_with_retries(self):
        # Enable retries and run test_create_smtp_configuration_all_params.
        _service.enable_retries()
        self.test_create_smtp_configuration_all_params()

        # Disable retries and run test_create_smtp_configuration_all_params.
        _service.disable_retries()
        self.test_create_smtp_configuration_all_params()

    @responses.activate
    def test_create_smtp_configuration_value_error(self):
        """
        test_create_smtp_configuration_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config')
        mock_response = '{"id": "id", "name": "name", "description": "description", "domain": "domain", "config": {"dkim": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}, "en_authorization": {"verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}, "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'testString'
        name = 'testString'
        domain = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "name": name,
            "domain": domain,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_smtp_configuration(**req_copy)

    def test_create_smtp_configuration_value_error_with_retries(self):
        # Enable retries and run test_create_smtp_configuration_value_error.
        _service.enable_retries()
        self.test_create_smtp_configuration_value_error()

        # Disable retries and run test_create_smtp_configuration_value_error.
        _service.disable_retries()
        self.test_create_smtp_configuration_value_error()


class TestListSmtpConfigurations:
    """
    Test Class for list_smtp_configurations
    """

    @responses.activate
    def test_list_smtp_configurations_all_params(self):
        """
        list_smtp_configurations()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "smtp_configurations": [{"id": "id", "name": "name", "description": "description", "domain": "domain", "config": {"dkim": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}, "en_authorization": {"verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}, "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        limit = 1
        offset = 0
        search = 'testString'

        # Invoke method
        response = _service.list_smtp_configurations(
            instance_id,
            limit=limit,
            offset=offset,
            search=search,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'search={}'.format(search) in query_string

    def test_list_smtp_configurations_all_params_with_retries(self):
        # Enable retries and run test_list_smtp_configurations_all_params.
        _service.enable_retries()
        self.test_list_smtp_configurations_all_params()

        # Disable retries and run test_list_smtp_configurations_all_params.
        _service.disable_retries()
        self.test_list_smtp_configurations_all_params()

    @responses.activate
    def test_list_smtp_configurations_required_params(self):
        """
        test_list_smtp_configurations_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "smtp_configurations": [{"id": "id", "name": "name", "description": "description", "domain": "domain", "config": {"dkim": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}, "en_authorization": {"verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}, "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.list_smtp_configurations(
            instance_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_smtp_configurations_required_params_with_retries(self):
        # Enable retries and run test_list_smtp_configurations_required_params.
        _service.enable_retries()
        self.test_list_smtp_configurations_required_params()

        # Disable retries and run test_list_smtp_configurations_required_params.
        _service.disable_retries()
        self.test_list_smtp_configurations_required_params()

    @responses.activate
    def test_list_smtp_configurations_value_error(self):
        """
        test_list_smtp_configurations_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "smtp_configurations": [{"id": "id", "name": "name", "description": "description", "domain": "domain", "config": {"dkim": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}, "en_authorization": {"verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}, "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_smtp_configurations(**req_copy)

    def test_list_smtp_configurations_value_error_with_retries(self):
        # Enable retries and run test_list_smtp_configurations_value_error.
        _service.enable_retries()
        self.test_list_smtp_configurations_value_error()

        # Disable retries and run test_list_smtp_configurations_value_error.
        _service.disable_retries()
        self.test_list_smtp_configurations_value_error()

    @responses.activate
    def test_list_smtp_configurations_with_pager_get_next(self):
        """
        test_list_smtp_configurations_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/smtp/config')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"smtp_configurations":[{"id":"id","name":"name","description":"description","domain":"domain","config":{"dkim":{"txt_name":"txt_name","txt_value":"txt_value","verification":"verification"},"en_authorization":{"verification":"verification"},"spf":{"txt_name":"txt_name","txt_value":"txt_value","verification":"verification"}},"updated_at":"2019-01-01T12:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"smtp_configurations":[{"id":"id","name":"name","description":"description","domain":"domain","config":{"dkim":{"txt_name":"txt_name","txt_value":"txt_value","verification":"verification"},"en_authorization":{"verification":"verification"},"spf":{"txt_name":"txt_name","txt_value":"txt_value","verification":"verification"}},"updated_at":"2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = SmtpConfigurationsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_smtp_configurations_with_pager_get_all(self):
        """
        test_list_smtp_configurations_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/smtp/config')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"smtp_configurations":[{"id":"id","name":"name","description":"description","domain":"domain","config":{"dkim":{"txt_name":"txt_name","txt_value":"txt_value","verification":"verification"},"en_authorization":{"verification":"verification"},"spf":{"txt_name":"txt_name","txt_value":"txt_value","verification":"verification"}},"updated_at":"2019-01-01T12:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"smtp_configurations":[{"id":"id","name":"name","description":"description","domain":"domain","config":{"dkim":{"txt_name":"txt_name","txt_value":"txt_value","verification":"verification"},"en_authorization":{"verification":"verification"},"spf":{"txt_name":"txt_name","txt_value":"txt_value","verification":"verification"}},"updated_at":"2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = SmtpConfigurationsPager(
            client=_service,
            instance_id='testString',
            limit=10,
            search='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestCreateSmtpUser:
    """
    Test Class for create_smtp_user
    """

    @responses.activate
    def test_create_smtp_user_all_params(self):
        """
        create_smtp_user()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users')
        mock_response = '{"id": "id", "description": "description", "domain": "domain", "smtp_config_id": "smtp_config_id", "username": "username", "password": "password", "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.create_smtp_user(
            instance_id,
            id,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'testString'

    def test_create_smtp_user_all_params_with_retries(self):
        # Enable retries and run test_create_smtp_user_all_params.
        _service.enable_retries()
        self.test_create_smtp_user_all_params()

        # Disable retries and run test_create_smtp_user_all_params.
        _service.disable_retries()
        self.test_create_smtp_user_all_params()

    @responses.activate
    def test_create_smtp_user_value_error(self):
        """
        test_create_smtp_user_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users')
        mock_response = '{"id": "id", "description": "description", "domain": "domain", "smtp_config_id": "smtp_config_id", "username": "username", "password": "password", "created_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.POST,
            url,
            body=mock_response,
            content_type='application/json',
            status=201,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_smtp_user(**req_copy)

    def test_create_smtp_user_value_error_with_retries(self):
        # Enable retries and run test_create_smtp_user_value_error.
        _service.enable_retries()
        self.test_create_smtp_user_value_error()

        # Disable retries and run test_create_smtp_user_value_error.
        _service.disable_retries()
        self.test_create_smtp_user_value_error()


class TestListSmtpUsers:
    """
    Test Class for list_smtp_users
    """

    @responses.activate
    def test_list_smtp_users_all_params(self):
        """
        list_smtp_users()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "users": [{"id": "id", "smtp_config_id": "smtp_config_id", "description": "description", "domain": "domain", "username": "username", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        limit = 1
        offset = 0
        search = 'testString'

        # Invoke method
        response = _service.list_smtp_users(
            instance_id,
            id,
            limit=limit,
            offset=offset,
            search=search,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'limit={}'.format(limit) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'search={}'.format(search) in query_string

    def test_list_smtp_users_all_params_with_retries(self):
        # Enable retries and run test_list_smtp_users_all_params.
        _service.enable_retries()
        self.test_list_smtp_users_all_params()

        # Disable retries and run test_list_smtp_users_all_params.
        _service.disable_retries()
        self.test_list_smtp_users_all_params()

    @responses.activate
    def test_list_smtp_users_required_params(self):
        """
        test_list_smtp_users_required_params()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "users": [{"id": "id", "smtp_config_id": "smtp_config_id", "description": "description", "domain": "domain", "username": "username", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.list_smtp_users(
            instance_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_smtp_users_required_params_with_retries(self):
        # Enable retries and run test_list_smtp_users_required_params.
        _service.enable_retries()
        self.test_list_smtp_users_required_params()

        # Disable retries and run test_list_smtp_users_required_params.
        _service.disable_retries()
        self.test_list_smtp_users_required_params()

    @responses.activate
    def test_list_smtp_users_value_error(self):
        """
        test_list_smtp_users_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users')
        mock_response = '{"total_count": 11, "offset": 6, "limit": 5, "users": [{"id": "id", "smtp_config_id": "smtp_config_id", "description": "description", "domain": "domain", "username": "username", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}], "first": {"href": "href"}, "previous": {"href": "href"}, "next": {"href": "href"}}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_smtp_users(**req_copy)

    def test_list_smtp_users_value_error_with_retries(self):
        # Enable retries and run test_list_smtp_users_value_error.
        _service.enable_retries()
        self.test_list_smtp_users_value_error()

        # Disable retries and run test_list_smtp_users_value_error.
        _service.disable_retries()
        self.test_list_smtp_users_value_error()

    @responses.activate
    def test_list_smtp_users_with_pager_get_next(self):
        """
        test_list_smtp_users_with_pager_get_next()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"users":[{"id":"id","smtp_config_id":"smtp_config_id","description":"description","domain":"domain","username":"username","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"users":[{"id":"id","smtp_config_id":"smtp_config_id","description":"description","domain":"domain","username":"username","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        all_results = []
        pager = SmtpUsersPager(
            client=_service,
            instance_id='testString',
            id='testString',
            limit=10,
            search='testString',
        )
        while pager.has_next():
            next_page = pager.get_next()
            assert next_page is not None
            all_results.extend(next_page)
        assert len(all_results) == 2

    @responses.activate
    def test_list_smtp_users_with_pager_get_all(self):
        """
        test_list_smtp_users_with_pager_get_all()
        """
        # Set up a two-page mock response
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users')
        mock_response1 = '{"next":{"href":"https://myhost.com/somePath?offset=1"},"total_count":2,"limit":1,"users":[{"id":"id","smtp_config_id":"smtp_config_id","description":"description","domain":"domain","username":"username","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        mock_response2 = '{"total_count":2,"limit":1,"users":[{"id":"id","smtp_config_id":"smtp_config_id","description":"description","domain":"domain","username":"username","created_at":"2019-01-01T12:00:00.000Z","updated_at":"2019-01-01T12:00:00.000Z"}]}'
        responses.add(
            responses.GET,
            url,
            body=mock_response1,
            content_type='application/json',
            status=200,
        )
        responses.add(
            responses.GET,
            url,
            body=mock_response2,
            content_type='application/json',
            status=200,
        )

        # Exercise the pager class for this operation
        pager = SmtpUsersPager(
            client=_service,
            instance_id='testString',
            id='testString',
            limit=10,
            search='testString',
        )
        all_results = pager.get_all()
        assert all_results is not None
        assert len(all_results) == 2


class TestGetSmtpConfiguration:
    """
    Test Class for get_smtp_configuration
    """

    @responses.activate
    def test_get_smtp_configuration_all_params(self):
        """
        get_smtp_configuration()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "domain": "domain", "config": {"dkim": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}, "en_authorization": {"verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}, "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_smtp_configuration(
            instance_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_smtp_configuration_all_params_with_retries(self):
        # Enable retries and run test_get_smtp_configuration_all_params.
        _service.enable_retries()
        self.test_get_smtp_configuration_all_params()

        # Disable retries and run test_get_smtp_configuration_all_params.
        _service.disable_retries()
        self.test_get_smtp_configuration_all_params()

    @responses.activate
    def test_get_smtp_configuration_value_error(self):
        """
        test_get_smtp_configuration_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "domain": "domain", "config": {"dkim": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}, "en_authorization": {"verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}, "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_smtp_configuration(**req_copy)

    def test_get_smtp_configuration_value_error_with_retries(self):
        # Enable retries and run test_get_smtp_configuration_value_error.
        _service.enable_retries()
        self.test_get_smtp_configuration_value_error()

        # Disable retries and run test_get_smtp_configuration_value_error.
        _service.disable_retries()
        self.test_get_smtp_configuration_value_error()


class TestUpdateSmtpConfiguration:
    """
    Test Class for update_smtp_configuration
    """

    @responses.activate
    def test_update_smtp_configuration_all_params(self):
        """
        update_smtp_configuration()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "domain": "domain", "config": {"dkim": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}, "en_authorization": {"verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}, "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.update_smtp_configuration(
            instance_id,
            id,
            name=name,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'

    def test_update_smtp_configuration_all_params_with_retries(self):
        # Enable retries and run test_update_smtp_configuration_all_params.
        _service.enable_retries()
        self.test_update_smtp_configuration_all_params()

        # Disable retries and run test_update_smtp_configuration_all_params.
        _service.disable_retries()
        self.test_update_smtp_configuration_all_params()

    @responses.activate
    def test_update_smtp_configuration_value_error(self):
        """
        test_update_smtp_configuration_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString')
        mock_response = '{"id": "id", "name": "name", "description": "description", "domain": "domain", "config": {"dkim": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}, "en_authorization": {"verification": "verification"}, "spf": {"txt_name": "txt_name", "txt_value": "txt_value", "verification": "verification"}}, "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        name = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_smtp_configuration(**req_copy)

    def test_update_smtp_configuration_value_error_with_retries(self):
        # Enable retries and run test_update_smtp_configuration_value_error.
        _service.enable_retries()
        self.test_update_smtp_configuration_value_error()

        # Disable retries and run test_update_smtp_configuration_value_error.
        _service.disable_retries()
        self.test_update_smtp_configuration_value_error()


class TestDeleteSmtpConfiguration:
    """
    Test Class for delete_smtp_configuration
    """

    @responses.activate
    def test_delete_smtp_configuration_all_params(self):
        """
        delete_smtp_configuration()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.delete_smtp_configuration(
            instance_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_smtp_configuration_all_params_with_retries(self):
        # Enable retries and run test_delete_smtp_configuration_all_params.
        _service.enable_retries()
        self.test_delete_smtp_configuration_all_params()

        # Disable retries and run test_delete_smtp_configuration_all_params.
        _service.disable_retries()
        self.test_delete_smtp_configuration_all_params()

    @responses.activate
    def test_delete_smtp_configuration_value_error(self):
        """
        test_delete_smtp_configuration_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_smtp_configuration(**req_copy)

    def test_delete_smtp_configuration_value_error_with_retries(self):
        # Enable retries and run test_delete_smtp_configuration_value_error.
        _service.enable_retries()
        self.test_delete_smtp_configuration_value_error()

        # Disable retries and run test_delete_smtp_configuration_value_error.
        _service.disable_retries()
        self.test_delete_smtp_configuration_value_error()


class TestGetSmtpUser:
    """
    Test Class for get_smtp_user
    """

    @responses.activate
    def test_get_smtp_user_all_params(self):
        """
        get_smtp_user()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users/testString')
        mock_response = '{"id": "id", "smtp_config_id": "smtp_config_id", "description": "description", "domain": "domain", "username": "username", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        user_id = 'testString'

        # Invoke method
        response = _service.get_smtp_user(
            instance_id,
            id,
            user_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_smtp_user_all_params_with_retries(self):
        # Enable retries and run test_get_smtp_user_all_params.
        _service.enable_retries()
        self.test_get_smtp_user_all_params()

        # Disable retries and run test_get_smtp_user_all_params.
        _service.disable_retries()
        self.test_get_smtp_user_all_params()

    @responses.activate
    def test_get_smtp_user_value_error(self):
        """
        test_get_smtp_user_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users/testString')
        mock_response = '{"id": "id", "smtp_config_id": "smtp_config_id", "description": "description", "domain": "domain", "username": "username", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        user_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
            "user_id": user_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_smtp_user(**req_copy)

    def test_get_smtp_user_value_error_with_retries(self):
        # Enable retries and run test_get_smtp_user_value_error.
        _service.enable_retries()
        self.test_get_smtp_user_value_error()

        # Disable retries and run test_get_smtp_user_value_error.
        _service.disable_retries()
        self.test_get_smtp_user_value_error()


class TestUpdateSmtpUser:
    """
    Test Class for update_smtp_user
    """

    @responses.activate
    def test_update_smtp_user_all_params(self):
        """
        update_smtp_user()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users/testString')
        mock_response = '{"id": "id", "smtp_config_id": "smtp_config_id", "description": "description", "domain": "domain", "username": "username", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        user_id = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.update_smtp_user(
            instance_id,
            id,
            user_id,
            description=description,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['description'] == 'testString'

    def test_update_smtp_user_all_params_with_retries(self):
        # Enable retries and run test_update_smtp_user_all_params.
        _service.enable_retries()
        self.test_update_smtp_user_all_params()

        # Disable retries and run test_update_smtp_user_all_params.
        _service.disable_retries()
        self.test_update_smtp_user_all_params()

    @responses.activate
    def test_update_smtp_user_value_error(self):
        """
        test_update_smtp_user_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users/testString')
        mock_response = '{"id": "id", "smtp_config_id": "smtp_config_id", "description": "description", "domain": "domain", "username": "username", "created_at": "2019-01-01T12:00:00.000Z", "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        user_id = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
            "user_id": user_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_smtp_user(**req_copy)

    def test_update_smtp_user_value_error_with_retries(self):
        # Enable retries and run test_update_smtp_user_value_error.
        _service.enable_retries()
        self.test_update_smtp_user_value_error()

        # Disable retries and run test_update_smtp_user_value_error.
        _service.disable_retries()
        self.test_update_smtp_user_value_error()


class TestDeleteSmtpUser:
    """
    Test Class for delete_smtp_user
    """

    @responses.activate
    def test_delete_smtp_user_all_params(self):
        """
        delete_smtp_user()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        user_id = 'testString'

        # Invoke method
        response = _service.delete_smtp_user(
            instance_id,
            id,
            user_id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_smtp_user_all_params_with_retries(self):
        # Enable retries and run test_delete_smtp_user_all_params.
        _service.enable_retries()
        self.test_delete_smtp_user_all_params()

        # Disable retries and run test_delete_smtp_user_all_params.
        _service.disable_retries()
        self.test_delete_smtp_user_all_params()

    @responses.activate
    def test_delete_smtp_user_value_error(self):
        """
        test_delete_smtp_user_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/users/testString')
        responses.add(
            responses.DELETE,
            url,
            status=204,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        user_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
            "user_id": user_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_smtp_user(**req_copy)

    def test_delete_smtp_user_value_error_with_retries(self):
        # Enable retries and run test_delete_smtp_user_value_error.
        _service.enable_retries()
        self.test_delete_smtp_user_value_error()

        # Disable retries and run test_delete_smtp_user_value_error.
        _service.disable_retries()
        self.test_delete_smtp_user_value_error()


class TestGetSmtpAllowedIps:
    """
    Test Class for get_smtp_allowed_ips
    """

    @responses.activate
    def test_get_smtp_allowed_ips_all_params(self):
        """
        get_smtp_allowed_ips()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/allowed_ips')
        mock_response = '{"subnets": ["subnets"], "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Invoke method
        response = _service.get_smtp_allowed_ips(
            instance_id,
            id,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_smtp_allowed_ips_all_params_with_retries(self):
        # Enable retries and run test_get_smtp_allowed_ips_all_params.
        _service.enable_retries()
        self.test_get_smtp_allowed_ips_all_params()

        # Disable retries and run test_get_smtp_allowed_ips_all_params.
        _service.disable_retries()
        self.test_get_smtp_allowed_ips_all_params()

    @responses.activate
    def test_get_smtp_allowed_ips_value_error(self):
        """
        test_get_smtp_allowed_ips_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/allowed_ips')
        mock_response = '{"subnets": ["subnets"], "updated_at": "2019-01-01T12:00:00.000Z"}'
        responses.add(
            responses.GET,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_smtp_allowed_ips(**req_copy)

    def test_get_smtp_allowed_ips_value_error_with_retries(self):
        # Enable retries and run test_get_smtp_allowed_ips_value_error.
        _service.enable_retries()
        self.test_get_smtp_allowed_ips_value_error()

        # Disable retries and run test_get_smtp_allowed_ips_value_error.
        _service.disable_retries()
        self.test_get_smtp_allowed_ips_value_error()


class TestUpdateVerifySmtp:
    """
    Test Class for update_verify_smtp
    """

    @responses.activate
    def test_update_verify_smtp_all_params(self):
        """
        update_verify_smtp()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/verify')
        mock_response = '{"status": [{"type": "type", "verification": "verification"}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        type = 'testString'

        # Invoke method
        response = _service.update_verify_smtp(
            instance_id,
            id,
            type,
            headers={},
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?', 1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'type={}'.format(type) in query_string

    def test_update_verify_smtp_all_params_with_retries(self):
        # Enable retries and run test_update_verify_smtp_all_params.
        _service.enable_retries()
        self.test_update_verify_smtp_all_params()

        # Disable retries and run test_update_verify_smtp_all_params.
        _service.disable_retries()
        self.test_update_verify_smtp_all_params()

    @responses.activate
    def test_update_verify_smtp_value_error(self):
        """
        test_update_verify_smtp_value_error()
        """
        # Set up mock
        url = preprocess_url('/v1/instances/testString/smtp/config/testString/verify')
        mock_response = '{"status": [{"type": "type", "verification": "verification"}]}'
        responses.add(
            responses.PATCH,
            url,
            body=mock_response,
            content_type='application/json',
            status=200,
        )

        # Set up parameter values
        instance_id = 'testString'
        id = 'testString'
        type = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "id": id,
            "type": type,
        }
        for param in req_param_dict.keys():
            req_copy = {key: val if key is not param else None for (key, val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_verify_smtp(**req_copy)

    def test_update_verify_smtp_value_error_with_retries(self):
        # Enable retries and run test_update_verify_smtp_value_error.
        _service.enable_retries()
        self.test_update_verify_smtp_value_error()

        # Disable retries and run test_update_verify_smtp_value_error.
        _service.disable_retries()
        self.test_update_verify_smtp_value_error()


# endregion
##############################################################################
# End of Service: SMTPConfigurations
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region


class TestModel_Buckets:
    """
    Test Class for Buckets
    """

    def test_buckets_serialization(self):
        """
        Test serialization/deserialization for Buckets
        """

        # Construct a json representation of a Buckets model
        buckets_model_json = {}
        buckets_model_json['doc_count'] = 38
        buckets_model_json['key_as_string'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of Buckets by calling from_dict on the json representation
        buckets_model = Buckets.from_dict(buckets_model_json)
        assert buckets_model != False

        # Construct a model instance of Buckets by calling from_dict on the json representation
        buckets_model_dict = Buckets.from_dict(buckets_model_json).__dict__
        buckets_model2 = Buckets(**buckets_model_dict)

        # Verify the model instances are equivalent
        assert buckets_model == buckets_model2

        # Convert model instance back to dict and verify no loss of data
        buckets_model_json2 = buckets_model.to_dict()
        assert buckets_model_json2 == buckets_model_json


class TestModel_DKIMAttributes:
    """
    Test Class for DKIMAttributes
    """

    def test_dkim_attributes_serialization(self):
        """
        Test serialization/deserialization for DKIMAttributes
        """

        # Construct a json representation of a DKIMAttributes model
        dkim_attributes_model_json = {}
        dkim_attributes_model_json['public_key'] = 'testString'
        dkim_attributes_model_json['selector'] = 'testString'
        dkim_attributes_model_json['verification'] = 'testString'

        # Construct a model instance of DKIMAttributes by calling from_dict on the json representation
        dkim_attributes_model = DKIMAttributes.from_dict(dkim_attributes_model_json)
        assert dkim_attributes_model != False

        # Construct a model instance of DKIMAttributes by calling from_dict on the json representation
        dkim_attributes_model_dict = DKIMAttributes.from_dict(dkim_attributes_model_json).__dict__
        dkim_attributes_model2 = DKIMAttributes(**dkim_attributes_model_dict)

        # Verify the model instances are equivalent
        assert dkim_attributes_model == dkim_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        dkim_attributes_model_json2 = dkim_attributes_model.to_dict()
        assert dkim_attributes_model_json2 == dkim_attributes_model_json


class TestModel_Destination:
    """
    Test Class for Destination
    """

    def test_destination_serialization(self):
        """
        Test serialization/deserialization for Destination
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_config_one_of_model = {}  # DestinationConfigOneOfWebhookDestinationConfig
        destination_config_one_of_model['url'] = 'https://cloud.ibm.com/nhwebhook/sendwebhook'
        destination_config_one_of_model['verb'] = 'post'
        destination_config_one_of_model['custom_headers'] = {'key1': 'testString'}
        destination_config_one_of_model['sensitive_headers'] = ['authorization']

        destination_config_model = {}  # DestinationConfig
        destination_config_model['params'] = destination_config_one_of_model

        # Construct a json representation of a Destination model
        destination_model_json = {}
        destination_model_json['id'] = 'testString'
        destination_model_json['name'] = 'testString'
        destination_model_json['description'] = 'testString'
        destination_model_json['type'] = 'webhook'
        destination_model_json['collect_failed_events'] = False
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


class TestModel_DestinationConfig:
    """
    Test Class for DestinationConfig
    """

    def test_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfig
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_config_one_of_model = {}  # DestinationConfigOneOfWebhookDestinationConfig
        destination_config_one_of_model['url'] = 'https://1ea472c0.us-south.apigw.appdomain.cloud/nhwebhook/sendwebhook'
        destination_config_one_of_model['verb'] = 'post'
        destination_config_one_of_model['custom_headers'] = {'key1': 'testString'}
        destination_config_one_of_model['sensitive_headers'] = ['authorization']

        # Construct a json representation of a DestinationConfig model
        destination_config_model_json = {}
        destination_config_model_json['params'] = destination_config_one_of_model

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


class TestModel_DestinationList:
    """
    Test Class for DestinationList
    """

    def test_destination_list_serialization(self):
        """
        Test serialization/deserialization for DestinationList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_list_item_model = {}  # DestinationListItem
        destination_list_item_model['id'] = '11fe18ba-d0c8-4108-9f07-355e8052a813'
        destination_list_item_model['name'] = 'SL Web'
        destination_list_item_model['description'] = 'This destination is for webhook purpose new'
        destination_list_item_model['type'] = 'webhook'
        destination_list_item_model['collect_failed_events'] = False
        destination_list_item_model['subscription_count'] = 2
        destination_list_item_model['subscription_names'] = ['Webhook Sub for new change']
        destination_list_item_model['updated_at'] = '2021-09-05T00:25:19.599000Z'

        page_href_response_model = {}  # PageHrefResponse
        page_href_response_model['href'] = (
            'https://us-south.event-notifications.cloud.ibm.com/event-notifications/v1/instances/9xxxxx-xxxxx-xxxxx-b3cd-xxxxx/destinations?limit=10&offset=0'
        )

        # Construct a json representation of a DestinationList model
        destination_list_model_json = {}
        destination_list_model_json['total_count'] = 38
        destination_list_model_json['offset'] = 38
        destination_list_model_json['limit'] = 38
        destination_list_model_json['destinations'] = [destination_list_item_model]
        destination_list_model_json['first'] = page_href_response_model
        destination_list_model_json['previous'] = page_href_response_model
        destination_list_model_json['next'] = page_href_response_model

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


class TestModel_DestinationListItem:
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
        destination_list_item_model_json['collect_failed_events'] = False
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


class TestModel_DestinationResponse:
    """
    Test Class for DestinationResponse
    """

    def test_destination_response_serialization(self):
        """
        Test serialization/deserialization for DestinationResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        destination_config_one_of_model = {}  # DestinationConfigOneOfWebhookDestinationConfig
        destination_config_one_of_model['url'] = 'https://cloud.ibm.com/nhwebhook/sendwebhook'
        destination_config_one_of_model['verb'] = 'post'
        destination_config_one_of_model['custom_headers'] = {'key1': 'testString'}
        destination_config_one_of_model['sensitive_headers'] = ['authorization']

        destination_config_model = {}  # DestinationConfig
        destination_config_model['params'] = destination_config_one_of_model

        # Construct a json representation of a DestinationResponse model
        destination_response_model_json = {}
        destination_response_model_json['id'] = 'testString'
        destination_response_model_json['name'] = 'testString'
        destination_response_model_json['description'] = 'testString'
        destination_response_model_json['type'] = 'webhook'
        destination_response_model_json['collect_failed_events'] = False
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


class TestModel_DestinationTagsSubscriptionResponse:
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
        destination_tags_subscription_response_model = DestinationTagsSubscriptionResponse.from_dict(
            destination_tags_subscription_response_model_json
        )
        assert destination_tags_subscription_response_model != False

        # Construct a model instance of DestinationTagsSubscriptionResponse by calling from_dict on the json representation
        destination_tags_subscription_response_model_dict = DestinationTagsSubscriptionResponse.from_dict(
            destination_tags_subscription_response_model_json
        ).__dict__
        destination_tags_subscription_response_model2 = DestinationTagsSubscriptionResponse(
            **destination_tags_subscription_response_model_dict
        )

        # Verify the model instances are equivalent
        assert destination_tags_subscription_response_model == destination_tags_subscription_response_model2

        # Convert model instance back to dict and verify no loss of data
        destination_tags_subscription_response_model_json2 = destination_tags_subscription_response_model.to_dict()
        assert destination_tags_subscription_response_model_json2 == destination_tags_subscription_response_model_json


class TestModel_ENAuthAttributes:
    """
    Test Class for ENAuthAttributes
    """

    def test_en_auth_attributes_serialization(self):
        """
        Test serialization/deserialization for ENAuthAttributes
        """

        # Construct a json representation of a ENAuthAttributes model
        en_auth_attributes_model_json = {}
        en_auth_attributes_model_json['verification'] = 'testString'

        # Construct a model instance of ENAuthAttributes by calling from_dict on the json representation
        en_auth_attributes_model = ENAuthAttributes.from_dict(en_auth_attributes_model_json)
        assert en_auth_attributes_model != False

        # Construct a model instance of ENAuthAttributes by calling from_dict on the json representation
        en_auth_attributes_model_dict = ENAuthAttributes.from_dict(en_auth_attributes_model_json).__dict__
        en_auth_attributes_model2 = ENAuthAttributes(**en_auth_attributes_model_dict)

        # Verify the model instances are equivalent
        assert en_auth_attributes_model == en_auth_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        en_auth_attributes_model_json2 = en_auth_attributes_model.to_dict()
        assert en_auth_attributes_model_json2 == en_auth_attributes_model_json


class TestModel_EmailAttributesResponseInvitedItems:
    """
    Test Class for EmailAttributesResponseInvitedItems
    """

    def test_email_attributes_response_invited_items_serialization(self):
        """
        Test serialization/deserialization for EmailAttributesResponseInvitedItems
        """

        # Construct a json representation of a EmailAttributesResponseInvitedItems model
        email_attributes_response_invited_items_model_json = {}
        email_attributes_response_invited_items_model_json['email'] = 'testString'
        email_attributes_response_invited_items_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        email_attributes_response_invited_items_model_json['expires_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of EmailAttributesResponseInvitedItems by calling from_dict on the json representation
        email_attributes_response_invited_items_model = EmailAttributesResponseInvitedItems.from_dict(
            email_attributes_response_invited_items_model_json
        )
        assert email_attributes_response_invited_items_model != False

        # Construct a model instance of EmailAttributesResponseInvitedItems by calling from_dict on the json representation
        email_attributes_response_invited_items_model_dict = EmailAttributesResponseInvitedItems.from_dict(
            email_attributes_response_invited_items_model_json
        ).__dict__
        email_attributes_response_invited_items_model2 = EmailAttributesResponseInvitedItems(
            **email_attributes_response_invited_items_model_dict
        )

        # Verify the model instances are equivalent
        assert email_attributes_response_invited_items_model == email_attributes_response_invited_items_model2

        # Convert model instance back to dict and verify no loss of data
        email_attributes_response_invited_items_model_json2 = email_attributes_response_invited_items_model.to_dict()
        assert email_attributes_response_invited_items_model_json2 == email_attributes_response_invited_items_model_json


class TestModel_EmailAttributesResponseSubscribedUnsubscribedItems:
    """
    Test Class for EmailAttributesResponseSubscribedUnsubscribedItems
    """

    def test_email_attributes_response_subscribed_unsubscribed_items_serialization(self):
        """
        Test serialization/deserialization for EmailAttributesResponseSubscribedUnsubscribedItems
        """

        # Construct a json representation of a EmailAttributesResponseSubscribedUnsubscribedItems model
        email_attributes_response_subscribed_unsubscribed_items_model_json = {}
        email_attributes_response_subscribed_unsubscribed_items_model_json['email'] = 'testString'
        email_attributes_response_subscribed_unsubscribed_items_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of EmailAttributesResponseSubscribedUnsubscribedItems by calling from_dict on the json representation
        email_attributes_response_subscribed_unsubscribed_items_model = (
            EmailAttributesResponseSubscribedUnsubscribedItems.from_dict(
                email_attributes_response_subscribed_unsubscribed_items_model_json
            )
        )
        assert email_attributes_response_subscribed_unsubscribed_items_model != False

        # Construct a model instance of EmailAttributesResponseSubscribedUnsubscribedItems by calling from_dict on the json representation
        email_attributes_response_subscribed_unsubscribed_items_model_dict = (
            EmailAttributesResponseSubscribedUnsubscribedItems.from_dict(
                email_attributes_response_subscribed_unsubscribed_items_model_json
            ).__dict__
        )
        email_attributes_response_subscribed_unsubscribed_items_model2 = (
            EmailAttributesResponseSubscribedUnsubscribedItems(
                **email_attributes_response_subscribed_unsubscribed_items_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            email_attributes_response_subscribed_unsubscribed_items_model
            == email_attributes_response_subscribed_unsubscribed_items_model2
        )

        # Convert model instance back to dict and verify no loss of data
        email_attributes_response_subscribed_unsubscribed_items_model_json2 = (
            email_attributes_response_subscribed_unsubscribed_items_model.to_dict()
        )
        assert (
            email_attributes_response_subscribed_unsubscribed_items_model_json2
            == email_attributes_response_subscribed_unsubscribed_items_model_json
        )


class TestModel_EnabledCountriesResponse:
    """
    Test Class for EnabledCountriesResponse
    """

    def test_enabled_countries_response_serialization(self):
        """
        Test serialization/deserialization for EnabledCountriesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        sms_country_config_model = {}  # SMSCountryConfig
        sms_country_config_model['number'] = '60454'
        sms_country_config_model['country'] = ['USA', 'CH']

        # Construct a json representation of a EnabledCountriesResponse model
        enabled_countries_response_model_json = {}
        enabled_countries_response_model_json['status'] = 'testString'
        enabled_countries_response_model_json['enabled_countries'] = [sms_country_config_model]

        # Construct a model instance of EnabledCountriesResponse by calling from_dict on the json representation
        enabled_countries_response_model = EnabledCountriesResponse.from_dict(enabled_countries_response_model_json)
        assert enabled_countries_response_model != False

        # Construct a model instance of EnabledCountriesResponse by calling from_dict on the json representation
        enabled_countries_response_model_dict = EnabledCountriesResponse.from_dict(
            enabled_countries_response_model_json
        ).__dict__
        enabled_countries_response_model2 = EnabledCountriesResponse(**enabled_countries_response_model_dict)

        # Verify the model instances are equivalent
        assert enabled_countries_response_model == enabled_countries_response_model2

        # Convert model instance back to dict and verify no loss of data
        enabled_countries_response_model_json2 = enabled_countries_response_model.to_dict()
        assert enabled_countries_response_model_json2 == enabled_countries_response_model_json


class TestModel_Histrogram:
    """
    Test Class for Histrogram
    """

    def test_histrogram_serialization(self):
        """
        Test serialization/deserialization for Histrogram
        """

        # Construct dict forms of any model objects needed in order to build this model.

        buckets_model = {}  # Buckets
        buckets_model['doc_count'] = 38
        buckets_model['key_as_string'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a Histrogram model
        histrogram_model_json = {}
        histrogram_model_json['buckets'] = [buckets_model]

        # Construct a model instance of Histrogram by calling from_dict on the json representation
        histrogram_model = Histrogram.from_dict(histrogram_model_json)
        assert histrogram_model != False

        # Construct a model instance of Histrogram by calling from_dict on the json representation
        histrogram_model_dict = Histrogram.from_dict(histrogram_model_json).__dict__
        histrogram_model2 = Histrogram(**histrogram_model_dict)

        # Verify the model instances are equivalent
        assert histrogram_model == histrogram_model2

        # Convert model instance back to dict and verify no loss of data
        histrogram_model_json2 = histrogram_model.to_dict()
        assert histrogram_model_json2 == histrogram_model_json


class TestModel_IntegrationCreateMetadata:
    """
    Test Class for IntegrationCreateMetadata
    """

    def test_integration_create_metadata_serialization(self):
        """
        Test serialization/deserialization for IntegrationCreateMetadata
        """

        # Construct a json representation of a IntegrationCreateMetadata model
        integration_create_metadata_model_json = {}
        integration_create_metadata_model_json['endpoint'] = 'testString'
        integration_create_metadata_model_json['crn'] = 'testString'
        integration_create_metadata_model_json['bucket_name'] = 'testString'

        # Construct a model instance of IntegrationCreateMetadata by calling from_dict on the json representation
        integration_create_metadata_model = IntegrationCreateMetadata.from_dict(integration_create_metadata_model_json)
        assert integration_create_metadata_model != False

        # Construct a model instance of IntegrationCreateMetadata by calling from_dict on the json representation
        integration_create_metadata_model_dict = IntegrationCreateMetadata.from_dict(
            integration_create_metadata_model_json
        ).__dict__
        integration_create_metadata_model2 = IntegrationCreateMetadata(**integration_create_metadata_model_dict)

        # Verify the model instances are equivalent
        assert integration_create_metadata_model == integration_create_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        integration_create_metadata_model_json2 = integration_create_metadata_model.to_dict()
        assert integration_create_metadata_model_json2 == integration_create_metadata_model_json


class TestModel_IntegrationCreateResponse:
    """
    Test Class for IntegrationCreateResponse
    """

    def test_integration_create_response_serialization(self):
        """
        Test serialization/deserialization for IntegrationCreateResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        integration_create_metadata_model = {}  # IntegrationCreateMetadata
        integration_create_metadata_model['endpoint'] = 'https://s3.us-west.cloud-object-storage.test.appdomain.cloud'
        integration_create_metadata_model['crn'] = (
            'crn:v1:bluemix:public:cloud-object-storage:global:a/xxxxxxx6db359a81a1dde8f44bxxxxxx:xxxxxxxx-1d48-xxxx-xxxx-xxxxxxxxxxxx:bucket:cloud-object-storage'
        )
        integration_create_metadata_model['bucket_name'] = 'cloud-object-storage'

        # Construct a json representation of a IntegrationCreateResponse model
        integration_create_response_model_json = {}
        integration_create_response_model_json['id'] = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        integration_create_response_model_json['type'] = 'testString'
        integration_create_response_model_json['metadata'] = integration_create_metadata_model
        integration_create_response_model_json['created_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of IntegrationCreateResponse by calling from_dict on the json representation
        integration_create_response_model = IntegrationCreateResponse.from_dict(integration_create_response_model_json)
        assert integration_create_response_model != False

        # Construct a model instance of IntegrationCreateResponse by calling from_dict on the json representation
        integration_create_response_model_dict = IntegrationCreateResponse.from_dict(
            integration_create_response_model_json
        ).__dict__
        integration_create_response_model2 = IntegrationCreateResponse(**integration_create_response_model_dict)

        # Verify the model instances are equivalent
        assert integration_create_response_model == integration_create_response_model2

        # Convert model instance back to dict and verify no loss of data
        integration_create_response_model_json2 = integration_create_response_model.to_dict()
        assert integration_create_response_model_json2 == integration_create_response_model_json


class TestModel_IntegrationGetResponse:
    """
    Test Class for IntegrationGetResponse
    """

    def test_integration_get_response_serialization(self):
        """
        Test serialization/deserialization for IntegrationGetResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        integration_metadata_model = {}  # IntegrationMetadata
        integration_metadata_model['endpoint'] = 'https://private.us-south.kms.cloud.ibm.com'
        integration_metadata_model['crn'] = 'crn:v1:staging:public:kms:us-south:a/****:****::'
        integration_metadata_model['root_key_id'] = 'cf49847c-bd3e-4fda-853f-2bcf0575a895'
        integration_metadata_model['bucket_name'] = 'cloud-object-storage'

        # Construct a json representation of a IntegrationGetResponse model
        integration_get_response_model_json = {}
        integration_get_response_model_json['id'] = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        integration_get_response_model_json['type'] = 'testString'
        integration_get_response_model_json['metadata'] = integration_metadata_model
        integration_get_response_model_json['created_at'] = '2019-01-01T12:00:00Z'
        integration_get_response_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of IntegrationGetResponse by calling from_dict on the json representation
        integration_get_response_model = IntegrationGetResponse.from_dict(integration_get_response_model_json)
        assert integration_get_response_model != False

        # Construct a model instance of IntegrationGetResponse by calling from_dict on the json representation
        integration_get_response_model_dict = IntegrationGetResponse.from_dict(
            integration_get_response_model_json
        ).__dict__
        integration_get_response_model2 = IntegrationGetResponse(**integration_get_response_model_dict)

        # Verify the model instances are equivalent
        assert integration_get_response_model == integration_get_response_model2

        # Convert model instance back to dict and verify no loss of data
        integration_get_response_model_json2 = integration_get_response_model.to_dict()
        assert integration_get_response_model_json2 == integration_get_response_model_json


class TestModel_IntegrationList:
    """
    Test Class for IntegrationList
    """

    def test_integration_list_serialization(self):
        """
        Test serialization/deserialization for IntegrationList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        integration_metadata_model = {}  # IntegrationMetadata
        integration_metadata_model['endpoint'] = 'https://private.us-south.kms.cloud.ibm.com'
        integration_metadata_model['crn'] = 'crn:v1:staging:public:kms:us-south:a/****:****::'
        integration_metadata_model['root_key_id'] = 'cf49847c-bd3e-4fda-853f-2bcf0575a895'
        integration_metadata_model['bucket_name'] = 'testString'

        integration_list_item_model = {}  # IntegrationListItem
        integration_list_item_model['id'] = 'bc0cb555-bf6d-444f-b8f3-069199b04a77'
        integration_list_item_model['type'] = 'kms'
        integration_list_item_model['metadata'] = integration_metadata_model
        integration_list_item_model['created_at'] = '2021-08-18T09:50:32.133000Z'
        integration_list_item_model['updated_at'] = '2021-08-18T09:50:32.133000Z'

        page_href_response_model = {}  # PageHrefResponse
        page_href_response_model['href'] = (
            'https://us-south.event-notifications.cloud.ibm.com/event-notifications/v1/instances/9xxxxx-xxxxx-xxxxx-b3cd-xxxxx/integrations?limit=10&offset=0'
        )

        # Construct a json representation of a IntegrationList model
        integration_list_model_json = {}
        integration_list_model_json['total_count'] = 0
        integration_list_model_json['offset'] = 38
        integration_list_model_json['limit'] = 38
        integration_list_model_json['integrations'] = [integration_list_item_model]
        integration_list_model_json['first'] = page_href_response_model
        integration_list_model_json['previous'] = page_href_response_model
        integration_list_model_json['next'] = page_href_response_model

        # Construct a model instance of IntegrationList by calling from_dict on the json representation
        integration_list_model = IntegrationList.from_dict(integration_list_model_json)
        assert integration_list_model != False

        # Construct a model instance of IntegrationList by calling from_dict on the json representation
        integration_list_model_dict = IntegrationList.from_dict(integration_list_model_json).__dict__
        integration_list_model2 = IntegrationList(**integration_list_model_dict)

        # Verify the model instances are equivalent
        assert integration_list_model == integration_list_model2

        # Convert model instance back to dict and verify no loss of data
        integration_list_model_json2 = integration_list_model.to_dict()
        assert integration_list_model_json2 == integration_list_model_json


class TestModel_IntegrationListItem:
    """
    Test Class for IntegrationListItem
    """

    def test_integration_list_item_serialization(self):
        """
        Test serialization/deserialization for IntegrationListItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        integration_metadata_model = {}  # IntegrationMetadata
        integration_metadata_model['endpoint'] = 'https://private.us-south.kms.cloud.ibm.com'
        integration_metadata_model['crn'] = 'crn:v1:staging:public:kms:us-south:a/****:****::'
        integration_metadata_model['root_key_id'] = 'cf49847c-bd3e-4fda-853f-2bcf0575a895'
        integration_metadata_model['bucket_name'] = 'testString'

        # Construct a json representation of a IntegrationListItem model
        integration_list_item_model_json = {}
        integration_list_item_model_json['id'] = '9fab83da-98cb-4f18-a7ba-b6f0435c9673'
        integration_list_item_model_json['type'] = 'testString'
        integration_list_item_model_json['metadata'] = integration_metadata_model
        integration_list_item_model_json['created_at'] = '2019-01-01T12:00:00Z'
        integration_list_item_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of IntegrationListItem by calling from_dict on the json representation
        integration_list_item_model = IntegrationListItem.from_dict(integration_list_item_model_json)
        assert integration_list_item_model != False

        # Construct a model instance of IntegrationListItem by calling from_dict on the json representation
        integration_list_item_model_dict = IntegrationListItem.from_dict(integration_list_item_model_json).__dict__
        integration_list_item_model2 = IntegrationListItem(**integration_list_item_model_dict)

        # Verify the model instances are equivalent
        assert integration_list_item_model == integration_list_item_model2

        # Convert model instance back to dict and verify no loss of data
        integration_list_item_model_json2 = integration_list_item_model.to_dict()
        assert integration_list_item_model_json2 == integration_list_item_model_json


class TestModel_IntegrationMetadata:
    """
    Test Class for IntegrationMetadata
    """

    def test_integration_metadata_serialization(self):
        """
        Test serialization/deserialization for IntegrationMetadata
        """

        # Construct a json representation of a IntegrationMetadata model
        integration_metadata_model_json = {}
        integration_metadata_model_json['endpoint'] = 'testString'
        integration_metadata_model_json['crn'] = 'testString'
        integration_metadata_model_json['root_key_id'] = 'testString'
        integration_metadata_model_json['bucket_name'] = 'testString'

        # Construct a model instance of IntegrationMetadata by calling from_dict on the json representation
        integration_metadata_model = IntegrationMetadata.from_dict(integration_metadata_model_json)
        assert integration_metadata_model != False

        # Construct a model instance of IntegrationMetadata by calling from_dict on the json representation
        integration_metadata_model_dict = IntegrationMetadata.from_dict(integration_metadata_model_json).__dict__
        integration_metadata_model2 = IntegrationMetadata(**integration_metadata_model_dict)

        # Verify the model instances are equivalent
        assert integration_metadata_model == integration_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        integration_metadata_model_json2 = integration_metadata_model.to_dict()
        assert integration_metadata_model_json2 == integration_metadata_model_json


class TestModel_Metric:
    """
    Test Class for Metric
    """

    def test_metric_serialization(self):
        """
        Test serialization/deserialization for Metric
        """

        # Construct dict forms of any model objects needed in order to build this model.

        buckets_model = {}  # Buckets
        buckets_model['doc_count'] = 38
        buckets_model['key_as_string'] = '2019-01-01T12:00:00Z'

        histrogram_model = {}  # Histrogram
        histrogram_model['buckets'] = [buckets_model]

        # Construct a json representation of a Metric model
        metric_model_json = {}
        metric_model_json['key'] = 'bounced'
        metric_model_json['doc_count'] = 38
        metric_model_json['histogram'] = histrogram_model

        # Construct a model instance of Metric by calling from_dict on the json representation
        metric_model = Metric.from_dict(metric_model_json)
        assert metric_model != False

        # Construct a model instance of Metric by calling from_dict on the json representation
        metric_model_dict = Metric.from_dict(metric_model_json).__dict__
        metric_model2 = Metric(**metric_model_dict)

        # Verify the model instances are equivalent
        assert metric_model == metric_model2

        # Convert model instance back to dict and verify no loss of data
        metric_model_json2 = metric_model.to_dict()
        assert metric_model_json2 == metric_model_json


class TestModel_Metrics:
    """
    Test Class for Metrics
    """

    def test_metrics_serialization(self):
        """
        Test serialization/deserialization for Metrics
        """

        # Construct dict forms of any model objects needed in order to build this model.

        buckets_model = {}  # Buckets
        buckets_model['doc_count'] = 1
        buckets_model['key_as_string'] = '2024-06-16T09:00:00Z'

        histrogram_model = {}  # Histrogram
        histrogram_model['buckets'] = [buckets_model]

        metric_model = {}  # Metric
        metric_model['key'] = 'bounced'
        metric_model['doc_count'] = 1
        metric_model['histogram'] = histrogram_model

        # Construct a json representation of a Metrics model
        metrics_model_json = {}
        metrics_model_json['metrics'] = [metric_model]

        # Construct a model instance of Metrics by calling from_dict on the json representation
        metrics_model = Metrics.from_dict(metrics_model_json)
        assert metrics_model != False

        # Construct a model instance of Metrics by calling from_dict on the json representation
        metrics_model_dict = Metrics.from_dict(metrics_model_json).__dict__
        metrics_model2 = Metrics(**metrics_model_dict)

        # Verify the model instances are equivalent
        assert metrics_model == metrics_model2

        # Convert model instance back to dict and verify no loss of data
        metrics_model_json2 = metrics_model.to_dict()
        assert metrics_model_json2 == metrics_model_json


class TestModel_NotificationCreate:
    """
    Test Class for NotificationCreate
    """

    def test_notification_create_serialization(self):
        """
        Test serialization/deserialization for NotificationCreate
        """

        # Construct a json representation of a NotificationCreate model
        notification_create_model_json = {}
        notification_create_model_json['specversion'] = '1.0'
        notification_create_model_json['time'] = '2019-01-01T12:00:00Z'
        notification_create_model_json['id'] = 'testString'
        notification_create_model_json['source'] = 'testString'
        notification_create_model_json['type'] = 'testString'
        notification_create_model_json['ibmenseverity'] = 'testString'
        notification_create_model_json['ibmensourceid'] = 'testString'
        notification_create_model_json['ibmendefaultshort'] = 'testString'
        notification_create_model_json['ibmendefaultlong'] = 'testString'
        notification_create_model_json['ibmensubject'] = 'testString'
        notification_create_model_json['ibmentemplates'] = 'testString'
        notification_create_model_json['ibmenmailto'] = 'testString'
        notification_create_model_json['ibmensmsto'] = 'testString'
        notification_create_model_json['ibmenhtmlbody'] = 'testString'
        notification_create_model_json['subject'] = 'testString'
        notification_create_model_json['ibmenmms'] = 'testString'
        notification_create_model_json['data'] = {'foo': 'bar'}
        notification_create_model_json['datacontenttype'] = 'application/json'
        notification_create_model_json['ibmenpushto'] = '{"platforms":["push_android"]}'
        notification_create_model_json['ibmenfcmbody'] = 'testString'
        notification_create_model_json['ibmenapnsbody'] = 'testString'
        notification_create_model_json['ibmenapnsheaders'] = 'testString'
        notification_create_model_json['ibmenchromebody'] = 'testString'
        notification_create_model_json['ibmenchromeheaders'] = '{"TTL":3600,"Topic":"test","Urgency":"high"}'
        notification_create_model_json['ibmenfirefoxbody'] = 'testString'
        notification_create_model_json['ibmenfirefoxheaders'] = '{"TTL":3600,"Topic":"test","Urgency":"high"}'
        notification_create_model_json['ibmenhuaweibody'] = 'testString'
        notification_create_model_json['ibmensafaribody'] = 'testString'
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


class TestModel_NotificationResponse:
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


class TestModel_PageHrefResponse:
    """
    Test Class for PageHrefResponse
    """

    def test_page_href_response_serialization(self):
        """
        Test serialization/deserialization for PageHrefResponse
        """

        # Construct a json representation of a PageHrefResponse model
        page_href_response_model_json = {}
        page_href_response_model_json['href'] = 'testString'

        # Construct a model instance of PageHrefResponse by calling from_dict on the json representation
        page_href_response_model = PageHrefResponse.from_dict(page_href_response_model_json)
        assert page_href_response_model != False

        # Construct a model instance of PageHrefResponse by calling from_dict on the json representation
        page_href_response_model_dict = PageHrefResponse.from_dict(page_href_response_model_json).__dict__
        page_href_response_model2 = PageHrefResponse(**page_href_response_model_dict)

        # Verify the model instances are equivalent
        assert page_href_response_model == page_href_response_model2

        # Convert model instance back to dict and verify no loss of data
        page_href_response_model_json2 = page_href_response_model.to_dict()
        assert page_href_response_model_json2 == page_href_response_model_json


class TestModel_Rules:
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


class TestModel_RulesGet:
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


class TestModel_SMSAttributesItems:
    """
    Test Class for SMSAttributesItems
    """

    def test_sms_attributes_items_serialization(self):
        """
        Test serialization/deserialization for SMSAttributesItems
        """

        # Construct a json representation of a SMSAttributesItems model
        sms_attributes_items_model_json = {}
        sms_attributes_items_model_json['phone_number'] = 'testString'
        sms_attributes_items_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of SMSAttributesItems by calling from_dict on the json representation
        sms_attributes_items_model = SMSAttributesItems.from_dict(sms_attributes_items_model_json)
        assert sms_attributes_items_model != False

        # Construct a model instance of SMSAttributesItems by calling from_dict on the json representation
        sms_attributes_items_model_dict = SMSAttributesItems.from_dict(sms_attributes_items_model_json).__dict__
        sms_attributes_items_model2 = SMSAttributesItems(**sms_attributes_items_model_dict)

        # Verify the model instances are equivalent
        assert sms_attributes_items_model == sms_attributes_items_model2

        # Convert model instance back to dict and verify no loss of data
        sms_attributes_items_model_json2 = sms_attributes_items_model.to_dict()
        assert sms_attributes_items_model_json2 == sms_attributes_items_model_json


class TestModel_SMSCountryConfig:
    """
    Test Class for SMSCountryConfig
    """

    def test_sms_country_config_serialization(self):
        """
        Test serialization/deserialization for SMSCountryConfig
        """

        # Construct a json representation of a SMSCountryConfig model
        sms_country_config_model_json = {}
        sms_country_config_model_json['number'] = 'testString'
        sms_country_config_model_json['country'] = ['testString']

        # Construct a model instance of SMSCountryConfig by calling from_dict on the json representation
        sms_country_config_model = SMSCountryConfig.from_dict(sms_country_config_model_json)
        assert sms_country_config_model != False

        # Construct a model instance of SMSCountryConfig by calling from_dict on the json representation
        sms_country_config_model_dict = SMSCountryConfig.from_dict(sms_country_config_model_json).__dict__
        sms_country_config_model2 = SMSCountryConfig(**sms_country_config_model_dict)

        # Verify the model instances are equivalent
        assert sms_country_config_model == sms_country_config_model2

        # Convert model instance back to dict and verify no loss of data
        sms_country_config_model_json2 = sms_country_config_model.to_dict()
        assert sms_country_config_model_json2 == sms_country_config_model_json


class TestModel_SMSInviteAttributesItems:
    """
    Test Class for SMSInviteAttributesItems
    """

    def test_sms_invite_attributes_items_serialization(self):
        """
        Test serialization/deserialization for SMSInviteAttributesItems
        """

        # Construct a json representation of a SMSInviteAttributesItems model
        sms_invite_attributes_items_model_json = {}
        sms_invite_attributes_items_model_json['phone_number'] = 'testString'
        sms_invite_attributes_items_model_json['updated_at'] = '2019-01-01T12:00:00Z'
        sms_invite_attributes_items_model_json['expires_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of SMSInviteAttributesItems by calling from_dict on the json representation
        sms_invite_attributes_items_model = SMSInviteAttributesItems.from_dict(sms_invite_attributes_items_model_json)
        assert sms_invite_attributes_items_model != False

        # Construct a model instance of SMSInviteAttributesItems by calling from_dict on the json representation
        sms_invite_attributes_items_model_dict = SMSInviteAttributesItems.from_dict(
            sms_invite_attributes_items_model_json
        ).__dict__
        sms_invite_attributes_items_model2 = SMSInviteAttributesItems(**sms_invite_attributes_items_model_dict)

        # Verify the model instances are equivalent
        assert sms_invite_attributes_items_model == sms_invite_attributes_items_model2

        # Convert model instance back to dict and verify no loss of data
        sms_invite_attributes_items_model_json2 = sms_invite_attributes_items_model.to_dict()
        assert sms_invite_attributes_items_model_json2 == sms_invite_attributes_items_model_json


class TestModel_SMTPAllowedIPs:
    """
    Test Class for SMTPAllowedIPs
    """

    def test_smtp_allowed_i_ps_serialization(self):
        """
        Test serialization/deserialization for SMTPAllowedIPs
        """

        # Construct a json representation of a SMTPAllowedIPs model
        smtp_allowed_i_ps_model_json = {}
        smtp_allowed_i_ps_model_json['subnets'] = ['testString']
        smtp_allowed_i_ps_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of SMTPAllowedIPs by calling from_dict on the json representation
        smtp_allowed_i_ps_model = SMTPAllowedIPs.from_dict(smtp_allowed_i_ps_model_json)
        assert smtp_allowed_i_ps_model != False

        # Construct a model instance of SMTPAllowedIPs by calling from_dict on the json representation
        smtp_allowed_i_ps_model_dict = SMTPAllowedIPs.from_dict(smtp_allowed_i_ps_model_json).__dict__
        smtp_allowed_i_ps_model2 = SMTPAllowedIPs(**smtp_allowed_i_ps_model_dict)

        # Verify the model instances are equivalent
        assert smtp_allowed_i_ps_model == smtp_allowed_i_ps_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_allowed_i_ps_model_json2 = smtp_allowed_i_ps_model.to_dict()
        assert smtp_allowed_i_ps_model_json2 == smtp_allowed_i_ps_model_json


class TestModel_SMTPConfig:
    """
    Test Class for SMTPConfig
    """

    def test_smtp_config_serialization(self):
        """
        Test serialization/deserialization for SMTPConfig
        """

        # Construct dict forms of any model objects needed in order to build this model.

        smtpdkim_attributes_model = {}  # SMTPDKIMAttributes
        smtpdkim_attributes_model['txt_name'] = (
            '35ef4bc3-a7a6-48e9-882a-6fd70c162ec2._domainkey.abc.event-notifications.test.cloud.ibm.com'
        )
        smtpdkim_attributes_model['txt_value'] = (
            'v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuzCOM3TfCHGzZ6myd5DIQPjahLjkbK15aiq7ElDhqHQwNq/5EnPutNptFg7LurV2o9Tl9GSrPFC9GGJn8+5wtJRoeHfSm//dPXB9dpQb4rRjono8obaAbc2A6tVBXdFf814tw04ZDw6JzCmn3RvVmAy5+mwQ+SL6oqbU62CMv6eLtF26MEagbUZKmp5mpru0natkV/mwPk/vudJ8eVoOyjTfwRws9dLc3JaTdT77wSkyKqW64nYePO4j8kVHXj2bQTm4M+GJL2bzc8RwPKPvdy/FiK4Op2qzbzHNGL/V9Fj9xhYE4p1sopLJtZaTvkbZqbvB1KZJ1YqByHl4zcL/uQIDAQAB'
        )
        smtpdkim_attributes_model['verification'] = 'PENDING'

        en_auth_attributes_model = {}  # ENAuthAttributes
        en_auth_attributes_model['verification'] = 'PENDING'

        spf_attributes_model = {}  # SPFAttributes
        spf_attributes_model['txt_name'] = 'test.com'
        spf_attributes_model['txt_value'] = 'v=spf1 include:mail.event-notifications.test.cloud.ibm.com -all'
        spf_attributes_model['verification'] = 'PENDING'

        # Construct a json representation of a SMTPConfig model
        smtp_config_model_json = {}
        smtp_config_model_json['dkim'] = smtpdkim_attributes_model
        smtp_config_model_json['en_authorization'] = en_auth_attributes_model
        smtp_config_model_json['spf'] = spf_attributes_model

        # Construct a model instance of SMTPConfig by calling from_dict on the json representation
        smtp_config_model = SMTPConfig.from_dict(smtp_config_model_json)
        assert smtp_config_model != False

        # Construct a model instance of SMTPConfig by calling from_dict on the json representation
        smtp_config_model_dict = SMTPConfig.from_dict(smtp_config_model_json).__dict__
        smtp_config_model2 = SMTPConfig(**smtp_config_model_dict)

        # Verify the model instances are equivalent
        assert smtp_config_model == smtp_config_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_config_model_json2 = smtp_config_model.to_dict()
        assert smtp_config_model_json2 == smtp_config_model_json


class TestModel_SMTPConfiguration:
    """
    Test Class for SMTPConfiguration
    """

    def test_smtp_configuration_serialization(self):
        """
        Test serialization/deserialization for SMTPConfiguration
        """

        # Construct dict forms of any model objects needed in order to build this model.

        smtpdkim_attributes_model = {}  # SMTPDKIMAttributes
        smtpdkim_attributes_model['txt_name'] = (
            '35ef4bc3-a7a6-48e9-882a-6fd70c162ec2._domainkey.abc.event-notifications.test.cloud.ibm.com'
        )
        smtpdkim_attributes_model['txt_value'] = (
            'v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuzCOM3TfCHGzZ6myd5DIQPjahLjkbK15aiq7ElDhqHQwNq/5EnPutNptFg7LurV2o9Tl9GSrPFC9GGJn8+5wtJRoeHfSm//dPXB9dpQb4rRjono8obaAbc2A6tVBXdFf814tw04ZDw6JzCmn3RvVmAy5+mwQ+SL6oqbU62CMv6eLtF26MEagbUZKmp5mpru0natkV/mwPk/vudJ8eVoOyjTfwRws9dLc3JaTdT77wSkyKqW64nYePO4j8kVHXj2bQTm4M+GJL2bzc8RwPKPvdy/FiK4Op2qzbzHNGL/V9Fj9xhYE4p1sopLJtZaTvkbZqbvB1KZJ1YqByHl4zcL/uQIDAQAB'
        )
        smtpdkim_attributes_model['verification'] = 'PENDING'

        en_auth_attributes_model = {}  # ENAuthAttributes
        en_auth_attributes_model['verification'] = 'SUCCESSFUL'

        spf_attributes_model = {}  # SPFAttributes
        spf_attributes_model['txt_name'] = 'maily.event-notifications.test.cloud.ibm.com'
        spf_attributes_model['txt_value'] = 'v=spf1 include:mail.event-notifications.test.cloud.ibm.com -all'
        spf_attributes_model['verification'] = 'PENDING'

        smtp_config_model = {}  # SMTPConfig
        smtp_config_model['dkim'] = smtpdkim_attributes_model
        smtp_config_model['en_authorization'] = en_auth_attributes_model
        smtp_config_model['spf'] = spf_attributes_model

        # Construct a json representation of a SMTPConfiguration model
        smtp_configuration_model_json = {}
        smtp_configuration_model_json['id'] = 'testString'
        smtp_configuration_model_json['name'] = 'testString'
        smtp_configuration_model_json['description'] = 'testString'
        smtp_configuration_model_json['domain'] = 'testString'
        smtp_configuration_model_json['config'] = smtp_config_model
        smtp_configuration_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of SMTPConfiguration by calling from_dict on the json representation
        smtp_configuration_model = SMTPConfiguration.from_dict(smtp_configuration_model_json)
        assert smtp_configuration_model != False

        # Construct a model instance of SMTPConfiguration by calling from_dict on the json representation
        smtp_configuration_model_dict = SMTPConfiguration.from_dict(smtp_configuration_model_json).__dict__
        smtp_configuration_model2 = SMTPConfiguration(**smtp_configuration_model_dict)

        # Verify the model instances are equivalent
        assert smtp_configuration_model == smtp_configuration_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_configuration_model_json2 = smtp_configuration_model.to_dict()
        assert smtp_configuration_model_json2 == smtp_configuration_model_json


class TestModel_SMTPConfigurationsList:
    """
    Test Class for SMTPConfigurationsList
    """

    def test_smtp_configurations_list_serialization(self):
        """
        Test serialization/deserialization for SMTPConfigurationsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        smtpdkim_attributes_model = {}  # SMTPDKIMAttributes
        smtpdkim_attributes_model['txt_name'] = (
            '35ef4bc3-a7a6-48e9-882a-6fd70c162ec2._domainkey.abc.event-notifications.test.cloud.ibm.com'
        )
        smtpdkim_attributes_model['txt_value'] = (
            'v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuzCOM3TfCHGzZ6myd5DIQPjahLjkbK15aiq7ElDhqHQwNq/5EnPutNptFg7LurV2o9Tl9GSrPFC9GGJn8+5wtJRoeHfSm//dPXB9dpQb4rRjono8obaAbc2A6tVBXdFf814tw04ZDw6JzCmn3RvVmAy5+mwQ+SL6oqbU62CMv6eLtF26MEagbUZKmp5mpru0natkV/mwPk/vudJ8eVoOyjTfwRws9dLc3JaTdT77wSkyKqW64nYePO4j8kVHXj2bQTm4M+GJL2bzc8RwPKPvdy/FiK4Op2qzbzHNGL/V9Fj9xhYE4p1sopLJtZaTvkbZqbvB1KZJ1YqByHl4zcL/uQIDAQAB'
        )
        smtpdkim_attributes_model['verification'] = 'PENDING'

        en_auth_attributes_model = {}  # ENAuthAttributes
        en_auth_attributes_model['verification'] = 'SUCCESSFUL'

        spf_attributes_model = {}  # SPFAttributes
        spf_attributes_model['txt_name'] = 'test.event-notifications.test.cloud.ibm.com'
        spf_attributes_model['txt_value'] = 'v=spf1 include:mail.event-notifications.test.cloud.ibm.com -all'
        spf_attributes_model['verification'] = 'SUCCESSFUL'

        smtp_config_model = {}  # SMTPConfig
        smtp_config_model['dkim'] = smtpdkim_attributes_model
        smtp_config_model['en_authorization'] = en_auth_attributes_model
        smtp_config_model['spf'] = spf_attributes_model

        smtp_configuration_model = {}  # SMTPConfiguration
        smtp_configuration_model['id'] = 'accec70c-752d-4920-bf86-146b2eade10f'
        smtp_configuration_model['name'] = 'revolutionize front-end markets'
        smtp_configuration_model['description'] = 'disintermediate clicks-and-mortar channels'
        smtp_configuration_model['domain'] = 'test.event-notifications.test.cloud.ibm.com'
        smtp_configuration_model['config'] = smtp_config_model
        smtp_configuration_model['updated_at'] = '2024-04-16T20:04:40.055000Z'

        page_href_response_model = {}  # PageHrefResponse
        page_href_response_model['href'] = 'testString'

        # Construct a json representation of a SMTPConfigurationsList model
        smtp_configurations_list_model_json = {}
        smtp_configurations_list_model_json['total_count'] = 38
        smtp_configurations_list_model_json['offset'] = 38
        smtp_configurations_list_model_json['limit'] = 38
        smtp_configurations_list_model_json['smtp_configurations'] = [smtp_configuration_model]
        smtp_configurations_list_model_json['first'] = page_href_response_model
        smtp_configurations_list_model_json['previous'] = page_href_response_model
        smtp_configurations_list_model_json['next'] = page_href_response_model

        # Construct a model instance of SMTPConfigurationsList by calling from_dict on the json representation
        smtp_configurations_list_model = SMTPConfigurationsList.from_dict(smtp_configurations_list_model_json)
        assert smtp_configurations_list_model != False

        # Construct a model instance of SMTPConfigurationsList by calling from_dict on the json representation
        smtp_configurations_list_model_dict = SMTPConfigurationsList.from_dict(
            smtp_configurations_list_model_json
        ).__dict__
        smtp_configurations_list_model2 = SMTPConfigurationsList(**smtp_configurations_list_model_dict)

        # Verify the model instances are equivalent
        assert smtp_configurations_list_model == smtp_configurations_list_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_configurations_list_model_json2 = smtp_configurations_list_model.to_dict()
        assert smtp_configurations_list_model_json2 == smtp_configurations_list_model_json


class TestModel_SMTPCreateResponse:
    """
    Test Class for SMTPCreateResponse
    """

    def test_smtp_create_response_serialization(self):
        """
        Test serialization/deserialization for SMTPCreateResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        smtpdkim_attributes_model = {}  # SMTPDKIMAttributes
        smtpdkim_attributes_model['txt_name'] = (
            '35ef4bc3-a7a6-48e9-882a-6fd70c162ec2._domainkey.abc.event-notifications.test.cloud.ibm.com'
        )
        smtpdkim_attributes_model['txt_value'] = (
            'v=DKIM1; h=sha256; k=rsa; p=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuzCOM3TfCHGzZ6myd5DIQPjahLjkbK15aiq7ElDhqHQwNq/5EnPutNptFg7LurV2o9Tl9GSrPFC9GGJn8+5wtJRoeHfSm//dPXB9dpQb4rRjono8obaAbc2A6tVBXdFf814tw04ZDw6JzCmn3RvVmAy5+mwQ+SL6oqbU62CMv6eLtF26MEagbUZKmp5mpru0natkV/mwPk/vudJ8eVoOyjTfwRws9dLc3JaTdT77wSkyKqW64nYePO4j8kVHXj2bQTm4M+GJL2bzc8RwPKPvdy/FiK4Op2qzbzHNGL/V9Fj9xhYE4p1sopLJtZaTvkbZqbvB1KZJ1YqByHl4zcL/uQIDAQAB'
        )
        smtpdkim_attributes_model['verification'] = 'PENDING'

        en_auth_attributes_model = {}  # ENAuthAttributes
        en_auth_attributes_model['verification'] = 'PENDING'

        spf_attributes_model = {}  # SPFAttributes
        spf_attributes_model['txt_name'] = 'cloudflare-ipfs.com'
        spf_attributes_model['txt_value'] = 'v=spf1 include:mail.event-notifications.test.cloud.ibm.com -all'
        spf_attributes_model['verification'] = 'SUCCESSFUL'

        smtp_config_model = {}  # SMTPConfig
        smtp_config_model['dkim'] = smtpdkim_attributes_model
        smtp_config_model['en_authorization'] = en_auth_attributes_model
        smtp_config_model['spf'] = spf_attributes_model

        # Construct a json representation of a SMTPCreateResponse model
        smtp_create_response_model_json = {}
        smtp_create_response_model_json['id'] = 'testString'
        smtp_create_response_model_json['name'] = 'testString'
        smtp_create_response_model_json['description'] = 'testString'
        smtp_create_response_model_json['domain'] = 'testString'
        smtp_create_response_model_json['config'] = smtp_config_model
        smtp_create_response_model_json['created_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of SMTPCreateResponse by calling from_dict on the json representation
        smtp_create_response_model = SMTPCreateResponse.from_dict(smtp_create_response_model_json)
        assert smtp_create_response_model != False

        # Construct a model instance of SMTPCreateResponse by calling from_dict on the json representation
        smtp_create_response_model_dict = SMTPCreateResponse.from_dict(smtp_create_response_model_json).__dict__
        smtp_create_response_model2 = SMTPCreateResponse(**smtp_create_response_model_dict)

        # Verify the model instances are equivalent
        assert smtp_create_response_model == smtp_create_response_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_create_response_model_json2 = smtp_create_response_model.to_dict()
        assert smtp_create_response_model_json2 == smtp_create_response_model_json


class TestModel_SMTPDKIMAttributes:
    """
    Test Class for SMTPDKIMAttributes
    """

    def test_smtpdkim_attributes_serialization(self):
        """
        Test serialization/deserialization for SMTPDKIMAttributes
        """

        # Construct a json representation of a SMTPDKIMAttributes model
        smtpdkim_attributes_model_json = {}
        smtpdkim_attributes_model_json['txt_name'] = 'testString'
        smtpdkim_attributes_model_json['txt_value'] = 'testString'
        smtpdkim_attributes_model_json['verification'] = 'testString'

        # Construct a model instance of SMTPDKIMAttributes by calling from_dict on the json representation
        smtpdkim_attributes_model = SMTPDKIMAttributes.from_dict(smtpdkim_attributes_model_json)
        assert smtpdkim_attributes_model != False

        # Construct a model instance of SMTPDKIMAttributes by calling from_dict on the json representation
        smtpdkim_attributes_model_dict = SMTPDKIMAttributes.from_dict(smtpdkim_attributes_model_json).__dict__
        smtpdkim_attributes_model2 = SMTPDKIMAttributes(**smtpdkim_attributes_model_dict)

        # Verify the model instances are equivalent
        assert smtpdkim_attributes_model == smtpdkim_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        smtpdkim_attributes_model_json2 = smtpdkim_attributes_model.to_dict()
        assert smtpdkim_attributes_model_json2 == smtpdkim_attributes_model_json


class TestModel_SMTPUser:
    """
    Test Class for SMTPUser
    """

    def test_smtp_user_serialization(self):
        """
        Test serialization/deserialization for SMTPUser
        """

        # Construct a json representation of a SMTPUser model
        smtp_user_model_json = {}
        smtp_user_model_json['id'] = 'testString'
        smtp_user_model_json['smtp_config_id'] = 'testString'
        smtp_user_model_json['description'] = 'testString'
        smtp_user_model_json['domain'] = 'testString'
        smtp_user_model_json['username'] = 'testString'
        smtp_user_model_json['created_at'] = '2019-01-01T12:00:00Z'
        smtp_user_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of SMTPUser by calling from_dict on the json representation
        smtp_user_model = SMTPUser.from_dict(smtp_user_model_json)
        assert smtp_user_model != False

        # Construct a model instance of SMTPUser by calling from_dict on the json representation
        smtp_user_model_dict = SMTPUser.from_dict(smtp_user_model_json).__dict__
        smtp_user_model2 = SMTPUser(**smtp_user_model_dict)

        # Verify the model instances are equivalent
        assert smtp_user_model == smtp_user_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_user_model_json2 = smtp_user_model.to_dict()
        assert smtp_user_model_json2 == smtp_user_model_json


class TestModel_SMTPUserResponse:
    """
    Test Class for SMTPUserResponse
    """

    def test_smtp_user_response_serialization(self):
        """
        Test serialization/deserialization for SMTPUserResponse
        """

        # Construct a json representation of a SMTPUserResponse model
        smtp_user_response_model_json = {}
        smtp_user_response_model_json['id'] = 'testString'
        smtp_user_response_model_json['description'] = 'testString'
        smtp_user_response_model_json['domain'] = 'testString'
        smtp_user_response_model_json['smtp_config_id'] = 'testString'
        smtp_user_response_model_json['username'] = 'testString'
        smtp_user_response_model_json['password'] = 'testString'
        smtp_user_response_model_json['created_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of SMTPUserResponse by calling from_dict on the json representation
        smtp_user_response_model = SMTPUserResponse.from_dict(smtp_user_response_model_json)
        assert smtp_user_response_model != False

        # Construct a model instance of SMTPUserResponse by calling from_dict on the json representation
        smtp_user_response_model_dict = SMTPUserResponse.from_dict(smtp_user_response_model_json).__dict__
        smtp_user_response_model2 = SMTPUserResponse(**smtp_user_response_model_dict)

        # Verify the model instances are equivalent
        assert smtp_user_response_model == smtp_user_response_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_user_response_model_json2 = smtp_user_response_model.to_dict()
        assert smtp_user_response_model_json2 == smtp_user_response_model_json


class TestModel_SMTPUsersList:
    """
    Test Class for SMTPUsersList
    """

    def test_smtp_users_list_serialization(self):
        """
        Test serialization/deserialization for SMTPUsersList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        smtp_user_model = {}  # SMTPUser
        smtp_user_model['id'] = '68e541cb-72b1-4eb6-ae51-766b3eaf8fd9'
        smtp_user_model['smtp_config_id'] = 'accec70c-752d-4920-bf86-146b2eade10f'
        smtp_user_model['description'] = 'disintermediate turn-key lifetime value'
        smtp_user_model['domain'] = 'ashwin.event-notifications.test.cloud.ibm.com'
        smtp_user_model['username'] = '39083891827184zey101'
        smtp_user_model['created_at'] = '2024-04-16T17:36:24.562000Z'
        smtp_user_model['updated_at'] = '2024-04-16T17:36:24.562000Z'

        page_href_response_model = {}  # PageHrefResponse
        page_href_response_model['href'] = (
            'https://us-south.event-notifications.cloud.ibm.com/event-notifications/v1/instances/9xxxxx-xxxxx-xxxxx-b3cd-xxxxx/destinations?limit=10&offset=0'
        )

        # Construct a json representation of a SMTPUsersList model
        smtp_users_list_model_json = {}
        smtp_users_list_model_json['total_count'] = 38
        smtp_users_list_model_json['offset'] = 38
        smtp_users_list_model_json['limit'] = 38
        smtp_users_list_model_json['users'] = [smtp_user_model]
        smtp_users_list_model_json['first'] = page_href_response_model
        smtp_users_list_model_json['previous'] = page_href_response_model
        smtp_users_list_model_json['next'] = page_href_response_model

        # Construct a model instance of SMTPUsersList by calling from_dict on the json representation
        smtp_users_list_model = SMTPUsersList.from_dict(smtp_users_list_model_json)
        assert smtp_users_list_model != False

        # Construct a model instance of SMTPUsersList by calling from_dict on the json representation
        smtp_users_list_model_dict = SMTPUsersList.from_dict(smtp_users_list_model_json).__dict__
        smtp_users_list_model2 = SMTPUsersList(**smtp_users_list_model_dict)

        # Verify the model instances are equivalent
        assert smtp_users_list_model == smtp_users_list_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_users_list_model_json2 = smtp_users_list_model.to_dict()
        assert smtp_users_list_model_json2 == smtp_users_list_model_json


class TestModel_SMTPVerificationResponse:
    """
    Test Class for SMTPVerificationResponse
    """

    def test_smtp_verification_response_serialization(self):
        """
        Test serialization/deserialization for SMTPVerificationResponse
        """

        # Construct a json representation of a SMTPVerificationResponse model
        smtp_verification_response_model_json = {}
        smtp_verification_response_model_json['type'] = 'testString'
        smtp_verification_response_model_json['verification'] = 'testString'

        # Construct a model instance of SMTPVerificationResponse by calling from_dict on the json representation
        smtp_verification_response_model = SMTPVerificationResponse.from_dict(smtp_verification_response_model_json)
        assert smtp_verification_response_model != False

        # Construct a model instance of SMTPVerificationResponse by calling from_dict on the json representation
        smtp_verification_response_model_dict = SMTPVerificationResponse.from_dict(
            smtp_verification_response_model_json
        ).__dict__
        smtp_verification_response_model2 = SMTPVerificationResponse(**smtp_verification_response_model_dict)

        # Verify the model instances are equivalent
        assert smtp_verification_response_model == smtp_verification_response_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_verification_response_model_json2 = smtp_verification_response_model.to_dict()
        assert smtp_verification_response_model_json2 == smtp_verification_response_model_json


class TestModel_SMTPVerificationUpdateResponse:
    """
    Test Class for SMTPVerificationUpdateResponse
    """

    def test_smtp_verification_update_response_serialization(self):
        """
        Test serialization/deserialization for SMTPVerificationUpdateResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        smtp_verification_response_model = {}  # SMTPVerificationResponse
        smtp_verification_response_model['type'] = 'spf'
        smtp_verification_response_model['verification'] = 'SUCCESSFUL'

        # Construct a json representation of a SMTPVerificationUpdateResponse model
        smtp_verification_update_response_model_json = {}
        smtp_verification_update_response_model_json['status'] = [smtp_verification_response_model]

        # Construct a model instance of SMTPVerificationUpdateResponse by calling from_dict on the json representation
        smtp_verification_update_response_model = SMTPVerificationUpdateResponse.from_dict(
            smtp_verification_update_response_model_json
        )
        assert smtp_verification_update_response_model != False

        # Construct a model instance of SMTPVerificationUpdateResponse by calling from_dict on the json representation
        smtp_verification_update_response_model_dict = SMTPVerificationUpdateResponse.from_dict(
            smtp_verification_update_response_model_json
        ).__dict__
        smtp_verification_update_response_model2 = SMTPVerificationUpdateResponse(
            **smtp_verification_update_response_model_dict
        )

        # Verify the model instances are equivalent
        assert smtp_verification_update_response_model == smtp_verification_update_response_model2

        # Convert model instance back to dict and verify no loss of data
        smtp_verification_update_response_model_json2 = smtp_verification_update_response_model.to_dict()
        assert smtp_verification_update_response_model_json2 == smtp_verification_update_response_model_json


class TestModel_SPFAttributes:
    """
    Test Class for SPFAttributes
    """

    def test_spf_attributes_serialization(self):
        """
        Test serialization/deserialization for SPFAttributes
        """

        # Construct a json representation of a SPFAttributes model
        spf_attributes_model_json = {}
        spf_attributes_model_json['txt_name'] = 'testString'
        spf_attributes_model_json['txt_value'] = 'testString'
        spf_attributes_model_json['verification'] = 'testString'

        # Construct a model instance of SPFAttributes by calling from_dict on the json representation
        spf_attributes_model = SPFAttributes.from_dict(spf_attributes_model_json)
        assert spf_attributes_model != False

        # Construct a model instance of SPFAttributes by calling from_dict on the json representation
        spf_attributes_model_dict = SPFAttributes.from_dict(spf_attributes_model_json).__dict__
        spf_attributes_model2 = SPFAttributes(**spf_attributes_model_dict)

        # Verify the model instances are equivalent
        assert spf_attributes_model == spf_attributes_model2

        # Convert model instance back to dict and verify no loss of data
        spf_attributes_model_json2 = spf_attributes_model.to_dict()
        assert spf_attributes_model_json2 == spf_attributes_model_json


class TestModel_Source:
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


class TestModel_SourceList:
    """
    Test Class for SourceList
    """

    def test_source_list_serialization(self):
        """
        Test serialization/deserialization for SourceList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        source_list_item_model = {}  # SourceListItem
        source_list_item_model['id'] = '00bb34e5-b8c1-4159-af15-8bc6980c3ab2:api'
        source_list_item_model['name'] = 'CloudEvents Source'
        source_list_item_model['description'] = 'This source is related cloud events'
        source_list_item_model['type'] = 'api'
        source_list_item_model['enabled'] = True
        source_list_item_model['updated_at'] = '2021-08-19T05:30:03.696000Z'
        source_list_item_model['topic_count'] = 0

        page_href_response_model = {}  # PageHrefResponse
        page_href_response_model['href'] = (
            'https://us-south.event-notifications.cloud.ibm.com/event-notifications/v1/instances/9xxxxx-xxxxx-xxxxx-b3cd-xxxxx/sources?limit=10&offset=0'
        )

        # Construct a json representation of a SourceList model
        source_list_model_json = {}
        source_list_model_json['total_count'] = 0
        source_list_model_json['offset'] = 38
        source_list_model_json['limit'] = 38
        source_list_model_json['sources'] = [source_list_item_model]
        source_list_model_json['first'] = page_href_response_model
        source_list_model_json['previous'] = page_href_response_model
        source_list_model_json['next'] = page_href_response_model

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


class TestModel_SourceListItem:
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


class TestModel_SourceResponse:
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


class TestModel_SourcesItems:
    """
    Test Class for SourcesItems
    """

    def test_sources_items_serialization(self):
        """
        Test serialization/deserialization for SourcesItems
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_model = {}  # Rules
        rules_model['enabled'] = True
        rules_model['event_type_filter'] = '$.*'
        rules_model['notification_filter'] = 'testString'

        # Construct a json representation of a SourcesItems model
        sources_items_model_json = {}
        sources_items_model_json['id'] = 'testString'
        sources_items_model_json['rules'] = [rules_model]

        # Construct a model instance of SourcesItems by calling from_dict on the json representation
        sources_items_model = SourcesItems.from_dict(sources_items_model_json)
        assert sources_items_model != False

        # Construct a model instance of SourcesItems by calling from_dict on the json representation
        sources_items_model_dict = SourcesItems.from_dict(sources_items_model_json).__dict__
        sources_items_model2 = SourcesItems(**sources_items_model_dict)

        # Verify the model instances are equivalent
        assert sources_items_model == sources_items_model2

        # Convert model instance back to dict and verify no loss of data
        sources_items_model_json2 = sources_items_model.to_dict()
        assert sources_items_model_json2 == sources_items_model_json


class TestModel_SourcesListItems:
    """
    Test Class for SourcesListItems
    """

    def test_sources_list_items_serialization(self):
        """
        Test serialization/deserialization for SourcesListItems
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_get_model = {}  # RulesGet
        rules_get_model['enabled'] = True
        rules_get_model['event_type_filter'] = '$.notification_event_info.event_type == \'test\''
        rules_get_model['notification_filter'] = '$.notification.findings[0].severity == \'LOW\''
        rules_get_model['updated_at'] = '2021-09-08T13:25:20.523533Z'
        rules_get_model['id'] = '218f4e30-9af2-4f70-b38b-738f923b0c4b'

        # Construct a json representation of a SourcesListItems model
        sources_list_items_model_json = {}
        sources_list_items_model_json['id'] = 'testString'
        sources_list_items_model_json['name'] = 'testString'
        sources_list_items_model_json['rules'] = [rules_get_model]

        # Construct a model instance of SourcesListItems by calling from_dict on the json representation
        sources_list_items_model = SourcesListItems.from_dict(sources_list_items_model_json)
        assert sources_list_items_model != False

        # Construct a model instance of SourcesListItems by calling from_dict on the json representation
        sources_list_items_model_dict = SourcesListItems.from_dict(sources_list_items_model_json).__dict__
        sources_list_items_model2 = SourcesListItems(**sources_list_items_model_dict)

        # Verify the model instances are equivalent
        assert sources_list_items_model == sources_list_items_model2

        # Convert model instance back to dict and verify no loss of data
        sources_list_items_model_json2 = sources_list_items_model.to_dict()
        assert sources_list_items_model_json2 == sources_list_items_model_json


class TestModel_Subscription:
    """
    Test Class for Subscription
    """

    def test_subscription_serialization(self):
        """
        Test serialization/deserialization for Subscription
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subscription_attributes_model = {}  # SubscriptionAttributesWebhookAttributesResponse
        subscription_attributes_model['signing_enabled'] = True
        subscription_attributes_model['add_notification_payload'] = True
        subscription_attributes_model['foo'] = 'testString'

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


class TestModel_SubscriptionList:
    """
    Test Class for SubscriptionList
    """

    def test_subscription_list_serialization(self):
        """
        Test serialization/deserialization for SubscriptionList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        subscription_list_item_model = {}  # SubscriptionListItem
        subscription_list_item_model['id'] = '60502ac0-5748-40b1-84b8-938b77f1c8d1'
        subscription_list_item_model['name'] = 'Test subscription'
        subscription_list_item_model['description'] = 'Developers of EN'
        subscription_list_item_model['destination_id'] = 'b5cb3f03-ff12-42f3-9fae-37ee27f2a81a'
        subscription_list_item_model['destination_name'] = 'Developers Email destination'
        subscription_list_item_model['destination_type'] = 'smtp_ibm'
        subscription_list_item_model['topic_id'] = '33d2b8d5-8ab8-46c7-97b9-c508afbf0701'
        subscription_list_item_model['topic_name'] = 'Developers topic'
        subscription_list_item_model['updated_at'] = '2021-08-18T09:50:32.133000Z'

        page_href_response_model = {}  # PageHrefResponse
        page_href_response_model['href'] = (
            'https://us-south.event-notifications.cloud.ibm.com/event-notifications/v1/instances/9xxxxx-xxxxx-xxxxx-b3cd-xxxxx/subscriptions?limit=10&offset=0'
        )

        # Construct a json representation of a SubscriptionList model
        subscription_list_model_json = {}
        subscription_list_model_json['total_count'] = 0
        subscription_list_model_json['offset'] = 38
        subscription_list_model_json['limit'] = 38
        subscription_list_model_json['subscriptions'] = [subscription_list_item_model]
        subscription_list_model_json['first'] = page_href_response_model
        subscription_list_model_json['previous'] = page_href_response_model
        subscription_list_model_json['next'] = page_href_response_model

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


class TestModel_SubscriptionListItem:
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


class TestModel_TagsSubscriptionList:
    """
    Test Class for TagsSubscriptionList
    """

    def test_tags_subscription_list_serialization(self):
        """
        Test serialization/deserialization for TagsSubscriptionList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tags_subscription_list_item_model = {}  # TagsSubscriptionListItem
        tags_subscription_list_item_model['id'] = '330cfdf8-7ae6-4afb-aac1-458243877d00'
        tags_subscription_list_item_model['device_id'] = '11fe18ba-d0c8-4108-9f07-355e8052a813'
        tags_subscription_list_item_model['tag_name'] = 'sl_web'
        tags_subscription_list_item_model['user_id'] = 'fcm_id_123'
        tags_subscription_list_item_model['updated_at'] = '2021-09-05T00:25:19.599000Z'

        page_href_response_model = {}  # PageHrefResponse
        page_href_response_model['href'] = (
            'https://us-south.event-notifications.cloud.ibm.com/event-notifications/v1/instances/9xxxxx-xxxxx-xxxxx-b3cd-xxxxx/destinations/axxxxx-xxxxx-xxxxx-rtc4-xxxxx/tag_subscriptions?limit=10&offset=0'
        )

        # Construct a json representation of a TagsSubscriptionList model
        tags_subscription_list_model_json = {}
        tags_subscription_list_model_json['total_count'] = 38
        tags_subscription_list_model_json['offset'] = 38
        tags_subscription_list_model_json['limit'] = 38
        tags_subscription_list_model_json['tag_subscriptions'] = [tags_subscription_list_item_model]
        tags_subscription_list_model_json['first'] = page_href_response_model
        tags_subscription_list_model_json['previous'] = page_href_response_model
        tags_subscription_list_model_json['next'] = page_href_response_model

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


class TestModel_TagsSubscriptionListItem:
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
        tags_subscription_list_item_model_dict = TagsSubscriptionListItem.from_dict(
            tags_subscription_list_item_model_json
        ).__dict__
        tags_subscription_list_item_model2 = TagsSubscriptionListItem(**tags_subscription_list_item_model_dict)

        # Verify the model instances are equivalent
        assert tags_subscription_list_item_model == tags_subscription_list_item_model2

        # Convert model instance back to dict and verify no loss of data
        tags_subscription_list_item_model_json2 = tags_subscription_list_item_model.to_dict()
        assert tags_subscription_list_item_model_json2 == tags_subscription_list_item_model_json


class TestModel_Template:
    """
    Test Class for Template
    """

    def test_template_serialization(self):
        """
        Test serialization/deserialization for Template
        """

        # Construct a json representation of a Template model
        template_model_json = {}
        template_model_json['id'] = 'testString'
        template_model_json['name'] = 'testString'
        template_model_json['description'] = 'testString'
        template_model_json['type'] = 'testString'
        template_model_json['subscription_count'] = 38
        template_model_json['subscription_names'] = ['testString']
        template_model_json['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of Template by calling from_dict on the json representation
        template_model = Template.from_dict(template_model_json)
        assert template_model != False

        # Construct a model instance of Template by calling from_dict on the json representation
        template_model_dict = Template.from_dict(template_model_json).__dict__
        template_model2 = Template(**template_model_dict)

        # Verify the model instances are equivalent
        assert template_model == template_model2

        # Convert model instance back to dict and verify no loss of data
        template_model_json2 = template_model.to_dict()
        assert template_model_json2 == template_model_json


class TestModel_TemplateList:
    """
    Test Class for TemplateList
    """

    def test_template_list_serialization(self):
        """
        Test serialization/deserialization for TemplateList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        template_model = {}  # Template
        template_model['id'] = '11fe18ba-0000-0000-9f07-355e8052a813'
        template_model['name'] = 'template name'
        template_model['description'] = 'Template description'
        template_model['type'] = 'smtp_custom.notification'
        template_model['subscription_count'] = 2
        template_model['subscription_names'] = ['abc', 'xyz']
        template_model['updated_at'] = '2021-09-05T00:25:19.599000Z'

        page_href_response_model = {}  # PageHrefResponse
        page_href_response_model['href'] = (
            'https://us-south.event-notifications.cloud.ibm.com/event-notifications/v1/instances/9xxxxx-xxxxx-xxxxx-b3cd-xxxxx/templates?limit=10&offset=0'
        )

        # Construct a json representation of a TemplateList model
        template_list_model_json = {}
        template_list_model_json['total_count'] = 38
        template_list_model_json['offset'] = 38
        template_list_model_json['limit'] = 38
        template_list_model_json['templates'] = [template_model]
        template_list_model_json['first'] = page_href_response_model
        template_list_model_json['previous'] = page_href_response_model
        template_list_model_json['next'] = page_href_response_model

        # Construct a model instance of TemplateList by calling from_dict on the json representation
        template_list_model = TemplateList.from_dict(template_list_model_json)
        assert template_list_model != False

        # Construct a model instance of TemplateList by calling from_dict on the json representation
        template_list_model_dict = TemplateList.from_dict(template_list_model_json).__dict__
        template_list_model2 = TemplateList(**template_list_model_dict)

        # Verify the model instances are equivalent
        assert template_list_model == template_list_model2

        # Convert model instance back to dict and verify no loss of data
        template_list_model_json2 = template_list_model.to_dict()
        assert template_list_model_json2 == template_list_model_json


class TestModel_TemplateResponse:
    """
    Test Class for TemplateResponse
    """

    def test_template_response_serialization(self):
        """
        Test serialization/deserialization for TemplateResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        template_config_one_of_model = {}  # TemplateConfigOneOfEmailTemplateConfig
        template_config_one_of_model['body'] = 'PGh0bWw+CiAgaGVsbG8gd29ybGQKPC9odG1sPg=='
        template_config_one_of_model['subject'] = 'This is the template subject'

        # Construct a json representation of a TemplateResponse model
        template_response_model_json = {}
        template_response_model_json['id'] = 'testString'
        template_response_model_json['name'] = 'testString'
        template_response_model_json['description'] = 'testString'
        template_response_model_json['type'] = 'testString'
        template_response_model_json['params'] = template_config_one_of_model
        template_response_model_json['created_at'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of TemplateResponse by calling from_dict on the json representation
        template_response_model = TemplateResponse.from_dict(template_response_model_json)
        assert template_response_model != False

        # Construct a model instance of TemplateResponse by calling from_dict on the json representation
        template_response_model_dict = TemplateResponse.from_dict(template_response_model_json).__dict__
        template_response_model2 = TemplateResponse(**template_response_model_dict)

        # Verify the model instances are equivalent
        assert template_response_model == template_response_model2

        # Convert model instance back to dict and verify no loss of data
        template_response_model_json2 = template_response_model.to_dict()
        assert template_response_model_json2 == template_response_model_json


class TestModel_TestDestinationResponse:
    """
    Test Class for TestDestinationResponse
    """

    def test_test_destination_response_serialization(self):
        """
        Test serialization/deserialization for TestDestinationResponse
        """

        # Construct a json representation of a TestDestinationResponse model
        test_destination_response_model_json = {}
        test_destination_response_model_json['status'] = 'testString'

        # Construct a model instance of TestDestinationResponse by calling from_dict on the json representation
        test_destination_response_model = TestDestinationResponse.from_dict(test_destination_response_model_json)
        assert test_destination_response_model != False

        # Construct a model instance of TestDestinationResponse by calling from_dict on the json representation
        test_destination_response_model_dict = TestDestinationResponse.from_dict(
            test_destination_response_model_json
        ).__dict__
        test_destination_response_model2 = TestDestinationResponse(**test_destination_response_model_dict)

        # Verify the model instances are equivalent
        assert test_destination_response_model == test_destination_response_model2

        # Convert model instance back to dict and verify no loss of data
        test_destination_response_model_json2 = test_destination_response_model.to_dict()
        assert test_destination_response_model_json2 == test_destination_response_model_json


class TestModel_Topic:
    """
    Test Class for Topic
    """

    def test_topic_serialization(self):
        """
        Test serialization/deserialization for Topic
        """

        # Construct dict forms of any model objects needed in order to build this model.

        rules_get_model = {}  # RulesGet
        rules_get_model['enabled'] = True
        rules_get_model['event_type_filter'] = '$.notification_event_info.event_type == \'test\''
        rules_get_model['notification_filter'] = '$.notification.findings[0].severity == \'LOW\''
        rules_get_model['updated_at'] = '2021-09-08T13:25:20.523533Z'
        rules_get_model['id'] = '218f4e30-9af2-4f70-b38b-738f923b0c4b'

        sources_list_items_model = {}  # SourcesListItems
        sources_list_items_model['id'] = '96dbf538-9fa7-4745-b9e4-32bb6f1dc47a:api'
        sources_list_items_model['name'] = 'Compliance source'
        sources_list_items_model['rules'] = [rules_get_model]

        subscription_list_item_model = {}  # SubscriptionListItem
        subscription_list_item_model['id'] = '87bef75e-f826-4aa9-b64d-91af9be5e12b'
        subscription_list_item_model['name'] = 'SMS Subscription on new change'
        subscription_list_item_model['description'] = (
            'This subscription is to send events from SCC to EN Admins via sms'
        )
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
        topic_model_json['sources'] = [sources_list_items_model]
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


class TestModel_TopicList:
    """
    Test Class for TopicList
    """

    def test_topic_list_serialization(self):
        """
        Test serialization/deserialization for TopicList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        topics_list_item_model = {}  # TopicsListItem
        topics_list_item_model['id'] = '33d2b8d5-8ab8-46c7-97b9-c508afbf0701'
        topics_list_item_model['name'] = 'Developers topic'
        topics_list_item_model['description'] = 'To send events to all EN developers'
        topics_list_item_model['source_count'] = 2
        topics_list_item_model['sources_names'] = ['Push Source', 'Custom source']
        topics_list_item_model['subscription_count'] = 3

        page_href_response_model = {}  # PageHrefResponse
        page_href_response_model['href'] = (
            'https://us-south.event-notifications.cloud.ibm.com/event-notifications/v1/instances/9xxxxx-xxxxx-xxxxx-b3cd-xxxxx/topics?limit=10&offset=0'
        )

        # Construct a json representation of a TopicList model
        topic_list_model_json = {}
        topic_list_model_json['total_count'] = 0
        topic_list_model_json['offset'] = 38
        topic_list_model_json['limit'] = 38
        topic_list_model_json['topics'] = [topics_list_item_model]
        topic_list_model_json['first'] = page_href_response_model
        topic_list_model_json['previous'] = page_href_response_model
        topic_list_model_json['next'] = page_href_response_model

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


class TestModel_TopicResponse:
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


class TestModel_TopicsListItem:
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


class TestModel_UpdateAttributesInvited:
    """
    Test Class for UpdateAttributesInvited
    """

    def test_update_attributes_invited_serialization(self):
        """
        Test serialization/deserialization for UpdateAttributesInvited
        """

        # Construct a json representation of a UpdateAttributesInvited model
        update_attributes_invited_model_json = {}
        update_attributes_invited_model_json['add'] = ['testString']
        update_attributes_invited_model_json['remove'] = ['testString']

        # Construct a model instance of UpdateAttributesInvited by calling from_dict on the json representation
        update_attributes_invited_model = UpdateAttributesInvited.from_dict(update_attributes_invited_model_json)
        assert update_attributes_invited_model != False

        # Construct a model instance of UpdateAttributesInvited by calling from_dict on the json representation
        update_attributes_invited_model_dict = UpdateAttributesInvited.from_dict(
            update_attributes_invited_model_json
        ).__dict__
        update_attributes_invited_model2 = UpdateAttributesInvited(**update_attributes_invited_model_dict)

        # Verify the model instances are equivalent
        assert update_attributes_invited_model == update_attributes_invited_model2

        # Convert model instance back to dict and verify no loss of data
        update_attributes_invited_model_json2 = update_attributes_invited_model.to_dict()
        assert update_attributes_invited_model_json2 == update_attributes_invited_model_json


class TestModel_UpdateAttributesSubscribed:
    """
    Test Class for UpdateAttributesSubscribed
    """

    def test_update_attributes_subscribed_serialization(self):
        """
        Test serialization/deserialization for UpdateAttributesSubscribed
        """

        # Construct a json representation of a UpdateAttributesSubscribed model
        update_attributes_subscribed_model_json = {}
        update_attributes_subscribed_model_json['remove'] = ['testString']

        # Construct a model instance of UpdateAttributesSubscribed by calling from_dict on the json representation
        update_attributes_subscribed_model = UpdateAttributesSubscribed.from_dict(
            update_attributes_subscribed_model_json
        )
        assert update_attributes_subscribed_model != False

        # Construct a model instance of UpdateAttributesSubscribed by calling from_dict on the json representation
        update_attributes_subscribed_model_dict = UpdateAttributesSubscribed.from_dict(
            update_attributes_subscribed_model_json
        ).__dict__
        update_attributes_subscribed_model2 = UpdateAttributesSubscribed(**update_attributes_subscribed_model_dict)

        # Verify the model instances are equivalent
        assert update_attributes_subscribed_model == update_attributes_subscribed_model2

        # Convert model instance back to dict and verify no loss of data
        update_attributes_subscribed_model_json2 = update_attributes_subscribed_model.to_dict()
        assert update_attributes_subscribed_model_json2 == update_attributes_subscribed_model_json


class TestModel_UpdateAttributesUnsubscribed:
    """
    Test Class for UpdateAttributesUnsubscribed
    """

    def test_update_attributes_unsubscribed_serialization(self):
        """
        Test serialization/deserialization for UpdateAttributesUnsubscribed
        """

        # Construct a json representation of a UpdateAttributesUnsubscribed model
        update_attributes_unsubscribed_model_json = {}
        update_attributes_unsubscribed_model_json['remove'] = ['testString']

        # Construct a model instance of UpdateAttributesUnsubscribed by calling from_dict on the json representation
        update_attributes_unsubscribed_model = UpdateAttributesUnsubscribed.from_dict(
            update_attributes_unsubscribed_model_json
        )
        assert update_attributes_unsubscribed_model != False

        # Construct a model instance of UpdateAttributesUnsubscribed by calling from_dict on the json representation
        update_attributes_unsubscribed_model_dict = UpdateAttributesUnsubscribed.from_dict(
            update_attributes_unsubscribed_model_json
        ).__dict__
        update_attributes_unsubscribed_model2 = UpdateAttributesUnsubscribed(
            **update_attributes_unsubscribed_model_dict
        )

        # Verify the model instances are equivalent
        assert update_attributes_unsubscribed_model == update_attributes_unsubscribed_model2

        # Convert model instance back to dict and verify no loss of data
        update_attributes_unsubscribed_model_json2 = update_attributes_unsubscribed_model.to_dict()
        assert update_attributes_unsubscribed_model_json2 == update_attributes_unsubscribed_model_json


class TestModel_VerificationResponse:
    """
    Test Class for VerificationResponse
    """

    def test_verification_response_serialization(self):
        """
        Test serialization/deserialization for VerificationResponse
        """

        # Construct a json representation of a VerificationResponse model
        verification_response_model_json = {}
        verification_response_model_json['type'] = 'testString'
        verification_response_model_json['verification'] = 'testString'

        # Construct a model instance of VerificationResponse by calling from_dict on the json representation
        verification_response_model = VerificationResponse.from_dict(verification_response_model_json)
        assert verification_response_model != False

        # Construct a model instance of VerificationResponse by calling from_dict on the json representation
        verification_response_model_dict = VerificationResponse.from_dict(verification_response_model_json).__dict__
        verification_response_model2 = VerificationResponse(**verification_response_model_dict)

        # Verify the model instances are equivalent
        assert verification_response_model == verification_response_model2

        # Convert model instance back to dict and verify no loss of data
        verification_response_model_json2 = verification_response_model.to_dict()
        assert verification_response_model_json2 == verification_response_model_json


class TestModel_DestinationConfigOneOfChromeDestinationConfig:
    """
    Test Class for DestinationConfigOneOfChromeDestinationConfig
    """

    def test_destination_config_one_of_chrome_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfChromeDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfChromeDestinationConfig model
        destination_config_one_of_chrome_destination_config_model_json = {}
        destination_config_one_of_chrome_destination_config_model_json['api_key'] = 'testString'
        destination_config_one_of_chrome_destination_config_model_json['website_url'] = 'testString'
        destination_config_one_of_chrome_destination_config_model_json['public_key'] = 'testString'
        destination_config_one_of_chrome_destination_config_model_json['pre_prod'] = False

        # Construct a model instance of DestinationConfigOneOfChromeDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_chrome_destination_config_model = (
            DestinationConfigOneOfChromeDestinationConfig.from_dict(
                destination_config_one_of_chrome_destination_config_model_json
            )
        )
        assert destination_config_one_of_chrome_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfChromeDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_chrome_destination_config_model_dict = (
            DestinationConfigOneOfChromeDestinationConfig.from_dict(
                destination_config_one_of_chrome_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_chrome_destination_config_model2 = DestinationConfigOneOfChromeDestinationConfig(
            **destination_config_one_of_chrome_destination_config_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_chrome_destination_config_model
            == destination_config_one_of_chrome_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_chrome_destination_config_model_json2 = (
            destination_config_one_of_chrome_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_chrome_destination_config_model_json2
            == destination_config_one_of_chrome_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfCodeEngineDestinationConfig:
    """
    Test Class for DestinationConfigOneOfCodeEngineDestinationConfig
    """

    def test_destination_config_one_of_code_engine_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfCodeEngineDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfCodeEngineDestinationConfig model
        destination_config_one_of_code_engine_destination_config_model_json = {}
        destination_config_one_of_code_engine_destination_config_model_json['url'] = 'testString'
        destination_config_one_of_code_engine_destination_config_model_json['verb'] = 'get'
        destination_config_one_of_code_engine_destination_config_model_json['type'] = 'job'
        destination_config_one_of_code_engine_destination_config_model_json['project_crn'] = 'testString'
        destination_config_one_of_code_engine_destination_config_model_json['job_name'] = 'testString'
        destination_config_one_of_code_engine_destination_config_model_json['custom_headers'] = {'key1': 'testString'}
        destination_config_one_of_code_engine_destination_config_model_json['sensitive_headers'] = ['testString']

        # Construct a model instance of DestinationConfigOneOfCodeEngineDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_code_engine_destination_config_model = (
            DestinationConfigOneOfCodeEngineDestinationConfig.from_dict(
                destination_config_one_of_code_engine_destination_config_model_json
            )
        )
        assert destination_config_one_of_code_engine_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfCodeEngineDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_code_engine_destination_config_model_dict = (
            DestinationConfigOneOfCodeEngineDestinationConfig.from_dict(
                destination_config_one_of_code_engine_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_code_engine_destination_config_model2 = (
            DestinationConfigOneOfCodeEngineDestinationConfig(
                **destination_config_one_of_code_engine_destination_config_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_code_engine_destination_config_model
            == destination_config_one_of_code_engine_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_code_engine_destination_config_model_json2 = (
            destination_config_one_of_code_engine_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_code_engine_destination_config_model_json2
            == destination_config_one_of_code_engine_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfCustomDomainEmailDestinationConfig:
    """
    Test Class for DestinationConfigOneOfCustomDomainEmailDestinationConfig
    """

    def test_destination_config_one_of_custom_domain_email_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfCustomDomainEmailDestinationConfig
        """

        # Construct dict forms of any model objects needed in order to build this model.

        dkim_attributes_model = {}  # DKIMAttributes
        dkim_attributes_model['public_key'] = 'testString'
        dkim_attributes_model['selector'] = 'testString'
        dkim_attributes_model['verification'] = 'testString'

        spf_attributes_model = {}  # SPFAttributes
        spf_attributes_model['txt_name'] = 'testString'
        spf_attributes_model['txt_value'] = 'testString'
        spf_attributes_model['verification'] = 'testString'

        # Construct a json representation of a DestinationConfigOneOfCustomDomainEmailDestinationConfig model
        destination_config_one_of_custom_domain_email_destination_config_model_json = {}
        destination_config_one_of_custom_domain_email_destination_config_model_json['domain'] = 'testString'
        destination_config_one_of_custom_domain_email_destination_config_model_json['dkim'] = dkim_attributes_model
        destination_config_one_of_custom_domain_email_destination_config_model_json['spf'] = spf_attributes_model

        # Construct a model instance of DestinationConfigOneOfCustomDomainEmailDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_custom_domain_email_destination_config_model = (
            DestinationConfigOneOfCustomDomainEmailDestinationConfig.from_dict(
                destination_config_one_of_custom_domain_email_destination_config_model_json
            )
        )
        assert destination_config_one_of_custom_domain_email_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfCustomDomainEmailDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_custom_domain_email_destination_config_model_dict = (
            DestinationConfigOneOfCustomDomainEmailDestinationConfig.from_dict(
                destination_config_one_of_custom_domain_email_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_custom_domain_email_destination_config_model2 = (
            DestinationConfigOneOfCustomDomainEmailDestinationConfig(
                **destination_config_one_of_custom_domain_email_destination_config_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_custom_domain_email_destination_config_model
            == destination_config_one_of_custom_domain_email_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_custom_domain_email_destination_config_model_json2 = (
            destination_config_one_of_custom_domain_email_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_custom_domain_email_destination_config_model_json2
            == destination_config_one_of_custom_domain_email_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfFCMDestinationConfig:
    """
    Test Class for DestinationConfigOneOfFCMDestinationConfig
    """

    def test_destination_config_one_of_fcm_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfFCMDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfFCMDestinationConfig model
        destination_config_one_of_fcm_destination_config_model_json = {}
        destination_config_one_of_fcm_destination_config_model_json['server_key'] = 'testString'
        destination_config_one_of_fcm_destination_config_model_json['sender_id'] = 'testString'
        destination_config_one_of_fcm_destination_config_model_json['pre_prod'] = False
        destination_config_one_of_fcm_destination_config_model_json['project_id'] = 'testString'
        destination_config_one_of_fcm_destination_config_model_json['private_key'] = 'testString'
        destination_config_one_of_fcm_destination_config_model_json['client_email'] = 'testString'

        # Construct a model instance of DestinationConfigOneOfFCMDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_fcm_destination_config_model = DestinationConfigOneOfFCMDestinationConfig.from_dict(
            destination_config_one_of_fcm_destination_config_model_json
        )
        assert destination_config_one_of_fcm_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfFCMDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_fcm_destination_config_model_dict = (
            DestinationConfigOneOfFCMDestinationConfig.from_dict(
                destination_config_one_of_fcm_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_fcm_destination_config_model2 = DestinationConfigOneOfFCMDestinationConfig(
            **destination_config_one_of_fcm_destination_config_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_fcm_destination_config_model
            == destination_config_one_of_fcm_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_fcm_destination_config_model_json2 = (
            destination_config_one_of_fcm_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_fcm_destination_config_model_json2
            == destination_config_one_of_fcm_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfFirefoxDestinationConfig:
    """
    Test Class for DestinationConfigOneOfFirefoxDestinationConfig
    """

    def test_destination_config_one_of_firefox_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfFirefoxDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfFirefoxDestinationConfig model
        destination_config_one_of_firefox_destination_config_model_json = {}
        destination_config_one_of_firefox_destination_config_model_json['website_url'] = 'testString'
        destination_config_one_of_firefox_destination_config_model_json['public_key'] = 'testString'
        destination_config_one_of_firefox_destination_config_model_json['pre_prod'] = False

        # Construct a model instance of DestinationConfigOneOfFirefoxDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_firefox_destination_config_model = (
            DestinationConfigOneOfFirefoxDestinationConfig.from_dict(
                destination_config_one_of_firefox_destination_config_model_json
            )
        )
        assert destination_config_one_of_firefox_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfFirefoxDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_firefox_destination_config_model_dict = (
            DestinationConfigOneOfFirefoxDestinationConfig.from_dict(
                destination_config_one_of_firefox_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_firefox_destination_config_model2 = DestinationConfigOneOfFirefoxDestinationConfig(
            **destination_config_one_of_firefox_destination_config_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_firefox_destination_config_model
            == destination_config_one_of_firefox_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_firefox_destination_config_model_json2 = (
            destination_config_one_of_firefox_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_firefox_destination_config_model_json2
            == destination_config_one_of_firefox_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfHuaweiDestinationConfig:
    """
    Test Class for DestinationConfigOneOfHuaweiDestinationConfig
    """

    def test_destination_config_one_of_huawei_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfHuaweiDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfHuaweiDestinationConfig model
        destination_config_one_of_huawei_destination_config_model_json = {}
        destination_config_one_of_huawei_destination_config_model_json['client_id'] = 'testString'
        destination_config_one_of_huawei_destination_config_model_json['client_secret'] = 'testString'
        destination_config_one_of_huawei_destination_config_model_json['pre_prod'] = False

        # Construct a model instance of DestinationConfigOneOfHuaweiDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_huawei_destination_config_model = (
            DestinationConfigOneOfHuaweiDestinationConfig.from_dict(
                destination_config_one_of_huawei_destination_config_model_json
            )
        )
        assert destination_config_one_of_huawei_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfHuaweiDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_huawei_destination_config_model_dict = (
            DestinationConfigOneOfHuaweiDestinationConfig.from_dict(
                destination_config_one_of_huawei_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_huawei_destination_config_model2 = DestinationConfigOneOfHuaweiDestinationConfig(
            **destination_config_one_of_huawei_destination_config_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_huawei_destination_config_model
            == destination_config_one_of_huawei_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_huawei_destination_config_model_json2 = (
            destination_config_one_of_huawei_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_huawei_destination_config_model_json2
            == destination_config_one_of_huawei_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfIBMCloudFunctionsDestinationConfig:
    """
    Test Class for DestinationConfigOneOfIBMCloudFunctionsDestinationConfig
    """

    def test_destination_config_one_of_ibm_cloud_functions_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfIBMCloudFunctionsDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfIBMCloudFunctionsDestinationConfig model
        destination_config_one_of_ibm_cloud_functions_destination_config_model_json = {}
        destination_config_one_of_ibm_cloud_functions_destination_config_model_json['url'] = 'testString'
        destination_config_one_of_ibm_cloud_functions_destination_config_model_json['api_key'] = 'testString'

        # Construct a model instance of DestinationConfigOneOfIBMCloudFunctionsDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_ibm_cloud_functions_destination_config_model = (
            DestinationConfigOneOfIBMCloudFunctionsDestinationConfig.from_dict(
                destination_config_one_of_ibm_cloud_functions_destination_config_model_json
            )
        )
        assert destination_config_one_of_ibm_cloud_functions_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfIBMCloudFunctionsDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_ibm_cloud_functions_destination_config_model_dict = (
            DestinationConfigOneOfIBMCloudFunctionsDestinationConfig.from_dict(
                destination_config_one_of_ibm_cloud_functions_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_ibm_cloud_functions_destination_config_model2 = (
            DestinationConfigOneOfIBMCloudFunctionsDestinationConfig(
                **destination_config_one_of_ibm_cloud_functions_destination_config_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_ibm_cloud_functions_destination_config_model
            == destination_config_one_of_ibm_cloud_functions_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_ibm_cloud_functions_destination_config_model_json2 = (
            destination_config_one_of_ibm_cloud_functions_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_ibm_cloud_functions_destination_config_model_json2
            == destination_config_one_of_ibm_cloud_functions_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfIBMCloudObjectStorageDestinationConfig:
    """
    Test Class for DestinationConfigOneOfIBMCloudObjectStorageDestinationConfig
    """

    def test_destination_config_one_of_ibm_cloud_object_storage_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfIBMCloudObjectStorageDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfIBMCloudObjectStorageDestinationConfig model
        destination_config_one_of_ibm_cloud_object_storage_destination_config_model_json = {}
        destination_config_one_of_ibm_cloud_object_storage_destination_config_model_json['bucket_name'] = 'testString'
        destination_config_one_of_ibm_cloud_object_storage_destination_config_model_json['instance_id'] = 'testString'
        destination_config_one_of_ibm_cloud_object_storage_destination_config_model_json['endpoint'] = 'testString'

        # Construct a model instance of DestinationConfigOneOfIBMCloudObjectStorageDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_ibm_cloud_object_storage_destination_config_model = (
            DestinationConfigOneOfIBMCloudObjectStorageDestinationConfig.from_dict(
                destination_config_one_of_ibm_cloud_object_storage_destination_config_model_json
            )
        )
        assert destination_config_one_of_ibm_cloud_object_storage_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfIBMCloudObjectStorageDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_ibm_cloud_object_storage_destination_config_model_dict = (
            DestinationConfigOneOfIBMCloudObjectStorageDestinationConfig.from_dict(
                destination_config_one_of_ibm_cloud_object_storage_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_ibm_cloud_object_storage_destination_config_model2 = (
            DestinationConfigOneOfIBMCloudObjectStorageDestinationConfig(
                **destination_config_one_of_ibm_cloud_object_storage_destination_config_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_ibm_cloud_object_storage_destination_config_model
            == destination_config_one_of_ibm_cloud_object_storage_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_ibm_cloud_object_storage_destination_config_model_json2 = (
            destination_config_one_of_ibm_cloud_object_storage_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_ibm_cloud_object_storage_destination_config_model_json2
            == destination_config_one_of_ibm_cloud_object_storage_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfIOSDestinationConfig:
    """
    Test Class for DestinationConfigOneOfIOSDestinationConfig
    """

    def test_destination_config_one_of_ios_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfIOSDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfIOSDestinationConfig model
        destination_config_one_of_ios_destination_config_model_json = {}
        destination_config_one_of_ios_destination_config_model_json['cert_type'] = 'p8'
        destination_config_one_of_ios_destination_config_model_json['is_sandbox'] = False
        destination_config_one_of_ios_destination_config_model_json['password'] = 'testString'
        destination_config_one_of_ios_destination_config_model_json['key_id'] = 'testString'
        destination_config_one_of_ios_destination_config_model_json['team_id'] = 'testString'
        destination_config_one_of_ios_destination_config_model_json['bundle_id'] = 'testString'
        destination_config_one_of_ios_destination_config_model_json['pre_prod'] = False

        # Construct a model instance of DestinationConfigOneOfIOSDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_ios_destination_config_model = DestinationConfigOneOfIOSDestinationConfig.from_dict(
            destination_config_one_of_ios_destination_config_model_json
        )
        assert destination_config_one_of_ios_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfIOSDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_ios_destination_config_model_dict = (
            DestinationConfigOneOfIOSDestinationConfig.from_dict(
                destination_config_one_of_ios_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_ios_destination_config_model2 = DestinationConfigOneOfIOSDestinationConfig(
            **destination_config_one_of_ios_destination_config_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_ios_destination_config_model
            == destination_config_one_of_ios_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_ios_destination_config_model_json2 = (
            destination_config_one_of_ios_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_ios_destination_config_model_json2
            == destination_config_one_of_ios_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfMSTeamsDestinationConfig:
    """
    Test Class for DestinationConfigOneOfMSTeamsDestinationConfig
    """

    def test_destination_config_one_of_ms_teams_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfMSTeamsDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfMSTeamsDestinationConfig model
        destination_config_one_of_ms_teams_destination_config_model_json = {}
        destination_config_one_of_ms_teams_destination_config_model_json['url'] = 'testString'

        # Construct a model instance of DestinationConfigOneOfMSTeamsDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_ms_teams_destination_config_model = (
            DestinationConfigOneOfMSTeamsDestinationConfig.from_dict(
                destination_config_one_of_ms_teams_destination_config_model_json
            )
        )
        assert destination_config_one_of_ms_teams_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfMSTeamsDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_ms_teams_destination_config_model_dict = (
            DestinationConfigOneOfMSTeamsDestinationConfig.from_dict(
                destination_config_one_of_ms_teams_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_ms_teams_destination_config_model2 = DestinationConfigOneOfMSTeamsDestinationConfig(
            **destination_config_one_of_ms_teams_destination_config_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_ms_teams_destination_config_model
            == destination_config_one_of_ms_teams_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_ms_teams_destination_config_model_json2 = (
            destination_config_one_of_ms_teams_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_ms_teams_destination_config_model_json2
            == destination_config_one_of_ms_teams_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfPagerDutyDestinationConfig:
    """
    Test Class for DestinationConfigOneOfPagerDutyDestinationConfig
    """

    def test_destination_config_one_of_pager_duty_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfPagerDutyDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfPagerDutyDestinationConfig model
        destination_config_one_of_pager_duty_destination_config_model_json = {}
        destination_config_one_of_pager_duty_destination_config_model_json['api_key'] = 'testString'
        destination_config_one_of_pager_duty_destination_config_model_json['routing_key'] = 'testString'

        # Construct a model instance of DestinationConfigOneOfPagerDutyDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_pager_duty_destination_config_model = (
            DestinationConfigOneOfPagerDutyDestinationConfig.from_dict(
                destination_config_one_of_pager_duty_destination_config_model_json
            )
        )
        assert destination_config_one_of_pager_duty_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfPagerDutyDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_pager_duty_destination_config_model_dict = (
            DestinationConfigOneOfPagerDutyDestinationConfig.from_dict(
                destination_config_one_of_pager_duty_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_pager_duty_destination_config_model2 = (
            DestinationConfigOneOfPagerDutyDestinationConfig(
                **destination_config_one_of_pager_duty_destination_config_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_pager_duty_destination_config_model
            == destination_config_one_of_pager_duty_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_pager_duty_destination_config_model_json2 = (
            destination_config_one_of_pager_duty_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_pager_duty_destination_config_model_json2
            == destination_config_one_of_pager_duty_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfSafariDestinationConfig:
    """
    Test Class for DestinationConfigOneOfSafariDestinationConfig
    """

    def test_destination_config_one_of_safari_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfSafariDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfSafariDestinationConfig model
        destination_config_one_of_safari_destination_config_model_json = {}
        destination_config_one_of_safari_destination_config_model_json['cert_type'] = 'p12'
        destination_config_one_of_safari_destination_config_model_json['password'] = 'testString'
        destination_config_one_of_safari_destination_config_model_json['website_url'] = 'testString'
        destination_config_one_of_safari_destination_config_model_json['website_name'] = 'testString'
        destination_config_one_of_safari_destination_config_model_json['url_format_string'] = 'testString'
        destination_config_one_of_safari_destination_config_model_json['website_push_id'] = 'testString'
        destination_config_one_of_safari_destination_config_model_json['pre_prod'] = False

        # Construct a model instance of DestinationConfigOneOfSafariDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_safari_destination_config_model = (
            DestinationConfigOneOfSafariDestinationConfig.from_dict(
                destination_config_one_of_safari_destination_config_model_json
            )
        )
        assert destination_config_one_of_safari_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfSafariDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_safari_destination_config_model_dict = (
            DestinationConfigOneOfSafariDestinationConfig.from_dict(
                destination_config_one_of_safari_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_safari_destination_config_model2 = DestinationConfigOneOfSafariDestinationConfig(
            **destination_config_one_of_safari_destination_config_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_safari_destination_config_model
            == destination_config_one_of_safari_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_safari_destination_config_model_json2 = (
            destination_config_one_of_safari_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_safari_destination_config_model_json2
            == destination_config_one_of_safari_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfServiceNowDestinationConfig:
    """
    Test Class for DestinationConfigOneOfServiceNowDestinationConfig
    """

    def test_destination_config_one_of_service_now_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfServiceNowDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfServiceNowDestinationConfig model
        destination_config_one_of_service_now_destination_config_model_json = {}
        destination_config_one_of_service_now_destination_config_model_json['client_id'] = 'testString'
        destination_config_one_of_service_now_destination_config_model_json['client_secret'] = 'testString'
        destination_config_one_of_service_now_destination_config_model_json['username'] = 'testString'
        destination_config_one_of_service_now_destination_config_model_json['password'] = 'testString'
        destination_config_one_of_service_now_destination_config_model_json['instance_name'] = 'testString'

        # Construct a model instance of DestinationConfigOneOfServiceNowDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_service_now_destination_config_model = (
            DestinationConfigOneOfServiceNowDestinationConfig.from_dict(
                destination_config_one_of_service_now_destination_config_model_json
            )
        )
        assert destination_config_one_of_service_now_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfServiceNowDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_service_now_destination_config_model_dict = (
            DestinationConfigOneOfServiceNowDestinationConfig.from_dict(
                destination_config_one_of_service_now_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_service_now_destination_config_model2 = (
            DestinationConfigOneOfServiceNowDestinationConfig(
                **destination_config_one_of_service_now_destination_config_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_service_now_destination_config_model
            == destination_config_one_of_service_now_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_service_now_destination_config_model_json2 = (
            destination_config_one_of_service_now_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_service_now_destination_config_model_json2
            == destination_config_one_of_service_now_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfSlackDestinationConfig:
    """
    Test Class for DestinationConfigOneOfSlackDestinationConfig
    """

    def test_destination_config_one_of_slack_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfSlackDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfSlackDestinationConfig model
        destination_config_one_of_slack_destination_config_model_json = {}
        destination_config_one_of_slack_destination_config_model_json['url'] = 'testString'

        # Construct a model instance of DestinationConfigOneOfSlackDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_slack_destination_config_model = (
            DestinationConfigOneOfSlackDestinationConfig.from_dict(
                destination_config_one_of_slack_destination_config_model_json
            )
        )
        assert destination_config_one_of_slack_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfSlackDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_slack_destination_config_model_dict = (
            DestinationConfigOneOfSlackDestinationConfig.from_dict(
                destination_config_one_of_slack_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_slack_destination_config_model2 = DestinationConfigOneOfSlackDestinationConfig(
            **destination_config_one_of_slack_destination_config_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_slack_destination_config_model
            == destination_config_one_of_slack_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_slack_destination_config_model_json2 = (
            destination_config_one_of_slack_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_slack_destination_config_model_json2
            == destination_config_one_of_slack_destination_config_model_json
        )


class TestModel_DestinationConfigOneOfWebhookDestinationConfig:
    """
    Test Class for DestinationConfigOneOfWebhookDestinationConfig
    """

    def test_destination_config_one_of_webhook_destination_config_serialization(self):
        """
        Test serialization/deserialization for DestinationConfigOneOfWebhookDestinationConfig
        """

        # Construct a json representation of a DestinationConfigOneOfWebhookDestinationConfig model
        destination_config_one_of_webhook_destination_config_model_json = {}
        destination_config_one_of_webhook_destination_config_model_json['url'] = 'testString'
        destination_config_one_of_webhook_destination_config_model_json['verb'] = 'get'
        destination_config_one_of_webhook_destination_config_model_json['custom_headers'] = {'key1': 'testString'}
        destination_config_one_of_webhook_destination_config_model_json['sensitive_headers'] = ['testString']

        # Construct a model instance of DestinationConfigOneOfWebhookDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_webhook_destination_config_model = (
            DestinationConfigOneOfWebhookDestinationConfig.from_dict(
                destination_config_one_of_webhook_destination_config_model_json
            )
        )
        assert destination_config_one_of_webhook_destination_config_model != False

        # Construct a model instance of DestinationConfigOneOfWebhookDestinationConfig by calling from_dict on the json representation
        destination_config_one_of_webhook_destination_config_model_dict = (
            DestinationConfigOneOfWebhookDestinationConfig.from_dict(
                destination_config_one_of_webhook_destination_config_model_json
            ).__dict__
        )
        destination_config_one_of_webhook_destination_config_model2 = DestinationConfigOneOfWebhookDestinationConfig(
            **destination_config_one_of_webhook_destination_config_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            destination_config_one_of_webhook_destination_config_model
            == destination_config_one_of_webhook_destination_config_model2
        )

        # Convert model instance back to dict and verify no loss of data
        destination_config_one_of_webhook_destination_config_model_json2 = (
            destination_config_one_of_webhook_destination_config_model.to_dict()
        )
        assert (
            destination_config_one_of_webhook_destination_config_model_json2
            == destination_config_one_of_webhook_destination_config_model_json
        )


class TestModel_SubscriptionAttributesCustomEmailAttributesResponse:
    """
    Test Class for SubscriptionAttributesCustomEmailAttributesResponse
    """

    def test_subscription_attributes_custom_email_attributes_response_serialization(self):
        """
        Test serialization/deserialization for SubscriptionAttributesCustomEmailAttributesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        email_attributes_response_invited_items_model = {}  # EmailAttributesResponseInvitedItems
        email_attributes_response_invited_items_model['email'] = 'testString'
        email_attributes_response_invited_items_model['updated_at'] = '2019-01-01T12:00:00Z'
        email_attributes_response_invited_items_model['expires_at'] = '2019-01-01T12:00:00Z'

        email_attributes_response_subscribed_unsubscribed_items_model = (
            {}
        )  # EmailAttributesResponseSubscribedUnsubscribedItems
        email_attributes_response_subscribed_unsubscribed_items_model['email'] = 'testString'
        email_attributes_response_subscribed_unsubscribed_items_model['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a SubscriptionAttributesCustomEmailAttributesResponse model
        subscription_attributes_custom_email_attributes_response_model_json = {}
        subscription_attributes_custom_email_attributes_response_model_json['invited'] = [
            email_attributes_response_invited_items_model
        ]
        subscription_attributes_custom_email_attributes_response_model_json['subscribed'] = [
            email_attributes_response_subscribed_unsubscribed_items_model
        ]
        subscription_attributes_custom_email_attributes_response_model_json['unsubscribed'] = [
            email_attributes_response_subscribed_unsubscribed_items_model
        ]
        subscription_attributes_custom_email_attributes_response_model_json['add_notification_payload'] = False
        subscription_attributes_custom_email_attributes_response_model_json['reply_to_mail'] = 'testString'
        subscription_attributes_custom_email_attributes_response_model_json['reply_to_name'] = 'testString'
        subscription_attributes_custom_email_attributes_response_model_json['from_name'] = 'testString'
        subscription_attributes_custom_email_attributes_response_model_json['from_email'] = 'testString'
        subscription_attributes_custom_email_attributes_response_model_json['template_id_notification'] = 'testString'
        subscription_attributes_custom_email_attributes_response_model_json['template_id_invitation'] = 'testString'
        subscription_attributes_custom_email_attributes_response_model_json['foo'] = 'testString'

        # Construct a model instance of SubscriptionAttributesCustomEmailAttributesResponse by calling from_dict on the json representation
        subscription_attributes_custom_email_attributes_response_model = (
            SubscriptionAttributesCustomEmailAttributesResponse.from_dict(
                subscription_attributes_custom_email_attributes_response_model_json
            )
        )
        assert subscription_attributes_custom_email_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesCustomEmailAttributesResponse by calling from_dict on the json representation
        subscription_attributes_custom_email_attributes_response_model_dict = (
            SubscriptionAttributesCustomEmailAttributesResponse.from_dict(
                subscription_attributes_custom_email_attributes_response_model_json
            ).__dict__
        )
        subscription_attributes_custom_email_attributes_response_model2 = (
            SubscriptionAttributesCustomEmailAttributesResponse(
                **subscription_attributes_custom_email_attributes_response_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            subscription_attributes_custom_email_attributes_response_model
            == subscription_attributes_custom_email_attributes_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_custom_email_attributes_response_model_json2 = (
            subscription_attributes_custom_email_attributes_response_model.to_dict()
        )
        assert (
            subscription_attributes_custom_email_attributes_response_model_json2
            == subscription_attributes_custom_email_attributes_response_model_json
        )

        # Test get_properties and set_properties methods.
        subscription_attributes_custom_email_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_custom_email_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_custom_email_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_custom_email_attributes_response_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_SubscriptionAttributesCustomSMSAttributesResponse:
    """
    Test Class for SubscriptionAttributesCustomSMSAttributesResponse
    """

    def test_subscription_attributes_custom_sms_attributes_response_serialization(self):
        """
        Test serialization/deserialization for SubscriptionAttributesCustomSMSAttributesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        sms_attributes_items_model = {}  # SMSAttributesItems
        sms_attributes_items_model['phone_number'] = 'testString'
        sms_attributes_items_model['updated_at'] = '2019-01-01T12:00:00Z'

        sms_invite_attributes_items_model = {}  # SMSInviteAttributesItems
        sms_invite_attributes_items_model['phone_number'] = 'testString'
        sms_invite_attributes_items_model['updated_at'] = '2019-01-01T12:00:00Z'
        sms_invite_attributes_items_model['expires_at'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a SubscriptionAttributesCustomSMSAttributesResponse model
        subscription_attributes_custom_sms_attributes_response_model_json = {}
        subscription_attributes_custom_sms_attributes_response_model_json['subscribed'] = [sms_attributes_items_model]
        subscription_attributes_custom_sms_attributes_response_model_json['unsubscribed'] = [sms_attributes_items_model]
        subscription_attributes_custom_sms_attributes_response_model_json['invited'] = [
            sms_invite_attributes_items_model
        ]
        subscription_attributes_custom_sms_attributes_response_model_json['foo'] = 'testString'

        # Construct a model instance of SubscriptionAttributesCustomSMSAttributesResponse by calling from_dict on the json representation
        subscription_attributes_custom_sms_attributes_response_model = (
            SubscriptionAttributesCustomSMSAttributesResponse.from_dict(
                subscription_attributes_custom_sms_attributes_response_model_json
            )
        )
        assert subscription_attributes_custom_sms_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesCustomSMSAttributesResponse by calling from_dict on the json representation
        subscription_attributes_custom_sms_attributes_response_model_dict = (
            SubscriptionAttributesCustomSMSAttributesResponse.from_dict(
                subscription_attributes_custom_sms_attributes_response_model_json
            ).__dict__
        )
        subscription_attributes_custom_sms_attributes_response_model2 = (
            SubscriptionAttributesCustomSMSAttributesResponse(
                **subscription_attributes_custom_sms_attributes_response_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            subscription_attributes_custom_sms_attributes_response_model
            == subscription_attributes_custom_sms_attributes_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_custom_sms_attributes_response_model_json2 = (
            subscription_attributes_custom_sms_attributes_response_model.to_dict()
        )
        assert (
            subscription_attributes_custom_sms_attributes_response_model_json2
            == subscription_attributes_custom_sms_attributes_response_model_json
        )

        # Test get_properties and set_properties methods.
        subscription_attributes_custom_sms_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_custom_sms_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_custom_sms_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_custom_sms_attributes_response_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_SubscriptionAttributesEmailAttributesResponse:
    """
    Test Class for SubscriptionAttributesEmailAttributesResponse
    """

    def test_subscription_attributes_email_attributes_response_serialization(self):
        """
        Test serialization/deserialization for SubscriptionAttributesEmailAttributesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        email_attributes_response_invited_items_model = {}  # EmailAttributesResponseInvitedItems
        email_attributes_response_invited_items_model['email'] = 'testString'
        email_attributes_response_invited_items_model['updated_at'] = '2019-01-01T12:00:00Z'
        email_attributes_response_invited_items_model['expires_at'] = '2019-01-01T12:00:00Z'

        email_attributes_response_subscribed_unsubscribed_items_model = (
            {}
        )  # EmailAttributesResponseSubscribedUnsubscribedItems
        email_attributes_response_subscribed_unsubscribed_items_model['email'] = 'testString'
        email_attributes_response_subscribed_unsubscribed_items_model['updated_at'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a SubscriptionAttributesEmailAttributesResponse model
        subscription_attributes_email_attributes_response_model_json = {}
        subscription_attributes_email_attributes_response_model_json['invited'] = [
            email_attributes_response_invited_items_model
        ]
        subscription_attributes_email_attributes_response_model_json['subscribed'] = [
            email_attributes_response_subscribed_unsubscribed_items_model
        ]
        subscription_attributes_email_attributes_response_model_json['unsubscribed'] = [
            email_attributes_response_subscribed_unsubscribed_items_model
        ]
        subscription_attributes_email_attributes_response_model_json['add_notification_payload'] = False
        subscription_attributes_email_attributes_response_model_json['reply_to_mail'] = 'testString'
        subscription_attributes_email_attributes_response_model_json['reply_to_name'] = 'testString'
        subscription_attributes_email_attributes_response_model_json['from_name'] = 'testString'
        subscription_attributes_email_attributes_response_model_json['foo'] = 'testString'

        # Construct a model instance of SubscriptionAttributesEmailAttributesResponse by calling from_dict on the json representation
        subscription_attributes_email_attributes_response_model = (
            SubscriptionAttributesEmailAttributesResponse.from_dict(
                subscription_attributes_email_attributes_response_model_json
            )
        )
        assert subscription_attributes_email_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesEmailAttributesResponse by calling from_dict on the json representation
        subscription_attributes_email_attributes_response_model_dict = (
            SubscriptionAttributesEmailAttributesResponse.from_dict(
                subscription_attributes_email_attributes_response_model_json
            ).__dict__
        )
        subscription_attributes_email_attributes_response_model2 = SubscriptionAttributesEmailAttributesResponse(
            **subscription_attributes_email_attributes_response_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_attributes_email_attributes_response_model
            == subscription_attributes_email_attributes_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_email_attributes_response_model_json2 = (
            subscription_attributes_email_attributes_response_model.to_dict()
        )
        assert (
            subscription_attributes_email_attributes_response_model_json2
            == subscription_attributes_email_attributes_response_model_json
        )

        # Test get_properties and set_properties methods.
        subscription_attributes_email_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_email_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_email_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_email_attributes_response_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_SubscriptionAttributesSMSAttributesResponse:
    """
    Test Class for SubscriptionAttributesSMSAttributesResponse
    """

    def test_subscription_attributes_sms_attributes_response_serialization(self):
        """
        Test serialization/deserialization for SubscriptionAttributesSMSAttributesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        sms_attributes_items_model = {}  # SMSAttributesItems
        sms_attributes_items_model['phone_number'] = 'testString'
        sms_attributes_items_model['updated_at'] = '2019-01-01T12:00:00Z'

        sms_invite_attributes_items_model = {}  # SMSInviteAttributesItems
        sms_invite_attributes_items_model['phone_number'] = 'testString'
        sms_invite_attributes_items_model['updated_at'] = '2019-01-01T12:00:00Z'
        sms_invite_attributes_items_model['expires_at'] = '2019-01-01T12:00:00Z'

        # Construct a json representation of a SubscriptionAttributesSMSAttributesResponse model
        subscription_attributes_sms_attributes_response_model_json = {}
        subscription_attributes_sms_attributes_response_model_json['subscribed'] = [sms_attributes_items_model]
        subscription_attributes_sms_attributes_response_model_json['unsubscribed'] = [sms_attributes_items_model]
        subscription_attributes_sms_attributes_response_model_json['invited'] = [sms_invite_attributes_items_model]
        subscription_attributes_sms_attributes_response_model_json['foo'] = 'testString'

        # Construct a model instance of SubscriptionAttributesSMSAttributesResponse by calling from_dict on the json representation
        subscription_attributes_sms_attributes_response_model = SubscriptionAttributesSMSAttributesResponse.from_dict(
            subscription_attributes_sms_attributes_response_model_json
        )
        assert subscription_attributes_sms_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesSMSAttributesResponse by calling from_dict on the json representation
        subscription_attributes_sms_attributes_response_model_dict = (
            SubscriptionAttributesSMSAttributesResponse.from_dict(
                subscription_attributes_sms_attributes_response_model_json
            ).__dict__
        )
        subscription_attributes_sms_attributes_response_model2 = SubscriptionAttributesSMSAttributesResponse(
            **subscription_attributes_sms_attributes_response_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_attributes_sms_attributes_response_model
            == subscription_attributes_sms_attributes_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_sms_attributes_response_model_json2 = (
            subscription_attributes_sms_attributes_response_model.to_dict()
        )
        assert (
            subscription_attributes_sms_attributes_response_model_json2
            == subscription_attributes_sms_attributes_response_model_json
        )

        # Test get_properties and set_properties methods.
        subscription_attributes_sms_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_sms_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_sms_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_sms_attributes_response_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_SubscriptionAttributesServiceNowAttributesResponse:
    """
    Test Class for SubscriptionAttributesServiceNowAttributesResponse
    """

    def test_subscription_attributes_service_now_attributes_response_serialization(self):
        """
        Test serialization/deserialization for SubscriptionAttributesServiceNowAttributesResponse
        """

        # Construct a json representation of a SubscriptionAttributesServiceNowAttributesResponse model
        subscription_attributes_service_now_attributes_response_model_json = {}
        subscription_attributes_service_now_attributes_response_model_json['assigned_to'] = 'testString'
        subscription_attributes_service_now_attributes_response_model_json['assignment_group'] = 'testString'
        subscription_attributes_service_now_attributes_response_model_json['foo'] = 'testString'

        # Construct a model instance of SubscriptionAttributesServiceNowAttributesResponse by calling from_dict on the json representation
        subscription_attributes_service_now_attributes_response_model = (
            SubscriptionAttributesServiceNowAttributesResponse.from_dict(
                subscription_attributes_service_now_attributes_response_model_json
            )
        )
        assert subscription_attributes_service_now_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesServiceNowAttributesResponse by calling from_dict on the json representation
        subscription_attributes_service_now_attributes_response_model_dict = (
            SubscriptionAttributesServiceNowAttributesResponse.from_dict(
                subscription_attributes_service_now_attributes_response_model_json
            ).__dict__
        )
        subscription_attributes_service_now_attributes_response_model2 = (
            SubscriptionAttributesServiceNowAttributesResponse(
                **subscription_attributes_service_now_attributes_response_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            subscription_attributes_service_now_attributes_response_model
            == subscription_attributes_service_now_attributes_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_service_now_attributes_response_model_json2 = (
            subscription_attributes_service_now_attributes_response_model.to_dict()
        )
        assert (
            subscription_attributes_service_now_attributes_response_model_json2
            == subscription_attributes_service_now_attributes_response_model_json
        )

        # Test get_properties and set_properties methods.
        subscription_attributes_service_now_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_service_now_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_service_now_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_service_now_attributes_response_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_SubscriptionAttributesSlackAttributesResponse:
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
        subscription_attributes_slack_attributes_response_model_json['template_id_notification'] = 'testString'
        subscription_attributes_slack_attributes_response_model_json['foo'] = 'testString'

        # Construct a model instance of SubscriptionAttributesSlackAttributesResponse by calling from_dict on the json representation
        subscription_attributes_slack_attributes_response_model = (
            SubscriptionAttributesSlackAttributesResponse.from_dict(
                subscription_attributes_slack_attributes_response_model_json
            )
        )
        assert subscription_attributes_slack_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesSlackAttributesResponse by calling from_dict on the json representation
        subscription_attributes_slack_attributes_response_model_dict = (
            SubscriptionAttributesSlackAttributesResponse.from_dict(
                subscription_attributes_slack_attributes_response_model_json
            ).__dict__
        )
        subscription_attributes_slack_attributes_response_model2 = SubscriptionAttributesSlackAttributesResponse(
            **subscription_attributes_slack_attributes_response_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_attributes_slack_attributes_response_model
            == subscription_attributes_slack_attributes_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_slack_attributes_response_model_json2 = (
            subscription_attributes_slack_attributes_response_model.to_dict()
        )
        assert (
            subscription_attributes_slack_attributes_response_model_json2
            == subscription_attributes_slack_attributes_response_model_json
        )

        # Test get_properties and set_properties methods.
        subscription_attributes_slack_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_slack_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_slack_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_slack_attributes_response_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_SubscriptionAttributesWebhookAttributesResponse:
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
        subscription_attributes_webhook_attributes_response_model = (
            SubscriptionAttributesWebhookAttributesResponse.from_dict(
                subscription_attributes_webhook_attributes_response_model_json
            )
        )
        assert subscription_attributes_webhook_attributes_response_model != False

        # Construct a model instance of SubscriptionAttributesWebhookAttributesResponse by calling from_dict on the json representation
        subscription_attributes_webhook_attributes_response_model_dict = (
            SubscriptionAttributesWebhookAttributesResponse.from_dict(
                subscription_attributes_webhook_attributes_response_model_json
            ).__dict__
        )
        subscription_attributes_webhook_attributes_response_model2 = SubscriptionAttributesWebhookAttributesResponse(
            **subscription_attributes_webhook_attributes_response_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_attributes_webhook_attributes_response_model
            == subscription_attributes_webhook_attributes_response_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_attributes_webhook_attributes_response_model_json2 = (
            subscription_attributes_webhook_attributes_response_model.to_dict()
        )
        assert (
            subscription_attributes_webhook_attributes_response_model_json2
            == subscription_attributes_webhook_attributes_response_model_json
        )

        # Test get_properties and set_properties methods.
        subscription_attributes_webhook_attributes_response_model.set_properties({})
        actual_dict = subscription_attributes_webhook_attributes_response_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        subscription_attributes_webhook_attributes_response_model.set_properties(expected_dict)
        actual_dict = subscription_attributes_webhook_attributes_response_model.get_properties()
        assert actual_dict == expected_dict


class TestModel_SubscriptionCreateAttributesCustomEmailAttributes:
    """
    Test Class for SubscriptionCreateAttributesCustomEmailAttributes
    """

    def test_subscription_create_attributes_custom_email_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesCustomEmailAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesCustomEmailAttributes model
        subscription_create_attributes_custom_email_attributes_model_json = {}
        subscription_create_attributes_custom_email_attributes_model_json['invited'] = ['testString']
        subscription_create_attributes_custom_email_attributes_model_json['add_notification_payload'] = False
        subscription_create_attributes_custom_email_attributes_model_json['reply_to_mail'] = 'testString'
        subscription_create_attributes_custom_email_attributes_model_json['reply_to_name'] = 'testString'
        subscription_create_attributes_custom_email_attributes_model_json['from_name'] = 'testString'
        subscription_create_attributes_custom_email_attributes_model_json['from_email'] = 'testString'
        subscription_create_attributes_custom_email_attributes_model_json['template_id_notification'] = 'testString'
        subscription_create_attributes_custom_email_attributes_model_json['template_id_invitation'] = 'testString'

        # Construct a model instance of SubscriptionCreateAttributesCustomEmailAttributes by calling from_dict on the json representation
        subscription_create_attributes_custom_email_attributes_model = (
            SubscriptionCreateAttributesCustomEmailAttributes.from_dict(
                subscription_create_attributes_custom_email_attributes_model_json
            )
        )
        assert subscription_create_attributes_custom_email_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesCustomEmailAttributes by calling from_dict on the json representation
        subscription_create_attributes_custom_email_attributes_model_dict = (
            SubscriptionCreateAttributesCustomEmailAttributes.from_dict(
                subscription_create_attributes_custom_email_attributes_model_json
            ).__dict__
        )
        subscription_create_attributes_custom_email_attributes_model2 = (
            SubscriptionCreateAttributesCustomEmailAttributes(
                **subscription_create_attributes_custom_email_attributes_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            subscription_create_attributes_custom_email_attributes_model
            == subscription_create_attributes_custom_email_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_custom_email_attributes_model_json2 = (
            subscription_create_attributes_custom_email_attributes_model.to_dict()
        )
        assert (
            subscription_create_attributes_custom_email_attributes_model_json2
            == subscription_create_attributes_custom_email_attributes_model_json
        )


class TestModel_SubscriptionCreateAttributesCustomSMSAttributes:
    """
    Test Class for SubscriptionCreateAttributesCustomSMSAttributes
    """

    def test_subscription_create_attributes_custom_sms_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesCustomSMSAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesCustomSMSAttributes model
        subscription_create_attributes_custom_sms_attributes_model_json = {}
        subscription_create_attributes_custom_sms_attributes_model_json['invited'] = ['testString']

        # Construct a model instance of SubscriptionCreateAttributesCustomSMSAttributes by calling from_dict on the json representation
        subscription_create_attributes_custom_sms_attributes_model = (
            SubscriptionCreateAttributesCustomSMSAttributes.from_dict(
                subscription_create_attributes_custom_sms_attributes_model_json
            )
        )
        assert subscription_create_attributes_custom_sms_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesCustomSMSAttributes by calling from_dict on the json representation
        subscription_create_attributes_custom_sms_attributes_model_dict = (
            SubscriptionCreateAttributesCustomSMSAttributes.from_dict(
                subscription_create_attributes_custom_sms_attributes_model_json
            ).__dict__
        )
        subscription_create_attributes_custom_sms_attributes_model2 = SubscriptionCreateAttributesCustomSMSAttributes(
            **subscription_create_attributes_custom_sms_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_create_attributes_custom_sms_attributes_model
            == subscription_create_attributes_custom_sms_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_custom_sms_attributes_model_json2 = (
            subscription_create_attributes_custom_sms_attributes_model.to_dict()
        )
        assert (
            subscription_create_attributes_custom_sms_attributes_model_json2
            == subscription_create_attributes_custom_sms_attributes_model_json
        )


class TestModel_SubscriptionCreateAttributesEmailAttributes:
    """
    Test Class for SubscriptionCreateAttributesEmailAttributes
    """

    def test_subscription_create_attributes_email_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesEmailAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesEmailAttributes model
        subscription_create_attributes_email_attributes_model_json = {}
        subscription_create_attributes_email_attributes_model_json['invited'] = ['testString']
        subscription_create_attributes_email_attributes_model_json['add_notification_payload'] = False
        subscription_create_attributes_email_attributes_model_json['reply_to_mail'] = 'testString'
        subscription_create_attributes_email_attributes_model_json['reply_to_name'] = 'testString'
        subscription_create_attributes_email_attributes_model_json['from_name'] = 'testString'

        # Construct a model instance of SubscriptionCreateAttributesEmailAttributes by calling from_dict on the json representation
        subscription_create_attributes_email_attributes_model = SubscriptionCreateAttributesEmailAttributes.from_dict(
            subscription_create_attributes_email_attributes_model_json
        )
        assert subscription_create_attributes_email_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesEmailAttributes by calling from_dict on the json representation
        subscription_create_attributes_email_attributes_model_dict = (
            SubscriptionCreateAttributesEmailAttributes.from_dict(
                subscription_create_attributes_email_attributes_model_json
            ).__dict__
        )
        subscription_create_attributes_email_attributes_model2 = SubscriptionCreateAttributesEmailAttributes(
            **subscription_create_attributes_email_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_create_attributes_email_attributes_model
            == subscription_create_attributes_email_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_email_attributes_model_json2 = (
            subscription_create_attributes_email_attributes_model.to_dict()
        )
        assert (
            subscription_create_attributes_email_attributes_model_json2
            == subscription_create_attributes_email_attributes_model_json
        )


class TestModel_SubscriptionCreateAttributesFCMAttributes:
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
        subscription_create_attributes_fcm_attributes_model = SubscriptionCreateAttributesFCMAttributes.from_dict(
            subscription_create_attributes_fcm_attributes_model_json
        )
        assert subscription_create_attributes_fcm_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesFCMAttributes by calling from_dict on the json representation
        subscription_create_attributes_fcm_attributes_model_dict = SubscriptionCreateAttributesFCMAttributes.from_dict(
            subscription_create_attributes_fcm_attributes_model_json
        ).__dict__
        subscription_create_attributes_fcm_attributes_model2 = SubscriptionCreateAttributesFCMAttributes(
            **subscription_create_attributes_fcm_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_create_attributes_fcm_attributes_model == subscription_create_attributes_fcm_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_fcm_attributes_model_json2 = (
            subscription_create_attributes_fcm_attributes_model.to_dict()
        )
        assert (
            subscription_create_attributes_fcm_attributes_model_json2
            == subscription_create_attributes_fcm_attributes_model_json
        )


class TestModel_SubscriptionCreateAttributesSMSAttributes:
    """
    Test Class for SubscriptionCreateAttributesSMSAttributes
    """

    def test_subscription_create_attributes_sms_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesSMSAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesSMSAttributes model
        subscription_create_attributes_sms_attributes_model_json = {}
        subscription_create_attributes_sms_attributes_model_json['invited'] = ['testString']

        # Construct a model instance of SubscriptionCreateAttributesSMSAttributes by calling from_dict on the json representation
        subscription_create_attributes_sms_attributes_model = SubscriptionCreateAttributesSMSAttributes.from_dict(
            subscription_create_attributes_sms_attributes_model_json
        )
        assert subscription_create_attributes_sms_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesSMSAttributes by calling from_dict on the json representation
        subscription_create_attributes_sms_attributes_model_dict = SubscriptionCreateAttributesSMSAttributes.from_dict(
            subscription_create_attributes_sms_attributes_model_json
        ).__dict__
        subscription_create_attributes_sms_attributes_model2 = SubscriptionCreateAttributesSMSAttributes(
            **subscription_create_attributes_sms_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_create_attributes_sms_attributes_model == subscription_create_attributes_sms_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_sms_attributes_model_json2 = (
            subscription_create_attributes_sms_attributes_model.to_dict()
        )
        assert (
            subscription_create_attributes_sms_attributes_model_json2
            == subscription_create_attributes_sms_attributes_model_json
        )


class TestModel_SubscriptionCreateAttributesServiceNowAttributes:
    """
    Test Class for SubscriptionCreateAttributesServiceNowAttributes
    """

    def test_subscription_create_attributes_service_now_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionCreateAttributesServiceNowAttributes
        """

        # Construct a json representation of a SubscriptionCreateAttributesServiceNowAttributes model
        subscription_create_attributes_service_now_attributes_model_json = {}
        subscription_create_attributes_service_now_attributes_model_json['assigned_to'] = 'testString'
        subscription_create_attributes_service_now_attributes_model_json['assignment_group'] = 'testString'

        # Construct a model instance of SubscriptionCreateAttributesServiceNowAttributes by calling from_dict on the json representation
        subscription_create_attributes_service_now_attributes_model = (
            SubscriptionCreateAttributesServiceNowAttributes.from_dict(
                subscription_create_attributes_service_now_attributes_model_json
            )
        )
        assert subscription_create_attributes_service_now_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesServiceNowAttributes by calling from_dict on the json representation
        subscription_create_attributes_service_now_attributes_model_dict = (
            SubscriptionCreateAttributesServiceNowAttributes.from_dict(
                subscription_create_attributes_service_now_attributes_model_json
            ).__dict__
        )
        subscription_create_attributes_service_now_attributes_model2 = SubscriptionCreateAttributesServiceNowAttributes(
            **subscription_create_attributes_service_now_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_create_attributes_service_now_attributes_model
            == subscription_create_attributes_service_now_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_service_now_attributes_model_json2 = (
            subscription_create_attributes_service_now_attributes_model.to_dict()
        )
        assert (
            subscription_create_attributes_service_now_attributes_model_json2
            == subscription_create_attributes_service_now_attributes_model_json
        )


class TestModel_SubscriptionCreateAttributesSlackAttributes:
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
        subscription_create_attributes_slack_attributes_model_json['template_id_notification'] = 'testString'

        # Construct a model instance of SubscriptionCreateAttributesSlackAttributes by calling from_dict on the json representation
        subscription_create_attributes_slack_attributes_model = SubscriptionCreateAttributesSlackAttributes.from_dict(
            subscription_create_attributes_slack_attributes_model_json
        )
        assert subscription_create_attributes_slack_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesSlackAttributes by calling from_dict on the json representation
        subscription_create_attributes_slack_attributes_model_dict = (
            SubscriptionCreateAttributesSlackAttributes.from_dict(
                subscription_create_attributes_slack_attributes_model_json
            ).__dict__
        )
        subscription_create_attributes_slack_attributes_model2 = SubscriptionCreateAttributesSlackAttributes(
            **subscription_create_attributes_slack_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_create_attributes_slack_attributes_model
            == subscription_create_attributes_slack_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_slack_attributes_model_json2 = (
            subscription_create_attributes_slack_attributes_model.to_dict()
        )
        assert (
            subscription_create_attributes_slack_attributes_model_json2
            == subscription_create_attributes_slack_attributes_model_json
        )


class TestModel_SubscriptionCreateAttributesWebhookAttributes:
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
        subscription_create_attributes_webhook_attributes_model = (
            SubscriptionCreateAttributesWebhookAttributes.from_dict(
                subscription_create_attributes_webhook_attributes_model_json
            )
        )
        assert subscription_create_attributes_webhook_attributes_model != False

        # Construct a model instance of SubscriptionCreateAttributesWebhookAttributes by calling from_dict on the json representation
        subscription_create_attributes_webhook_attributes_model_dict = (
            SubscriptionCreateAttributesWebhookAttributes.from_dict(
                subscription_create_attributes_webhook_attributes_model_json
            ).__dict__
        )
        subscription_create_attributes_webhook_attributes_model2 = SubscriptionCreateAttributesWebhookAttributes(
            **subscription_create_attributes_webhook_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_create_attributes_webhook_attributes_model
            == subscription_create_attributes_webhook_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_create_attributes_webhook_attributes_model_json2 = (
            subscription_create_attributes_webhook_attributes_model.to_dict()
        )
        assert (
            subscription_create_attributes_webhook_attributes_model_json2
            == subscription_create_attributes_webhook_attributes_model_json
        )


class TestModel_SubscriptionUpdateAttributesCustomEmailUpdateAttributes:
    """
    Test Class for SubscriptionUpdateAttributesCustomEmailUpdateAttributes
    """

    def test_subscription_update_attributes_custom_email_update_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesCustomEmailUpdateAttributes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        update_attributes_invited_model = {}  # UpdateAttributesInvited
        update_attributes_invited_model['add'] = ['testString']
        update_attributes_invited_model['remove'] = ['testString']

        update_attributes_subscribed_model = {}  # UpdateAttributesSubscribed
        update_attributes_subscribed_model['remove'] = ['testString']

        update_attributes_unsubscribed_model = {}  # UpdateAttributesUnsubscribed
        update_attributes_unsubscribed_model['remove'] = ['testString']

        # Construct a json representation of a SubscriptionUpdateAttributesCustomEmailUpdateAttributes model
        subscription_update_attributes_custom_email_update_attributes_model_json = {}
        subscription_update_attributes_custom_email_update_attributes_model_json['invited'] = (
            update_attributes_invited_model
        )
        subscription_update_attributes_custom_email_update_attributes_model_json['add_notification_payload'] = False
        subscription_update_attributes_custom_email_update_attributes_model_json['reply_to_mail'] = 'testString'
        subscription_update_attributes_custom_email_update_attributes_model_json['reply_to_name'] = 'testString'
        subscription_update_attributes_custom_email_update_attributes_model_json['from_name'] = 'testString'
        subscription_update_attributes_custom_email_update_attributes_model_json['from_email'] = 'testString'
        subscription_update_attributes_custom_email_update_attributes_model_json['subscribed'] = (
            update_attributes_subscribed_model
        )
        subscription_update_attributes_custom_email_update_attributes_model_json['unsubscribed'] = (
            update_attributes_unsubscribed_model
        )
        subscription_update_attributes_custom_email_update_attributes_model_json['template_id_notification'] = (
            'testString'
        )
        subscription_update_attributes_custom_email_update_attributes_model_json['template_id_invitation'] = (
            'testString'
        )

        # Construct a model instance of SubscriptionUpdateAttributesCustomEmailUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_custom_email_update_attributes_model = (
            SubscriptionUpdateAttributesCustomEmailUpdateAttributes.from_dict(
                subscription_update_attributes_custom_email_update_attributes_model_json
            )
        )
        assert subscription_update_attributes_custom_email_update_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesCustomEmailUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_custom_email_update_attributes_model_dict = (
            SubscriptionUpdateAttributesCustomEmailUpdateAttributes.from_dict(
                subscription_update_attributes_custom_email_update_attributes_model_json
            ).__dict__
        )
        subscription_update_attributes_custom_email_update_attributes_model2 = (
            SubscriptionUpdateAttributesCustomEmailUpdateAttributes(
                **subscription_update_attributes_custom_email_update_attributes_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            subscription_update_attributes_custom_email_update_attributes_model
            == subscription_update_attributes_custom_email_update_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_custom_email_update_attributes_model_json2 = (
            subscription_update_attributes_custom_email_update_attributes_model.to_dict()
        )
        assert (
            subscription_update_attributes_custom_email_update_attributes_model_json2
            == subscription_update_attributes_custom_email_update_attributes_model_json
        )


class TestModel_SubscriptionUpdateAttributesCustomSMSUpdateAttributes:
    """
    Test Class for SubscriptionUpdateAttributesCustomSMSUpdateAttributes
    """

    def test_subscription_update_attributes_custom_sms_update_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesCustomSMSUpdateAttributes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        update_attributes_invited_model = {}  # UpdateAttributesInvited
        update_attributes_invited_model['add'] = ['testString']
        update_attributes_invited_model['remove'] = ['testString']

        update_attributes_subscribed_model = {}  # UpdateAttributesSubscribed
        update_attributes_subscribed_model['remove'] = ['testString']

        update_attributes_unsubscribed_model = {}  # UpdateAttributesUnsubscribed
        update_attributes_unsubscribed_model['remove'] = ['testString']

        # Construct a json representation of a SubscriptionUpdateAttributesCustomSMSUpdateAttributes model
        subscription_update_attributes_custom_sms_update_attributes_model_json = {}
        subscription_update_attributes_custom_sms_update_attributes_model_json['invited'] = (
            update_attributes_invited_model
        )
        subscription_update_attributes_custom_sms_update_attributes_model_json['subscribed'] = (
            update_attributes_subscribed_model
        )
        subscription_update_attributes_custom_sms_update_attributes_model_json['unsubscribed'] = (
            update_attributes_unsubscribed_model
        )

        # Construct a model instance of SubscriptionUpdateAttributesCustomSMSUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_custom_sms_update_attributes_model = (
            SubscriptionUpdateAttributesCustomSMSUpdateAttributes.from_dict(
                subscription_update_attributes_custom_sms_update_attributes_model_json
            )
        )
        assert subscription_update_attributes_custom_sms_update_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesCustomSMSUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_custom_sms_update_attributes_model_dict = (
            SubscriptionUpdateAttributesCustomSMSUpdateAttributes.from_dict(
                subscription_update_attributes_custom_sms_update_attributes_model_json
            ).__dict__
        )
        subscription_update_attributes_custom_sms_update_attributes_model2 = (
            SubscriptionUpdateAttributesCustomSMSUpdateAttributes(
                **subscription_update_attributes_custom_sms_update_attributes_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            subscription_update_attributes_custom_sms_update_attributes_model
            == subscription_update_attributes_custom_sms_update_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_custom_sms_update_attributes_model_json2 = (
            subscription_update_attributes_custom_sms_update_attributes_model.to_dict()
        )
        assert (
            subscription_update_attributes_custom_sms_update_attributes_model_json2
            == subscription_update_attributes_custom_sms_update_attributes_model_json
        )


class TestModel_SubscriptionUpdateAttributesEmailUpdateAttributes:
    """
    Test Class for SubscriptionUpdateAttributesEmailUpdateAttributes
    """

    def test_subscription_update_attributes_email_update_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesEmailUpdateAttributes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        update_attributes_invited_model = {}  # UpdateAttributesInvited
        update_attributes_invited_model['add'] = ['testString']
        update_attributes_invited_model['remove'] = ['testString']

        update_attributes_subscribed_model = {}  # UpdateAttributesSubscribed
        update_attributes_subscribed_model['remove'] = ['testString']

        update_attributes_unsubscribed_model = {}  # UpdateAttributesUnsubscribed
        update_attributes_unsubscribed_model['remove'] = ['testString']

        # Construct a json representation of a SubscriptionUpdateAttributesEmailUpdateAttributes model
        subscription_update_attributes_email_update_attributes_model_json = {}
        subscription_update_attributes_email_update_attributes_model_json['invited'] = update_attributes_invited_model
        subscription_update_attributes_email_update_attributes_model_json['add_notification_payload'] = False
        subscription_update_attributes_email_update_attributes_model_json['reply_to_mail'] = 'testString'
        subscription_update_attributes_email_update_attributes_model_json['reply_to_name'] = 'testString'
        subscription_update_attributes_email_update_attributes_model_json['from_name'] = 'testString'
        subscription_update_attributes_email_update_attributes_model_json['subscribed'] = (
            update_attributes_subscribed_model
        )
        subscription_update_attributes_email_update_attributes_model_json['unsubscribed'] = (
            update_attributes_unsubscribed_model
        )

        # Construct a model instance of SubscriptionUpdateAttributesEmailUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_email_update_attributes_model = (
            SubscriptionUpdateAttributesEmailUpdateAttributes.from_dict(
                subscription_update_attributes_email_update_attributes_model_json
            )
        )
        assert subscription_update_attributes_email_update_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesEmailUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_email_update_attributes_model_dict = (
            SubscriptionUpdateAttributesEmailUpdateAttributes.from_dict(
                subscription_update_attributes_email_update_attributes_model_json
            ).__dict__
        )
        subscription_update_attributes_email_update_attributes_model2 = (
            SubscriptionUpdateAttributesEmailUpdateAttributes(
                **subscription_update_attributes_email_update_attributes_model_dict
            )
        )

        # Verify the model instances are equivalent
        assert (
            subscription_update_attributes_email_update_attributes_model
            == subscription_update_attributes_email_update_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_email_update_attributes_model_json2 = (
            subscription_update_attributes_email_update_attributes_model.to_dict()
        )
        assert (
            subscription_update_attributes_email_update_attributes_model_json2
            == subscription_update_attributes_email_update_attributes_model_json
        )


class TestModel_SubscriptionUpdateAttributesSMSUpdateAttributes:
    """
    Test Class for SubscriptionUpdateAttributesSMSUpdateAttributes
    """

    def test_subscription_update_attributes_sms_update_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesSMSUpdateAttributes
        """

        # Construct dict forms of any model objects needed in order to build this model.

        update_attributes_invited_model = {}  # UpdateAttributesInvited
        update_attributes_invited_model['add'] = ['testString']
        update_attributes_invited_model['remove'] = ['testString']

        update_attributes_subscribed_model = {}  # UpdateAttributesSubscribed
        update_attributes_subscribed_model['remove'] = ['testString']

        update_attributes_unsubscribed_model = {}  # UpdateAttributesUnsubscribed
        update_attributes_unsubscribed_model['remove'] = ['testString']

        # Construct a json representation of a SubscriptionUpdateAttributesSMSUpdateAttributes model
        subscription_update_attributes_sms_update_attributes_model_json = {}
        subscription_update_attributes_sms_update_attributes_model_json['invited'] = update_attributes_invited_model
        subscription_update_attributes_sms_update_attributes_model_json['subscribed'] = (
            update_attributes_subscribed_model
        )
        subscription_update_attributes_sms_update_attributes_model_json['unsubscribed'] = (
            update_attributes_unsubscribed_model
        )

        # Construct a model instance of SubscriptionUpdateAttributesSMSUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_sms_update_attributes_model = (
            SubscriptionUpdateAttributesSMSUpdateAttributes.from_dict(
                subscription_update_attributes_sms_update_attributes_model_json
            )
        )
        assert subscription_update_attributes_sms_update_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesSMSUpdateAttributes by calling from_dict on the json representation
        subscription_update_attributes_sms_update_attributes_model_dict = (
            SubscriptionUpdateAttributesSMSUpdateAttributes.from_dict(
                subscription_update_attributes_sms_update_attributes_model_json
            ).__dict__
        )
        subscription_update_attributes_sms_update_attributes_model2 = SubscriptionUpdateAttributesSMSUpdateAttributes(
            **subscription_update_attributes_sms_update_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_update_attributes_sms_update_attributes_model
            == subscription_update_attributes_sms_update_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_sms_update_attributes_model_json2 = (
            subscription_update_attributes_sms_update_attributes_model.to_dict()
        )
        assert (
            subscription_update_attributes_sms_update_attributes_model_json2
            == subscription_update_attributes_sms_update_attributes_model_json
        )


class TestModel_SubscriptionUpdateAttributesServiceNowAttributes:
    """
    Test Class for SubscriptionUpdateAttributesServiceNowAttributes
    """

    def test_subscription_update_attributes_service_now_attributes_serialization(self):
        """
        Test serialization/deserialization for SubscriptionUpdateAttributesServiceNowAttributes
        """

        # Construct a json representation of a SubscriptionUpdateAttributesServiceNowAttributes model
        subscription_update_attributes_service_now_attributes_model_json = {}
        subscription_update_attributes_service_now_attributes_model_json['assigned_to'] = 'testString'
        subscription_update_attributes_service_now_attributes_model_json['assignment_group'] = 'testString'

        # Construct a model instance of SubscriptionUpdateAttributesServiceNowAttributes by calling from_dict on the json representation
        subscription_update_attributes_service_now_attributes_model = (
            SubscriptionUpdateAttributesServiceNowAttributes.from_dict(
                subscription_update_attributes_service_now_attributes_model_json
            )
        )
        assert subscription_update_attributes_service_now_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesServiceNowAttributes by calling from_dict on the json representation
        subscription_update_attributes_service_now_attributes_model_dict = (
            SubscriptionUpdateAttributesServiceNowAttributes.from_dict(
                subscription_update_attributes_service_now_attributes_model_json
            ).__dict__
        )
        subscription_update_attributes_service_now_attributes_model2 = SubscriptionUpdateAttributesServiceNowAttributes(
            **subscription_update_attributes_service_now_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_update_attributes_service_now_attributes_model
            == subscription_update_attributes_service_now_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_service_now_attributes_model_json2 = (
            subscription_update_attributes_service_now_attributes_model.to_dict()
        )
        assert (
            subscription_update_attributes_service_now_attributes_model_json2
            == subscription_update_attributes_service_now_attributes_model_json
        )


class TestModel_SubscriptionUpdateAttributesSlackAttributes:
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
        subscription_update_attributes_slack_attributes_model_json['template_id_notification'] = 'testString'

        # Construct a model instance of SubscriptionUpdateAttributesSlackAttributes by calling from_dict on the json representation
        subscription_update_attributes_slack_attributes_model = SubscriptionUpdateAttributesSlackAttributes.from_dict(
            subscription_update_attributes_slack_attributes_model_json
        )
        assert subscription_update_attributes_slack_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesSlackAttributes by calling from_dict on the json representation
        subscription_update_attributes_slack_attributes_model_dict = (
            SubscriptionUpdateAttributesSlackAttributes.from_dict(
                subscription_update_attributes_slack_attributes_model_json
            ).__dict__
        )
        subscription_update_attributes_slack_attributes_model2 = SubscriptionUpdateAttributesSlackAttributes(
            **subscription_update_attributes_slack_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_update_attributes_slack_attributes_model
            == subscription_update_attributes_slack_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_slack_attributes_model_json2 = (
            subscription_update_attributes_slack_attributes_model.to_dict()
        )
        assert (
            subscription_update_attributes_slack_attributes_model_json2
            == subscription_update_attributes_slack_attributes_model_json
        )


class TestModel_SubscriptionUpdateAttributesWebhookAttributes:
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
        subscription_update_attributes_webhook_attributes_model = (
            SubscriptionUpdateAttributesWebhookAttributes.from_dict(
                subscription_update_attributes_webhook_attributes_model_json
            )
        )
        assert subscription_update_attributes_webhook_attributes_model != False

        # Construct a model instance of SubscriptionUpdateAttributesWebhookAttributes by calling from_dict on the json representation
        subscription_update_attributes_webhook_attributes_model_dict = (
            SubscriptionUpdateAttributesWebhookAttributes.from_dict(
                subscription_update_attributes_webhook_attributes_model_json
            ).__dict__
        )
        subscription_update_attributes_webhook_attributes_model2 = SubscriptionUpdateAttributesWebhookAttributes(
            **subscription_update_attributes_webhook_attributes_model_dict
        )

        # Verify the model instances are equivalent
        assert (
            subscription_update_attributes_webhook_attributes_model
            == subscription_update_attributes_webhook_attributes_model2
        )

        # Convert model instance back to dict and verify no loss of data
        subscription_update_attributes_webhook_attributes_model_json2 = (
            subscription_update_attributes_webhook_attributes_model.to_dict()
        )
        assert (
            subscription_update_attributes_webhook_attributes_model_json2
            == subscription_update_attributes_webhook_attributes_model_json
        )


class TestModel_TemplateConfigOneOfEmailTemplateConfig:
    """
    Test Class for TemplateConfigOneOfEmailTemplateConfig
    """

    def test_template_config_one_of_email_template_config_serialization(self):
        """
        Test serialization/deserialization for TemplateConfigOneOfEmailTemplateConfig
        """

        # Construct a json representation of a TemplateConfigOneOfEmailTemplateConfig model
        template_config_one_of_email_template_config_model_json = {}
        template_config_one_of_email_template_config_model_json['body'] = 'testString'
        template_config_one_of_email_template_config_model_json['subject'] = 'testString'

        # Construct a model instance of TemplateConfigOneOfEmailTemplateConfig by calling from_dict on the json representation
        template_config_one_of_email_template_config_model = TemplateConfigOneOfEmailTemplateConfig.from_dict(
            template_config_one_of_email_template_config_model_json
        )
        assert template_config_one_of_email_template_config_model != False

        # Construct a model instance of TemplateConfigOneOfEmailTemplateConfig by calling from_dict on the json representation
        template_config_one_of_email_template_config_model_dict = TemplateConfigOneOfEmailTemplateConfig.from_dict(
            template_config_one_of_email_template_config_model_json
        ).__dict__
        template_config_one_of_email_template_config_model2 = TemplateConfigOneOfEmailTemplateConfig(
            **template_config_one_of_email_template_config_model_dict
        )

        # Verify the model instances are equivalent
        assert template_config_one_of_email_template_config_model == template_config_one_of_email_template_config_model2

        # Convert model instance back to dict and verify no loss of data
        template_config_one_of_email_template_config_model_json2 = (
            template_config_one_of_email_template_config_model.to_dict()
        )
        assert (
            template_config_one_of_email_template_config_model_json2
            == template_config_one_of_email_template_config_model_json
        )


class TestModel_TemplateConfigOneOfSlackTemplateConfig:
    """
    Test Class for TemplateConfigOneOfSlackTemplateConfig
    """

    def test_template_config_one_of_slack_template_config_serialization(self):
        """
        Test serialization/deserialization for TemplateConfigOneOfSlackTemplateConfig
        """

        # Construct a json representation of a TemplateConfigOneOfSlackTemplateConfig model
        template_config_one_of_slack_template_config_model_json = {}
        template_config_one_of_slack_template_config_model_json['body'] = 'testString'

        # Construct a model instance of TemplateConfigOneOfSlackTemplateConfig by calling from_dict on the json representation
        template_config_one_of_slack_template_config_model = TemplateConfigOneOfSlackTemplateConfig.from_dict(
            template_config_one_of_slack_template_config_model_json
        )
        assert template_config_one_of_slack_template_config_model != False

        # Construct a model instance of TemplateConfigOneOfSlackTemplateConfig by calling from_dict on the json representation
        template_config_one_of_slack_template_config_model_dict = TemplateConfigOneOfSlackTemplateConfig.from_dict(
            template_config_one_of_slack_template_config_model_json
        ).__dict__
        template_config_one_of_slack_template_config_model2 = TemplateConfigOneOfSlackTemplateConfig(
            **template_config_one_of_slack_template_config_model_dict
        )

        # Verify the model instances are equivalent
        assert template_config_one_of_slack_template_config_model == template_config_one_of_slack_template_config_model2

        # Convert model instance back to dict and verify no loss of data
        template_config_one_of_slack_template_config_model_json2 = (
            template_config_one_of_slack_template_config_model.to_dict()
        )
        assert (
            template_config_one_of_slack_template_config_model_json2
            == template_config_one_of_slack_template_config_model_json
        )


# endregion
##############################################################################
# End of Model Tests
##############################################################################
