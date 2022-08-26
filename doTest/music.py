#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   music.py    
@Contact :   1171460872@qq.com
@License :   (C)Copyright 2021-2022, 

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/19 16:35   Bowen fu      1.0         None
"""
# from seleniumwire import webdriver
#
# driver = webdriver.Chrome(executable_path='E:\\Codes\\python\\wxRobot\\Tools\\chromedriver.exe')
#
# driver.get('https://www.baidu.com')
#
# for request in driver.requests:
#     if request.response:
#         print(
#             request.url,
#             request.response.status_code,
#             request.response.headers['Content-Type']
#         )



s = '@Robot 音乐 龙卷风'
print(s.split('音乐')[-1].strip())
