# IBM Cloud Event Notifications Python Admin SDK 0.0.4

Python client library to interact with various [IBM Cloud Event Notifications APIs](https://cloud.ibm.com/apidocs?category=event-notifications).

Disclaimer: this SDK is being released initially as a **pre-release** version.
Changes might occur which impact applications that use this SDK.

## Table of Contents

<!-- toc -->

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Initialize SDK](#initialize-sdk)  
- [Using the SDK](#using-the-sdk)
- [Set Environment](#set-environment)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

<!-- tocstop -->

## Overview

The IBM Cloud Event Notifications Python SDK allows developers to programmatically interact with Event Notifications service in IBM cloud.

Service Name | Module Name | Imported Class Name
--- | --- | ---
[Event Notifications Service](https://cloud.ibm.com/apidocs/event-notifications) | ibm_eventnotifications | EventNotificationsV1

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An Event Notifications Instance
* Python 3.6 or above.

## Installation


To install, use pip or easy_install:
```bash
pip install --upgrade "ibm_eventnotifications>=0.0.4"
```
or
```bash
easy_install --upgrade "ibm_eventnotifications>=0.0.4"
```

## Initialize SDK
Initialize the sdk to connect with your Event Notifications service instance.

```py
from ibm_eventnotifications.event_notifications_v1 import EventNotificationsV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

 # Create an IAM authenticator.
authenticator = IAMAuthenticator('<iam-api-key>')

# Construct the service client.
event_notifications_service = EventNotificationsV1(authenticator=authenticator)

# Set our custom service URL (optional)
event_notifications_service.set_service_url('https://' + region + '.event-notifications.cloud.ibm.com/event-notifications')

```
- region : Region of the Event Notifications Instance

## Using the SDK

SDK Methods to consume

- [Source](#source)
	- [List Sources](#list-sources)
	- [Get Source](#get-sources)
- [Topics](#topics)
	- [Create Topics](#create-topic)
	- [List Topics](#list-topic)
	- [Get Topic](#get-topic)
	- [Update Topics](#update-topic)
	- [Delete Topics](#delete-topic)
- [Destinations](#destinations)
	- [Create Destination](#create-destination)
	- [List Destinations](#list-destinations)
	- [Get Destination](#get-destination)
	- [Update Destination](#update-destination)
	- [Delete Destination](#delete-destination)
- [Subscriptions](#subscriptions)
	- [Create Subscription](#create-subscription)
	- [List Subscriptions](#list-subscriptions)
	- [Get Subscription](#get-subscription)
	- [Update Subscription](#update-subscription)
	- [Delete Subscription](#delete-subscription)
- [Send Notifications](#send-notifications)

## Source 

### List Sources

```py
source_list = event_notifications_service.list_sources(
    <instance-id>, # Event notifications service instance GUID
  ).get_result()

print(json.dumps(source_list, indent=2))
```

### Get Sources

```py

source = event_notifications_service.get_source(
      <instance-id>, # Event notifications service instance GUID
      id=<source-id>,   # Event notifications service instance Source ID
  ).get_result()

print(json.dumps(source, indent=2))

```

## Topics 

### Create Topic

```py

rules_model = {
    'enabled': False,
    'event_type_filter': '$.notification_event_info.event_type == \'cert_manager\'', #Add your event type filter here.
    'notification_filter': '$.notification.findings[0].severity == \'MODERATE\'', #Add your notification filter here.
}

# Construct a dict representation of a TopicUpdateSourcesItem model
topic_update_sources_item_model = {
    'id': <source_id>,
    'rules': [rules_model],
}

topic_response = event_notifications_service.create_topic(
    <instance_id>,
    name=<topic-name>,
    description=<topic-description>,
    sources=[topic_update_sources_item_model]
)

print(json.dumps(topic_response, indent=2))
```

### List Topics

```py
topic_list = event_notifications_service.list_topics(
    <instance-id>,
).get_result()

print(json.dumps(topic_list, indent=2))
```

### Get Topic

```py
topic = event_notifications_service.get_topic(
      <instance-id>, # Event notifications service instance GUID
      id=<topic-id>, # Event notifications service instance Topic ID
  ).get_result()

print(json.dumps(topic, indent=2))
```

### Update Topic
```py

rules_model = {
    'enabled': True,
    'event_type_filter': '$.notification_event_info.event_type == \'core_cert_manager\'',
    'notification_filter': '$.notification.findings[0].severity == \'SEVERE\'',
}

# Construct a dict representation of a TopicUpdateSourcesItem model
topic_update_sources_item_model = {
    'id': <source-id>,  # Event notifications service instance Source ID
    'rules': [rules_model],
}

description = "Updated Topic for GCM notifications"
name = 'Updated Admin Topic Compliance'
topic = event_notifications_service.replace_topic(
    <instance-id>, # Event notifications service instance GUID
    id=<topic-id>, # Event notifications service instance Topic ID
    name=<topic-update-name> # Event notifications service instance Topic Name
    description=<topic-update-description> # Event notifications service instance Topic description
    sources=[topic_update_sources_item_model]
)

print(json.dumps(topic, indent=2))

rulesModel := &eventnotificationsv1.Rules{
	Enabled:            core.BoolPtr(true),
	EventTypeFilter:    core.StringPtr("$.notification_event_info.event_type == 'core_cert_manager'"), # Add your event type filter here.
	NotificationFilter: core.StringPtr("$.notification.findings[0].severity == 'SEVERE'"), # Add your notification filter here.
}
```
### Delete Topic
```py
response = event_notifications_service.delete_topic(
      <instance-id>,
      id=<topic-id>,
  )

```
## Destinations 

### Create Destination

```py

destination_config_params_model = {
      'url': '<destination-config-url>',
      'verb': '<destination-config-verb>',
      'custom_headers': {'<header-key>': '<header-value>', },
      'sensitive_headers': ['<header-key>'],
  }

# Construct a dict representation of a DestinationConfig model
destination_config_model = {
    'params': destination_config_params_model,
}

destination = event_notifications_service.create_destination(
    <instance-id>,
    <destination-name>,
    type=<destination-type>,
    description=description,
    config=destination_config_model
).get_result()

print(json.dumps(destination, indent=2))
```

### List Destinations

```py
destination_list = event_notifications_service.list_destinations(
    <instance-id>,
).get_result()

print(json.dumps(destination_list, indent=2))
```

### Get Destination

```py
destination = event_notifications_service.get_destination(
      <instance-id>,       # Event notifications service instance GUID
      id=<destination-id>,    # Event notifications service instance Destination ID
  ).get_result()

print(json.dumps(destination, indent=2))
```

### Update Destination
```py
# Construct a dict representation of a DestinationConfigParamsWebhookDestinationConfig model
destination_config_params_model = {
    'url': '<destination-config-update-url>',
    'verb': '<destination-config-update-verb>',
    'sensitive_headers': ['<header-key>'],
}

# Construct a dict representation of a DestinationConfig model
destination_config_model = {
    'params': destination_config_params_model,
}

destination = event_notifications_service.update_destination(
    <instance-id>,      # Event notifications service instance GUID
    id=<destination-id>,   # Event notifications service instance Destination ID
    name=<destination-update-name>,
    description=<destination-update-description>,
    config=destination_config_model
).get_result()

print(json.dumps(destination, indent=2))

```
### Delete Destination

```py
response = event_notifications_service.delete_destination(
      <instance-id>,		# Event notifications service instance GUID
      id=<destination-id>,	# Event notifications service instance Destination ID
  )
```

## Subscriptions 

### Create Subscription

```py
#`While Creating Subscription use any of one option from webhook, or email`

subscription_create_attributes_model = {
    'signing_enabled': False,
}

            
subscription = event_notifications_service.create_subscription(
    <instance-id>,	# Event notifications service instance GUID
    name,
    <destination-id>, # Event notifications service instance Destination ID
    <topic-id> # Event notifications service instance Topic ID
    attributes=subscription_create_attributes_model,
    description=<subscription-description>
).get_result()

print(json.dumps(subscription, indent=2))
```

### List Subscriptions

```py
subscription_list = event_notifications_service.list_subscriptions(
     <instance-id>,	# Event notifications service instance GUID
 ).get_result()

print(json.dumps(subscription_list, indent=2))

```

### Get Subscription

```py
 subscription = event_notifications_service.get_subscription(
     <instance-id>,	# Event notifications service instance GUID
     id=<subscription-id>,	# Event notifications service instance Subscription ID
 ).get_result()

print(json.dumps(subscription, indent=2))
```

### Update Subscription
```py

 subscription_update_attributes_model = {
     'signing_enabled': True,
 }

 subscription = event_notifications_service.update_subscription(
     <instance-id>,	# Event notifications service instance GUID
     id=<subscription-id>,	# Event notifications service instance Subscription ID
     name=<subscription-update-name>,
     description=<subscription-update-description>,
     attributes=subscription_update_attributes_model
 ).get_result()

 print(json.dumps(subscription, indent=2))
```
### Delete Subscription
```py
response = event_notifications_service.delete_subscription(
     <instance-id>,	# Event notifications service instance GUID
     id=<subscription-id>,	# Event notifications service instance Subscriptions ID
 )
```
### Send Notifications


```py
notification_devices_model = {
            'fcm_devices': ['<fcm-device-ids>'],
            'apns_devices': ['<apns-device-ids>'],
            'user_ids': ['<user-ids>'],
            'tags': ['<tag-names>'],
            'platforms': ['<device-platforms>'],
          }

notification_apns_body_model = {
                "aps": {
                    "alert": "<notification-message>",
                    "badge": 5,
                },
            }
notification_fcm_body_model = {
                "notification": {
                    "title": "<notification-title>",
                    "body": "<notification-message>",
                },
            }

message_apns_headers = {
                "apns-collapse-id": "<apns-apns-collapse-id-value>",
            }

notification_id := "<notification-id>"
notification_subject := "<notification-subject>"
notification_severity := "<notification-severity>"
type_value := "<notification-type>"
notifications_source := "<notification-source>"


notification_response = event_notifications_service.send_notifications(
                instance_id,
                subject=notification_subject,
                severity=notification_severity,
                id=notification_id,
                source=notifications_source,
                en_source_id=source_id,
                type=type_value,
                time='<notification-time>',
                data={},
                push_to=notification_devices_model,
                message_fcm_body=notification_fcm_body_model,
                message_apns_body=notification_apns_body_model,
                message_apns_headers=message_apns_headers,
            ).get_result()

```

<details open>
<summary>Send Notifications Variables</summary>
<br>

- **FCM Target NotificationFcmDevices** - Set up the push notifications targets.
  - *UserIds* (Array of **String**) - Send notification to the specified userIds.
  - *FcmDevices* (Array of **String**) - Send notification to the list of specified devices.
  - *Tags* (Array of **String**) - Send notification to the devices that have subscribed to any of these tags.
  - *Platforms* (Array of **String**) - Send notification to the devices of the specified platforms. Pass 'G' for google (Android) devices. Pass 'A' for iOS  devices.
- **FCM MessageFcmBody** - Set payload specific to Android platform [Refer this FCM official [link](https://firebase.google.com/docs/cloud-messaging/http-server-ref#notification-payload-support)]. We support `notification` and `data` keys in FCM.
- **iOS MessageApnsBody** - Set payload specific to iOS platform [Refer this APNs official doc [link](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html)].
- **APNs MessageApnsHeaders** - Set headers required for the APNs message [Refer this APNs official [link](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns)(Table 1 Header fields for a POST request)].
- **Event Notifications SendNotificationsOptions** - Event Notifications Send Notifications method. 
  - *InstanceID* (**String**) - Event Notifications instance AppGUID. 
  - *Subject* (**String**) - Subject for the notifications. 
  - *Severity* (**String**) - Severity for the notifications. 
  - *ID* (**ID**) - ID for the notifications. 
  - *Source* (**String**) - Source of the notifications. 
  - *EnSourceID* (**String**) - Event Notifications instance Source ID. 
  - *Type* (**String**) - Type for the notifications. 
  - *Time* (**String**) - Time of the notifications. 
  - *Data* (**map[string]interface{}**) - Data for the notifications. Supported only for `Webhook` destination. 
  - *PushTo* (**NotificationFcmDevices**) - Targets for the FCM notifications. 
  - *MessageFcmBody* (**NotificationFcmBody**) - Message body for the FCM notifications. 
  - *MessageApnsBody* (**NotificationApnsBody**) - Message body for the APNs notifications. 
  - *MessageApnsHeaders* (**map[string]interface{}**) - Headers for the APNs notifications. 
  - *Datacontenttype* (**String**) - Data content type of the notifications. 
  - *Specversion* (**String**) - Spec version of the Event Notifications. Default value is `1.0`. 

</details>

## Set Environment

Find `event_notifications_v1.env.hide` in the repo and rename it to `event_notifications_v1.env`. After that add the values for,

- `EVENT_NOTIFICATIONS_URL` - Add the Event Notifications service instance Url.
- `EVENT_NOTIFICATIONS_APIKEY` - Add the Event Notifications service instance apikey.
- `EVENT_NOTIFICATIONS_GUID` - Add the Event Notifications service instance GUID.

Optional 
- `EVENT_NOTIFICATIONS_AUTH_URL` - Add the IAM url if you are using IBM test cloud.
- `EVENT_NOTIFICATIONS_FCM_KEY` - Add firebase server key for Android FCM destination.
- `EVENT_NOTIFICATIONS_FCM_ID` - Add firebase sender Id for Android FCM destination.

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](https://github.com/IBM/event-notifications-python-admin-sdk/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](LICENSE).
