# Python Programming Test — 32547 Unix Systems Programming

Programming exercises covering the Python content of weeks 7–12. For each task, write a script that satisfies the requirements. A reference solution is given immediately below.

---

## Tasks

**1.** Write a Python script that uses the most portable shebang line and, when run directly (`./hello.py`), prints `Hello, Unix`.

```python
#!/usr/bin/env python3
print("Hello, Unix")
```

---

**2.** Take exactly two command-line arguments and print them concatenated as strings (no space, no separator).
Example: `python3 script.py 10 20` → `1020`

```python
import sys
print(sys.argv[1] + sys.argv[2])
```

---

**3.** Demonstrate the difference between mutable and immutable types: build a list and append to it, then build a tuple of the same elements and show that mutation fails. Print both objects and any exception message.

```python
nums = [1, 2, 3]
nums.append(4)
print(nums)

t = (1, 2, 3)
try:
    t.append(4)
except AttributeError as e:
    print("tuple is immutable:", e)
print(t)
```

---

**4.** Given the string `"error 42 occurred at line 7"`, extract every run of digits and print them as a list of strings.

```python
import re
text = "error 42 occurred at line 7"
print(re.findall(r"\d+", text))
```

---

**5.** Read a line from stdin. Print `start` if the pattern `world` is at the very beginning of the line, `inside` if it appears anywhere else, and `none` if it does not appear at all. Use `re.match` and `re.search`.

```python
import re, sys
line = sys.stdin.readline().rstrip("\n")
if re.match(r"world", line):
    print("start")
elif re.search(r"world", line):
    print("inside")
else:
    print("none")
```

---

**6.** Read usernames from stdin (one per line). Print the count of distinct usernames using a `set`.

```python
import sys
names = {line.strip() for line in sys.stdin if line.strip()}
print(len(names))
```

---

**7.** Define a function `append_value(lst, value)` that appends to a list. Demonstrate that the change is visible to the caller by printing the list after the call.

```python
def append_value(lst, value):
    lst.append(value)

nums = [1, 2, 3]
append_value(nums, 99)
print(nums)
```

---

**8.** Append the line `service started` (with newline) to `system.log` without overwriting any existing content. The script must succeed whether or not the file already exists.

```python
with open("system.log", "a", encoding="utf-8") as f:
    f.write("service started\n")
```

---

**9.** Serialize the dictionary `{"name": "alice", "uid": 1001}` to a file `user.json` as JSON.

```python
import json
with open("user.json", "w", encoding="utf-8") as f:
    json.dump({"name": "alice", "uid": 1001}, f)
```

---

**10.** Fork a child process. The child must print `child PID=<its-pid>` and exit. The parent must print `parent PID=<its-pid> child=<child-pid>` and `wait` for the child.

```python
import os
pid = os.fork()
if pid == 0:
    print(f"child PID={os.getpid()}")
    os._exit(0)
else:
    print(f"parent PID={os.getpid()} child={pid}")
    os.wait()
```

---

**11.** Given `s = "Unix Programming"`, print the substring covering indices 5 through 11 inclusive.

```python
s = "Unix Programming"
print(s[5:12])
```

---

**12.** Create two list objects with equal values but different identities, plus a third name that aliases the first. Print, for both pairs, the result of `==` and `is`.

```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b)
print(a == c, a is c)
```

---

**13.** Print the result of comparing the integer `10` and the string `"10"` with both `==` and `is`.

```python
x, y = 10, "10"
print(x == y, x is y)
```

---

**14.** Read a float from stdin and print it formatted with exactly 2 decimal places, prefixed by `pi = `.

```python
value = float(input())
print(f"pi = {value:.2f}")
```

---

**15.** Read an integer `N` from `sys.argv[1]` and print the sum of all integers from 1 to `N` inclusive.

```python
import sys
n = int(sys.argv[1])
print(sum(range(1, n + 1)))
```

---

**16.** Read a single line from stdin and print `valid` if it matches a basic email pattern (`word@word.word`), otherwise `invalid`.

```python
import re, sys
line = sys.stdin.readline().strip()
print("valid" if re.fullmatch(r"\w+@\w+\.\w+", line) else "invalid")
```

---

**17.** Read a line and replace any run of whitespace with a single underscore. Print the result.

```python
import re
print(re.sub(r"\s+", "_", input()))
```

---

