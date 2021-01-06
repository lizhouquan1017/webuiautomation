# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/13 下午1:08
@Auth ： lizhouquan
@File ：appserve.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import configparser
import os

# 根目录
root_path = os.path.dirname(os.path.dirname(__file__))

# 默认配置项
default_cfg = 'config.ini'


class ReadIni(object):
    """
    @note: 读取配置文件ini的类，可以配置文件，默认文件为config.ini
    @isPageView:是否为页面元素配置文件，@file_name:文件名称
    """

    def __init__(self, is_page_view=True, file_name=None):
        """
        初始化读取项
        :param is_page_view: 是否是页面
        :param file_name: 文件名称
        """
        if file_name is None and is_page_view is False:
            file_path = os.path.join(root_path + r'/config/' + default_cfg)
        elif is_page_view is False and file_name is not None:
            file_path = os.path.join(root_path + r'/config/' + file_name+'.ini')
            print(file_path)
        else:
            file_path = os.path.join(root_path + r'/pages/' + file_name+'.ini')
            print(file_path)
        self.cfg = configparser.ConfigParser()
        self.cfg.read(file_path, encoding="utf-8-sig")

    def read_config(self, para1, para2):
        """
        @para1: 配置文件模块
        @para2: 配置文件子模块
        @return:data 子模块内容
        """
        _data = self.cfg.get(para1, para2)
        return _data
