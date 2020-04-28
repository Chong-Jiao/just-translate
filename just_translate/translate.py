#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json
import time

language_list = {'auto':'自动检测',
'zh':'中文', 'en':'英文', 'wym':'文言文',
'jp':'日语', 'cht':'繁体中文', 'ru':'俄语'}

def translate(q, appid,secretKey, toLang = 'zh', fromLang = 'auto'):
    print('正在查询: ', q)
       
    httpClient = None
    myurl = '/api/trans/vip/translate'
    
    #fromLang = 'auto'   #原文语种
    #toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    #q= 'apple'
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
    
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
    
        return result
    
    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()

def show_result(result):
    if(result is None):
        print('查询失败')
    #print('|翻译结果|')
    print('***'*15)
    print('源语言：{}　｜　目标语言：{}'.format(language_list[result['from']], language_list[result['to']]))
    print('---'*15)
    result_list = result['trans_result']
    for x in result_list:
        try:
            print(x['src'])
            print('>>>')
            print(x['dst'])
        except:
            print('')
    print('***'*15)
