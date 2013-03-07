#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from distutils.core import setup
#from setuptools import setup

try:
    #import setuptools
    from setuptools import setup
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()


import distutils.sysconfig
import os
import sys

"""
# ディレクトリ構成
.
├── MANIFEST.in
├── README.txt
├── scripts
│   ├── sayecho
│   ├── sayhello
│   ├── sayhellolist
│   └── sayhoge
├── setup.py
└── src
    ├── exersise
    │   ├── __init__.py
    │   ├── echo.py
    │   ├── echolist.py
    │   ├── hoge
    │   │   ├── __init__.py
    │   │   └── echo.py
    │   ├── moduledata
    │   │   ├── goodbylist
    │   │   │   └── goodbylist.txt
    │   │   ├── hellolist.txt
    │   │   └── trash
    │   │       ├── 001
    │   │       ├── 002
    │   │       ├── 003.txt
    │   │       └── 004.txt
    │   └── otherdata
    │       ├── goodbylist
    │       │   └── goodbylist.txt
    │       ├── hellolist.txt
    │       └── trash
    │           ├── 001
    │           ├── 002
    │           ├── 003.txt
    │           └── 004.txt
    └── exersise2
        ├── __init__.py
        └── echo.py
"""


setup(name='SetupPyExersise',
    version='1.0',
    description='setup.py exersise',
    author='Yasuhiro Ota',
    author_email='ya-ota@ccm-lulu.com',
    url='http://blog.ccm-lulu.com',
    license='http://ccm-lulu.mit-license.org/',

## package_xxxx の扱い方

      #### 
      # site-package のパスの取得
      # distutils.sysconfig.get_python_lib()

      #### 
      # packages の にいれるパッケージ名とpackage_dir # に指定するディレクトリ配下のディレクトリ名は合わせる
      # 一致していないと -> error: package directory 'src/exersise' does not exist
      #.

      ####
      #packages=['exersise'],
      #package_dir={'': 'src'},
        # 上記場合だとinstall後は以下の様な使い方ができる
        #  import exersise
        #  exersise.echo.echo("hello")

      #####
      # モジュール１つの時
      # これでは hoge モジュールははいらない
      #packages=['exersise'],
      #package_dir={'': 'src'},
      # or
      #package_dir={'exersise': 'src/exersise'},

      #####
      # モジュールを並列で２つ置きたいとき パターン
      #packages=['exersise', 'exersisetwo'],
      #package_dir={'exersise': 'src/exersise', 'exersisetwo': 'src/exersise2'},

      #####
      # モジュールを階層で２つ置きたいとき パターン
      # hoge モジュールも入る

    packages=['exersise', 'exersise.hoge', 'exersise.tests'],
    package_dir={'': 'src'},

      # データファイルはまず MANIFEST.in に書いて sdist に含めるようにしておく
      # src配下がルートとなり、exersise パッケージの配下にデータが有るのを検知する
    package_data={'exersise': ['moduledata/*.txt']},

      # モジュール内で使用するけど configuration files, message catalogs, data
      # files以外のやつは別管理する。
      # そのなかから data_files で配置先を決める
      # デフォルトでインストールさきは /usr/local 
      # 例) /usr/local/exersise/hellolist.txt
      # 例) /usr/local/exersise/goodbylist.txt
      #
      # パスは以下のプロパティで確認できる
      # print sys.exec_prefix
      # print sys.prefix

    data_files=[('exersise', ['src/exersise/otherdata/hellolist.txt', 'src/exersise/otherdata/goodbylist/goodbylist.txt'])],


      #scriptsディレクトリのファイルが /usr/local/bin へ配置される(ファイルがコピーされる)
    scripts=['scripts/sayhello', 'scripts/sayecho', 'scripts/sayhoge', 'scripts/sayhellolist'],

    test_suite="exersise.tests",


     )





