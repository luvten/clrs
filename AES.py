#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
import base64

#块大小，被加密块必须是这个值得倍数。
BLOCK_SIZE = 32

#秘钥长度，必须为16 (*AES-128*), 24 (*AES-192*), 32 (*AES-256*)字节长度。
KEY_LONG = 32

#用于补齐被加密块的长度不足BLOCK_SIZE倍数的部分。
BLOCK_PADDING = '{'

#用于补齐秘钥的长度不足KEY_LONG倍数的部分。
KEY_PADDING = '}'

#补齐
pad = lambda s, l, p: s + (l - len(s) % l) * p

#AES，默认采用ECB模式加密，先AES加密再，在进行base64编码，否则数据库识别不了。
EncryptAES = lambda k, s: base64.b64encode(AES.new(pad(k, KEY_LONG, KEY_PADDING)).encrypt(pad(s,BLOCK_SIZE,BLOCK_PADDING)))

#先进行base64解码，再AES解密，最后去掉补齐部分。
DecryptAES = lambda k, e: AES.new(pad(k, KEY_LONG, KEY_PADDING)).decrypt(base64.b64decode(e)).rstrip(BLOCK_PADDING)

#例子
if __name__ == '__main__':
    encoded = EncryptAES('secret_key', 'password')
    print 'Encrypted string:', encoded

    decoded = DecryptAES('secret_key', encoded)
    print 'Decrypted string:', decoded
