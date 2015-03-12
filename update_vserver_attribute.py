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
                    "Action":"UpdateVServerAttribute",
                    "VServerId":"953e6c08-0e7b-4739-99b8-8e28567307be",
                    "Region":"cn-north-03",
                    "ULBId":"ulb-0tc4sm", 
                    "VServerName":"testvserver1",
                    "Protocol":"TCP",
                    "FrontendPort":"80",
                    "Method":"Source",
                    "PersistenceType":"None",
                    "ClientTimeout":"1000",
                    }
    response = ApiClient.get("/", Parameters );
    print response;
