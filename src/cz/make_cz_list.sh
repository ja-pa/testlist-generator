#!/bin/bash

echo "Processing gambling sites..."
python3 gambling_parser.py>gambling.csv
echo "Processing fake news sites..."
python3 evropske_hodnoty_parser.py>eh_fakenews.csv

sed -i '/url,category_code,category_description,date_added,source,notes/d' ./gambling.csv
sed -i '/url,category_code,category_description,date_added,source,notes/d' ./eh_fakenews.csv


echo "Merging lists..."
echo "url,category_code,category_description,date_added,source,notes">cz.csv
cat gambling.csv>>cz.csv
cat eh_fakenews.csv>>cz.csv
cat others_sites.txt>>cz.csv

echo "Removing temp files"
rm gambling.csv>>cz.csv
rm eh_fakenews.csv>>cz.csv

echo "List: cz.csv"
