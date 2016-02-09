# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ParameterGroupingPostRequiredParameters(Model):
    """
    Additional parameters for the postRequired operation.

    :param int body:
    :param str custom_header:
    :param int query: Query parameter with default. Default value: 30 .
    :param str path: Path parameter
    """

    _required = ['body', 'path']

    def __init__(self, *args, **kwargs):
        self.body = None
        self.custom_header = None
        self.query = None
        self.path = None

        super(ParameterGroupingPostRequiredParameters, self).__init__(*args, **kwargs)