# just-translate

`just-translate`是一个调用百度翻译API进行翻译的小工具，使用本软件免费，但是使用者需要自行注册百度翻译开发者账户
注册地址:　http://api.fanyi.baidu.com/

`just-translate` is a free tool for translation via baidu api, you have to register a account at http://api.fanyi.baidu.com/ before using this software.

## 安装

`pip install .`

## 使用 (Usage)

1. `python -m just_translate -h`

```
-h  帮助
-u  更新账户信息
-s  [lang] 指定源语言类型
-d  [lang]     指定目标语言类型
    auto   : 自动检测
    zh     : 中文
    en     : 英文
    wym    : 文言文
    jp     : 日语
    cht    : 繁体中文
    ru     : 俄语
```

2. `python -m just_translate "hello"`

3. `python -m just_translate -d en "中文"`

4. `python -m just_translate -d zh "hello"`

```
正在查询:  hello
*********************************************
源语言：英文　｜　目标语言：中文
---------------------------------------------
hello
>>>
你好
*********************************************
```
