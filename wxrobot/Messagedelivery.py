#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   Messagedelivery.py
@Contact :   1171460872@qq.com
@License :   (C)Copyright 2021-2022,

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/17 16:29   Bowen fu      1.0        消息分发处理
"""

import json
from Models.community import Community
from Models.reply import Reply

class Messages():
    def __init__(self,mess:str):
        self.mess = mess
        self.comm = Community()
        self.inid = ""
        self.content = ""
        self.path = ""
        self.senderid = ""
        self.person = 0 # 1个人，2群
        self.getMessage(mess)

    def handMessage(self):
        self.comm.doCommunity(self.content,self.inid)

    def getMessage(self,mess:str):
        mess_dic = json.loads(mess)
        if mess_dic['msgtype'] == 'friend':
            # 个人消息接收
            self.inid = mess_dic['friendwxid']
            self.content = mess_dic['content']
            self.path = mess_dic['path']
            print(f'{self.inid}向你发送了{self.content}')
            self.person = 1

        elif mess_dic['msgtype'] == 'groud':
            # 群消息接收
            self.inid = mess_dic['chatroomid']
            self.senderid = mess_dic['senderid']
            self.content = mess_dic['content']
            self.path = mess_dic['path']
            print(f'{self.inid}群组中的{self.senderid}向发送了{self.content}')
            self.person = 2

    def savedb(self):
        pass


# def get_message(mess:str):
#     mess_dic = json.loads(mess)
#
#     if mess_dic['msgtype'] == 'friend':
#         # 个人消息接收
#         inid = mess_dic['friendwxid']
#         content = mess_dic['content']
#         path =  mess_dic['path']
#
#         print(f'{inid}向你发送了{content}')
#
#     elif mess_dic['msgtype'] == 'groud':
#         # 群消息接收
#         inid = mess_dic['chatroomid']
#         senderid = mess_dic['senderid']
#         content = mess_dic['content']
#         path = mess_dic['path']
#         print(f'{inid}群组中的{senderid}向发送了{content}')
#     else:
#         print(mess)
#         return False
#
#     if path == '':
#         content_text(content,inid)
#     elif 'Image' in path:
#         content_jpg(path,inid)
#     elif 'Video' in path:
#         content_video(path,inid)
#     elif 'File' in path:
#         content_file(path,inid)


# def content_text(mess,inid):
#     rmess = Community().doCommunity(mess)
#     if rmess == "":
#         return
#     Reply().replyByText(mess=rmess,toid=inid)
#
# def content_file(path,inid):
#
#     pass
#
# def content_jpg(path,inid):
#     print(f"接收文件{path}")
#
#     pass
#
# def write2db():
#
#     pass
#
# def content_video(path,inid):
#
#     pass



