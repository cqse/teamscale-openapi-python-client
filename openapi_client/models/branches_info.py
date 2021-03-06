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


class BranchesInfo(object):
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
        'main_branch_name': 'str',
        'branch_names': 'list[str]',
        'deleted_branches': 'list[str]',
        'anonymous_branches': 'list[str]',
        'aliases': 'dict(str, str)'
    }

    attribute_map = {
        'main_branch_name': 'mainBranchName',
        'branch_names': 'branchNames',
        'deleted_branches': 'deletedBranches',
        'anonymous_branches': 'anonymousBranches',
        'aliases': 'aliases'
    }

    def __init__(self, main_branch_name=None, branch_names=None, deleted_branches=None, anonymous_branches=None, aliases=None, local_vars_configuration=None):  # noqa: E501
        """BranchesInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._main_branch_name = None
        self._branch_names = None
        self._deleted_branches = None
        self._anonymous_branches = None
        self._aliases = None
        self.discriminator = None

        if main_branch_name is not None:
            self.main_branch_name = main_branch_name
        if branch_names is not None:
            self.branch_names = branch_names
        if deleted_branches is not None:
            self.deleted_branches = deleted_branches
        if anonymous_branches is not None:
            self.anonymous_branches = anonymous_branches
        if aliases is not None:
            self.aliases = aliases

    @property
    def main_branch_name(self):
        """Gets the main_branch_name of this BranchesInfo.  # noqa: E501


        :return: The main_branch_name of this BranchesInfo.  # noqa: E501
        :rtype: str
        """
        return self._main_branch_name

    @main_branch_name.setter
    def main_branch_name(self, main_branch_name):
        """Sets the main_branch_name of this BranchesInfo.


        :param main_branch_name: The main_branch_name of this BranchesInfo.  # noqa: E501
        :type: str
        """

        self._main_branch_name = main_branch_name

    @property
    def branch_names(self):
        """Gets the branch_names of this BranchesInfo.  # noqa: E501


        :return: The branch_names of this BranchesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._branch_names

    @branch_names.setter
    def branch_names(self, branch_names):
        """Sets the branch_names of this BranchesInfo.


        :param branch_names: The branch_names of this BranchesInfo.  # noqa: E501
        :type: list[str]
        """

        self._branch_names = branch_names

    @property
    def deleted_branches(self):
        """Gets the deleted_branches of this BranchesInfo.  # noqa: E501


        :return: The deleted_branches of this BranchesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._deleted_branches

    @deleted_branches.setter
    def deleted_branches(self, deleted_branches):
        """Sets the deleted_branches of this BranchesInfo.


        :param deleted_branches: The deleted_branches of this BranchesInfo.  # noqa: E501
        :type: list[str]
        """

        self._deleted_branches = deleted_branches

    @property
    def anonymous_branches(self):
        """Gets the anonymous_branches of this BranchesInfo.  # noqa: E501


        :return: The anonymous_branches of this BranchesInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._anonymous_branches

    @anonymous_branches.setter
    def anonymous_branches(self, anonymous_branches):
        """Sets the anonymous_branches of this BranchesInfo.


        :param anonymous_branches: The anonymous_branches of this BranchesInfo.  # noqa: E501
        :type: list[str]
        """

        self._anonymous_branches = anonymous_branches

    @property
    def aliases(self):
        """Gets the aliases of this BranchesInfo.  # noqa: E501


        :return: The aliases of this BranchesInfo.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this BranchesInfo.


        :param aliases: The aliases of this BranchesInfo.  # noqa: E501
        :type: dict(str, str)
        """

        self._aliases = aliases

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
        if not isinstance(other, BranchesInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BranchesInfo):
            return True

        return self.to_dict() != other.to_dict()
