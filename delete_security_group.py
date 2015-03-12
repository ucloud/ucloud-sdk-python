#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import json

#实例化 API 句柄


if __name__=='__main__':
    arg_length = len(sys.argv)
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    Parameters={
                "Action":"DeleteSecurityGroup",
                "Region":"cn-north-03",
                "GroupId":"6584"
                }
    response = ApiClient.get("/", Parameters);
    print response;
