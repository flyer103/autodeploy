#!/usr/bin/env python3

# --------------------------------------------
# Author: zhangyifei <zhangyifei@baixing.com>
# Date: 2014-10-23 23:44:31
# --------------------------------------------

"""获取配置
"""

import yaml


def get_configs():
    """提供配置文件"""
    with open('settings.yaml', 'r') as fp:
        configs = yaml.load(fp)

    return configs
