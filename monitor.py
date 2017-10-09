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

# 在while循环中每间隔3s检查一次被监视的临时节点的存在性
while True:
    if client.exists("/test/failure_detection/worker"):
        print("The worker is alive.")
        time.sleep(3.0)
    else:
        print("The worker is died.")
        break
client.stop()
