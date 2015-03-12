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
    Parameters={"Action":"CreateEIP", "OperatorName":"Duplet", "Bandwidth":"2", "ChargeType":"Month","Region":"cn-east-01"}
    response = ApiClient.get("/", Parameters);
    print response;
