# !/usr/bin/python
# -*- encoding: utf-8 -*-
# @author:spider1998
# encoding:UTF-8
from weibo import APIClient
import webbrowser
import re, time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

APP_KEY = '3426081082'  # 注意替换这里为自己申请的App信息
APP_SECRET = '8a1d957f34d9617e0c57935c257be86a'
CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'  # 回调授权页面

client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
url = client.get_authorize_url()
webbrowser.open_new(url)  # 打开默认浏览器获取code参数

print ('输入url中code后面的内容后按回车键：')

code = raw_input()
r = client.request_access_token(code)
access_token = r.access_token
expires_in = r.expires_in
client.set_access_token(access_token, expires_in)

comment_num = 1
i = 1

while True:
    r = client.comments.show.get(id=4316409892716932, count=200, page=i)
    if len(r.comments):
        for st in r.comments:
            created_at = st.created_at
            comment_id = st.id
            text = re.sub('回复.*?:', '', str(st.text))
            comment = re.sub("#","",text)
            user_name = st.user.screen_name
            followers = st.user.followers_count
            follow = st.user.friends_count
            province = st.user.province
            f = open("comments.txt","a")
            f.write(comment+"\n")
            f.close()
            comment_num += 1
        i += 1
        time.sleep(4)
        print comment_num
    else:
        break
