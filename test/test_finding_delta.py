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
from openapi_client.models.finding_delta import FindingDelta  # noqa: E501
from openapi_client.rest import ApiException

class TestFindingDelta(unittest.TestCase):
    """FindingDelta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FindingDelta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = openapi_client.models.finding_delta.FindingDelta()  # noqa: E501
        if include_optional :
            return FindingDelta(
                added_findings = [
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
                findings_in_changed_code = [
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
                removed_findings = [
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
                number_of_added_findings = 56, 
                number_of_findings_in_changed_code = 56, 
                number_of_removed_findings = 56, 
                finding_summary = [
                    openapi_client.models.findings_summary_category_info.FindingsSummaryCategoryInfo(
                        category_name = '0', 
                        count = 56, 
                        count_red = 56, 
                        group_infos = [
                            openapi_client.models.findings_summary_group_info.FindingsSummaryGroupInfo(
                                group_name = '0', 
                                count = 56, 
                                count_red = 56, 
                                type_id_infos = [
                                    openapi_client.models.findings_summary_type_id_info.FindingsSummaryTypeIdInfo(
                                        type_id_name = '0', 
                                        count = 56, 
                                        count_red = 56, )
                                    ], )
                            ], )
                    ]
            )
        else :
            return FindingDelta(
        )

    def testFindingDelta(self):
        """Test FindingDelta"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()