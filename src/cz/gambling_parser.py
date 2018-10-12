#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Info:
These sites are Censored by Czech law number 186/2016 Sb, § 82.
Government Gazette http://aplikace.mvcr.cz/sbirka-zakonu/ViewFile.aspx?type=z&id=52826
"""

import requests
import json


resp = requests.get("https://blacklist.salamek.cz/api/blacklist")
blacklist = json.loads(resp.text)

print("url,category_code,category_description,date_added,source,notes")
for site in blacklist["data"]:
    url = "http://" + site["dns"]
    date = site["dns_date_published"].split("T")[0]
    print("%s,GMB,Gambling,%s,Czech Ministry of Finance," % (url, date))
