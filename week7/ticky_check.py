#!/usr/bin/env python3
import re
import sys

def get_txt(file):
    txt_list = []
    with open(file) as f:
      for line in f.readlines():
          txt_list.append(line.strip())
    return txt_list
def findall(data, name):
    for line in data:
        result = re.search(r"ticky: {} ([\w ]*) ".format(name), line)
        if result is not None:
           print(result.group(0))


file = sys.argv[1]

data = get_txt(file)

findall(data, "ERROR")
