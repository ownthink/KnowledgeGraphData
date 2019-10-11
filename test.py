import sys
import csv

with open('ownthink_v2.csv', 'r', encoding='utf8') as fin:
  reader = csv.reader(fin)
  for index, read in enumerate(reader):
    print(read)
    
    if index > 10:
      sys.exit(0)