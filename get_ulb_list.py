#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk import UcloudApiClient
import config
from pprint import pprint
import sys


def get_ulb_list(region):
    """get one user's ulb list"""
    api_client = UcloudApiClient(config.base_url, config.public_key,
                                 config.private_key)

    params = {};
    params['Action'] = "DescribeULB"
    params['Region'] = region

    response = api_client.get("/", params)
    pprint(response)


if __name__ == '__main__':
    # region description can be found in get_metric.py file
    usage = '%s Region\n' % (sys.argv[0])
    argc = len(sys.argv)
    if argc != 2:
        sys.stderr.write(usage)
        sys.exit(1)
    get_ulb_list(sys.argv[1])
