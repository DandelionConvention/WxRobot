import requests
import json

wxid = 'wxid_44vgbawac1kt29'

# data_dic = {
#     "type": "get_friends",
#     "wxid": wxid,
# }
# data_dic = {"type":"get_robot"}

# data_dic = {
#     "type": "send_msg",
#     "wxid": wxid,  # 本人微信id
#     "to_wxid": "wxid_p13efzpxuv6m22",  # 接收方微信id
#     "msg": "个非寻"
# }

# data_dic = {
#     "msg type": "friend",
#     "robot": "wxid_44vgbawac1kt29",
#     "friendwxid": "wxid_p13efzpxuv6m22",
#     "content": "",
#     "path": ""
# }

# data_dic = {
#     "type": "auto_down",
#     "wxid": "wxid_p13efzpxuv6m22",
# }

# data_dic = {
#     "type": "get_chatroom",
#     "wxid": "wxid_44vgbawac1kt29",
# }

data_dic = {"type": "send_msg", "wxid":"wxid_44vgbawac1kt29", "to_wxid": "wxid_p13efzpxuv6m22", "msg": "\u662f\u662f\u8fd8\u672a\u5f00\u53d1\uff0c\u656c\u8bf7\u671f\u5f85\uff01\uff01!"}

data_json = json.dumps(data_dic)
re = requests.post(url='http://127.0.0.1:8888', data=data_json).content
print(re)
