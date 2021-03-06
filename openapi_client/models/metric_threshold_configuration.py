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


class MetricThresholdConfiguration(object):
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
        'name': 'str',
        'options': 'dict(str, str)',
        'base_configuration_name': 'str',
        'metric_threshold_group_list': 'list[MetricThresholdGroup]'
    }

    attribute_map = {
        'name': 'name',
        'options': 'options',
        'base_configuration_name': 'baseConfigurationName',
        'metric_threshold_group_list': 'metricThresholdGroupList'
    }

    def __init__(self, name=None, options=None, base_configuration_name=None, metric_threshold_group_list=None, local_vars_configuration=None):  # noqa: E501
        """MetricThresholdConfiguration - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._options = None
        self._base_configuration_name = None
        self._metric_threshold_group_list = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if base_configuration_name is not None:
            self.base_configuration_name = base_configuration_name
        if metric_threshold_group_list is not None:
            self.metric_threshold_group_list = metric_threshold_group_list

    @property
    def name(self):
        """Gets the name of this MetricThresholdConfiguration.  # noqa: E501


        :return: The name of this MetricThresholdConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricThresholdConfiguration.


        :param name: The name of this MetricThresholdConfiguration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this MetricThresholdConfiguration.  # noqa: E501


        :return: The options of this MetricThresholdConfiguration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this MetricThresholdConfiguration.


        :param options: The options of this MetricThresholdConfiguration.  # noqa: E501
        :type: dict(str, str)
        """

        self._options = options

    @property
    def base_configuration_name(self):
        """Gets the base_configuration_name of this MetricThresholdConfiguration.  # noqa: E501


        :return: The base_configuration_name of this MetricThresholdConfiguration.  # noqa: E501
        :rtype: str
        """
        return self._base_configuration_name

    @base_configuration_name.setter
    def base_configuration_name(self, base_configuration_name):
        """Sets the base_configuration_name of this MetricThresholdConfiguration.


        :param base_configuration_name: The base_configuration_name of this MetricThresholdConfiguration.  # noqa: E501
        :type: str
        """

        self._base_configuration_name = base_configuration_name

    @property
    def metric_threshold_group_list(self):
        """Gets the metric_threshold_group_list of this MetricThresholdConfiguration.  # noqa: E501


        :return: The metric_threshold_group_list of this MetricThresholdConfiguration.  # noqa: E501
        :rtype: list[MetricThresholdGroup]
        """
        return self._metric_threshold_group_list

    @metric_threshold_group_list.setter
    def metric_threshold_group_list(self, metric_threshold_group_list):
        """Sets the metric_threshold_group_list of this MetricThresholdConfiguration.


        :param metric_threshold_group_list: The metric_threshold_group_list of this MetricThresholdConfiguration.  # noqa: E501
        :type: list[MetricThresholdGroup]
        """

        self._metric_threshold_group_list = metric_threshold_group_list

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
        if not isinstance(other, MetricThresholdConfiguration):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricThresholdConfiguration):
            return True

        return self.to_dict() != other.to_dict()
