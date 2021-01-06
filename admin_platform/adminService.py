# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/25 上午10:12
@Auth ： lizhouquan
@File ：adminService.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

import sys
import os
from time import sleep
from base.basePage import BaseOperation
from util.read_ini import ReadIni
from util.mylogger import get_logger
sys.path.append('./..')


class AdminService(BaseOperation):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.efg = ReadIni(file_name='admin_server_page.ini')
        self.cfg = ReadIni(is_page_view=False)
        self.driver.set_page_load_timeout(30)
        self.driver.set_script_timeout(30)
        self.logger = get_logger()

    def click_app_release_review(self):
        """
        点击应用发布审核
        :return:
        """
        self.get_element('app_release_review', 'package_format', self.efg).click()

    def click_app_package_format(self):
        """
        点击包格式检查
        :return:
        """
        self.get_element('app_release_review', 'package_format', self.efg).click()

    def click_app_safety_review(self):
        """
        点击应用安全检测
        :return:
        """
        self.get_element('app_release_review', 'app_safety', self.efg).click()

    def click_app_signatrue_review(self):
        """
        点击应用签名
        :return:
        """
        self.get_element('app_release_review', 'app_signatrue', self.efg).click()

    def click_app_document_review(self):
        """
        点击应用文案
        :return:
        """
        self.get_element('app_release_review', 'app_document', self.efg).click()

    def click_app_compatibility_review(self):
        """
        点击应用兼容性
        :return:
        """
        self.get_element('app_release_review', 'app_compatibility', self.efg).click()

    def click_app_last_review_review(self):
        """
        点击应用兼容性
        :return:
        """
        self.get_element('app_release_review', 'app_last_review', self.efg).click()

    def click_app_publish_review_review(self):
        """
        点击应用推仓
        :return:
        """
        self.get_element('app_release_review', 'app_publish', self.efg).click()

    def skip_review(self, name):
        value = self.get_element('review_list', 'app_name', self.efg).text
        if name == value:
            self.get_element('review_list', 'skip_bt', self.efg).click()
            sleep(1)

    def typewrite_skip_reason(self, reason):
        self.send_keys('review_list', 'skip_reason', self.efg, reason)
        sleep(1)
        self.get_element('review_list', 'confirm_bt', self.efg).click()
        sleep(1)

    def app_format_check(self, name, reason):
        self.click_app_package_format()
        e = self.get_element('review_list', 'app_name', self.efg)
        if e:
            self.skip_review(name)
            self.typewrite_skip_reason(reason)
        else:
            self.click_app_safety_review()

    def app_safety_check(self, name, reason):
        self.click_app_safety_review()
        e = self.get_element('review_list', 'app_name', self.efg)
        if e:
            self.skip_review(name)
            self.typewrite_skip_reason(reason)
        else:
            self.click_app_signatrue_review()

    def first_review(self):
        self.click_app_signatrue_review()
        e = self.get_element('review_list', 'app_name', self.efg)
        print("first %s" % e)
        while e:
            sleep(10)
            self.refresh_window()
            e = self.get_element('review_list', 'app_name', self.efg)
            print("second %s" % e)
        self.click_app_document_review()
        sleep(1)

    def click_review_bt(self):
        self.get_element('review_list', 'review_bt', self.efg).click()
        sleep(1)

    def review_pass(self, stage, reason):
        self.get_element('review_detail', 'review_bt', self.efg).click()
        sleep(1)
        if stage == 1:
            self.send_keys('review_detail', 'first_review_reason', self.efg, reason)
            sleep(1)
            self.get_element('review_detail', 'first_pass_bt', self.efg).click()
        elif stage == 2:
            self.send_keys('review_detail', 'second_review_reason', self.efg, reason)
            sleep(1)
            self.get_element('review_detail', 'second_pass_bt', self.efg).click()
        elif stage == 3:
            self.send_keys('review_detail', 'last_review_reason', self.efg, reason)
            sleep(1)
            self.get_element('review_detail', 'last_pass_bt', self.efg).click()

    def review_refuse(self, stage, reason):
        self.get_element('review_detail', 'review_bt', self.efg).click()
        sleep(1)
        if stage == 1:
            self.send_keys('review_detail', 'first_review_reason', self.efg, reason)
            sleep(1)
            self.get_element('review_detail', 'first_refuse_bt', self.efg).click()
        elif stage == 2:
            self.send_keys('review_detail', 'second_review_reason', self.efg, reason)
            sleep(1)
            self.get_element('review_detail', 'second_refuse_bt', self.efg).click()
        elif stage == 3:
            self.send_keys('review_detail', 'last_review_reason', self.efg, reason)
            sleep(1)
            self.get_element('review_detail', 'last_refuse_bt', self.efg).click()
