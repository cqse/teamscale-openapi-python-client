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
from openapi_client.api.monitoring_api import MonitoringApi  # noqa: E501
from openapi_client.rest import ApiException


class TestMonitoringApi(unittest.TestCase):
    """MonitoringApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.monitoring_api.MonitoringApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_health_status(self):
        """Test case for get_health_status

        Get system health status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
