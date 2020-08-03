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


class MetricAssessment(object):
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
        'description': 'str',
        'value_type': 'str',
        'aggregation': 'str',
        'properties': 'list[str]',
        'value': 'object',
        'string_value': 'str',
        'formatted_text_value': 'str',
        'trend': 'str',
        'rating': 'str',
        'trend_delta': 'str',
        'available_in_project': 'bool',
        'metric_thresholds': 'EvaluatedMetricThreshold',
        'display_name': 'str',
        'sub_path': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'value_type': 'valueType',
        'aggregation': 'aggregation',
        'properties': 'properties',
        'value': 'value',
        'string_value': 'stringValue',
        'formatted_text_value': 'formattedTextValue',
        'trend': 'trend',
        'rating': 'rating',
        'trend_delta': 'trendDelta',
        'available_in_project': 'availableInProject',
        'metric_thresholds': 'metricThresholds',
        'display_name': 'displayName',
        'sub_path': 'subPath'
    }

    def __init__(self, name=None, description=None, value_type=None, aggregation=None, properties=None, value=None, string_value=None, formatted_text_value=None, trend=None, rating=None, trend_delta=None, available_in_project=None, metric_thresholds=None, display_name=None, sub_path=None, local_vars_configuration=None):  # noqa: E501
        """MetricAssessment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._value_type = None
        self._aggregation = None
        self._properties = None
        self._value = None
        self._string_value = None
        self._formatted_text_value = None
        self._trend = None
        self._rating = None
        self._trend_delta = None
        self._available_in_project = None
        self._metric_thresholds = None
        self._display_name = None
        self._sub_path = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if value_type is not None:
            self.value_type = value_type
        if aggregation is not None:
            self.aggregation = aggregation
        if properties is not None:
            self.properties = properties
        if value is not None:
            self.value = value
        if string_value is not None:
            self.string_value = string_value
        if formatted_text_value is not None:
            self.formatted_text_value = formatted_text_value
        if trend is not None:
            self.trend = trend
        if rating is not None:
            self.rating = rating
        if trend_delta is not None:
            self.trend_delta = trend_delta
        if available_in_project is not None:
            self.available_in_project = available_in_project
        if metric_thresholds is not None:
            self.metric_thresholds = metric_thresholds
        if display_name is not None:
            self.display_name = display_name
        if sub_path is not None:
            self.sub_path = sub_path

    @property
    def name(self):
        """Gets the name of this MetricAssessment.  # noqa: E501


        :return: The name of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MetricAssessment.


        :param name: The name of this MetricAssessment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this MetricAssessment.  # noqa: E501


        :return: The description of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MetricAssessment.


        :param description: The description of this MetricAssessment.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def value_type(self):
        """Gets the value_type of this MetricAssessment.  # noqa: E501


        :return: The value_type of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this MetricAssessment.


        :param value_type: The value_type of this MetricAssessment.  # noqa: E501
        :type: str
        """
        allowed_values = ["NUMERIC", "TIMESTAMP", "ASSESSMENT", "COUNTER_SET"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and value_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `value_type` ({0}), must be one of {1}"  # noqa: E501
                .format(value_type, allowed_values)
            )

        self._value_type = value_type

    @property
    def aggregation(self):
        """Gets the aggregation of this MetricAssessment.  # noqa: E501


        :return: The aggregation of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._aggregation

    @aggregation.setter
    def aggregation(self, aggregation):
        """Sets the aggregation of this MetricAssessment.


        :param aggregation: The aggregation of this MetricAssessment.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUM", "MIN", "MAX", "UNION", "NONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and aggregation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `aggregation` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation, allowed_values)
            )

        self._aggregation = aggregation

    @property
    def properties(self):
        """Gets the properties of this MetricAssessment.  # noqa: E501


        :return: The properties of this MetricAssessment.  # noqa: E501
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this MetricAssessment.


        :param properties: The properties of this MetricAssessment.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["SIZE_METRIC", "RATIO_METRIC", "HIDDEN", "LOW_IS_BAD", "QUALITY_NEUTRAL"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(properties).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `properties` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(properties) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._properties = properties

    @property
    def value(self):
        """Gets the value of this MetricAssessment.  # noqa: E501


        :return: The value of this MetricAssessment.  # noqa: E501
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MetricAssessment.


        :param value: The value of this MetricAssessment.  # noqa: E501
        :type: object
        """

        self._value = value

    @property
    def string_value(self):
        """Gets the string_value of this MetricAssessment.  # noqa: E501


        :return: The string_value of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this MetricAssessment.


        :param string_value: The string_value of this MetricAssessment.  # noqa: E501
        :type: str
        """

        self._string_value = string_value

    @property
    def formatted_text_value(self):
        """Gets the formatted_text_value of this MetricAssessment.  # noqa: E501


        :return: The formatted_text_value of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._formatted_text_value

    @formatted_text_value.setter
    def formatted_text_value(self, formatted_text_value):
        """Sets the formatted_text_value of this MetricAssessment.


        :param formatted_text_value: The formatted_text_value of this MetricAssessment.  # noqa: E501
        :type: str
        """

        self._formatted_text_value = formatted_text_value

    @property
    def trend(self):
        """Gets the trend of this MetricAssessment.  # noqa: E501


        :return: The trend of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._trend

    @trend.setter
    def trend(self, trend):
        """Sets the trend of this MetricAssessment.


        :param trend: The trend of this MetricAssessment.  # noqa: E501
        :type: str
        """
        allowed_values = ["UP", "DOWN", "STABLE", "NA"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and trend not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `trend` ({0}), must be one of {1}"  # noqa: E501
                .format(trend, allowed_values)
            )

        self._trend = trend

    @property
    def rating(self):
        """Gets the rating of this MetricAssessment.  # noqa: E501


        :return: The rating of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this MetricAssessment.


        :param rating: The rating of this MetricAssessment.  # noqa: E501
        :type: str
        """
        allowed_values = ["RED", "ORANGE", "YELLOW", "GREEN", "BASELINE", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and rating not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `rating` ({0}), must be one of {1}"  # noqa: E501
                .format(rating, allowed_values)
            )

        self._rating = rating

    @property
    def trend_delta(self):
        """Gets the trend_delta of this MetricAssessment.  # noqa: E501


        :return: The trend_delta of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._trend_delta

    @trend_delta.setter
    def trend_delta(self, trend_delta):
        """Sets the trend_delta of this MetricAssessment.


        :param trend_delta: The trend_delta of this MetricAssessment.  # noqa: E501
        :type: str
        """

        self._trend_delta = trend_delta

    @property
    def available_in_project(self):
        """Gets the available_in_project of this MetricAssessment.  # noqa: E501


        :return: The available_in_project of this MetricAssessment.  # noqa: E501
        :rtype: bool
        """
        return self._available_in_project

    @available_in_project.setter
    def available_in_project(self, available_in_project):
        """Sets the available_in_project of this MetricAssessment.


        :param available_in_project: The available_in_project of this MetricAssessment.  # noqa: E501
        :type: bool
        """

        self._available_in_project = available_in_project

    @property
    def metric_thresholds(self):
        """Gets the metric_thresholds of this MetricAssessment.  # noqa: E501


        :return: The metric_thresholds of this MetricAssessment.  # noqa: E501
        :rtype: EvaluatedMetricThreshold
        """
        return self._metric_thresholds

    @metric_thresholds.setter
    def metric_thresholds(self, metric_thresholds):
        """Sets the metric_thresholds of this MetricAssessment.


        :param metric_thresholds: The metric_thresholds of this MetricAssessment.  # noqa: E501
        :type: EvaluatedMetricThreshold
        """

        self._metric_thresholds = metric_thresholds

    @property
    def display_name(self):
        """Gets the display_name of this MetricAssessment.  # noqa: E501


        :return: The display_name of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this MetricAssessment.


        :param display_name: The display_name of this MetricAssessment.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def sub_path(self):
        """Gets the sub_path of this MetricAssessment.  # noqa: E501


        :return: The sub_path of this MetricAssessment.  # noqa: E501
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """Sets the sub_path of this MetricAssessment.


        :param sub_path: The sub_path of this MetricAssessment.  # noqa: E501
        :type: str
        """

        self._sub_path = sub_path

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
        if not isinstance(other, MetricAssessment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetricAssessment):
            return True

        return self.to_dict() != other.to_dict()
