# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/30 下午4:01
@Auth ： lizhouquan
@File ：adminLoginPage.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from pathlib import Path
from base.basePage import BasePage
from util.read_ini import ReadIni
from util.mylogger import get_logger

file_name = Path(__file__).name[0:-3]


class AdminLoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.efg = ReadIni(file_name=file_name)
        self.cfg = ReadIni(is_page_view=False)
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.logger = get_logger()
        self.url = self.cfg.read_config('admin', 'url')

    def open_admin_url(self):
        self.open_url(self.url)
