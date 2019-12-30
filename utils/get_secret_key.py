#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : li
# @Email   : wytheli168@163.com
# @Time    : 19-12-30 下午2:46
# @Description: 博客参考： https://blog.csdn.net/guohewei123/article/details/99647528

import os
import base64
import random
import time
import hashlib

# 方法一
tmp = os.urandom(44)
secret_key = base64.b64encode(tmp)
# 生成长度为60的SECRET_KEY
print(secret_key)


# 方法二
def get_random_secret_key(length=12, allowed_chars=None, secret_key=None):
    """
    生成随机字符串
    :param length: 随机字符串长度
    :param allowed_chars: 随机字符串字符取值范围
    :param secret_key: 生成随机字符串的随机字符串
    :return:
    """
    if secret_key is None:
        secret_key = "n&^-9#k*-6pwzsjt-qsc@s3$l46k(7e%f80e7gx^f#vouf3yvz"
    if allowed_chars is None:
        allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

    random.seed(
        hashlib.sha256(
            ("%s%s%s" % (
                random.getstate(),
                time.time(),
                secret_key)).encode('utf-8')
        ).digest())
    ret = ''.join(random.choice(allowed_chars) for i in range(length))
    return ret


a = get_random_secret_key(50)
print(a)