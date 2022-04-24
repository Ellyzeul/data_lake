from os import environ
import re


def get_es_headers():
    url = environ['BONSAI_URL']

    auth = re.search('https\:\/\/(.*)\@', url).group(1).split(':')
    host = url.replace('https://%s:%s@' % (auth[0], auth[1]), '')

    match = re.search('(:\d+)', host)
    if match:
        p = match.group(0)
        host = host.replace(p, '')
        port = int(p.split(':')[1])
    else:
        port = 443
    
    es_header = [{
        'host': host,
        'port': port,
        'use_ssl': True
    }], (auth[0],auth[1])

    return es_header