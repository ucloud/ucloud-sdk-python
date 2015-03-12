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
                    "Action":"UpdateULBAttribute", 
                    "Region":"cn-north-03",
                    "ULBId":"ulb-kix4tp",
                    "VServerId":"8aae44ba-f3fd-4162-9e32-2e64b89b646b",
                    "VServerName":"Testapi"
            }
    response = ApiClient.get("/", Parameters);
    print json.dumps(Parameters, sort_keys=True, indent=4, separators=(',', ': '))
    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
