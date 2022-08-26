#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   reply.py
@Contact :   1171460872@qq.com
@License :   (C)Copyright 2021-2022,

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/5/17 16:57   Bowen fu      1.0         消息回复
"""

import requests
import json


class Reply():
    def __init__(self):
        self.wxid = 'wxid_44vgbawac1kt29'  # 个人微信id
        self.friendList = []
        self.groupList = []
        # self.autoDownload()  # 开启自动下载

    def replyByText(self, mess: str, toid: str):
        """
        :param toid: 个人id 和 聊天群id
        :param wxid:
        :param mess: 发送消息
        :return: Null
    {
        "type": "send_msg",
        "to_wxid": "hytpnpn",  # 接收方微信id
        "msg": "个非寻"
    }
        """

        mess_dic = {
            "type": "send_msg",
            "to_wxid": toid,
            "wxid": self.wxid,
            "msg": mess
        }
        self.doRequests(mess_dic)

    def replyToPersonInGroup(self, mess: str, nickname: str, groupid: str, personid: str):
        """
        :param nickname:
        :param personid:
        :param groupid:
        :param mess:
        :return: Null
    发@文本消息
    {
        "type":"send_at_msg",
        "chatroomid":"chatroomid132123",
        "wxid":"wxid_m4xxzn7sxzm22",
        "at_wxid":"hytpnpn",
        "nickname":"不知不道",
        "msg":"个非寻"
    }
        """
        mess_dic = {
            "type": "send_at_msg",
            "chatroomid": groupid,
            "wxid": self.wxid,
            "at_wxid": personid,
            "nickname": nickname,
            "msg": mess
        }
        self.doRequests(mess_dic)

    def replyByImage(self, abs_path: str, toid: str):
        """
        :param id:
        :return:

    {
        "type": "send_image",
        "wxid": "wxid_m4xxzn7sxzm22",
        "to_wxid": "hytpnpn",
        "path":
    }
        """

        mess_dic = {
            "type": "send_image",
            "wxid": self.wxid,
            "to_wxid": toid,
            "path": abs_path,
        }
        self.doRequests(mess_dic)

    def replyByFile(self, abs_path: str, toid: str):
        """
        :param id:
        :return:

    {
        "type": "send_file",
        "wxid": "wxid_m4xxzn7sxzm22",
        "to_wxid": "hytpnpn",
        "path":
    }
        """
        mess_dic = {
            "type": "send_file",
            "wxid": self.wxid,
            "to_wxid": toid,
            "path": abs_path,
        }
        self.doRequests(mess_dic)

    def autoDownload(self):
        """
        :return:
        {
            "type": "auto_down",
            "wxid": "wxid_m4xxzn7sxzm22",
        }
        """
        mess_dic = {
            "type": "auto_down",
            "wxid": self.wxid,
        }
        self.doRequests(mess_dic)

    def doRequests(self, mess_dict: dict):
        url = 'http://127.0.0.1:8888'
        mess_json = json.dumps(mess_dict)
        requests.post(url=url, data=mess_json)
        print(f'发送消息{mess_json}')
