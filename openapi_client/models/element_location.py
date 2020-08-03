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


class ElementLocation(object):
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
        'location': 'str',
        'uniform_path': 'str',
        'type': 'str'
    }

    attribute_map = {
        'location': 'location',
        'uniform_path': 'uniformPath',
        'type': 'type'
    }

    discriminator_value_class_map = {
        'QualifiedNameLocation': 'QualifiedNameLocation',
        'TextRegionLocation': 'TextRegionLocation'
    }

    def __init__(self, location=None, uniform_path=None, type=None, local_vars_configuration=None):  # noqa: E501
        """ElementLocation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._location = None
        self._uniform_path = None
        self._type = None
        self.discriminator = 'type'

        if location is not None:
            self.location = location
        if uniform_path is not None:
            self.uniform_path = uniform_path
        self.type = type

    @property
    def location(self):
        """Gets the location of this ElementLocation.  # noqa: E501


        :return: The location of this ElementLocation.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ElementLocation.


        :param location: The location of this ElementLocation.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def uniform_path(self):
        """Gets the uniform_path of this ElementLocation.  # noqa: E501


        :return: The uniform_path of this ElementLocation.  # noqa: E501
        :rtype: str
        """
        return self._uniform_path

    @uniform_path.setter
    def uniform_path(self, uniform_path):
        """Sets the uniform_path of this ElementLocation.


        :param uniform_path: The uniform_path of this ElementLocation.  # noqa: E501
        :type: str
        """

        self._uniform_path = uniform_path

    @property
    def type(self):
        """Gets the type of this ElementLocation.  # noqa: E501


        :return: The type of this ElementLocation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ElementLocation.


        :param type: The type of this ElementLocation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, ElementLocation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ElementLocation):
            return True

        return self.to_dict() != other.to_dict()