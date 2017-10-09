# -*- coding: utf-8 -*-
"""
Dec: 创建一个被监视的临时性节点
Created on : 2017.10.08
Author : Iflier
"""
print(__doc__)

import time
import logging
from kazoo.client import KazooClient

logging.basicConfig()

client = KazooClient(hosts='127.0.0.1:2181')
client.start()

# 被装饰的函数带有节点的值和ZnodeStat实例作为参数
@client.DataWatch('/test/zoo/node')
def func(data, stat):
    if data:
        print("Data is {0}".format(data))
        print("Version is {0}".format(stat.version))
    else:
        print("Data is unavailable !")

while True:
    try:
        time.sleep(5.0)
    except KeyboardInterrupt:
        break
print("exit.")
client.stop()
