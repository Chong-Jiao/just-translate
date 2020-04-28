import os
import json

def encode(appid, secretKey):
    ''' 编码，简单的加密，用于示范
    '''
    appid = appid[-1] + appid[:-1]
    secretKey = secretKey[-1] + secretKey[:-1]
    return appid, secretKey

def decode(appid, secretKey):
    appid = appid[1:] + appid[0]
    secretKey = secretKey[1:] + secretKey[0]
    return appid, secretKey

def write_configure(appid, secretKey):
    thisfile = os.path.abspath(__file__)
    path, _ = os.path.split(thisfile)
    with open(os.path.join(path, 'configure.usr_data'), 'w', encoding='utf-8') as f:
        encoded_id, encoded_key = encode(appid, secretKey)
        json.dump({'appid':encoded_id, 'secretKey':encoded_key}, f)

def read_configure():
    thisfile = os.path.abspath(__file__)
    path, _ = os.path.split(thisfile)
    try:
        with open(os.path.join(path, 'configure.usr_data'), encoding='utf-8') as f:
            dict_file = json.load(f)
        encoded_id, encoded_key = dict_file.values()
        appid, secretKey = decode(encoded_id, encoded_key)
    except:
        appid, secretKey = None, None
    return appid, secretKey