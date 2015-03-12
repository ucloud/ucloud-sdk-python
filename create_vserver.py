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
                    "Action":"CreateVServer",
                    "Region":"cn-north-03",
                    "ULBID":"ulb-tep0yy", 
                    "VServerName":"testvserver1",
                    "Protocol":"TCP",
                    "FrontendPort":"80",
                    "Method":"Source",
                    "PersistenceType":"None"}
    response = ApiClient.get("/", Parameters );
    print response;
