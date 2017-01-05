# -*- coding: utf-8 -*-

import requests
from datetime import datetime
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

conf = {}

conf['data_file'] = './data/data2_1000.json'

conf['etx_info_weblist_file'] = './data/etx_info_weblist_file_1000plus.json'

conf['more_then_user_num'] = 0

conf['tmp_ext_file'] = './tmp/ext.crx'

conf['tmp_path'] = './tmp/'

conf['threadnum'] = 15

conf['HTTP_HEADERS'] = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2403.157 Safari/537.36"
}
