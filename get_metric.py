#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sdk import UcloudApiClient
import config
from pprint import pprint
import sys


def get_metric(region, resource_type, resource_id, metric_name,
               timerange=1 * 60 * 60):
    """Get UCloud monitor data
    Region: "cn-east-01"|"cn-north-01"|"cn-south-01"|"hk-01"|"cn-north-02"
                华东       北京bgpa         华南      香港    北京bgpb
    ResourceType: 'uhost'|'udb'|'umem'|'ulb'
    MetricName:
        uhost:
            'NetworkIn'
            'NetworkOut'
            'CPUUtilization'
            'IORead'
            'IOWrite'
            'DiskReadOps'
            'DiskWriteOps'
            'NICIn'
            'NICOut'
            'MemUsage'
            'DataSpaceUsage'
            'RootSpaceUsage'
            'ReadonlyDiskCount'
            'RunnableProcessCount'
            'BlockProcessCount'
        udb:
            'CPUUtilization'
            'MemUsage'
            'QPS'
            'ExpensiveQuery'

        ulb:
            'NetworkOut'
            'CurrentConnections'

        umem:
            'Usage'
            'QPS'
            'InstanceCount'

    """
    api_client = UcloudApiClient(config.base_url, config.public_key,
                                 config.private_key)

    params = {};
    params['Region'] = region
    params['Action'] = 'GetMetric' 
    params['ResourceType'] = resource_type 
    params['ResourceID'] = resource_id 
    params['MetricName'] = metric_name
    params['TimeRange'] = timerange 
    response = api_client.get("/", params)
    pprint(response)


if __name__ == '__main__':
    # get_metric('cn-east-01', 'uhost', 'uhost-ezsffw', 'NetworkOut')
    usage = "%s Region ResourceType ResourceID MetricName [TimeRange]\n" % (sys.argv[0])
    argc = len(sys.argv)
    if argc < 5:
        sys.stderr.write(usage)
        sys.exit(1)
    region = sys.argv[1]
    resource_type = sys.argv[2]
    resource_id = sys.argv[3]
    metric_name = sys.argv[4]
    if argc == 6:
        timerange = sys.argv[5]
    get_metric(region, resource_type, resource_id, metric_name)
