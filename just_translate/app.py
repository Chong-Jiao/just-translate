import sys
from just_translate import translate 
from just_translate import read_configure
import time

def update_account():
    appid = input('appid>>')
    print('')
    secretKey = input('secretKey>>')
    print('')
    read_configure.write_configure(appid, secretKey)
    return appid, secretKey

def parse_arg(args):
    n = len(args)
    arg_dict={}
    i = 1
    while(i<n):
        if(args[i]=='-h'):
            arg_dict['h'] = 'help'
            break
        elif(args[i]=='-u'):
            arg_dict['u'] = 'update'
            i = i+1
        elif(args[i]=='-s'):
            arg_dict['s'] = args[i+1]
            i = i + 2
        elif(args[i]=='-d'):
            arg_dict['d'] = args[i+1]
            i = i + 2
        else:
            text = args[i:]
            return text, arg_dict
    return [], arg_dict

def run():
    args = sys.argv
    texts, arg_dict = parse_arg(args)

    if not(arg_dict.get('h') is None):
        print('-h  帮助')
        print('-u  更新账户信息')
        print('-s [lang]  指定源语言类型')
        print('-d [lang]  指定目标语言类型')
        
        for k, v in translate.language_list.items():
            print('    {:6} : {}'.format(k, v))
        exit()
    appid, secretKey = read_configure.read_configure()
    if((appid is None) or (secretKey is None)):
        print('首次使用，请输入账号信息\n')
        appid, secretKey = update_account()
    if not(arg_dict.get('u') is None):
        appid, secretKey = update_account()
    for text in texts:
        result = translate.translate(text,appid, secretKey, fromLang=arg_dict.get('s', 'auto'), toLang=arg_dict.get('d', 'zh'))
        translate.show_result(result)
        # sleep for next query，针对普通用户，每秒至多查询一次
        time.sleep(1)