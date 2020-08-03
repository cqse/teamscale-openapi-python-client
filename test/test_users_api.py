# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.users_api import UsersApi  # noqa: E501
from openapi_client.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.users_api.UsersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_users(self):
        """Test case for delete_users

        Delete users  # noqa: E501
        """
        pass

    def test_edit_users(self):
        """Test case for edit_users

        Edit users  # noqa: E501
        """
        pass

    def test_get_all_users(self):
        """Test case for get_all_users

        Get all users  # noqa: E501
        """
        pass

    def test_get_user(self):
        """Test case for get_user

        Get user  # noqa: E501
        """
        pass

    def test_put_user(self):
        """Test case for put_user

        Update user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()