# coding:utf-8

import os

def run(**args):
    
    print("[*] In dirlister module.目录列表：")
    files = os.listdir(".") 
    
    return str(files)