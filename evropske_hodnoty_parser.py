#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Czech disinformation news site (according to think tank Evropske hodnoty)
https://www.evropskehodnoty.cz/
"""

import requests
import re


def extract_url(site_url):
    resp = requests.get(site_url)
    m = re.search('<strong>WWW</strong>: <a href="(.+?)">', resp.text)
    if m:
        url = m.group(1)
        return url


resp = requests.get("https://www.evropskehodnoty.cz/fungovani-ceskych-dezinformacnich-webu/weby_list/")
m = re.findall('<td width="255"><a href="(.+?)">', resp.text, re.DOTALL)
print("url,category_code,category_description,date_added,source,notes")
for link in m:
    url = extract_url(link)
    date = "2016-07-26"
    note = "Think tank Evropske hodnoty,Czech disinformation news site (according to think tank Evropske hodnoty)"
    print("%s,NEWS,News Media,%s,%s" % (url, date, note))
