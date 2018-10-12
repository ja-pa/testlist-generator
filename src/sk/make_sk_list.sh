#!/bin/bash

#Remove old data
[ -d "www.financnasprava.sk" ] && rm -rf www.financnasprava.sk

echo "Downloading list..."
wget -r -A.pdf https://www.financnasprava.sk/sk/elektronicke-sluzby/verejne-sluzby/zoznamy/zoznam-zakazanych-webov

echo "Converting to text..."
find ./ -name "*.pdf" -exec echo {} \;|xargs pdftotext

echo "Parsing url..."
text_path=$(find ./ -name "*.txt" -exec echo {} \;|xargs realpath)
../utils/extract_url.py $text_path>url_list.txt

echo "---------------------------"
date_item=$(date +%Y-%m-%d)


echo "url,category_code,category_description,date_added,source,notes">sk.csv
while read p; do
  echo "$p"
  echo "$p,GMB,Gambling,$date_item,Financial Administration Slovak Republic,">>sk.csv
done <url_list.txt
