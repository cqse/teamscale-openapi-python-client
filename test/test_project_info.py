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
from openapi_client.models.project_info import ProjectInfo  # noqa: E501
from openapi_client.rest import ApiException

class TestProjectInfo(unittest.TestCase):
    """ProjectInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.project_info.ProjectInfo()  # noqa: E501
        if include_optional :
            return ProjectInfo(
                id = '0', 
                name = '0', 
                alias = '0', 
                parent_project_id = '0', 
                description = '0', 
                creation_timestamp = 56, 
                deleting = True, 
                reanalyzing = True
            )
        else :
            return ProjectInfo(
        )

    def testProjectInfo(self):
        """Test ProjectInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
