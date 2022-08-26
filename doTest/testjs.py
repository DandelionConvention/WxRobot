#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   testjs.py    
@Contact :   1171460872@qq.com
@License :   (C)Copyright 2021-2022, 

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/18 12:30   Bowen fu      1.0         None
"""
import execjs

import execjs

# 实例化node对象
node = execjs.get()
# js文件编译
ctx = node.compile(open('./FreeMusic.js',encoding='utf8').read())
# 执行js
funcName = 'encode("text=" + "周杰伦" + "&page=" + "1" + "&type=" + "migu")'
pwd = ctx.call(funcName)
print(pwd)