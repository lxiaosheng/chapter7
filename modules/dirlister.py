# coding:utf-8

import os

def run(**args):
    
    print "[*] In dirlister module.目录列表："
    files = os.listdir(".")  #当前目录
    
    return str(files)

#print run()