**18.** Count the occurrences of the **whole word** `cat` (not `category`, not `concat`) in `"the cat sat on the cathedral, concatenate"`.

```python
import re
text = "the cat sat on the cathedral, concatenate"
print(len(re.findall(r"\bcat\b", text)))
```

---

**19.** On the input `"<a><b>"`, print the result of a greedy match `r"<.*>"` and a non-greedy match `r"<.*?>"`.

```python
import re
s = "<a><b>"
print(re.search(r"<.*>", s).group())
print(re.search(r"<.*?>", s).group())
```

---

**20.** Reverse the list `[1, 2, 3, 4, 5]` using slicing (no `.reverse()` and no `reversed()`).

```python
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
```

---

**21.** Given `A = {1, 2, 3, 4}` and `B = {3, 4, 5}`, print the elements that are in `A` but not in `B`.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5}
print(A - B)
```

---

**22.** Given the tuple `("alice", 1001, "/bin/bash")`, unpack it into `user, uid, shell` and print only `uid`.

```python
record = ("alice", 1001, "/bin/bash")
user, uid, shell = record
print(uid)
```

---

**23.** Given `d = {"a": 1, "b": 2}`, look up the key `"c"` with a default of `0` so that no `KeyError` is raised.

```python
d = {"a": 1, "b": 2}
print(d.get("c", 0))
```

---

**24.** Write a function `total(*nums)` that returns the sum of all positional arguments. Demonstrate it on `total(1, 2, 3, 4)`.

```python
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))
```

---

**25.** Write a function `greet(**kwargs)` that returns the value associated with the keyword `name`, or `"anon"` if no such keyword was given. Demonstrate it on `greet(name="bob")` and `greet()`.

```python
def greet(**kwargs):
    return kwargs.get("name", "anon")

print(greet(name="bob"))
print(greet())
```

---

**26.** Create a new file `new.txt` and write `first` to it — but only if the file does not already exist. If it does, print `already exists`. Use the exclusive open mode.

```python
try:
    with open("new.txt", "x", encoding="utf-8") as f:
        f.write("first")
except FileExistsError:
    print("already exists")
```

---

**27.** Pack the integer `7` and the float `3.14` into one bytes object using `struct` with format `"if"`. Print the byte length and the bytes.

```python
import struct
data = struct.pack("if", 7, 3.14)
print(len(data), data)
```

---

**28.** Open `data.txt`, read its full content, then `seek(0)` back to the start and read it again. Verify the two reads are equal.

```python
with open("data.txt", "r", encoding="utf-8") as f:
    first = f.read()
    f.seek(0)
    second = f.read()
