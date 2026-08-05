#!/usr/bin/env python3

import re

s = input("string: ")
regex = input("regExx: ")

x = re.match(regex, s)
xx = re.search(regex, s)
xxx = re.findall(regex, s)

repl = input("Replacement: ")
xxxx = re.sub(regex, repl, s)

print(xxxx)
# print(xxxx.group())

# (base) ➜  week8 git:(master) ✗ python3 numbermatch.py 
# string: 22 alfred st sydney
# regExx: \d
# <re.Match object; span=(0, 1), match='2'>
# 2
# (base) ➜  week8 git:(master) ✗ 

# ====================== Error case ======================

# (base) ➜  week8 git:(master) ✗ python3 numbermatch.py
# string: NSW 2196 Sydney
# regExx: \d
# None
# Traceback (most recent call last):
#   File "/Users/kimjinkyeong/Desktop/stack_training/32547 Unix Programming/week8/numbermatch.py", line 11, in <module>
#     print(x.group())
#           ^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'group'
# (base) ➜  week8 git:(master) ✗ 

# ====================== Search ======================

# (base) ➜  week8 git:(master) ✗ python3 numbermatch.py
# string: NSW 2222 Syd
# regExx: \d
# <re.Match object; span=(4, 5), match='2'>
# 2
# (base) ➜  week8 git:(master) ✗ 

# ====================== Findall ======================

# (base) ➜  week8 git:(master) ✗ python3 numbermatch.py
# string: 13 Sydn St 3345 nsw
# regExx: \d
# ['1', '3', '3', '3', '4', '5']
# Traceback (most recent call last):
#   File "/Users/kimjinkyeong/Desktop/stack_training/32547 Unix Programming/week8/numbermatch.py", line 13, in <module>
#     print(xxx.group())
#           ^^^^^^^^^
# AttributeError: 'list' object has no attribute 'group'
# (base) ➜  week8 git:(master) ✗ 

# ====================== Replace ======================

# (base) ➜  week8 git:(master) ✗ python3 numbermatch.py
# string: 12 syd st 2244 nsw
# regExx: \d
# Replacement: _
# __ syd st ____ nsw
# (base) ➜  week8 git:(master) ✗ 

# (base) ➜  week8 git:(master) ✗ python3 numbermatch.py
# string: hello helllo hellllo
# regExx: (ll)
# Replacement: _
# he_o he_lo he__o
# (base) ➜  week8 git:(master) ✗ 

# (base) ➜  week8 git:(master) ✗ python3 numbermatch.py
# string: Tom and caterina have a cat
# regExx: cat*
# Replacement: HAT
# Tom and HATerina have a HAT
# (base) ➜  week8 git:(master) ✗ 

# (base) ➜  week8 git:(master) ✗ python3 numbermatch.py
# string: Carina has a cat
# regExx: cat*
# Replacement: HAT
# Carina has a HAT
# (base) ➜  week8 git:(master) ✗ 

# (base) ➜  week8 git:(master) ✗ python3 numbermatch.py
# string: carina has a cat 
# regExx: cat*
# Replacement: PAT
# PATrina has a PAT
# (base) ➜  week8 git:(master) ✗ 







