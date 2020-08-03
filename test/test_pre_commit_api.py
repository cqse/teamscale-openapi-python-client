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
from openapi_client.api.pre_commit_api import PreCommitApi  # noqa: E501
from openapi_client.rest import ApiException


class TestPreCommitApi(unittest.TestCase):
    """PreCommitApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.pre_commit_api.PreCommitApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_pre_commit_server_limits(self):
        """Test case for get_pre_commit_server_limits

        Get pre-commit server limits  # noqa: E501
        """
        pass

    def test_poll_pre_commit_results(self):
        """Test case for poll_pre_commit_results

        Poll pre-commit results  # noqa: E501
        """
        pass

    def test_process_pre_commit(self):
        """Test case for process_pre_commit

        Trigger pre-commit analysis  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()