print(first == second)
```

---

**29.** Print the contents of `notes.txt`. If the file is missing, print `missing` instead of crashing.

```python
try:
    with open("notes.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("missing")
```

---

**30.** Print the full path of every regular file under the current directory, recursively.

```python
import os
for dirpath, _, files in os.walk("."):
    for name in files:
        print(os.path.join(dirpath, name))
```

---

**31.** Read two integers `a` and `b` from CLI args. Print `a // b`, `a % b`, and `a ** b` separated by spaces.

```python
import sys
a, b = int(sys.argv[1]), int(sys.argv[2])
print(a // b, a % b, a ** b)
```

---

**32.** Prompt the user with `> ` and echo the input back, prefixed with `you typed: `.

```python
line = input("> ")
print("you typed:", line)
```

---

**33.** Strip leading/trailing whitespace from `"  hello  "` and print the result.

```python
print("  hello  ".strip())
```

---

**34.** Print whether `"x"` is in `"unix"` and whether `"z"` is **not** in `"unix"`, separated by a space.

```python
print("x" in "unix", "z" not in "unix")
```

---

**35.** Split `"a,b,c"` on commas and print the resulting list.

```python
print("a,b,c".split(","))
```

---

**36.** Print the result of `True and False or True`. Add a comment explaining which operator binds tighter.

```python
# `and` binds tighter than `or`: (True and False) or True → False or True → True
print(True and False or True)
```

---

**37.** Write a function `report(status)` that uses `match-case` and returns `"OK"` for `"running"`, `"OFF"` for `"stopped"`, and `"UNKNOWN"` for anything else. Print the result for each.

```python
def report(status):
    match status:
        case "running":
            return "OK"
        case "stopped":
            return "OFF"
        case _:
            return "UNKNOWN"

for s in ["running", "stopped", "broken"]:
    print(report(s))
```

---

**38.** Use a `while` loop to find the first integer `i` (starting at 0) such that `i == 3`, then print `i`. Use `break` to exit.

```python
i = 0
while i < 5:
    if i == 3:
        break
    i += 1
print(i)
```

---

**39.** Sum the odd integers in `range(1, 6)` using a `for` loop and `continue` to skip even numbers. Print the total.

```python
total = 0
for n in range(1, 6):
    if n % 2 == 0:
        continue
    total += n
print(total)
```

---

**40.** Tokenize `"one  two   three"` on any run of whitespace using `re.split` and print the resulting list.

```python
import re
print(re.split(r"\s+", "one  two   three"))
```

---

**41.** Use a regex with two capture groups to extract the user name and host from `"user@host"`. Print them on one line separated by a space.

```python
import re
m = re.search(r"(\w+)@(\w+)", "user@host")
print(m.group(1), m.group(2))
```

---

**42.** Print every match of the regex `a{2,4}` in `"a aa aaa aaaa aaaaa"`.

```python
import re
print(re.findall(r"a{2,4}", "a aa aaa aaaa aaaaa"))
```

---

**43.** Sort the list `[3, 1, 2]` in place using `.sort()` and print the resulting list.

```python
nums = [3, 1, 2]
nums.sort()
print(nums)
```

---

**44.** Iterate the dictionary `{"a": 1, "b": 2}` and print each key/value pair on its own line.

```python
d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)
```

---

**45.** Write a function `min_max(nums)` that returns both the minimum and the maximum as a tuple. Print both values for `[3, 1, 4, 1, 5]`.

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)
```

---

**46.** Write a function `greet(name, greeting="Hello")` that returns `"<greeting>, <name>"`. Call it as `greet("Bob")` and print the result.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Bob"))
```

---

**47.** Read all lines of `data.txt` into a list and print the line count.

```python
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(len(lines))
```

---

**48.** Encode the string `"unix"` to UTF-8 bytes and print the resulting bytes object.

```python
print("unix".encode("utf-8"))
```

---

**49.** Pack `7` and `3.14` with `struct.pack("if", 7, 3.14)`, then unpack the bytes back into `(int, float)` and print them.

```python
import struct
data = struct.pack("if", 7, 3.14)
n, x = struct.unpack("if", data)
print(n, x)
```

---

**50.** Create a TCP (IPv4) socket. Print its `family` and `type` attributes, then close it.

```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s.family, s.type)
s.close()
```

---

**51.** Print the type object of the integer literal `42`.

```python
print(type(42))
```

---

**52.** Print the number of characters in the string `"Unix"`.

```python
print(len("Unix"))
```

---

**53.** Print the string `"ab"` repeated three times concatenated together.

```python
print("ab" * 3)
```

---

**54.** For each value in `[0, "", [], "0", None, [0]]`, print the value and whether it is truthy.

```python
for v in [0, "", [], "0", None, [0]]:
    print(repr(v), bool(v))
```

---

**55.** Read an integer `n` from stdin and print whether `1 < n < 10` (using a chained comparison).

```python
n = int(input())
print(1 < n < 10)
```

---

**56.** Read two strings from CLI args, convert them to integers, and print their sum.

```python
import sys
print(int(sys.argv[1]) + int(sys.argv[2]))
```

---

**57.** Read a line from stdin and print it in upper case.

```python
print(input().upper())
```

---

**58.** Replace every `'l'` in `"hello"` with `'L'` and print the result.

```python
print("hello".replace("l", "L"))
```

---

**59.** Print whether `"unix systems"` starts with `"unix"`.

```python
print("unix systems".startswith("unix"))
```

---

**60.** Print the index of the first occurrence of `'z'` in `"abc"` using `.find()` (must print `-1`).

```python
print("abc".find("z"))
```

---

**61.** Initialise `x = 5`, increment it by 3 using `+=`, then print `x`.

```python
x = 5
x += 3
print(x)
```

---

**62.** Iterate the string `"ab"` with `enumerate` and print each `index value` pair on its own line.

```python
for i, ch in enumerate("ab"):
    print(i, ch)
```

---

**63.** Print all even numbers from 0 (inclusive) to 10 (exclusive) using `range` with step 2 — print as a list.

