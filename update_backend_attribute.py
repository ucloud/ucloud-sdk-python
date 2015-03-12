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
                    "Region":"cn-north-03",
                    "ULBId":"ulb-a3qq0o",
                    "Action":"UpdateBackendAttribute", 
                    "BackendId":"293cf207-6d91-4aeb-b846-a50828f99d22",
                    "Port":"8080",
                    "Enabled":"0"
            }
    response = ApiClient.get("/", Parameters);
    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
