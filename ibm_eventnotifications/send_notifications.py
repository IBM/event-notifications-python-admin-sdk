# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.46.1-a5569134-20220316-164819

from ibm_cloud_sdk_core import DetailedResponse
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string
from datetime import datetime
from enum import Enum
from typing import Dict, List
import json
from .common import get_sdk_headers

from ibm_eventnotifications.event_notifications_v1 import EventNotificationsV1

#########################
# Send Notifications
#########################

class Lights():
    """
    Allows setting the notification LED color on receiving push notification .

    :attr str led_argb: (optional) The color of the led. The hardware will do its
          best approximation.
    :attr int led_on_ms: (optional) The number of milliseconds for the LED to be on
          while it's flashing. The hardware will do its best approximation.
    :attr str led_off_ms: (optional) The number of milliseconds for the LED to be
          off while it's flashing. The hardware will do its best approximation.
    """

    def __init__(self,
                 *,
                 led_argb: str = None,
                 led_on_ms: int = None,
                 led_off_ms: str = None) -> None:
        """
        Initialize a Lights object.

        :param str led_argb: (optional) The color of the led. The hardware will do
               its best approximation.
        :param int led_on_ms: (optional) The number of milliseconds for the LED to
               be on while it's flashing. The hardware will do its best approximation.
        :param str led_off_ms: (optional) The number of milliseconds for the LED to
               be off while it's flashing. The hardware will do its best approximation.
        """
        self.led_argb = led_argb
        self.led_on_ms = led_on_ms
        self.led_off_ms = led_off_ms

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Lights':
        """Initialize a Lights object from a json dictionary."""
        args = {}
        if 'led_argb' in _dict:
            args['led_argb'] = _dict.get('led_argb')
        if 'led_on_ms' in _dict:
            args['led_on_ms'] = _dict.get('led_on_ms')
        if 'led_off_ms' in _dict:
            args['led_off_ms'] = _dict.get('led_off_ms')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Lights object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'led_argb') and self.led_argb is not None:
            _dict['led_argb'] = self.led_argb
        if hasattr(self, 'led_on_ms') and self.led_on_ms is not None:
            _dict['led_on_ms'] = self.led_on_ms
        if hasattr(self, 'led_off_ms') and self.led_off_ms is not None:
            _dict['led_off_ms'] = self.led_off_ms
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Lights object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Lights') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Lights') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NotificationAPNSBody():
    """
    Payload describing a APNs Notifications body.

    """

    def __init__(self,
                 **kwargs) -> None:
        """
        Initialize a NotificationAPNSBody object.

        :param **kwargs: (optional) Any additional properties.
        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['NotificationAPNSBodyMessageENData', 'NotificationAPNSBodyNotificationPayload']))
        raise Exception(msg)

class NotificationAPNSBodyMessageData():
    """
    Payload describing a apns notifications body message Data.

    :attr str alert: The notification message to be shown to the user.
    :attr int badge: (optional) The number to display as the badge of the
          application icon.
    :attr str interactive_category: (optional) The category identifier to be used
          for the interactive push notifications.
    :attr str ios_action_key: (optional) The title for the Action key.
    :attr object payload: (optional) Custom JSON payload that will be sent as part
          of the notification message.
    :attr str sound: (optional) The name of the sound file in the application
          bundle. The sound of this file is played as an alert.
    :attr str title_loc_key: (optional) The key to a title string in the
          Localizable.strings file for the current localization. The key string can be
          formatted with %@ and %n$@ specifiers to take the variables specified in the
          titleLocArgs array.
    :attr str loc_key: (optional) A key to an alert-message string in a
          Localizabl.strings file for the current localization (which is set by the
          userÃ¢â‚¬â„¢s language preference).
            The key string can be formatted with %@ and %n$@ specifiers to take the
          variables specified in the locArgs array.
    :attr str launch_image: (optional) The filename of an image file in the app
          bundle, with or without the filename extension. The image is used as the launch
          image when users tap the action button or move the action slider.
    :attr List[str] title_loc_args: (optional) Variable string values to appear in
          place of the format specifiers in title-loc-key.
    :attr List[str] loc_args: (optional) Variable string values to appear in place
          of the format specifiers in locKey.
    :attr str title: (optional) The title of Rich Push notifications (Supported only
          on iOS 10 and above).
    :attr str subtitle: (optional) The subtitle of the Rich Notifications.(Supported
          only on iOS 10 and above).
    :attr str attachment_url: (optional) The link to the iOS notifications media
          (video, audio, GIF, images - Supported only on iOS 10 and above).
    :attr str type: (optional)
    :attr str apns_collapse_id: (optional) Multiple notifications with the same
          collapse identifier are displayed to the user as a single notification.
    :attr str apns_thread_id: (optional) An app-specific identifier for grouping
          related notifications. This value corresponds to the threadIdentifier property
          in the UNNotificationContent object.
    :attr str apns_group_summary_arg: (optional) The string the notification adds to
          the category's summary format string.
    :attr int apns_group_summary_arg_count: (optional) The number of items the
          notification adds to the category's summary format string.
    """

    def __init__(self,
                 alert: str,
                 *,
                 badge: int = None,
                 interactive_category: str = None,
                 ios_action_key: str = None,
                 payload: object = None,
                 sound: str = None,
                 title_loc_key: str = None,
                 loc_key: str = None,
                 launch_image: str = None,
                 title_loc_args: List[str] = None,
                 loc_args: List[str] = None,
                 title: str = None,
                 subtitle: str = None,
                 attachment_url: str = None,
                 type: str = None,
                 apns_collapse_id: str = None,
                 apns_thread_id: str = None,
                 apns_group_summary_arg: str = None,
                 apns_group_summary_arg_count: int = None) -> None:
        """
        Initialize a NotificationAPNSBodyMessageData object.

        :param str alert: The notification message to be shown to the user.
        :param int badge: (optional) The number to display as the badge of the
               application icon.
        :param str interactive_category: (optional) The category identifier to be
               used for the interactive push notifications.
        :param str ios_action_key: (optional) The title for the Action key.
        :param object payload: (optional) Custom JSON payload that will be sent as
               part of the notification message.
        :param str sound: (optional) The name of the sound file in the application
               bundle. The sound of this file is played as an alert.
        :param str title_loc_key: (optional) The key to a title string in the
               Localizable.strings file for the current localization. The key string can
               be formatted with %@ and %n$@ specifiers to take the variables specified in
               the titleLocArgs array.
        :param str loc_key: (optional) A key to an alert-message string in a
               Localizabl.strings file for the current localization (which is set by the
               userÃ¢â‚¬â„¢s language preference).
                 The key string can be formatted with %@ and %n$@ specifiers to take the
               variables specified in the locArgs array.
        :param str launch_image: (optional) The filename of an image file in the
               app bundle, with or without the filename extension. The image is used as
               the launch image when users tap the action button or move the action
               slider.
        :param List[str] title_loc_args: (optional) Variable string values to
               appear in place of the format specifiers in title-loc-key.
        :param List[str] loc_args: (optional) Variable string values to appear in
               place of the format specifiers in locKey.
        :param str title: (optional) The title of Rich Push notifications
               (Supported only on iOS 10 and above).
        :param str subtitle: (optional) The subtitle of the Rich
               Notifications.(Supported only on iOS 10 and above).
        :param str attachment_url: (optional) The link to the iOS notifications
               media (video, audio, GIF, images - Supported only on iOS 10 and above).
        :param str type: (optional)
        :param str apns_collapse_id: (optional) Multiple notifications with the
               same collapse identifier are displayed to the user as a single
               notification.
        :param str apns_thread_id: (optional) An app-specific identifier for
               grouping related notifications. This value corresponds to the
               threadIdentifier property in the UNNotificationContent object.
        :param str apns_group_summary_arg: (optional) The string the notification
               adds to the category's summary format string.
        :param int apns_group_summary_arg_count: (optional) The number of items the
               notification adds to the category's summary format string.
        """
        self.alert = alert
        self.badge = badge
        self.interactive_category = interactive_category
        self.ios_action_key = ios_action_key
        self.payload = payload
        self.sound = sound
        self.title_loc_key = title_loc_key
        self.loc_key = loc_key
        self.launch_image = launch_image
        self.title_loc_args = title_loc_args
        self.loc_args = loc_args
        self.title = title
        self.subtitle = subtitle
        self.attachment_url = attachment_url
        self.type = type
        self.apns_collapse_id = apns_collapse_id
        self.apns_thread_id = apns_thread_id
        self.apns_group_summary_arg = apns_group_summary_arg
        self.apns_group_summary_arg_count = apns_group_summary_arg_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationAPNSBodyMessageData':
        """Initialize a NotificationAPNSBodyMessageData object from a json dictionary."""
        args = {}
        if 'alert' in _dict:
            args['alert'] = _dict.get('alert')
        else:
            raise ValueError('Required property \'alert\' not present in NotificationAPNSBodyMessageData JSON')
        if 'badge' in _dict:
            args['badge'] = _dict.get('badge')
        if 'interactiveCategory' in _dict:
            args['interactive_category'] = _dict.get('interactiveCategory')
        if 'iosActionKey' in _dict:
            args['ios_action_key'] = _dict.get('iosActionKey')
        if 'payload' in _dict:
            args['payload'] = _dict.get('payload')
        if 'sound' in _dict:
            args['sound'] = _dict.get('sound')
        if 'titleLocKey' in _dict:
            args['title_loc_key'] = _dict.get('titleLocKey')
        if 'locKey' in _dict:
            args['loc_key'] = _dict.get('locKey')
        if 'launchImage' in _dict:
            args['launch_image'] = _dict.get('launchImage')
        if 'titleLocArgs' in _dict:
            args['title_loc_args'] = _dict.get('titleLocArgs')
        if 'locArgs' in _dict:
            args['loc_args'] = _dict.get('locArgs')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'subtitle' in _dict:
            args['subtitle'] = _dict.get('subtitle')
        if 'attachmentUrl' in _dict:
            args['attachment_url'] = _dict.get('attachmentUrl')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'apnsCollapseId' in _dict:
            args['apns_collapse_id'] = _dict.get('apnsCollapseId')
        if 'apnsThreadId' in _dict:
            args['apns_thread_id'] = _dict.get('apnsThreadId')
        if 'apnsGroupSummaryArg' in _dict:
            args['apns_group_summary_arg'] = _dict.get('apnsGroupSummaryArg')
        if 'apnsGroupSummaryArgCount' in _dict:
            args['apns_group_summary_arg_count'] = _dict.get('apnsGroupSummaryArgCount')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationAPNSBodyMessageData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'alert') and self.alert is not None:
            _dict['alert'] = self.alert
        if hasattr(self, 'badge') and self.badge is not None:
            _dict['badge'] = self.badge
        if hasattr(self, 'interactive_category') and self.interactive_category is not None:
            _dict['interactiveCategory'] = self.interactive_category
        if hasattr(self, 'ios_action_key') and self.ios_action_key is not None:
            _dict['iosActionKey'] = self.ios_action_key
        if hasattr(self, 'payload') and self.payload is not None:
            _dict['payload'] = self.payload
        if hasattr(self, 'sound') and self.sound is not None:
            _dict['sound'] = self.sound
        if hasattr(self, 'title_loc_key') and self.title_loc_key is not None:
            _dict['titleLocKey'] = self.title_loc_key
        if hasattr(self, 'loc_key') and self.loc_key is not None:
            _dict['locKey'] = self.loc_key
        if hasattr(self, 'launch_image') and self.launch_image is not None:
            _dict['launchImage'] = self.launch_image
        if hasattr(self, 'title_loc_args') and self.title_loc_args is not None:
            _dict['titleLocArgs'] = self.title_loc_args
        if hasattr(self, 'loc_args') and self.loc_args is not None:
            _dict['locArgs'] = self.loc_args
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'subtitle') and self.subtitle is not None:
            _dict['subtitle'] = self.subtitle
        if hasattr(self, 'attachment_url') and self.attachment_url is not None:
            _dict['attachmentUrl'] = self.attachment_url
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'apns_collapse_id') and self.apns_collapse_id is not None:
            _dict['apnsCollapseId'] = self.apns_collapse_id
        if hasattr(self, 'apns_thread_id') and self.apns_thread_id is not None:
            _dict['apnsThreadId'] = self.apns_thread_id
        if hasattr(self, 'apns_group_summary_arg') and self.apns_group_summary_arg is not None:
            _dict['apnsGroupSummaryArg'] = self.apns_group_summary_arg
        if hasattr(self, 'apns_group_summary_arg_count') and self.apns_group_summary_arg_count is not None:
            _dict['apnsGroupSummaryArgCount'] = self.apns_group_summary_arg_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NotificationAPNSBodyMessageData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationAPNSBodyMessageData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationAPNSBodyMessageData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        type.
        """
        DEFAULT = 'DEFAULT'
        MIXED = 'MIXED'
        SILENT = 'SILENT'


