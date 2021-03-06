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
from openapi_client.models.analysis_profile import AnalysisProfile  # noqa: E501
from openapi_client.rest import ApiException

class TestAnalysisProfile(unittest.TestCase):
    """AnalysisProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnalysisProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.analysis_profile.AnalysisProfile()  # noqa: E501
        if include_optional :
            return AnalysisProfile(
                name = '0', 
                languages = [
                    'JAVA'
                    ], 
                tools = [
                    'TEAMSCALE'
                    ], 
                options = {
                    'key' : '0'
                    }, 
                quality_indicators = [
                    openapi_client.models.quality_indicator.QualityIndicator(
                        name = '0', 
                        options = {
                            'key' : '0'
                            }, 
                        groups = [
                            openapi_client.models.analysis_group.AnalysisGroup(
                                name = '0', )
                            ], )
                    ], 
                description = '0'
            )
        else :
            return AnalysisProfile(
        )

    def testAnalysisProfile(self):
        """Test AnalysisProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
