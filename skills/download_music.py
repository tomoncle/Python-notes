# -*- coding=utf-8 -*-

import requests
import json
import urllib
import urllib2

# 查看外链生成器的　url 方法
data = requests.post(
    url='http://music.163.com/weapi/song/enhance/player/url',
    data={
        'params': 'iPslhRDpIz9eXPL6tuauyLF7NSU7yIetfu0vlx7lzfhlZGm21DICXpBCTmAqdiznd6LMnR6bGegIXGWyjNcHaOpjUC4E9ZLNt42hmQnA6QnYwitYsvs6CrKuXFp8pCJb',
        'encSecKey': '47911c978b596e8c832e76ae96c0660ef6380d7f9e71c56e3ce7d90cf6978b385a6c5cba169cdf74d39cecae564cdaedfbc28e65cef01fbaeb3e0d27c228d6b0a63151ecb2d16a920eb37608d173c5824aa689dbfdb4fce2877df3702eb70cff009a20b84f94ca581b09f0c4840d51881af7702cf07a26e8a16f647739006ff0'
    },
)

# print json.loads(data.content)
if data.content:
    url = json.loads(data.content).get('data')[0].get('url')
    print url
    # download 1
    # urllib.urlretrieve(url, url.split('/')[-1])

    # download 2
    # r = requests.get(url)
    # with open(url.split('/')[-1], "wb") as code:
    #     code.write(r.content)

    # download 3
    f = urllib2.urlopen(url)
    with open(url.split('/')[-1], "wb") as code:
        code.write(f.read())