```python
print(list(range(0, 10, 2)))
```

---

**64.** Given `m = [[1, 2], [3, 4]]`, print the element at row 1, column 0.

```python
m = [[1, 2], [3, 4]]
print(m[1][0])
```

---

**65.** Demonstrate that `list.append` returns `None` (not the new list) by printing both the call's return value and the modified list.

```python
nums = [1, 2, 3]
print(nums.append(5))
print(nums)
```

---

**66.** Start with the list `[1, 2]`, extend it with `[3, 4]`, and print the result. (Use `extend`, not `+`.)

```python
a = [1, 2]
a.extend([3, 4])
print(a)
```

---

**67.** Pop the last element from `[10, 20, 30]`. Print the popped value and the remaining list.

```python
nums = [10, 20, 30]
last = nums.pop()
print(last, nums)
```

---

**68.** Show that `dict.keys()` is a *view*: capture `keys = d.keys()`, mutate `d`, then print the keys after the mutation.

```python
d = {"a": 1}
keys = d.keys()
d["b"] = 2
print(list(keys))
```

---

**69.** Print whether the key `"a"` is in the dict `{"a": 1, "b": 2}`.

```python
print("a" in {"a": 1, "b": 2})
```

---

**70.** Start with `d = {"a": 1}`, call `d.update({"b": 2, "a": 99})`, then print `d`.

```python
d = {"a": 1}
d.update({"b": 2, "a": 99})
print(d)
```

---

**71.** Start with the set `{1, 2}`, add `2` again, then add `3`. Print the resulting set.

```python
s = {1, 2}
s.add(2)
s.add(3)
print(s)
```

---

**72.** Print the intersection of `{1, 2, 3}` and `{2, 3, 4}` using the `&` operator.

```python
print({1, 2, 3} & {2, 3, 4})
```

---

**73.** Build a tuple containing only the integer `1`. Print its `type` and `len`.

```python
t = (1,)
print(type(t), len(t))
```

---

**74.** Pair `[1, 2, 3]` with `["a", "b", "c"]` using `zip` and print the result as a list of tuples.

```python
print(list(zip([1, 2, 3], ["a", "b", "c"])))
```

---

**75.** Sort the list `["bb", "a", "ccc"]` ascending by string length using `sorted` with a key function.

```python
print(sorted(["bb", "a", "ccc"], key=len))
```

---

**76.** Define a `lambda` that multiplies two numbers, call it with `3` and `4`, and print the result.

```python
mul = lambda x, y: x * y
print(mul(3, 4))
```

---

**77.** Define a module-level counter `count = 0` and a function `inc()` that uses `global` to increment it. Call `inc()` twice and print the final counter.

```python
count = 0

def inc():
    global count
    count += 1

inc()
inc()
print(count)
```

---

**78.** Define a function `noop()` whose body is just `return` (no value), call it, and print the returned value.

```python
def noop():
    return

print(noop())
```

---

**79.** Define a function `todo()` whose body is just `pass`, call it, and print `ok`.

```python
def todo():
    pass

todo()
print("ok")
```

---

**80.** Print the lengths of the raw string `r"\n"` and the regular string `"\n"` separated by a space.

```python
print(len(r"\n"), len("\n"))
```

---

**81.** Extract every run of lowercase letters from `"Hello World"` using a regex with the character class `[a-z]+`.

```python
import re
print(re.findall(r"[a-z]+", "Hello World"))
```

---

**82.** Read a line from stdin and print whether it starts with `abc` (use a regex anchored with `^`).

```python
import re
line = input()
print(bool(re.match(r"^abc", line)))
```

---

**83.** For each word in `["color", "colour", "colr"]`, print whether it matches the pattern `colou?r` (full match).

```python
import re
for word in ["color", "colour", "colr"]:
    print(word, bool(re.fullmatch(r"colou?r", word)))
```

---

**84.** Show the difference between `\d+` and `\d*` against the empty string by printing `re.fullmatch` for each.

```python
import re
print(re.fullmatch(r"\d+", ""))
print(re.fullmatch(r"\d*", ""))
```

---

**85.** Find the first run of digits in `"abc123def"` and print the start index.

```python
import re
m = re.search(r"\d+", "abc123def")
print(m.start())
```

---

**86.** Search `"abc"` for `"xyz"` and print whether the result is `None`.

