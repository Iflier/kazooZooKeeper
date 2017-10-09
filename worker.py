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

if not client.exists("/test/failure_detection"):
    client.ensure_path("/test/failure_detection")

# 创建一个带有数据的临时节点
client.create("/test/failure_detection/worker", value=b"money happy freedom",
              ephemeral=True)
while True:
    try:
        print("Node alive.")
        time.sleep(3.0)
    except KeyboardInterrupt:
        break
print("Node has gone!")
client.stop()
