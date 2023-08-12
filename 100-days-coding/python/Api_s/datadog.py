#!/usr/bin/python3
'''Search for hosts in a datadog'''
import requests


def datadog(hosts):
    headers = {'Authentication': 'fba78d8d0884eefb36cef55765f2d404'}
    url = 'https://api.datadoghq.com/api/v1/{}/totals.json'.format(hosts)
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return 0
    return("Response Status Code:", response.status_code)
    return("Response Content:", response.content)

active_hosts = datadog('hosts')
print(active_hosts)
