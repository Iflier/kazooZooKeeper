# -*- coding: utf-8 -*-
"""
Dec: 监视一个节点的子节点的变化（创建和删除）
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

# 以变化的节点名称为参数
@client.ChildrenWatch("/test/zoo/node/test2")
def func(children):
    print("Children are {0}".format(children))

while True:
    try:
        time.sleep(3.0)
    except KeyboardInterrupt:
        break

print("exit.")
client.stop()
