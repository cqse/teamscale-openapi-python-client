# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import openapi_client
from openapi_client.models.metric_threshold import MetricThreshold  # noqa: E501
from openapi_client.rest import ApiException

class TestMetricThreshold(unittest.TestCase):
    """MetricThreshold unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetricThreshold
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.metric_threshold.MetricThreshold()  # noqa: E501
        if include_optional :
            return MetricThreshold(
                name = '0', 
                options = {
                    'key' : '0'
                    }, 
                custom_name = '0', 
                threshold_yellow = 1.337, 
                threshold_red = 1.337, 
                sub_path = '0', 
                metric_schema_source = 'CODE_METRICS', 
                assessment_specification = 'DEFAULT', 
                evaluation_options = [
                    'ASSESSMENT_METRIC_RED_IF_ANY_THRESHOLD_VIOLATED'
                    ], 
                inherited_from_configuration = '0', 
                is_inherited = True, 
                preceding_threshold_display_name = '0'
            )
        else :
            return MetricThreshold(
        )

    def testMetricThreshold(self):
        """Test MetricThreshold"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
