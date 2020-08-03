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
from openapi_client.models.findings_with_count import FindingsWithCount  # noqa: E501
from openapi_client.rest import ApiException

class TestFindingsWithCount(unittest.TestCase):
    """FindingsWithCount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FindingsWithCount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.findings_with_count.FindingsWithCount()  # noqa: E501
        if include_optional :
            return FindingsWithCount(
                findings = [
                    openapi_client.models.tracked_finding.TrackedFinding(
                        group_name = '0', 
                        category_name = '0', 
                        message = '0', 
                        location = openapi_client.models.element_location.ElementLocation(
                            uniform_path = '0', 
                            type = '0', ), 
                        id = '0', 
                        birth = openapi_client.models.commit_descriptor.CommitDescriptor(
                            branch_name = '0', 
                            timestamp = 56, ), 
                        death = openapi_client.models.commit_descriptor.CommitDescriptor(
                            branch_name = '0', 
                            timestamp = 56, ), 
                        assessment = 'RED', 
                        sibling_locations = [
                            openapi_client.models.element_location.ElementLocation(
                                uniform_path = '0', 
                                type = '0', )
                            ], 
                        secondary_locations = [
                            openapi_client.models.element_location.ElementLocation(
                                uniform_path = '0', 
                                type = '0', )
                            ], 
                        properties = {
                            'key' : None
                            }, 
                        statement_path = [
                            openapi_client.models.statement_path_element.StatementPathElement(
                                predecessors = [
                                    56
                                    ], 
                                description = '0', )
                            ], 
                        analysis_timestamp = 56, 
                        type_id = '0', )
                    ], 
                non_blacklisted_findings_count = 56, 
                tolerated_findings_count = 56, 
                false_positives_count = 56
            )
        else :
            return FindingsWithCount(
        )

    def testFindingsWithCount(self):
        """Test FindingsWithCount"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()