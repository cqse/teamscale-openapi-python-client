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


class PrioritizableTestCluster(object):
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
        'cluster_id': 'str',
        'tests': 'list[PrioritizableTest]',
        'current_score': 'float'
    }

    attribute_map = {
        'cluster_id': 'clusterId',
        'tests': 'tests',
        'current_score': 'currentScore'
    }

    def __init__(self, cluster_id=None, tests=None, current_score=None, local_vars_configuration=None):  # noqa: E501
        """PrioritizableTestCluster - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_id = None
        self._tests = None
        self._current_score = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if tests is not None:
            self.tests = tests
        if current_score is not None:
            self.current_score = current_score

    @property
    def cluster_id(self):
        """Gets the cluster_id of this PrioritizableTestCluster.  # noqa: E501


        :return: The cluster_id of this PrioritizableTestCluster.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this PrioritizableTestCluster.


        :param cluster_id: The cluster_id of this PrioritizableTestCluster.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def tests(self):
        """Gets the tests of this PrioritizableTestCluster.  # noqa: E501


        :return: The tests of this PrioritizableTestCluster.  # noqa: E501
        :rtype: list[PrioritizableTest]
        """
        return self._tests

    @tests.setter
    def tests(self, tests):
        """Sets the tests of this PrioritizableTestCluster.


        :param tests: The tests of this PrioritizableTestCluster.  # noqa: E501
        :type: list[PrioritizableTest]
        """

        self._tests = tests

    @property
    def current_score(self):
        """Gets the current_score of this PrioritizableTestCluster.  # noqa: E501


        :return: The current_score of this PrioritizableTestCluster.  # noqa: E501
        :rtype: float
        """
        return self._current_score

    @current_score.setter
    def current_score(self, current_score):
        """Sets the current_score of this PrioritizableTestCluster.


        :param current_score: The current_score of this PrioritizableTestCluster.  # noqa: E501
        :type: float
        """

        self._current_score = current_score

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
        if not isinstance(other, PrioritizableTestCluster):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PrioritizableTestCluster):
            return True

        return self.to_dict() != other.to_dict()