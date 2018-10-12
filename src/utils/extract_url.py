#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 10:32:59 2018

@author: cznic
"""
import re
import sys
import os

if __name__ == "__main__":
    if len(sys.argv)>1 and os.path.isfile(sys.argv[1]):
        with open(sys.argv[1],"r") as fp:
            data=fp.read()
            url_list=re.findall(r'(https?://\S+)', data)
            print("\n".join(url_list))