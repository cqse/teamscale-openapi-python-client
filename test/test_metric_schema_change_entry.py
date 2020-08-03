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
from openapi_client.models.metric_schema_change_entry import MetricSchemaChangeEntry  # noqa: E501
from openapi_client.rest import ApiException

class TestMetricSchemaChangeEntry(unittest.TestCase):
    """MetricSchemaChangeEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MetricSchemaChangeEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.metric_schema_change_entry.MetricSchemaChangeEntry()  # noqa: E501
        if include_optional :
            return MetricSchemaChangeEntry(
                metric_id = '0', 
                analysis_group = '0', 
                metric_definition = openapi_client.models.metric_directory_schema_entry.MetricDirectorySchemaEntry(
                    name = '0', 
                    description = '0', 
                    aggregation = 'SUM', 
                    value_type = 'NUMERIC', 
                    properties = [
                        'SIZE_METRIC'
                        ], )
            )
        else :
            return MetricSchemaChangeEntry(
        )

    def testMetricSchemaChangeEntry(self):
        """Test MetricSchemaChangeEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()