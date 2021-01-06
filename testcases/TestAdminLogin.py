# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/30 下午4:13
@Auth ： lizhouquan
@File ：TestAdminLogin.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import pytest
from base.initdriver import init_driver
from admin_platform.adminLoginPage import AdminLoginPage


class TestAdminLogin(object):

    def setup_class(self):
        self.driver = init_driver()
        self.admin_login_page = AdminLoginPage(self.driver)

    def test_admin_login(self):
        self.admin_login_page.open_admin_url()



