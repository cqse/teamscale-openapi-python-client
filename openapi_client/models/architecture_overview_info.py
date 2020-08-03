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


class ArchitectureOverviewInfo(object):
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
        'uniform_path': 'str',
        'change_type': 'str',
        'is_repository_architecture': 'bool',
        'violations': 'int',
        'orphans': 'int',
        'finding_creation': 'str',
        'creation_timestamp': 'int',
        'modification_timestamp': 'int'
    }

    attribute_map = {
        'uniform_path': 'uniformPath',
        'change_type': 'changeType',
        'is_repository_architecture': 'isRepositoryArchitecture',
        'violations': 'violations',
        'orphans': 'orphans',
        'finding_creation': 'findingCreation',
        'creation_timestamp': 'creationTimestamp',
        'modification_timestamp': 'modificationTimestamp'
    }

    def __init__(self, uniform_path=None, change_type=None, is_repository_architecture=None, violations=None, orphans=None, finding_creation=None, creation_timestamp=None, modification_timestamp=None, local_vars_configuration=None):  # noqa: E501
        """ArchitectureOverviewInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uniform_path = None
        self._change_type = None
        self._is_repository_architecture = None
        self._violations = None
        self._orphans = None
        self._finding_creation = None
        self._creation_timestamp = None
        self._modification_timestamp = None
        self.discriminator = None

        if uniform_path is not None:
            self.uniform_path = uniform_path
        if change_type is not None:
            self.change_type = change_type
        if is_repository_architecture is not None:
            self.is_repository_architecture = is_repository_architecture
        if violations is not None:
            self.violations = violations
        if orphans is not None:
            self.orphans = orphans
        if finding_creation is not None:
            self.finding_creation = finding_creation
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if modification_timestamp is not None:
            self.modification_timestamp = modification_timestamp

    @property
    def uniform_path(self):
        """Gets the uniform_path of this ArchitectureOverviewInfo.  # noqa: E501


        :return: The uniform_path of this ArchitectureOverviewInfo.  # noqa: E501
        :rtype: str
        """
        return self._uniform_path

    @uniform_path.setter
    def uniform_path(self, uniform_path):
        """Sets the uniform_path of this ArchitectureOverviewInfo.


        :param uniform_path: The uniform_path of this ArchitectureOverviewInfo.  # noqa: E501
        :type: str
        """

        self._uniform_path = uniform_path

    @property
    def change_type(self):
        """Gets the change_type of this ArchitectureOverviewInfo.  # noqa: E501


        :return: The change_type of this ArchitectureOverviewInfo.  # noqa: E501
        :rtype: str
        """
        return self._change_type

    @change_type.setter
    def change_type(self, change_type):
        """Sets the change_type of this ArchitectureOverviewInfo.


        :param change_type: The change_type of this ArchitectureOverviewInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADD", "MODIFY", "DELETE", "NONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and change_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `change_type` ({0}), must be one of {1}"  # noqa: E501
                .format(change_type, allowed_values)
            )

        self._change_type = change_type

    @property
    def is_repository_architecture(self):
        """Gets the is_repository_architecture of this ArchitectureOverviewInfo.  # noqa: E501


        :return: The is_repository_architecture of this ArchitectureOverviewInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_repository_architecture

    @is_repository_architecture.setter
    def is_repository_architecture(self, is_repository_architecture):
        """Sets the is_repository_architecture of this ArchitectureOverviewInfo.


        :param is_repository_architecture: The is_repository_architecture of this ArchitectureOverviewInfo.  # noqa: E501
        :type: bool
        """

        self._is_repository_architecture = is_repository_architecture

    @property
    def violations(self):
        """Gets the violations of this ArchitectureOverviewInfo.  # noqa: E501


        :return: The violations of this ArchitectureOverviewInfo.  # noqa: E501
        :rtype: int
        """
        return self._violations

    @violations.setter
    def violations(self, violations):
        """Sets the violations of this ArchitectureOverviewInfo.


        :param violations: The violations of this ArchitectureOverviewInfo.  # noqa: E501
        :type: int
        """

        self._violations = violations

    @property
    def orphans(self):
        """Gets the orphans of this ArchitectureOverviewInfo.  # noqa: E501


        :return: The orphans of this ArchitectureOverviewInfo.  # noqa: E501
        :rtype: int
        """
        return self._orphans

    @orphans.setter
    def orphans(self, orphans):
        """Sets the orphans of this ArchitectureOverviewInfo.


        :param orphans: The orphans of this ArchitectureOverviewInfo.  # noqa: E501
        :type: int
        """

        self._orphans = orphans

    @property
    def finding_creation(self):
        """Gets the finding_creation of this ArchitectureOverviewInfo.  # noqa: E501


        :return: The finding_creation of this ArchitectureOverviewInfo.  # noqa: E501
        :rtype: str
        """
        return self._finding_creation

    @finding_creation.setter
    def finding_creation(self, finding_creation):
        """Sets the finding_creation of this ArchitectureOverviewInfo.


        :param finding_creation: The finding_creation of this ArchitectureOverviewInfo.  # noqa: E501
        :type: str
        """

        self._finding_creation = finding_creation

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this ArchitectureOverviewInfo.  # noqa: E501


        :return: The creation_timestamp of this ArchitectureOverviewInfo.  # noqa: E501
        :rtype: int
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this ArchitectureOverviewInfo.


        :param creation_timestamp: The creation_timestamp of this ArchitectureOverviewInfo.  # noqa: E501
        :type: int
        """

        self._creation_timestamp = creation_timestamp

    @property
    def modification_timestamp(self):
        """Gets the modification_timestamp of this ArchitectureOverviewInfo.  # noqa: E501


        :return: The modification_timestamp of this ArchitectureOverviewInfo.  # noqa: E501
        :rtype: int
        """
        return self._modification_timestamp

    @modification_timestamp.setter
    def modification_timestamp(self, modification_timestamp):
        """Sets the modification_timestamp of this ArchitectureOverviewInfo.


        :param modification_timestamp: The modification_timestamp of this ArchitectureOverviewInfo.  # noqa: E501
        :type: int
        """

        self._modification_timestamp = modification_timestamp

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
        if not isinstance(other, ArchitectureOverviewInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ArchitectureOverviewInfo):
            return True

        return self.to_dict() != other.to_dict()