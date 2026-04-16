#!/usr/bin/env python3

import re
import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    if re.search('fred', line):
        print(line)