```python
import re
print(re.search(r"xyz", "abc") is None)
```

---

**87.** Case-insensitively check whether `"Unix"` matches the pattern `unix` and print the boolean result.

```python
import re
print(bool(re.search(r"unix", "Unix", re.IGNORECASE)))
```

---

**88.** Read the entire contents of `data.txt` into a single string and print the character count.

```python
with open("data.txt", "r", encoding="utf-8") as f:
    data = f.read()
print(len(data))
```

---

**89.** Iterate `data.txt` line by line and print each line **without** its trailing newline.

```python
with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip("\n"))
```

---

**90.** Open `data.txt`, read 5 characters, then print the current file position via `tell()`.

```python
with open("data.txt", "r", encoding="utf-8") as f:
    f.read(5)
    print(f.tell())
```

---

**91.** Build the path `dir/file.txt` portably with `os.path.join` and print it.

```python
import os
print(os.path.join("dir", "file.txt"))
```

---

**92.** Print whether the path `data.txt` is a regular file (not a directory).

```python
import os
print(os.path.isfile("data.txt"))
```

---

**93.** Read `users.csv` with the `csv` module and print every row as a list of strings.

```python
import csv
with open("users.csv", "r", newline="", encoding="utf-8") as f:
    for row in csv.reader(f):
        print(row)
```

---

**94.** Parse the JSON string `'{"name": "alice"}'` with `json.loads`, then read and parse `user.json` with `json.load`. Print both results.

```python
import json
print(json.loads('{"name": "alice"}'))
with open("user.json", "r", encoding="utf-8") as f:
    print(json.load(f))
```

---

**95.** Open `data.bin` in binary read mode and print the first 4 bytes.

```python
with open("data.bin", "rb") as f:
    print(f.read(4))
```

---

**96.** Pack the integer `7` as a 4-byte signed int with format `"i"`, unpack the result, and print it.

```python
import struct
data = struct.pack("i", 7)
print(struct.unpack("i", data))
```

---

**97.** Print the current process's PID.

```python
import os
print(os.getpid())
```

---

**98.** Build an `os.pipe`, fork. The child writes `hello` to the write end and exits. The parent reads from the read end and prints the decoded message.

```python
import os
r, w = os.pipe()
if os.fork() == 0:
    os.close(r)
    os.write(w, b"hello")
    os.close(w)
    os._exit(0)
else:
    os.close(w)
    print(os.read(r, 100).decode())
    os.close(r)
    os.wait()
```

---

**99.** Register a SIGINT handler that prints `interrupted` (without exiting). Then sleep for up to 5 seconds. (User can press Ctrl+C to test.)

```python
import signal, time
def handler(signum, frame):
    print("interrupted")

signal.signal(signal.SIGINT, handler)
time.sleep(5)
```

---

**100.** Write a TCP server that listens on `127.0.0.1:9000`, accepts one connection, echoes back up to 1024 bytes, then closes.

```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("127.0.0.1", 9000))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        conn.sendall(data)
```

---

**101.** Print `a`, `b`, `c` separated by `-` instead of the default space.

```python
print("a", "b", "c", sep="-")
```

---

**102.** Read an integer `n` and print `even` or `odd` using a single ternary (conditional) expression.

```python
n = int(input())
print("even" if n % 2 == 0 else "odd")
```

---

**103.** Print the character whose Unicode code point is `65`, then print the code point of `"A"`.

```python
print(chr(65))
print(ord("A"))
```

---

**104.** Print the sum of `[1, 2, 3]`.

```python
print(sum([1, 2, 3]))
```

---

**105.** Print `round(3.7)`.

```python
print(round(3.7))
```

---

**106.** Print quotient and remainder of `17 / 5` using `divmod`.

```python
print(divmod(17, 5))
```

---

**107.** Join the list `["a", "b", "c"]` with `-` and print the resulting string.

```python
print("-".join(["a", "b", "c"]))
```

---

**108.** Use `str.format` with two positional placeholders to produce `nginx and redis`. Print it.

```python
print("{} and {}".format("nginx", "redis"))
```

---

**109.** Use printf-style `%` formatting to produce `User: alice, UID: 1001`.

```python
print("User: %s, UID: %d" % ("alice", 1001))
```

---

**110.** Print `not (3 > 5)`.

```python
print(not (3 > 5))
```

---

