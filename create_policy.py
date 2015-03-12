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
                    "Action":"CreatePolicy", 
                    "Region":"cn-north-03",
                    "GroupId":"ulb-fr-2axjbg",
                    "Match":"ok",
                    "ULBId":"ulb-kix4tp",
                    "VServerId":"8aae44ba-f3fd-4162-9e32-2e64b89b646b",
                    "BackendId.0":"6277e964-83de-4548-b598-6b4d5a67a442"
            }
    response = ApiClient.get("/", Parameters);
    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
