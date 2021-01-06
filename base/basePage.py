# -*- coding: utf-8 -*-
"""
@Time ： 2020/11/13 下午1:08
@Auth ： lizhouquan
@File ：appserve.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import csv
import os
import sys
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep, strftime, localtime, time
from util.mylogger import get_logger
from util.read_ini import ReadIni
from selenium.webdriver.support.select import Select
import pyautogui as gui

sys.path.append('./..')
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT_PATH + '/config/data_config.xml')


class BasePage(object):
    """
    基础操作
    """

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)
        self.logger = get_logger()

    def open_url(self, url):
        """
        浏览器输入网址,打开登录服务
        :param url:
        :return:
        """
        self.driver.get(url)
        self.logger.debug('open url is %s' % url)

    def max_windows(self):
        """
        窗口最大化
        :return:
        """
        self.driver.maximize_window()

    def close_window(self):
        """
        关闭系统窗口
        :return:
        """
        self.driver.close()
        self.driver.quit()
        self.logger.debug('--------close windows-------')

    def refresh_window(self):
        """
        刷新系统窗口
        :return:
        """
        self.driver.refresh()
        self.logger.debug('--------System Window refreshed---------')

    def get_element(self, section, key, efg):
        """
        获取配置文件中的页面元素:
        :param section: 元素模块
        :param key: 元素id,name,classname,xpath
        :param efg: 页面元素
        :return: 返回找到的元素
        """
        data = efg.read_config(section, key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        self.logger.debug("locate by:[" + by + "] value:[" + value + ']')
        try:
            if by == 'id':
                return WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id(value))
            elif by == 'name':
                return WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_name(value))
            elif by == 'classname':
                return WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_class_name(value))
            elif by == 'text':
                return WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_link_text(value))
            elif by == 'xpath':
                return WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(value))
        except Exception as e:
            self.logger.error('NoSuchElement:' + str(e))

    def get_elements(self, section, key, efg):
        """
        获取配置文件中的页面元素:
        :param section: 元素模块
        :param key: 元素id,name,classname,xpath
        :param efg: 页面元素
        :return: 返回找到的元素list
        """
        data = efg.read_config(section, key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        self.logger.debug("locate by:[" + by + "] value:[" + value + ']')
        try:
            if by == 'id':
                return WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_id(value))
            elif by == 'name':
                return WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_name(value))
            elif by == 'classname':
                return WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_class_name(value))
            elif by == 'xpath':
                return WebDriverWait(self.driver, 10).until(lambda x: x.find_elements_by_xpath(value))
        except Exception as e:
            self.logger.error('NoSuchElement:' + str(e))

    def send_keys(self, section, key, efg, value):
        """
        输入框输入值
        :param section:
        :param key:
        :param efg:
        :param value:
        :return:
        """
        self.get_element(section, key, efg).send_keys(value)

    def click(self, section, key, efg):
        """
        对元素进行点击操作
        :param section:
        :param key:
        :param efg:
        :return:
        """
        self.get_element(section, key, efg).click()

    def get_driver_name(self):
        """
        获取浏览器名称
        :return: name
        """
        name = self.driver.name
        return name

    def get_driver_current_url(self):
        """
        获取当前窗口url
        :return: url
        """
        url = self.driver.current_url
        return url

    def get_driver_title(self):
        """
        获取浏览器标题
        :return: title
        """
        title = self.driver.title
        return title

    def get_windows_handles(self):
        """
        获取当前窗口句柄
        :return: handles
        """
        handles = self.driver.handles
        return handles

    def driver_back(self):
        """
        后退
        :return:
        """
        self.driver.back()

    def driver_forward(self):
        """
        前进
        :return:
        """
        self.driver.forward()

    def screenshot_png(self):
        st = strftime("%Y-%m-%d-%H-%M-%S", localtime(time()))
        file_name = __file__ + st + '.png'
        file_path = os.path.join(ROOT_PATH, 'screenshot', file_name)
        self.driver.get_screenshot_as_file(file_path)

    def roll(self, element, index=None):
        """
        滚动页面:
        :param element: 滚动时参考的元素，路径或者元素对象
        :param index: index:up 元素在最上，down 元素在最下
        :return:
        """
        if index == 'up':
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        elif index == 'down':
            self.driver.execute_script("arguments[0].scrollIntoView(false);", element)
        else:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.logger.debug('Scrolls %s to location' % element)

    def get_element_attribute(self, section, key, efg, attr):
        """
        获取元素属性值
        :param section:
        :param key:
        :param efg:
        :param attr:
        :return: e_value
        """
        e = self.get_element(section, key, efg)
        e_value = e.get_attribute(attr)
        return e_value

    def find_element_parent(self, section, key, efg):
        """
        查找元素的父节点
        :param section:
        :param key:
        :param efg:
        :return: e
        """
        e = self.get_element(section, key, efg)
        e.find_element_by_xpath('..')
        return e

    def execute_js(self, js):
        self.driver.execute_script()
