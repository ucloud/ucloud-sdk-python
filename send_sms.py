#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sdk import UcloudApiClient
from config import *
import sys
import json

#实例化 API 句柄

if __name__=='__main__':
    arg_length = len(sys.argv)
    if arg_length == 1 or arg_length == 2 :
        print './sendsms.py "1377777777777|137888888888" "测试短信"'
        sys.exit()
    ApiClient = UcloudApiClient(base_url, public_key, private_key)
    phones = sys.argv[1].split('|')
    Parameters={
            "Action":"SendSms",
            "Content":sys.argv[2]
            }
    if sys.platform == 'win32' : 
        Parameters={
                "Action":"SendSms",
                "Content": "windows 命令行测试不支持传中文请谅解"
                }

    for i in range(len(phones)):
        Parameters['Phone.'+str(i)] = phones[i]
    response = ApiClient.get("/", Parameters );
    print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
