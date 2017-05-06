# 微信聊天机器人
# author : 全世界
# Time:2017-5-6
import itchat
from itchat.content import *
import json
from urllib import request
from urllib import parse

@itchat.msg_register([TEXT])
def text_reply(msg):
    info = msg['Text']
    url = 'http://www.tuling123.com/openapi/api'
    data = {u'key': "c7b34262d25a4e30a889f37a8c8339e5", "info": info, u"loc": msg['User']['City'], "userid": msg['FromUserName']}
    data = parse.urlencode(data).encode(encoding='UTF8')
    url2 = request.Request(url, data)
    response = request.urlopen(url2)
    apicontent = response.read().decode('utf-8')
    s = json.loads(apicontent, encoding='utf-8')
    print(msg['User']['NickName'] + ":" + info)
    print("**********发送人信息*********")
    print("姓名：" + msg['User']['NickName'])
    print("城市：" + msg["User"]['Province'] + msg['User']['City'])
    print("签名：" + msg['User']['Signature'])
    if s['code'] == 100000:
        itchat.send(s['text'],msg['FromUserName'])

@itchat.msg_register(TEXT,isGroupChat=True)
def groupchat_reply(msg):
    if msg['isAt']:
        print(msg['ActualNickName'] + ": " + msg['Content'])
        info = msg['Content']
        url = 'http://www.tuling123.com/openapi/api'
        data = {u'key': "c7b34262d25a4e30a889f37a8c8339e5", "info": info, u"loc": msg['User']['City'], "userid": msg['FromUserName']}
        data = parse.urlencode(data).encode(encoding='UTF8')
        url2 = request.Request(url, data)
        response = request.urlopen(url2)
        apicontent = response.read().decode('utf-8')
        s = json.loads(apicontent, encoding='utf-8')
        itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'], s['text']), msg['FromUserName'])

print("*****************************Minokun微信智能聊天机器人1.0版*****************************")
print()
print("作者：全世界")
print("时间：2017-5-6")
print("功能：不只可以聊天，讲笑话，查公交，菜谱，天气，完全就是百科全书哦，和那些路边的妖艳货完全不一样的！")
print("ps：后续还会加上更刺激的功能，嘿，好好期待吧！")
print()
print("*****************************开始咯*****************************")
itchat.auto_login(hotReload=True)
itchat.run(debug=True)