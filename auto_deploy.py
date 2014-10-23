#!/usr/bin/env python3

# --------------------------------------------
# Author: flyer <flyer103#gmail.com>
# Date: 2014-10-23 18:14:19
# --------------------------------------------

"""github 自动部署.
"""

import os
import sys
import subprocess

from flask import Flask, request

sys.path.append(os.path.join(os.path.abspath(__file__).rsplit('/', 1)[0], 'logger'))

from configs import get_configs
from mylogger import Logger

log_main = Logger.get_logger(__file__)


app = Flask(__name__)

configs_sys = get_configs()         # 系统配置


# Route
@app.route('/deploy/<project>', methods=['POST'])
def deploy(project=None):
    if project.upper() not in configs_sys['GIT']:
        log_main.critical('No such project: {0}'.format(project))
        sys.exit(-1)

    html_url = request.json['repository']['html_url']
    local_url = configs_sys['GIT'][project.upper()]['URL']

    if html_url != local_url:
        log_main.critical('Project {0} does not match {1} from github'.format(local_url, html_url))
        sys.exit(-1)

    operation = configs_sys['GIT'][project.upper()]['OPERATION']

    subprocess.call(operation, shell=True)

    return 'success'


if __name__ == '__main__':
    debug = True if configs_sys['LOCAL']['DEBUG'] else False
    host = configs_sys['LOCAL']['HOST']
    port = configs_sys['LOCAL']['PORT']
    
    configs_app = {
        'debug': debug,
        'host': host,
        'port': port,
    }
    app.run(**configs_app)
