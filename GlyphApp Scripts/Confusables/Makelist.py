#MenuTitle: Sort unicode list
# -*- coding: utf-8 -*-
__doc__="""
Sort and clean the unicode confusables list
"""

# 
# https://twitter.com/luke_prowse
#

import codecs

fd = codecs.open('data_confusables.txt','r')
data = fd.read().splitlines()
fd.close()
#presets = data.split("\n")

totalLines = str(len(data))

counter = 0
sorted_lines = list()

sortst = "#\t"

for li in data:
    if li.find(sortst) != -1: # \t = tab
    	li = li.strip(sortst)
        counter+=1
        sorted_lines.append(li)

f= open("data_confusables-sorted.txt","w+")
for i in sorted_lines:
    f.write(i + "\n")
f.close() 


wlist = ""