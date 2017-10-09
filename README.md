# kazooZooKeeper
Some examples of Zookeeper client kazoo

worker.py and monitor.py:
worker.py创建一个临时（ephemeral=True）节点，接收到键盘中断后，client会断开
与Zookeeper的连接。接着monitor.py检查到临时性的节点不存在了，也会输出提示。

watchData.py and watchchildren.py：
分别用于监视指定节点的数据变化或子节点的变化
