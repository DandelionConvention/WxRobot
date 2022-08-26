#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   MusicDown.py
@Contact :   1171460872@qq.com
@License :   (C)Copyright 2021-2022,

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/17 21:37   Bowen fu      1.0         None
"""
import requests
import os
from seleniumwire import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time

def MusicDown(name):
    filePath ='F:\\life\\music'
    musicPath = ''
    for root,dirs,files in os.walk(filePath):
        for file in files:
            #获取文件所属目录
            # print(root)
            #获取文件路径
            if name in file:
                musicPath = os.path.join(root,file)

    return musicPath

def FreeMusic(name):
    # r.send(i.hasContent && i.data || null)
    url = 'http://tools.liumingye.cn/music/?page=searchPage'
    driver = webdriver.Chrome(executable_path='E:\\Codes\\python\\wxRobot\\Tools\\chromedriver.exe')
    # driver.create_options()


    driver.get(url=url)
    Einput = driver.find_element(By.ID,'input')
    Einput.send_keys(name)
    Einput.send_keys(Keys.ENTER)
    time.sleep(3)
    data = []

    for request in driver.requests:
        if request.url == 'http://59.110.45.28/m/api/search':
            if request.response:
                if request.response.status_code == 200:
                    datas = json.loads(request.response.body.decode())
                    # print(datas)
                    data = list(datas['data']['list'])
                    break
                else:
                    return f'没有找到{name}'

    r_data = ''
    song = data[0]
    if 'url_flac' in song.keys():
        r_data = str(song['name']) + ' '+ str(song['artist'])+ ':' + str(song['url_flac'])
    else:
        r_data = str(song['name']) + ' ' + str(song['artist']) + ':' + str(song['url_320'])

    return r_data



