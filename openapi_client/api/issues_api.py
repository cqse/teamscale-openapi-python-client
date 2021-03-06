# coding: utf-8

"""
    Teamscale REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 6.1.2
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class IssuesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_issue_metric_descriptor(self, project, issue_metric_descriptor, **kwargs):  # noqa: E501
        """Create issue metric  # noqa: E501

        Creates an issue metric descriptor in the system. This service is public API since Teamscale 6.0. The API requires the user to have Edit Issue Metrics permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_issue_metric_descriptor(project, issue_metric_descriptor, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param IssueMetricDescriptor issue_metric_descriptor: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_issue_metric_descriptor_with_http_info(project, issue_metric_descriptor, **kwargs)  # noqa: E501

    def create_issue_metric_descriptor_with_http_info(self, project, issue_metric_descriptor, **kwargs):  # noqa: E501
        """Create issue metric  # noqa: E501

        Creates an issue metric descriptor in the system. This service is public API since Teamscale 6.0. The API requires the user to have Edit Issue Metrics permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_issue_metric_descriptor_with_http_info(project, issue_metric_descriptor, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param IssueMetricDescriptor issue_metric_descriptor: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project',
            'issue_metric_descriptor'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_issue_metric_descriptor" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project' is set
        if self.api_client.client_side_validation and ('project' not in local_var_params or  # noqa: E501
                                                        local_var_params['project'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project` when calling `create_issue_metric_descriptor`")  # noqa: E501
        # verify the required parameter 'issue_metric_descriptor' is set
        if self.api_client.client_side_validation and ('issue_metric_descriptor' not in local_var_params or  # noqa: E501
                                                        local_var_params['issue_metric_descriptor'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `issue_metric_descriptor` when calling `create_issue_metric_descriptor`")  # noqa: E501

        if self.api_client.client_side_validation and 'project' in local_var_params and not re.search(r'^(?!aliases$)[-_.a-zA-Z0-9]+$', local_var_params['project']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `project` when calling `create_issue_metric_descriptor`, must conform to the pattern `/^(?!aliases$)[-_.a-zA-Z0-9]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'issue_metric_descriptor' in local_var_params:
            body_params = local_var_params['issue_metric_descriptor']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/projects/{project}/issues/metrics', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_issue_finding_badge(self, project, issue_id, **kwargs):  # noqa: E501
        """Get issue finding badge  # noqa: E501

        Creates a finding badge for the given issue. This service is public API since Teamscale 5.9. The API requires the user to have View Project permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_issue_finding_badge(project, issue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param str issue_id: ID of the issue to create a finding badge for (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_issue_finding_badge_with_http_info(project, issue_id, **kwargs)  # noqa: E501

    def get_issue_finding_badge_with_http_info(self, project, issue_id, **kwargs):  # noqa: E501
        """Get issue finding badge  # noqa: E501

        Creates a finding badge for the given issue. This service is public API since Teamscale 5.9. The API requires the user to have View Project permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_issue_finding_badge_with_http_info(project, issue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param str issue_id: ID of the issue to create a finding badge for (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project',
            'issue_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_issue_finding_badge" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project' is set
        if self.api_client.client_side_validation and ('project' not in local_var_params or  # noqa: E501
                                                        local_var_params['project'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project` when calling `get_issue_finding_badge`")  # noqa: E501
        # verify the required parameter 'issue_id' is set
        if self.api_client.client_side_validation and ('issue_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['issue_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `issue_id` when calling `get_issue_finding_badge`")  # noqa: E501

        if self.api_client.client_side_validation and 'project' in local_var_params and not re.search(r'^(?!aliases$)[-_.a-zA-Z0-9]+$', local_var_params['project']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `project` when calling `get_issue_finding_badge`, must conform to the pattern `/^(?!aliases$)[-_.a-zA-Z0-9]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']  # noqa: E501
        if 'issue_id' in local_var_params:
            path_params['issueId'] = local_var_params['issue_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/projects/{project}/issues/{issueId}/findings-badge', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_issue_finding_churn(self, project, issue_id, **kwargs):  # noqa: E501
        """Get issue finding churn  # noqa: E501

        Determines an aggregated finding churn across all commits of the issue. This service is public API since Teamscale 5.9. The API requires the user to have View Project permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_issue_finding_churn(project, issue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param str issue_id: ID of the issue to determine the finding churn for (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: FindingChurnList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_issue_finding_churn_with_http_info(project, issue_id, **kwargs)  # noqa: E501

    def get_issue_finding_churn_with_http_info(self, project, issue_id, **kwargs):  # noqa: E501
        """Get issue finding churn  # noqa: E501

        Determines an aggregated finding churn across all commits of the issue. This service is public API since Teamscale 5.9. The API requires the user to have View Project permissions on the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_issue_finding_churn_with_http_info(project, issue_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str project: The project alias or id. (required)
        :param str issue_id: ID of the issue to determine the finding churn for (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(FindingChurnList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'project',
            'issue_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_issue_finding_churn" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'project' is set
        if self.api_client.client_side_validation and ('project' not in local_var_params or  # noqa: E501
                                                        local_var_params['project'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `project` when calling `get_issue_finding_churn`")  # noqa: E501
        # verify the required parameter 'issue_id' is set
        if self.api_client.client_side_validation and ('issue_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['issue_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `issue_id` when calling `get_issue_finding_churn`")  # noqa: E501

        if self.api_client.client_side_validation and 'project' in local_var_params and not re.search(r'^(?!aliases$)[-_.a-zA-Z0-9]+$', local_var_params['project']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `project` when calling `get_issue_finding_churn`, must conform to the pattern `/^(?!aliases$)[-_.a-zA-Z0-9]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'project' in local_var_params:
            path_params['project'] = local_var_params['project']  # noqa: E501
        if 'issue_id' in local_var_params:
            path_params['issueId'] = local_var_params['issue_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/projects/{project}/issues/{issueId}/finding-churn', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FindingChurnList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