**111.** Iterate `range(3)` with a `for-else`. The `else` clause must print `completed` because the loop ends without `break`.

```python
for n in range(3):
    if n == 5:
        break
else:
    print("completed")
```

---

**112.** Print every pair `(i, j)` for `i` in `range(2)` and `j` in `range(3)` on a single line, space-separated.

```python
for i in range(2):
    for j in range(3):
        print(i, j, end=" ")
print()
```

---

**113.** Run `re.findall(r"(\d+)-(\d+)", "1-2 and 3-4")` and print the result.

```python
import re
print(re.findall(r"(\d+)-(\d+)", "1-2 and 3-4"))
```

---

**114.** With `re.MULTILINE`, find every line that **starts** with `ERROR` in a multi-line string.

```python
import re
text = "ERROR: a\nINFO: b\nERROR: c"
print(re.findall(r"^ERROR.*", text, re.MULTILINE))
```

---

**115.** Use a regex with a backreference `\1` to find any immediately repeated word in `"hello hello world"`.

```python
import re
print(re.findall(r"\b(\w+) \1\b", "hello hello world"))
```

---

**116.** Use a non-capturing group `(?:...)` to match either `cat` or `dog` followed by `s`. Print all matches in `"cats dogs fish"`.

```python
import re
print(re.findall(r"(?:cat|dog)s", "cats dogs fish"))
```

---

**117.** Find all occurrences of `cat` or `dog` (alternation) in `"a cat and a dog"` and print them.

```python
import re
print(re.findall(r"cat|dog", "a cat and a dog"))
```

---

**118.** Count the literal dot characters in `"127.0.0.1"` using a regex with `\.`.

```python
import re
print(len(re.findall(r"\.", "127.0.0.1")))
```

---

**119.** Make an independent copy of `[1, 2, 3]` with `.copy()`, append `4` to the copy, and print both lists.

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a, b)
```

---

**120.** Delete the element at index 1 of `[10, 20, 30]` with `del`. Print the resulting list.

```python
nums = [10, 20, 30]
del nums[1]
print(nums)
```

---

**121.** Print the maximum value of `[3, 1, 4, 1, 5, 9]`.

```python
print(max([3, 1, 4, 1, 5, 9]))
```

---

**122.** Use `any()` to check whether `[0, "", None, "hello"]` contains any truthy value. Print the result.

```python
print(any([0, "", None, "hello"]))
```

---

**123.** Given `d = {"a": 1, "b": 2}`, print its values as a list.

```python
d = {"a": 1, "b": 2}
print(list(d.values()))
```

---

**124.** Given `d = {"a": 1}`, attempt to pop key `"x"` with a default of `None` (must not raise). Print both the popped value and the dict.

```python
d = {"a": 1}
print(d.pop("x", None))
print(d)
```

---

**125.** Show that `set.discard` does not raise on a missing element while `set.remove` does. Use `try/except`.

```python
s = {1, 2}
s.discard(99)  # silent
try:
    s.remove(99)
except KeyError:
    print("KeyError on remove")
```

---

**126.** Print whether `{1, 2}` is a subset of `{1, 2, 3}` using `.issubset`.

```python
print({1, 2}.issubset({1, 2, 3}))
```

---

**127.** Print the union of `{1, 2}` and `{3, 4}` using the `.union()` method (not the `|` operator).

```python
print({1, 2}.union({3, 4}))
```

---

**128.** Unpack `[1, 2, 3, 4]` into `a` (first element) and `b` (the rest as a list) using starred unpacking. Print both.

```python
a, *b = [1, 2, 3, 4]
print(a, b)
```

---

**129.** Rewrite the function `add_item(item, items=[])` so the default does **not** persist between calls. Demonstrate by calling it twice with different items and showing each call returns a fresh list.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items

print(add_item("a"))
print(add_item("b"))
```

---

**130.** Write a recursive `factorial(n)` and print `factorial(5)`.

```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

print(factorial(5))
```

---

**131.** Define an `outer()` function that contains a nested `inner()` returning `"hi"`. Call `inner` from `outer` and print the result.

```python
def outer():
    def inner():
        return "hi"
    return inner()

print(outer())
```

---

**132.** Swap two variables `x = 10` and `y = 20` using tuple packing and unpacking, then print them.

```python
x, y = 10, 20
x, y = y, x
print(x, y)
```

---

