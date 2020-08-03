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


class PreCommitUploadData(object):
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
        'uniform_path_to_content_map': 'dict(str, str)',
        'deleted_uniform_paths': 'list[str]'
    }

    attribute_map = {
        'uniform_path_to_content_map': 'uniformPathToContentMap',
        'deleted_uniform_paths': 'deletedUniformPaths'
    }

    def __init__(self, uniform_path_to_content_map=None, deleted_uniform_paths=None, local_vars_configuration=None):  # noqa: E501
        """PreCommitUploadData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uniform_path_to_content_map = None
        self._deleted_uniform_paths = None
        self.discriminator = None

        if uniform_path_to_content_map is not None:
            self.uniform_path_to_content_map = uniform_path_to_content_map
        if deleted_uniform_paths is not None:
            self.deleted_uniform_paths = deleted_uniform_paths

    @property
    def uniform_path_to_content_map(self):
        """Gets the uniform_path_to_content_map of this PreCommitUploadData.  # noqa: E501


        :return: The uniform_path_to_content_map of this PreCommitUploadData.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._uniform_path_to_content_map

    @uniform_path_to_content_map.setter
    def uniform_path_to_content_map(self, uniform_path_to_content_map):
        """Sets the uniform_path_to_content_map of this PreCommitUploadData.


        :param uniform_path_to_content_map: The uniform_path_to_content_map of this PreCommitUploadData.  # noqa: E501
        :type: dict(str, str)
        """

        self._uniform_path_to_content_map = uniform_path_to_content_map

    @property
    def deleted_uniform_paths(self):
        """Gets the deleted_uniform_paths of this PreCommitUploadData.  # noqa: E501


        :return: The deleted_uniform_paths of this PreCommitUploadData.  # noqa: E501
        :rtype: list[str]
        """
        return self._deleted_uniform_paths

    @deleted_uniform_paths.setter
    def deleted_uniform_paths(self, deleted_uniform_paths):
        """Sets the deleted_uniform_paths of this PreCommitUploadData.


        :param deleted_uniform_paths: The deleted_uniform_paths of this PreCommitUploadData.  # noqa: E501
        :type: list[str]
        """

        self._deleted_uniform_paths = deleted_uniform_paths

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
        if not isinstance(other, PreCommitUploadData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PreCommitUploadData):
            return True

        return self.to_dict() != other.to_dict()