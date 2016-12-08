# -*- coding: utf-8 -*-
import ctypes
import os

if __name__ == '__main__':
    fp = open('test.jpg','rb')
    data = fp.read()
    datalen=len(data)
    easypr=ctypes.CDLL("easyprpy.dll")
    modelpath=os.path.join("../model")
    ptr=easypr.init(modelpath)
    easypr.plateRecognize.restype=ctypes.c_char_p
    st=easypr.plateRecognize(ptr,data,datalen)
    easypr.deleteptr(ptr)
    print st