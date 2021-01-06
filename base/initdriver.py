# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/30 下午1:11
@Auth ： lizhouquan
@File ：initdriver.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os
import sys
from selenium import webdriver
from util.read_ini import ReadIni

init_driver = ReadIni(is_page_view=False, file_name='driver')
view = int(init_driver.read_config('driver_init', 'view'))
driver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chromedriver')


def init_driver():
    """
    初始化driver配置
    :return: 返回driver对象
    """
    if view == 1:
        # 配置chrome浏览器无界面测试
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

    elif view == 0:
        # 启用谷歌浏览器
        driver = webdriver.Chrome(driver_path)
    else:
        # 启用火狐浏览器
        driver = webdriver.Firefox()
    return driver