**133.** Write `apply(fn, x)` that returns `fn(x)`. Pass `str.upper` as `fn` and `"unix"` as `x`, and print the result.

```python
def apply(fn, x):
    return fn(x)

print(apply(str.upper, "unix"))
```

---

**134.** Write `"hello"` to a file `out.txt` and print the integer returned by `file.write` (the number of characters).

```python
with open("out.txt", "w", encoding="utf-8") as f:
    n = f.write("hello")
print(n)
```

---

**135.** Delete the file `tmp.txt`. If it does not exist, print `missing` instead of crashing.

```python
import os
try:
    os.remove("tmp.txt")
except FileNotFoundError:
    print("missing")
```

---

**136.** Print the size in bytes of the file `data.txt` using `os.path.getsize`.

```python
import os
print(os.path.getsize("data.txt"))
```

---

**137.** Print the basename of the path `/home/user/data.txt`.

```python
import os
print(os.path.basename("/home/user/data.txt"))
```

---

**138.** Split `report.csv` into a `(root, ext)` pair using `os.path.splitext` and print it.

```python
import os
print(os.path.splitext("report.csv"))
```

---

**139.** Create the directory tree `a/b/c` even when intermediate directories don't exist. Re-running the script must not crash.

```python
import os
os.makedirs("a/b/c", exist_ok=True)
```

---

**140.** Pack the float `3.14` as an 8-byte double with format `"d"`, unpack it back, and print both the byte length and the recovered value.

```python
import struct
data = struct.pack("d", 3.14)
print(len(data), struct.unpack("d", data))
```

---

**141.** Compute and print the SHA-256 hex digest of the bytes `b"unix"`.

```python
import hashlib
print(hashlib.sha256(b"unix").hexdigest())
```

---

**142.** Demonstrate that `bytes` is immutable but `bytearray` is mutable: try to assign to index 0 of each.

```python
b = bytes(b"abc")
try:
    b[0] = 65
except TypeError:
    print("bytes immutable")

ba = bytearray(b"abc")
ba[0] = 65
print(ba)
```

---

**143.** Caesar-shift an uppercase string by `n` with wrap-around (so `Z + 1` becomes `A`). Apply shift `3` to `"XYZ"` and print the result.

```python
def shift(s, n):
    return "".join(
        chr((ord(c) - ord("A") + n) % 26 + ord("A")) for c in s
    )

print(shift("XYZ", 3))
```

---

**144.** Print the current process's parent PID using `os.getppid`.

```python
import os
print(os.getppid())
```

---

**145.** Fork a child that exits with status 0. In the parent, `waitpid` for it and print its exit status (the value returned by `os.WEXITSTATUS`).

```python
import os
pid = os.fork()
if pid == 0:
    os._exit(0)
else:
    _, status = os.waitpid(pid, 0)
    print("child exited:", os.WEXITSTATUS(status))
```

---

**146.** Fork a child that loops forever sleeping. In the parent, sleep briefly, then send `SIGTERM` to the child with `os.kill` and reap it.

```python
import os, signal, time
pid = os.fork()
if pid == 0:
    while True:
        time.sleep(1)
else:
    time.sleep(0.5)
    os.kill(pid, signal.SIGTERM)
    os.waitpid(pid, 0)
```

---

**147.** Run `echo hello` via `subprocess.run`, capture its stdout as a string, and print it stripped of trailing whitespace.

```python
import subprocess
r = subprocess.run(["echo", "hello"], capture_output=True, text=True)
print(r.stdout.strip())
```

---

**148.** Use `multiprocessing.Process` to spawn a child that prints `n * 2` for `n = 5`. Wait for it.

```python
from multiprocessing import Process

def task(n):
    print(n * 2)

if __name__ == "__main__":
    p = Process(target=task, args=(5,))
    p.start()
    p.join()
```

---

**149.** Connect a TCP client to `127.0.0.1:9000`, send `b"ping"`, receive up to 1024 bytes, and print the decoded response.

```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 9000))
    s.sendall(b"ping")
    data = s.recv(1024)
print(data.decode())
```

---

**150.** Write a tiny UDP echo server bound to `127.0.0.1:9001`. Receive one datagram with `recvfrom` and send it back to the sender with `sendto`.

```python
import socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(("127.0.0.1", 9001))
    data, addr = s.recvfrom(1024)
    s.sendto(data, addr)
```

---