class NotificationDevices():
    """
    Payload describing a FCM Notifications targets.

    :attr List[str] fcm_devices: (optional) List of FCM deviceIds.
    :attr List[str] apns_devices: (optional) List of APNs deviceIds.
    :attr List[str] user_ids: (optional) List of userIds.
    :attr List[str] tags: (optional) List of tags.
    :attr List[str] platforms: (optional) List of platforms.
    """

    def __init__(self,
                 *,
                 fcm_devices: List[str] = None,
                 apns_devices: List[str] = None,
                 user_ids: List[str] = None,
                 tags: List[str] = None,
                 platforms: List[str] = None) -> None:
        """
        Initialize a NotificationDevices object.

        :param List[str] fcm_devices: (optional) List of FCM deviceIds.
        :param List[str] apns_devices: (optional) List of APNs deviceIds.
        :param List[str] user_ids: (optional) List of userIds.
        :param List[str] tags: (optional) List of tags.
        :param List[str] platforms: (optional) List of platforms.
        """
        self.fcm_devices = fcm_devices
        self.apns_devices = apns_devices
        self.user_ids = user_ids
        self.tags = tags
        self.platforms = platforms

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationDevices':
        """Initialize a NotificationDevices object from a json dictionary."""
        args = {}
        if 'fcm_devices' in _dict:
            args['fcm_devices'] = _dict.get('fcm_devices')
        if 'apns_devices' in _dict:
            args['apns_devices'] = _dict.get('apns_devices')
        if 'user_ids' in _dict:
            args['user_ids'] = _dict.get('user_ids')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'platforms' in _dict:
            args['platforms'] = _dict.get('platforms')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationDevices object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'fcm_devices') and self.fcm_devices is not None:
            _dict['fcm_devices'] = self.fcm_devices
        if hasattr(self, 'apns_devices') and self.apns_devices is not None:
            _dict['apns_devices'] = self.apns_devices
        if hasattr(self, 'user_ids') and self.user_ids is not None:
            _dict['user_ids'] = self.user_ids
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'platforms') and self.platforms is not None:
            _dict['platforms'] = self.platforms
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NotificationDevices object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationDevices') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationDevices') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NotificationFCMBody():
    """
    NotificationFCMBody.

    """

    def __init__(self,
                 **kwargs) -> None:
        """
        Initialize a NotificationFCMBody object.

        :param **kwargs: (optional) Any additional properties.
        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
                  ", ".join(['NotificationFCMBodyMessageENData', 'NotificationFCMBodyNotificationPayload']))
        raise Exception(msg)

class NotificationFCMBodyMessageData():
    """
    Payload describing a fcm notifications body message Data.

    :attr str alert: The notification message to be shown to the user.
    :attr str collapse_key: (optional) Dozed devices to display only the latest
          notification and discard old low priority notifications.
    :attr str interactive_category: (optional) The category identifier to be used
          for the interactive push notifications.
    :attr str icon: (optional) Specify the name of the icon to be displayed for the
          notification. Make sure the icon is already packaged with the client
          application.
    :attr bool delay_while_idle: (optional) When this parameter is set to true, it
          indicates that the
            message should not be sent until the device becomes active.
    :attr bool sync: (optional) Device group messaging makes it possible for every
          app instance in a group to reflect the latest messaging state.
    :attr str visibility: (optional) private/public - Visibility of this
          notification, which affects how and when the notifications are revealed on a
          secure locked screen.
    :attr str redact: (optional) Content specified will show up on a secure locked
          screen on the device when visibility is set to Private.
    :attr dict payload: (optional) Custom JSON payload that will be sent as part of
          the notification message.
    :attr str priority: (optional) A string value that indicates the priority of
          this notification. Allowed values are 'max', 'high', 'default', 'low' and 'min'.
          High/Max priority notifications along with 'sound' field may be used for Heads
          up notification in Android 5.0 or higher.sampleval='low'.
    :attr str sound: (optional) The sound file (on device) that will be attempted to
          play when the notification arrives on the device.
    :attr int time_to_live: (optional) This parameter specifies how long (in
          seconds) the message
            should be kept in GCM storage if the device is offline.
    :attr Lights lights: (optional) Allows setting the notification LED color on
          receiving push notification .
    :attr str android_title: (optional) The title of Rich Push notifications.
    :attr str group_id: (optional) Set this notification to be part of a group of
          notifications sharing the same key. Grouped notifications may display in a
          cluster or stack on devices which support such rendering.
    :attr Style style: (optional) Options to specify for Android expandable
          notifications. The types of expandable notifications are picture_notification,
          bigtext_notification, inbox_notification.
    :attr str type: (optional) Notification type.
    """

    def __init__(self,
                 alert: str,
                 *,
                 collapse_key: str = None,
                 interactive_category: str = None,
                 icon: str = None,
                 delay_while_idle: bool = None,
                 sync: bool = None,
                 visibility: str = None,
                 redact: str = None,
                 payload: dict = None,
                 priority: str = None,
                 sound: str = None,
                 time_to_live: int = None,
                 lights: 'Lights' = None,
                 android_title: str = None,
                 group_id: str = None,
                 style: 'Style' = None,
                 type: str = None) -> None:
        """
        Initialize a NotificationFCMBodyMessageData object.

        :param str alert: The notification message to be shown to the user.
        :param str collapse_key: (optional) Dozed devices to display only the
               latest notification and discard old low priority notifications.
        :param str interactive_category: (optional) The category identifier to be
               used for the interactive push notifications.
        :param str icon: (optional) Specify the name of the icon to be displayed
               for the notification. Make sure the icon is already packaged with the
               client application.
        :param bool delay_while_idle: (optional) When this parameter is set to
               true, it indicates that the
                 message should not be sent until the device becomes active.
        :param bool sync: (optional) Device group messaging makes it possible for
               every app instance in a group to reflect the latest messaging state.
        :param str visibility: (optional) private/public - Visibility of this
               notification, which affects how and when the notifications are revealed on
               a secure locked screen.
        :param str redact: (optional) Content specified will show up on a secure
               locked screen on the device when visibility is set to Private.
        :param dict payload: (optional) Custom JSON payload that will be sent as
               part of the notification message.
        :param str priority: (optional) A string value that indicates the priority
               of this notification. Allowed values are 'max', 'high', 'default', 'low'
               and 'min'. High/Max priority notifications along with 'sound' field may be
               used for Heads up notification in Android 5.0 or higher.sampleval='low'.
        :param str sound: (optional) The sound file (on device) that will be
               attempted to play when the notification arrives on the device.
        :param int time_to_live: (optional) This parameter specifies how long (in
               seconds) the message
                 should be kept in GCM storage if the device is offline.
        :param Lights lights: (optional) Allows setting the notification LED color
               on receiving push notification .
        :param str android_title: (optional) The title of Rich Push notifications.
        :param str group_id: (optional) Set this notification to be part of a group
               of notifications sharing the same key. Grouped notifications may display in
               a cluster or stack on devices which support such rendering.
        :param Style style: (optional) Options to specify for Android expandable
               notifications. The types of expandable notifications are
               picture_notification, bigtext_notification, inbox_notification.
        :param str type: (optional) Notification type.
        """
        self.alert = alert
        self.collapse_key = collapse_key
        self.interactive_category = interactive_category
        self.icon = icon
        self.delay_while_idle = delay_while_idle
        self.sync = sync
        self.visibility = visibility
        self.redact = redact
        self.payload = payload
        self.priority = priority
        self.sound = sound
        self.time_to_live = time_to_live
        self.lights = lights
        self.android_title = android_title
        self.group_id = group_id
        self.style = style
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationFCMBodyMessageData':
        """Initialize a NotificationFCMBodyMessageData object from a json dictionary."""
        args = {}
        if 'alert' in _dict:
            args['alert'] = _dict.get('alert')
        else:
            raise ValueError('Required property \'alert\' not present in NotificationFCMBodyMessageData JSON')
        if 'collapse_key' in _dict:
            args['collapse_key'] = _dict.get('collapse_key')
        if 'interactive_category' in _dict:
            args['interactive_category'] = _dict.get('interactive_category')
        if 'icon' in _dict:
            args['icon'] = _dict.get('icon')
        if 'delay_while_idle' in _dict:
            args['delay_while_idle'] = _dict.get('delay_while_idle')
        if 'sync' in _dict:
            args['sync'] = _dict.get('sync')
        if 'visibility' in _dict:
            args['visibility'] = _dict.get('visibility')
        if 'redact' in _dict:
            args['redact'] = _dict.get('redact')
        if 'payload' in _dict:
            args['payload'] = _dict.get('payload')
        if 'priority' in _dict:
            args['priority'] = _dict.get('priority')
        if 'sound' in _dict:
            args['sound'] = _dict.get('sound')
        if 'time_to_live' in _dict:
            args['time_to_live'] = _dict.get('time_to_live')
        if 'lights' in _dict:
            args['lights'] = Lights.from_dict(_dict.get('lights'))
        if 'android_title' in _dict:
            args['android_title'] = _dict.get('android_title')
        if 'group_id' in _dict:
            args['group_id'] = _dict.get('group_id')
        if 'style' in _dict:
            args['style'] = Style.from_dict(_dict.get('style'))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationFCMBodyMessageData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'alert') and self.alert is not None:
            _dict['alert'] = self.alert
        if hasattr(self, 'collapse_key') and self.collapse_key is not None:
            _dict['collapse_key'] = self.collapse_key
        if hasattr(self, 'interactive_category') and self.interactive_category is not None:
            _dict['interactive_category'] = self.interactive_category
        if hasattr(self, 'icon') and self.icon is not None:
            _dict['icon'] = self.icon
        if hasattr(self, 'delay_while_idle') and self.delay_while_idle is not None:
            _dict['delay_while_idle'] = self.delay_while_idle
        if hasattr(self, 'sync') and self.sync is not None:
            _dict['sync'] = self.sync
        if hasattr(self, 'visibility') and self.visibility is not None:
            _dict['visibility'] = self.visibility
        if hasattr(self, 'redact') and self.redact is not None:
            _dict['redact'] = self.redact
        if hasattr(self, 'payload') and self.payload is not None:
            _dict['payload'] = self.payload
        if hasattr(self, 'priority') and self.priority is not None:
            _dict['priority'] = self.priority
        if hasattr(self, 'sound') and self.sound is not None:
            _dict['sound'] = self.sound
        if hasattr(self, 'time_to_live') and self.time_to_live is not None:
            _dict['time_to_live'] = self.time_to_live
        if hasattr(self, 'lights') and self.lights is not None:
            _dict['lights'] = self.lights.to_dict()
        if hasattr(self, 'android_title') and self.android_title is not None:
            _dict['android_title'] = self.android_title
        if hasattr(self, 'group_id') and self.group_id is not None:
            _dict['group_id'] = self.group_id
        if hasattr(self, 'style') and self.style is not None:
            _dict['style'] = self.style.to_dict()
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this NotificationFCMBodyMessageData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationFCMBodyMessageData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationFCMBodyMessageData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Notification type.
        """
        DEFAULT = 'DEFAULT'
        SILENT = 'SILENT'

