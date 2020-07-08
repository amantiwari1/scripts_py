#!/usr/bin/env python3
import sys
import os

txt = sys.argv[1]

with open(txt) as f:
  for line in f.readlines():
    old = line.strip()
    new = old.replace("jane","jdoe")
    os.system("mv {} {}".format(old, new))


f.close()
