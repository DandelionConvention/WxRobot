#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   community.py
@Contact :   1171460872@qq.com
@License :   (C)Copyright 2021-2022,

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/17 20:09   Bowen fu      1.0        交流模块
"""
from Models.reply import Reply
from Models.MusicDown import MusicDown,FreeMusic


class Community():
    def __init__(self):
        self.rep = Reply()
        self.functions = 'Welcome Using Robot v1.0\n1.音乐搜索\n2.B站视频下载\n3.电影资源搜索\n4.百度文库VIP下载\n5.待开发。。。'
        self.intrudce = '-- Robot --:\nauthor:付博闻\nversion:1.0Test\ntime:2022.5.17\nweiChat:3.6.0.18\n\n简介：群管理机器人，用作聊天文件保存，聊天图片保存，内置功能插件，测试版本不定时下线。'

    def doCommunity(self,mess:str,inid:str):
        if '@Robot' in mess:
            node = mess.split('Robot')[-1][1:]
            print(f'node处理--->{node}')
            if node == '':
                self.rep.replyByText(mess=self.intrudce, toid=inid)
                # return self.intrudce
            elif node == '功能介绍':
                self.rep.replyByText(mess=self.functions,toid=inid)
                # return self.functions
            elif "音乐" in node:
                # @Robot 音乐 龙卷风
                musicName = node.split('音乐')[-1].strip()
                # musicPath = MusicDown(musicName)
                musicUrl = FreeMusic(musicName)
                self.rep.replyByText(mess=f'{musicUrl}', toid=inid)

                # if musicPath == "":
                #     self.rep.replyByText(mess=f'没有找到 ：{musicName}', toid=inid)
                # else:
                #     self.rep.replyByFile(abs_path=musicPath,toid=inid)
            else:
                return node + '还未开发，敬请期待！！!'
        else:
            return ""







