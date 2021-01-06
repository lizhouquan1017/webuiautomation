# -*- coding: utf-8 -*-
"""
@Time ： 2020/12/30 上午10:03
@Auth ： lizhouquan
@File ：mylogger.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import os
import logging.config
import datetime

log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)) + '/log/')

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_name = datetime.datetime.now().strftime('%Y-%m-%d') + '.log'
log_path = os.path.join(log_dir + log_name)


standard_format = '%(asctime)s - %(threadName)s:%(thread)d - module:%(module)s - %(filename)s:%(lineno)d -' \
                  '%(levelname)s - %(message)s'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

test_format = '%(asctime)s] %(message)s'

LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'test': {
            'format': test_format
        },
    },
    'filters': {},
    # handlers是日志的接收者,不同的handler会将日志输出到不同的位置
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            # 'maxBytes': 1024*1024*5,  # 日志大小 5M
            'maxBytes': 1000,
            'backupCount': 5,
            'filename': log_path,
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
        # 打印到文件的日志,收集info及以上的日志
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',  # 保存到文件
            'filename': log_path,
            'encoding': 'utf-8',
            'formatter': 'test',

        },
    },
    # loggers是日志的产生者，产生的日志会传递给handler然后控制输出
    'loggers': {
        # logging.getLogger(__name__)拿到的logger配置
        'kkk': {
            'handlers': ['console', 'other'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '终端提示': {
            'handlers': ['console', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
        '': {
            'handlers': ['default', ],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',  # loggers(第一层日志级别关限制)--->handlers(第二层日志级别关卡限制)
            'propagate': False,  # 默认为True，向上（更高level的logger）传递，通常设置为False即可，否则会一份日志向上层层传递
        },
    },
}


def get_logger():
    logging.config.dictConfig(LOGGING_DIC)
    logger = logging.getLogger('default.logger')
    logger_error = logging.getLogger('error.logger')
    return logger
