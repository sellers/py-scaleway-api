#!/usr/bin/env python
# initial crude python API wrapper for scaleway.com
# developers.scaleway.com for API details
# Chris G. Sellers - 2015

from ConfigParser import ConfigParser
import os
import urllib2
import json

class swauth(object):
    '''
    let's get authentication informatin
    '''

    def __init__(self, token=None):
        '''
        initialization of token if not set
        '''

        if token is None:
            self.token = swconfig()
        else:
            self.token = token

        print self.token

    def conn(self):
        ''' get authenticated connection '''
        req = urllib2.Request(url='https://api.scaleway.com/')
        req.add_header('X-Auth-Token', self.token)
        try:
            json = urllib2.urlopen(req)
        except urllib2.HTTPError as err:
            print('unable to connect, autherr {}'.format(err))
            raise
        return(self.token)


class swconfig(object):
    '''
    configuration information
    following in boto's terms we'll use
    /etc/py-scaleway.cfg
    ~/.py-scaleway
    '''

    def __init__(self):
        '''
        look for files
        '''
        self.configs = {'user': '/Users/sellers/.py-scaleway',
                        'default': '/etc/py-scaleway.cfg'}

    def get(self):
        '''
        load the configuration data
        '''

        config = ConfigParser()
        try:
            config.readfp(open(self.configs['user'], 'rb'))
        except IOError as err:
            print('Unable to read user config {}'.format(err))
        try:
            config.readfp(open(self.configs['default'], 'rb'))
        except IOError as err:
            print('unable to read default config {}'.format(err))

        config.readfp(open('/Users/csellers/.py-scaleway', 'rb'))
        token = config.get('Credentials', 'token')
        print token
        return token

class scaleway():
    '''
    '''


    def __init__(self, token=None):
        '''
        '''

        self.token = token

    def request(self, path=None):
        '''
        '''

        req = urllib2.Request('https://api.scaleway.com/{}'.format(path))
        req.add_header('X-Auth-Token', self.token)
        response = json.dumps(urllib2.urlopen(req))
        return response


    def get_tokens(self):
        '''
        '''

        tokens = self.request('/tokens')
        print tokens

    def get_orgs(self):
        '''
        '''

        orgs = self.request('/organizations')
        print orgs


auth = swauth()
token = auth.conn()
conn = scaleway(swauth().conn())
conn.get_orgs()
