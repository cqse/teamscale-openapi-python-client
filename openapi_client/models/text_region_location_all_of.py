# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1.2
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from openapi_client.configuration import Configuration


class TextRegionLocationAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'raw_start_offset': 'int',
        'raw_end_offset': 'int',
        'raw_start_line': 'int',
        'raw_end_line': 'int',
        'type': 'str'
    }

    attribute_map = {
        'raw_start_offset': 'rawStartOffset',
        'raw_end_offset': 'rawEndOffset',
        'raw_start_line': 'rawStartLine',
        'raw_end_line': 'rawEndLine',
        'type': 'type'
    }

    def __init__(self, raw_start_offset=None, raw_end_offset=None, raw_start_line=None, raw_end_line=None, type=None, local_vars_configuration=None):  # noqa: E501
        """TextRegionLocationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._raw_start_offset = None
        self._raw_end_offset = None
        self._raw_start_line = None
        self._raw_end_line = None
        self._type = None
        self.discriminator = None

        if raw_start_offset is not None:
            self.raw_start_offset = raw_start_offset
        if raw_end_offset is not None:
            self.raw_end_offset = raw_end_offset
        if raw_start_line is not None:
            self.raw_start_line = raw_start_line
        if raw_end_line is not None:
            self.raw_end_line = raw_end_line
        if type is not None:
            self.type = type

    @property
    def raw_start_offset(self):
        """Gets the raw_start_offset of this TextRegionLocationAllOf.  # noqa: E501


        :return: The raw_start_offset of this TextRegionLocationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._raw_start_offset

    @raw_start_offset.setter
    def raw_start_offset(self, raw_start_offset):
        """Sets the raw_start_offset of this TextRegionLocationAllOf.


        :param raw_start_offset: The raw_start_offset of this TextRegionLocationAllOf.  # noqa: E501
        :type: int
        """

        self._raw_start_offset = raw_start_offset

    @property
    def raw_end_offset(self):
        """Gets the raw_end_offset of this TextRegionLocationAllOf.  # noqa: E501


        :return: The raw_end_offset of this TextRegionLocationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._raw_end_offset

    @raw_end_offset.setter
    def raw_end_offset(self, raw_end_offset):
        """Sets the raw_end_offset of this TextRegionLocationAllOf.


        :param raw_end_offset: The raw_end_offset of this TextRegionLocationAllOf.  # noqa: E501
        :type: int
        """

        self._raw_end_offset = raw_end_offset

    @property
    def raw_start_line(self):
        """Gets the raw_start_line of this TextRegionLocationAllOf.  # noqa: E501


        :return: The raw_start_line of this TextRegionLocationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._raw_start_line

    @raw_start_line.setter
    def raw_start_line(self, raw_start_line):
        """Sets the raw_start_line of this TextRegionLocationAllOf.


        :param raw_start_line: The raw_start_line of this TextRegionLocationAllOf.  # noqa: E501
        :type: int
        """

        self._raw_start_line = raw_start_line

    @property
    def raw_end_line(self):
        """Gets the raw_end_line of this TextRegionLocationAllOf.  # noqa: E501


        :return: The raw_end_line of this TextRegionLocationAllOf.  # noqa: E501
        :rtype: int
        """
        return self._raw_end_line

    @raw_end_line.setter
    def raw_end_line(self, raw_end_line):
        """Sets the raw_end_line of this TextRegionLocationAllOf.


        :param raw_end_line: The raw_end_line of this TextRegionLocationAllOf.  # noqa: E501
        :type: int
        """

        self._raw_end_line = raw_end_line

    @property
    def type(self):
        """Gets the type of this TextRegionLocationAllOf.  # noqa: E501


        :return: The type of this TextRegionLocationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TextRegionLocationAllOf.


        :param type: The type of this TextRegionLocationAllOf.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TextRegionLocationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextRegionLocationAllOf):
            return True

        return self.to_dict() != other.to_dict()
