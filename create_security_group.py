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
                "Action":"CreateSecurityGroup",
                "GroupName":"test3", 
                "Rule.0":"TCP|53|0.0.0.0/0|ACCEPT|50",
                "Rule.1":"TCP|80|0.0.0.0/0|ACCEPT|50",
                "Region":"cn-north-03",
                "Description":"test"
                }
    response = ApiClient.get("/", Parameters);
    print response;
