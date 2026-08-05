# [user@sahara ~]$ python3
# Python 3.14.3 (main, Feb 13 2026, 15:31:44) [GCC 15.2.1 20260209] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import re
# >>> re.search("cat", "the cat sat on the mat",)
# <re.Match object; span=(4, 7), match='cat'>
# >>> re.match("cat", "the cat sat on the mat")
# >>> re.match("cat", "cat sat on the mat")
# <re.Match object; span=(0, 3), match='cat'>
# >>> re.match("cat", "cat sat on the mat cat")
# <re.Match object; span=(0, 3), match='cat'>
# >>> re.match("cat", "cat sat on the mat")
# <re.Match object; span=(0, 3), match='cat'>
# >>> re.search("CAT", "the cat sat on the mat")
# >>> re.search("CAT", "the cat sat on the mat", re.IGNORECASE)
# <re.Match object; span=(4, 7), match='cat'>
# >>> re.split(" ", "the cat sat on the mat")
# ['the', 'cat', 'sat', 'on', 'the', 'mat']
# >>> re.split(" ", "the    cat sat on the mat")
# ['the', '', '', '', 'cat', 'sat', 'on', 'the', 'mat']
# >>> re.split(" +", "the    cat sat on the mat")
# ['the', 'cat', 'sat', 'on', 'the', 'mat']
# >>> re.split(r" +", "the    cat sat on the mat")
# ['the', 'cat', 'sat', 'on', 'the', 'mat']
# >>> re.findall("bag", "the bag is inside another bag")
# ['bag', 'bag']
# >>> re.findall("bag", "there is a bug inside the big bag")
# ['bag']
# >>> re.findall("b.g", "there is a bug inside the big bag")
# ['bug', 'big', 'bag']
# >>> re.sub("b.g", "cat", "there is a bug inside the big bag")
# 'there is a cat inside the cat cat'
# >>> re.sub("b.g", "cat", "there is a bug inside the big bag", flags=re.IGNORECASE)
# 'there is a cat inside the cat cat'
# >>> re.sub("b.g", "cat", "there is a BUG inside the big bag", flags=re.IGNORECASE)
# 'there is a cat inside the cat cat'
# >>> re.search("cat", "the cat sat on the mat")
# <re.Match object; span=(4, 7), match='cat'>
# >>> m = re.search("cat", "the cat sat on the mat")
# >>> m
# <re.Match object; span=(4, 7), match='cat'>
# >>> m.start()
# 4
# >>> print(f"the match was found at position {m.start()}")
# the match was found at position 4
# >>> 