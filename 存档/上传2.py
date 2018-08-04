
import os
import re

from datetime import datetime

import python_webdav.client as webdav_client


def setUp():

    client = webdav_client.Client('https://pubdav.ctfile.com',
                               webdav_path='.',
                               realm='test-realm',
                               port=443)
    client.set_connection(username='jiqi1136@163.com', password='q962946')

setUp()