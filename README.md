# Miaooo的图书馆

服务运行在nicooo.xyz

- 功能

    图书馆

    博客（开发中）

    在线计算（开发中）


- 安装配置教程
1. 我的环境为Ubuntu 20.04

    conda 4.10.3

    python 3.9.7
    
    nginx
    
    mysql

2. 配置conda环境
```
    conda create -n web_env

    conda activate web_env

    conda install uwsgi # 很重要
```
其他哪个报错就装哪个包（使用pip install 包名）

3. 修改uwsgi.ini，config.py

- 使用

    static/books 图书目录

    static/img 图书封面（代码还没写）
    
    先运行nginx

    先运行book_databse.py

    调试运行main.py

    生产运行start_uwsgi.sh

    停止运行stop_uwsgi.sh !!! 会清空log文件 clear log ！！！