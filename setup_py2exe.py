'''
Created on 2015/06/16

@author: yoshi
'''
# -*- coding: utf-8 -*- 

from distutils.core import setup

option = {
    "compressed"    :    1    ,
    "optimize"      :    2    ,
    "bundle_files"  :    1
}

setup(
    options = {
        "py2exe"    :    option
    },

    console = [
        {"script"   :    "conv_encoding_gui.pyw"}
    ],

    zipfile = None
)