class Style():
    """
    Options to specify for Android expandable notifications. The types of expandable
    notifications are picture_notification, bigtext_notification, inbox_notification.

    :attr str type: (optional) Specifies the type of expandable notifications.  The
          possible values are bigtext_notification, picture_notification,
          inbox_notification.
    :attr str title: (optional) Specifies the title of the notification.  The title
          is displayed when the notification is expanded.  Title must be specified for all
          three expandable notification.
    :attr str url: (optional) An URL from which the picture has to be obtained for
          the notification.  Must be specified for picture_notification.
    :attr str text: (optional) The big text that needs to be displayed on expanding
          a bigtext_notification.  Must be specified for bigtext_notification.
    :attr List[str] lines: (optional) An array of strings that is to be displayed in
          inbox style for inbox_notification.  Must be specified for inbox_notification.
    """

    # The set of defined properties for the class
    _properties = frozenset(['type', 'title', 'url', 'text', 'lines'])

    def __init__(self,
                 *,
                 type: str = None,
                 title: str = None,
                 url: str = None,
                 text: str = None,
                 lines: List[str] = None,
                 **kwargs) -> None:
        """
        Initialize a Style object.

        :param str type: (optional) Specifies the type of expandable notifications.
                The possible values are bigtext_notification, picture_notification,
               inbox_notification.
        :param str title: (optional) Specifies the title of the notification.  The
               title is displayed when the notification is expanded.  Title must be
               specified for all three expandable notification.
        :param str url: (optional) An URL from which the picture has to be obtained
               for the notification.  Must be specified for picture_notification.
        :param str text: (optional) The big text that needs to be displayed on
               expanding a bigtext_notification.  Must be specified for
               bigtext_notification.
        :param List[str] lines: (optional) An array of strings that is to be
               displayed in inbox style for inbox_notification.  Must be specified for
               inbox_notification.
        :param **kwargs: (optional) Any additional properties.
        """
        self.type = type
        self.title = title
        self.url = url
        self.text = text
        self.lines = lines
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Style':
        """Initialize a Style object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'lines' in _dict:
            args['lines'] = _dict.get('lines')
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Style object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'lines') and self.lines is not None:
            _dict['lines'] = self.lines
        for _key in [k for k in vars(self).keys() if k not in Style._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of Style"""
        _dict = {}

        for _key in [k for k in vars(self).keys() if k not in Style._properties]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of Style"""
        for _key in [k for k in vars(self).keys() if k not in Style._properties]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            if _key not in Style._properties:
                setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this Style object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Style') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Style') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NotificationResponse():
    """
    Payload describing a notifications response.

    :attr str notification_id: Notification ID.
    """

    # The set of defined properties for the class
    _properties = frozenset(['notification_id'])

    def __init__(self,
                 notification_id: str,
                 **kwargs) -> None:
        """
        Initialize a NotificationResponse object.

        :param str notification_id: Notification ID.
        :param **kwargs: (optional) Any additional properties.
        """
        self.notification_id = notification_id
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationResponse':
        """Initialize a NotificationResponse object from a json dictionary."""
        args = {}
        if 'notification_id' in _dict:
            args['notification_id'] = _dict.get('notification_id')
        else:
            raise ValueError('Required property \'notification_id\' not present in NotificationResponse JSON')
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'notification_id') and self.notification_id is not None:
            _dict['notification_id'] = self.notification_id
        for _key in [k for k in vars(self).keys() if k not in NotificationResponse._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of NotificationResponse"""
        _dict = {}

        for _key in [k for k in vars(self).keys() if k not in NotificationResponse._properties]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of NotificationResponse"""
        for _key in [k for k in vars(self).keys() if k not in NotificationResponse._properties]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            if _key not in NotificationResponse._properties:
                setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this NotificationResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NotificationAPNSBodyMessageENData(NotificationAPNSBody):
    """
    Payload describing a fcm notifications body message.

    :attr NotificationAPNSBodyMessageData en_data: (optional) Payload describing a
          apns notifications body message Data.
    """

    # The set of defined properties for the class
    _properties = frozenset(['en_data'])

    def __init__(self,
                 *,
                 en_data: 'NotificationAPNSBodyMessageData' = None,
                 **kwargs) -> None:
        """
        Initialize a NotificationAPNSBodyMessageENData object.

        :param NotificationAPNSBodyMessageData en_data: (optional) Payload
               describing a apns notifications body message Data.
        :param **kwargs: (optional) Any additional properties.
        """
        # pylint: disable=super-init-not-called
        self.en_data = en_data
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationAPNSBodyMessageENData':
        """Initialize a NotificationAPNSBodyMessageENData object from a json dictionary."""
        args = {}
        if 'en_data' in _dict:
            args['en_data'] = NotificationAPNSBodyMessageData.from_dict(_dict.get('en_data'))
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationAPNSBodyMessageENData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'en_data') and self.en_data is not None:
            _dict['en_data'] = self.en_data.to_dict()
        for _key in [k for k in vars(self).keys() if k not in NotificationAPNSBodyMessageENData._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of NotificationAPNSBodyMessageENData"""
        _dict = {}

        for _key in [k for k in vars(self).keys() if k not in NotificationAPNSBodyMessageENData._properties]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of NotificationAPNSBodyMessageENData"""
        for _key in [k for k in vars(self).keys() if k not in NotificationAPNSBodyMessageENData._properties]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            if _key not in NotificationAPNSBodyMessageENData._properties:
                setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this NotificationAPNSBodyMessageENData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationAPNSBodyMessageENData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationAPNSBodyMessageENData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NotificationAPNSBodyNotificationPayload(NotificationAPNSBody):
    """
    The attributes for an FCM/APNs notification.

    """

    def __init__(self,
                 **kwargs) -> None:
        """
        Initialize a NotificationAPNSBodyNotificationPayload object.

        :param **kwargs: (optional) Any additional properties.
        """
        # pylint: disable=super-init-not-called
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationAPNSBodyNotificationPayload':
        """Initialize a NotificationAPNSBodyNotificationPayload object from a json dictionary."""
        return cls(**_dict)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationAPNSBodyNotificationPayload object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        return vars(self)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of NotificationAPNSBodyNotificationPayload"""
        _dict = {}

        for _key in [k for k in vars(self).keys()]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of NotificationAPNSBodyNotificationPayload"""
        for _key in [k for k in vars(self).keys()]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this NotificationAPNSBodyNotificationPayload object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationAPNSBodyNotificationPayload') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationAPNSBodyNotificationPayload') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NotificationFCMBodyMessageENData(NotificationFCMBody):
    """
    Payload describing a fcm notifications body message.

    :attr NotificationFCMBodyMessageData en_data: (optional) Payload describing a
          fcm notifications body message Data.
    """

    # The set of defined properties for the class
    _properties = frozenset(['en_data'])

    def __init__(self,
                 *,
                 en_data: 'NotificationFCMBodyMessageData' = None,
                 **kwargs) -> None:
        """
        Initialize a NotificationFCMBodyMessageENData object.

        :param NotificationFCMBodyMessageData en_data: (optional) Payload
               describing a fcm notifications body message Data.
        :param **kwargs: (optional) Any additional properties.
        """
        # pylint: disable=super-init-not-called
        self.en_data = en_data
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationFCMBodyMessageENData':
        """Initialize a NotificationFCMBodyMessageENData object from a json dictionary."""
        args = {}
        if 'en_data' in _dict:
            args['en_data'] = NotificationFCMBodyMessageData.from_dict(_dict.get('en_data'))
        args.update({k:v for (k, v) in _dict.items() if k not in cls._properties})
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationFCMBodyMessageENData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'en_data') and self.en_data is not None:
            _dict['en_data'] = self.en_data.to_dict()
        for _key in [k for k in vars(self).keys() if k not in NotificationFCMBodyMessageENData._properties]:
            if getattr(self, _key, None) is not None:
                _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of NotificationFCMBodyMessageENData"""
        _dict = {}

        for _key in [k for k in vars(self).keys() if k not in NotificationFCMBodyMessageENData._properties]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of NotificationFCMBodyMessageENData"""
        for _key in [k for k in vars(self).keys() if k not in NotificationFCMBodyMessageENData._properties]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            if _key not in NotificationFCMBodyMessageENData._properties:
                setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this NotificationFCMBodyMessageENData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationFCMBodyMessageENData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationFCMBodyMessageENData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class NotificationFCMBodyNotificationPayload(NotificationFCMBody):
    """
    The attributes for an FCM/APNs notification.

    """

    def __init__(self,
                 **kwargs) -> None:
        """
        Initialize a NotificationFCMBodyNotificationPayload object.

        :param **kwargs: (optional) Any additional properties.
        """
        # pylint: disable=super-init-not-called
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'NotificationFCMBodyNotificationPayload':
        """Initialize a NotificationFCMBodyNotificationPayload object from a json dictionary."""
        return cls(**_dict)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a NotificationFCMBodyNotificationPayload object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        return vars(self)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of NotificationFCMBodyNotificationPayload"""
        _dict = {}

        for _key in [k for k in vars(self).keys()]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of NotificationFCMBodyNotificationPayload"""
        for _key in [k for k in vars(self).keys()]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            setattr(self, _key, _value)

    def __str__(self) -> str:
        """Return a `str` version of this NotificationFCMBodyNotificationPayload object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'NotificationFCMBodyNotificationPayload') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'NotificationFCMBodyNotificationPayload') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

