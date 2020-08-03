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


class BackupApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_backup(self, **kwargs):  # noqa: E501
        """Export backup.  # noqa: E501

        Triggers the creation of a backup and returns its ID. This service is public API since Teamscale 6.1. The user needs to have the permission to export global data provided the backup contains any and the permission to backup project data for all projects contained in the backup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_backup(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool backup_global: Include global data in the backup.
        :param list[str] include_project: Include project data in the backup. May be present multiple times.
        :param bool use_local_crypto_key: Use the local key (if configured) instead of Teamscale default key for encryption.
        :param str backup_path: The backup path. If this is not set, a new internal path will be generated.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_backup_with_http_info(**kwargs)  # noqa: E501

    def create_backup_with_http_info(self, **kwargs):  # noqa: E501
        """Export backup.  # noqa: E501

        Triggers the creation of a backup and returns its ID. This service is public API since Teamscale 6.1. The user needs to have the permission to export global data provided the backup contains any and the permission to backup project data for all projects contained in the backup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_backup_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param bool backup_global: Include global data in the backup.
        :param list[str] include_project: Include project data in the backup. May be present multiple times.
        :param bool use_local_crypto_key: Use the local key (if configured) instead of Teamscale default key for encryption.
        :param str backup_path: The backup path. If this is not set, a new internal path will be generated.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'backup_global',
            'include_project',
            'use_local_crypto_key',
            'backup_path'
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
                    " to method create_backup" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'backup_global' in local_var_params:
            form_params.append(('backup-global', local_var_params['backup_global']))  # noqa: E501
        if 'include_project' in local_var_params:
            form_params.append(('include-project', local_var_params['include_project']))  # noqa: E501
            collection_formats['include-project'] = 'csv'  # noqa: E501
        if 'use_local_crypto_key' in local_var_params:
            form_params.append(('use-local-crypto-key', local_var_params['use_local_crypto_key']))  # noqa: E501
        if 'backup_path' in local_var_params:
            form_params.append(('backup-path', local_var_params['backup_path']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/backups/export', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def download_backup(self, backup_id, **kwargs):  # noqa: E501
        """Download backup  # noqa: E501

        Allows downloading a Teamscale backup from the temporary file store. This service is public API since Teamscale 6.1. The user needs to have the permission to backup global data provided it is contained in the backup and the permission to backup project data for all projects contained in the backup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_backup(backup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str backup_id: The backup ID. (required)
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
        return self.download_backup_with_http_info(backup_id, **kwargs)  # noqa: E501

    def download_backup_with_http_info(self, backup_id, **kwargs):  # noqa: E501
        """Download backup  # noqa: E501

        Allows downloading a Teamscale backup from the temporary file store. This service is public API since Teamscale 6.1. The user needs to have the permission to backup global data provided it is contained in the backup and the permission to backup project data for all projects contained in the backup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.download_backup_with_http_info(backup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str backup_id: The backup ID. (required)
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
            'backup_id'
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
                    " to method download_backup" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'backup_id' is set
        if self.api_client.client_side_validation and ('backup_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['backup_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `backup_id` when calling `download_backup`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backupId'] = local_var_params['backup_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/backups/export/{backupId}/download', 'GET',
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

    def get_backup_status(self, backup_id, **kwargs):  # noqa: E501
        """Get the backup status  # noqa: E501

        Get the current backup import/export status This service is public API since Teamscale 6.1. The user needs to be able to configure projects. In addition the user needs to have the permission to backup global data provided the backup contains any global data and the permission to backup project data for all projects contained in the backup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_status(backup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str backup_id: The backup ID. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BackupStatusBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_backup_status_with_http_info(backup_id, **kwargs)  # noqa: E501

    def get_backup_status_with_http_info(self, backup_id, **kwargs):  # noqa: E501
        """Get the backup status  # noqa: E501

        Get the current backup import/export status This service is public API since Teamscale 6.1. The user needs to be able to configure projects. In addition the user needs to have the permission to backup global data provided the backup contains any global data and the permission to backup project data for all projects contained in the backup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_status_with_http_info(backup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str backup_id: The backup ID. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BackupStatusBase, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'backup_id'
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
                    " to method get_backup_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'backup_id' is set
        if self.api_client.client_side_validation and ('backup_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['backup_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `backup_id` when calling `get_backup_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backupId'] = local_var_params['backup_id']  # noqa: E501

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
            '/api/backups/export/{backupId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BackupStatusBase',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_backup_status1(self, backup_id, **kwargs):  # noqa: E501
        """Get the backup status  # noqa: E501

        Get the current backup import/export status This service is public API since Teamscale 6.1. The user needs to be able to configure projects. In addition the user needs to have the permission to backup global data provided the backup contains any global data and the permission to backup project data for all projects contained in the backup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_status1(backup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str backup_id: The backup ID. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: BackupStatusBase
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_backup_status1_with_http_info(backup_id, **kwargs)  # noqa: E501

    def get_backup_status1_with_http_info(self, backup_id, **kwargs):  # noqa: E501
        """Get the backup status  # noqa: E501

        Get the current backup import/export status This service is public API since Teamscale 6.1. The user needs to be able to configure projects. In addition the user needs to have the permission to backup global data provided the backup contains any global data and the permission to backup project data for all projects contained in the backup.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_status1_with_http_info(backup_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str backup_id: The backup ID. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(BackupStatusBase, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'backup_id'
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
                    " to method get_backup_status1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'backup_id' is set
        if self.api_client.client_side_validation and ('backup_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['backup_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `backup_id` when calling `get_backup_status1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'backup_id' in local_var_params:
            path_params['backupId'] = local_var_params['backup_id']  # noqa: E501

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
            '/api/backups/import/{backupId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BackupStatusBase',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_summary(self, **kwargs):  # noqa: E501
        """Get the complete backup summary  # noqa: E501

        Get the summary of the 10 most recent backups. This service is public API since Teamscale 6.1. The API requires the user to have Backup Global Data permissions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_summary(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BackupJobSummary]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_summary_with_http_info(**kwargs)  # noqa: E501

    def get_summary_with_http_info(self, **kwargs):  # noqa: E501
        """Get the complete backup summary  # noqa: E501

        Get the summary of the 10 most recent backups. This service is public API since Teamscale 6.1. The API requires the user to have Backup Global Data permissions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_summary_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[BackupJobSummary], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
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
                    " to method get_summary" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/backups/export/summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BackupJobSummary]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_summary1(self, **kwargs):  # noqa: E501
        """Get the complete backup summary  # noqa: E501

        Get the summary of the 10 most recent backups. This service is public API since Teamscale 6.1. The API requires the user to have Backup Global Data permissions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_summary1(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[BackupJobSummary]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_summary1_with_http_info(**kwargs)  # noqa: E501

    def get_summary1_with_http_info(self, **kwargs):  # noqa: E501
        """Get the complete backup summary  # noqa: E501

        Get the summary of the 10 most recent backups. This service is public API since Teamscale 6.1. The API requires the user to have Backup Global Data permissions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_summary1_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[BackupJobSummary], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
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
                    " to method get_summary1" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

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
            '/api/backups/import/summary', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BackupJobSummary]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def import_backup(self, **kwargs):  # noqa: E501
        """Import backup.  # noqa: E501

        Triggers the import of a backup and returns the job ID. This service is public API since Teamscale 6.1. The API requires the user to have Backup Global Data permissions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_backup(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[object] backup: The backups to import.
        :param str backup_path: Path to the backup.
        :param bool shadow_mode: Whether to enable shadow mode right after import.
        :param bool skip_project_creation: Whether to skip the project creation and only import backup data into existing projects.
        :param bool skip_project_validation: Whether to skip the project validation on import
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.import_backup_with_http_info(**kwargs)  # noqa: E501

    def import_backup_with_http_info(self, **kwargs):  # noqa: E501
        """Import backup.  # noqa: E501

        Triggers the import of a backup and returns the job ID. This service is public API since Teamscale 6.1. The API requires the user to have Backup Global Data permissions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.import_backup_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param list[object] backup: The backups to import.
        :param str backup_path: Path to the backup.
        :param bool shadow_mode: Whether to enable shadow mode right after import.
        :param bool skip_project_creation: Whether to skip the project creation and only import backup data into existing projects.
        :param bool skip_project_validation: Whether to skip the project validation on import
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(str, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'backup',
            'backup_path',
            'shadow_mode',
            'skip_project_creation',
            'skip_project_validation'
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
                    " to method import_backup" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'backup' in local_var_params:
            form_params.append(('backup', local_var_params['backup']))  # noqa: E501
            collection_formats['backup'] = 'csv'  # noqa: E501
        if 'backup_path' in local_var_params:
            form_params.append(('backup-path', local_var_params['backup_path']))  # noqa: E501
        if 'shadow_mode' in local_var_params:
            form_params.append(('shadow-mode', local_var_params['shadow_mode']))  # noqa: E501
        if 'skip_project_creation' in local_var_params:
            form_params.append(('skip-project-creation', local_var_params['skip_project_creation']))  # noqa: E501
        if 'skip_project_validation' in local_var_params:
            form_params.append(('skip-project-validation', local_var_params['skip_project_validation']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/api/backups/import', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