def send_notifications(self,
                       instance_id: str,
                       ibmenseverity: str,
                       ibmensourceid: str,
                       subject: str,
                       id: str,
                       source: str,
                       type: str,
                       time: datetime,
                       *,
                       data: dict = None,
                       ibmenfcmbody: 'NotificationFCMBody' = None,
                       ibmenapnsbody: 'NotificationAPNSBody' = None,
                       ibmenpushto: 'NotificationDevices' = None,
                       ibmenapnsheaders: dict = None,
                       datacontenttype: str = None,
                       specversion: str = None,
                       **kwargs
                       ) -> DetailedResponse:
    """
    Send a notification.

    Send a notification.

    :param str instance_id: Unique identifier for IBM Cloud Event Notifications
           instance.
    :param str ibmenseverity: The Notifications id.
    :param str ibmensourceid: The Event Notifications source id.
    :param str subject: The Notifications subject.
    :param str id: The Notifications id.
    :param str source: The source of Notifications.
    :param str type: The Notifications type.
    :param datetime time: The Notifications time.
    :param dict data: (optional) The Notifications data for webhook.
    :param NotificationFCMBody ibmenfcmbody: (optional)
    :param NotificationAPNSBody ibmenapnsbody: (optional) Payload describing a
           APNs Notifications body.
    :param NotificationDevices ibmenpushto: (optional) Payload describing a FCM
           Notifications targets.
    :param dict ibmenapnsheaders: (optional) The attributes for an FCM/APNs
           notification.
    :param str datacontenttype: (optional) The Notifications content type.
    :param str specversion: (optional) The Notifications specversion.
    :param dict headers: A `dict` containing the request headers
    :return: A `DetailedResponse` containing the result, headers and HTTP status code.
    :rtype: DetailedResponse with `dict` result representing a `NotificationResponse` object
    """

    if instance_id is None:
        raise ValueError('instance_id must be provided')
    if ibmenseverity is None:
        raise ValueError('ibmenseverity must be provided')
    if ibmensourceid is None:
        raise ValueError('ibmensourceid must be provided')
    if subject is None:
        raise ValueError('subject must be provided')
    if id is None:
        raise ValueError('id must be provided')
    if source is None:
        raise ValueError('source must be provided')
    if type is None:
        raise ValueError('type must be provided')
    if time is None:
        raise ValueError('time must be provided')
    time = datetime_to_string(time)
    if ibmenfcmbody is not None:
        ibmenfcmbody = json.dumps(convert_model(ibmenfcmbody))
    if ibmenapnsbody is not None:
        ibmenapnsbody = json.dumps(convert_model(ibmenapnsbody))
    if ibmenpushto is not None:
        ibmenpushto = json.dumps(convert_model(ibmenpushto))
    if ibmenapnsheaders is not None:
        ibmenapnsheaders = json.dumps(convert_model(ibmenapnsheaders))
    headers = {}
    sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                  service_version='V1',
                                  operation_id='send_notifications')
    headers.update(sdk_headers)

    data = {
        'ibmenseverity': ibmenseverity,
        'ibmensourceid': ibmensourceid,
        'subject': subject,
        'id': id,
        'source': source,
        'type': type,
        'time': time,
        'data': data,
        'ibmenfcmbody': ibmenfcmbody,
        'ibmenapnsbody': ibmenapnsbody,
        'ibmenpushto': ibmenpushto,
        'ibmenapnsheaders': ibmenapnsheaders,
        'datacontenttype': 'application/json',
        'specversion': '1.0'
    }
    data = {k: v for (k, v) in data.items() if v is not None}
    data = json.dumps(data)
    headers['content-type'] = 'application/json'

    if 'headers' in kwargs:
        headers.update(kwargs.get('headers'))
    headers['Accept'] = 'application/json'

    path_param_keys = ['instance_id']
    path_param_values = self.encode_path_vars(instance_id)
    path_param_dict = dict(zip(path_param_keys, path_param_values))
    url = '/v1/instances/{instance_id}/notifications'.format(**path_param_dict)
    request = self.prepare_request(method='POST',
                                   url=url,
                                   headers=headers,
                                   data=data)

    response = self.send(request, **kwargs)
    return response


EventNotificationsV1.send_notifications = send_notifications
