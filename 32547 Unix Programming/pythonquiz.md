# Python Quiz — 32547 Unix Systems Programming

Practice multiple-choice questions covering the Python content of weeks 7–12.

---

## Questions

**1.** Which of the following is the most portable shebang line for a Python script intended to run on multiple Unix systems?

A. `#!python3`
B. `#!/usr/local/bin/python`
C. `#!/usr/bin/env python3`
D. `#!/bin/python3`

---

**2.** Given the script:

```python
import sys
print(sys.argv[1] + sys.argv[2])
```

It is run as: `python3 script.py 10 20`. What is printed?

A. `30`
B. `1020`
C. `script.py1020`
D. A `TypeError` is raised

---

**3.** Which statement about mutability in Python is correct?

A. `tuple` and `list` are both mutable.
B. `str` is mutable because slicing returns a modified string.
C. `list`, `set`, and `dict` are mutable; `tuple` and `str` are immutable.
D. All built-in collection types are immutable by default.

---

**4.** What does the following code print?

```python
import re
text = "error 42 occurred at line 7"
result = re.findall(r"\d+", text)
print(result)
```

A. `['42']`
B. `['42', '7']`
C. `[42, 7]`
D. `'42 7'`

---

**5.** What is the difference between `re.match()` and `re.search()`?

A. `re.match()` searches the entire string; `re.search()` only checks the start.
B. `re.match()` only checks the beginning of the string; `re.search()` scans the whole string for the first match.
C. They are functionally identical.
D. `re.match()` returns a list; `re.search()` returns a single string.

---

**6.** Which data structure should you choose to store a collection of *unique* usernames where order does not matter?

A. `list`
B. `tuple`
C. `set`
D. `dict`

---

**7.** What does this code output?

```python
def modify(values):
    values.append(99)

nums = [1, 2, 3]
modify(nums)
print(nums)
```

A. `[1, 2, 3]`
B. `[1, 2, 3, 99]`
C. `[99, 1, 2, 3]`
D. A `NameError` is raised because `nums` is not visible inside `modify`

---

**8.** Which `open()` mode opens a file for writing, **creates it if it does not exist**, and **preserves** any existing content by writing at the end of the file?

A. `"w"`
B. `"r+"`
C. `"a"`
D. `"x"`

---

**9.** What does the following snippet do?

```python
import json
with open("user.json", "w", encoding="utf-8") as f:
    json.dump({"name": "alice", "uid": 1001}, f)
```

A. Reads JSON from `user.json` into a dictionary.
B. Serializes the dictionary into JSON text and writes it to `user.json`.
C. Appends the dictionary to `user.json` without overwriting.
D. Raises an error because dictionaries cannot be written to text files.

---

**10.** In Python's `os.fork()` model, immediately after a successful `fork()` call:

A. The child process starts executing from `main()` again, while the parent continues from after `fork()`.
B. Both parent and child continue from the line after `fork()`; `fork()` returns `0` in the child and the child's PID in the parent.
C. Only the parent continues; the child is suspended until `wait()` is called.
D. `fork()` returns the same PID in both parent and child, and they share the same memory.

---

**11.** What does this print?

```python
s = "Unix Programming"
print(s[5:12])
```

A. `Program`
B. `Programm`
C. `rogramm`
D. `Program `

---

**12.** Which operator checks whether two variables refer to the **same object** in memory (not just equal values)?

A. `==`
B. `=`
C. `is`
D. `in`

---

**13.** What is the output?

```python
x = 10
y = "10"
print(x == y, x is y)
```

A. `True True`
B. `True False`
C. `False False`
D. `False True`

---

**14.** Which f-string prints `pi = 3.14`?

A. `f"pi = {3.14159:.2f}"`
B. `f"pi = {3.14159:2f}"`
C. `f"pi = %.2f" % 3.14159`
D. `f"pi = {3.14159, 2}"`

---

**15.** What does this loop print?

```python
total = 0
for n in range(1, 5):
    total += n
print(total)
```

A. `4`
B. `10`
C. `15`
D. `1234`

---

**16.** What does the regex `^\w+@\w+\.\w+$` most closely describe?

A. Any string containing a digit and a dot
B. A simple email-like pattern: word, `@`, word, `.`, word
C. A URL pattern starting with `http`
D. A whitespace-separated three-word sentence

---

**17.** What does `re.sub(r"\s+", "_", "hello   world  unix")` return?

A. `"hello_world_unix"`
B. `"hello world unix"`
C. `"hello___world__unix"`
D. `"helloworldunix"`

---

**18.** Which special sequence matches a **word boundary** in Python regex?

A. `\w`
B. `\W`
C. `\b`
D. `\s`

---

**19.** Greedy vs non-greedy: applying `r"<.*>"` and `r"<.*?>"` to `"<a><b>"` yields what?

A. Both return `"<a>"`
B. Greedy → `"<a><b>"`, non-greedy → `"<a>"`
C. Greedy → `"<a>"`, non-greedy → `"<a><b>"`
D. Both return `"<a><b>"`

---

**20.** What is printed?

```python
nums = [1, 2, 3, 4, 5]
print(nums[::-1])
```

A. `[5, 4, 3, 2, 1]`
B. `[1, 2, 3, 4, 5]`
C. `[5]`
D. `SyntaxError`

---

**21.** Which set operation returns elements **only in A but not in B**?

A. `A | B`
B. `A & B`
C. `A - B`
D. `A ^ B`

---

**22.** What does this print?

```python
record = ("alice", 1001, "/bin/bash")
user, uid, shell = record
print(uid)
```

A. `alice`
B. `1001`
C. `/bin/bash`
D. `TypeError`

---

**23.** Given `d = {"a": 1, "b": 2}`, what does `d.get("c", 0)` return?

A. `None`
B. `KeyError`
C. `0`
D. `"c"`

---

**24.** What does this output?

```python
def f(a, b=10, *args):
    return a + b + sum(args)

print(f(1, 2, 3, 4))
```

A. `10`
B. `15`
C. `20`
D. `TypeError`

---

**25.** What does this print?

```python
def g(**kwargs):
    return kwargs.get("name", "anon")

print(g(name="bob"))
```

A. `bob`
B. `anon`
C. `name=bob`
D. `KeyError`

---

**26.** Which `open()` mode raises an error if the file **already exists**?

A. `"w"`
B. `"a"`
C. `"x"`
D. `"r+"`

---

**27.** What does `struct.pack("if", 7, 3.14)` produce?

A. The string `"7 3.14"`
B. A `bytes` object containing the binary representation of an int and a float
C. A tuple `(7, 3.14)`
D. A list of integers

---

**28.** After `f.seek(0)`, the next read will:

A. Read from the end of the file
B. Read from the current position
C. Read from the beginning of the file
D. Raise an error because seek requires a record size

---

**29.** Which is the **safest, most idiomatic** way to handle a missing file?

A. Check `os.path.exists()` then call `open()` without try/except
B. Use `try` / `except FileNotFoundError` around `open()`
C. Use `try` / `except Exception` to catch everything
D. Always call `open()` and ignore errors

---

**30.** Which function recursively walks through a directory tree in Python?

A. `os.listdir`
B. `os.walk`
C. `os.scandir`
D. `os.chdir`

---

**31.** What does this print?

```python
print(7 // 2, 7 % 2, 2 ** 3)
```

A. `3.5 1 6`
B. `3 1 8`
C. `3 0 6`
D. `3.5 0 8`

---

**32.** What is the return type of Python's built-in `input()` function?

A. `int`
B. `str`
C. depends on what the user types
D. `bytes`

---

**33.** What does `"  hello  ".strip()` return?

A. `"hello"`
B. `"  hello"`
C. `"hello  "`
D. `"  hello  "`

---

**34.** What is printed?

```python
print("x" in "unix", "z" not in "unix")
```

A. `True True`
B. `True False`
C. `False True`
D. `False False`

---

**35.** What does `"a,b,c".split(",")` return?

A. `['a', 'b', 'c']`
B. `'a b c'`
C. `('a', 'b', 'c')`
D. `'a,b,c'`

---

**36.** What is the result of `True and False or True`?

A. `True`
B. `False`
C. `None`
D. `SyntaxError`

---

**37.** What does this print?

```python
status = "running"
match status:
    case "running":
        print("OK")
    case "stopped":
        print("OFF")
    case _:
        print("UNKNOWN")
```

A. `OK`
B. `OFF`
C. `UNKNOWN`
D. `SyntaxError`

---

**38.** What does this loop print?

```python
i = 0
while i < 5:
    if i == 3:
        break
    i += 1
print(i)
```

A. `3`
B. `4`
C. `5`
D. `0`

---

**39.** What does this print?

```python
total = 0
for n in range(1, 6):
    if n % 2 == 0:
        continue
    total += n
print(total)
```

A. `6`
B. `9`
C. `15`
D. `5`

---

**40.** What does `re.split(r"\s+", "one  two   three")` return?

A. `['one', 'two', 'three']`
B. `['one  two   three']`
C. `'one two three'`
D. `['one', '', 'two', '', '', 'three']`

---

**41.** What does this print?

```python
import re
m = re.search(r"(\w+)@(\w+)", "user@host")
print(m.group(1), m.group(2))
```

A. `user host`
B. `user@host user@host`
C. `user@host @host`
D. `None None`

---

**42.** What does the regex `a{2,4}` match?

A. Exactly 2 or exactly 4 `a`s
B. Between 2 and 4 `a`s (inclusive)
C. Two `a`s followed by four `a`s
D. The literal text `a{2,4}`

---

**43.** What does this print?

```python
nums = [3, 1, 2]
result = nums.sort()
print(result)
```

A. `[1, 2, 3]`
B. `[3, 1, 2]`
C. `None`
D. `SyntaxError`

---

**44.** What does this loop print?

```python
d = {"a": 1, "b": 2}
for k, v in d.items():
    print(k, v)
```

A. `a b 1 2`
B. `a 1` then `b 2` on the next line
C. `('a', 1) ('b', 2)`
D. `ValueError: too many values to unpack`

---

**45.** What does this print?

```python
def split_name(s):
    parts = s.split(" ")
    return parts[0], parts[1]

first, last = split_name("Alice Smith")
print(last)
```

A. `Alice`
B. `Smith`
C. `('Alice', 'Smith')`
D. `['Alice', 'Smith']`

---

**46.** What does this print?

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Bob"))
```

A. `Hello, Bob`
B. `Bob`
C. `Hello,`
D. `TypeError: missing argument`

---

**47.** What does `file.readlines()` return when called on an open text file?

A. The first line as a string
B. The whole file as a single string
C. A list where each element is a line (with trailing newline)
D. A generator that yields lines lazily

---

**48.** What does `"unix".encode("utf-8")` return?

A. `"unix"`
B. `b"unix"`
C. `[117, 110, 105, 120]`
D. Raises an error because strings cannot be encoded

---

**49.** What is the return type of `struct.unpack(fmt, data)`?

A. A single value
B. A list of values
C. A tuple of values (even when only one value is unpacked)
D. A dictionary

---

**50.** Which call creates a **TCP** socket in Python?

A. `socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`
B. `socket.socket(socket.AF_INET, socket.SOCK_STREAM)`
C. `socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)`
D. `socket.tcp()`

---

**51.** What does `print(type(42))` output?

A. `int`
B. `<class 'int'>`
C. `Number`
D. `42`

---

**52.** What is the result of `len("Unix")`?

A. `3`
B. `4`
C. `5`
D. `TypeError`

---

**53.** What does `print("ab" * 3)` output?

A. `ab ab ab`
B. `ababab`
C. `['ab', 'ab', 'ab']`
D. `TypeError`

---

**54.** Which value is **truthy** in Python?

A. `0`
B. `""`
C. `[]`
D. `"0"`

---

**55.** What does `print(1 < 5 < 10)` output?

A. `True`
B. `False`
C. `SyntaxError`
D. `TypeError`

---

**56.** What does `print(int("42") + 8)` output?

A. `428`
B. `50`
C. `42 + 8`
D. `TypeError`

---

**57.** What does `"unix".upper()` return?

A. `"UNIX"`
B. `"unix"`
C. `"Unix"`
D. `None`

---

**58.** What does `"hello".replace("l", "L")` return?

A. `"heLLo"`
B. `"heLlo"`
C. `"hello"`
D. `"HELLO"`

---

**59.** What does `"unix systems".startswith("unix")` return?

A. `True`
B. `False`
C. `0`
D. `Error`

---

**60.** What does `"abc".find("z")` return?

A. `0`
B. `-1`
C. `None`
D. raises `ValueError`

---

**61.** After running `x = 5; x += 3`, what is the value of `x`?

A. `5`
B. `3`
C. `8`
D. `53`

---

**62.** What does this print?

```python
for i, ch in enumerate("ab"):
    print(i, ch)
```

A. `0 a` then `1 b`
B. `1 a` then `2 b`
C. `a 0` then `b 1`
D. `Error`

---

**63.** What does `list(range(0, 10, 2))` produce?

A. `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
B. `[0, 2, 4, 6, 8]`
C. `[2, 4, 6, 8, 10]`
D. `[0, 2, 4, 6, 8, 10]`

---

**64.** Given `m = [[1, 2], [3, 4]]`, what does `print(m[1][0])` output?

A. `1`
B. `2`
C. `3`
D. `4`

---

**65.** Given `nums = [1, 2, 3]`, what does `nums.append(5)` **return**?

A. `[1, 2, 3, 5]`
B. `5`
C. `None`
D. `4`

---

**66.** Given `a = [1, 2]; a.extend([3, 4])`, what is `a`?

A. `[1, 2, [3, 4]]`
B. `[1, 2, 3, 4]`
C. `[3, 4, 1, 2]`
D. `Error`

---

**67.** Given `nums = [10, 20, 30]`, what does `nums.pop()` return, and what is `nums` after?

A. returns `10`, list becomes `[20, 30]`
B. returns `30`, list becomes `[10, 20]`
C. returns `None`, list unchanged
D. returns `30`, list unchanged

---

**68.** What does `dict.keys()` return?

A. A `list` of keys
B. A `tuple` of keys
C. A view object that reflects changes to the dict
D. A `set` of keys

---

**69.** What does `print("a" in {"a": 1, "b": 2})` output?

A. `True`
B. `False`
C. `1`
D. `Error`

---

**70.** After this code, what is `d`?

```python
d = {"a": 1}
d.update({"b": 2, "a": 99})
```

A. `{"a": 1, "b": 2}`
B. `{"a": 99, "b": 2}`
C. `{"a": 1}`
D. `Error: duplicate key`

---

**71.** Given `s = {1, 2}; s.add(2); s.add(3)`, what is `s`?

A. `{1, 2, 2, 3}`
B. `{1, 2, 3}`
C. `[1, 2, 3]`
D. `{1, 3}`

---

**72.** What does `{1, 2, 3} & {2, 3, 4}` return?

A. `{1, 2, 3, 4}`
B. `{2, 3}`
C. `{1, 4}`
D. `{1}`

---

**73.** Which of the following is a **tuple** containing a single integer?

A. `(1)`
B. `(1,)`
C. `[1]`
D. `{1}`

---

**74.** What does `list(zip([1, 2, 3], ["a", "b", "c"]))` return?

A. `[1, 2, 3, "a", "b", "c"]`
B. `[(1, "a"), (2, "b"), (3, "c")]`
C. `{1: "a", 2: "b", 3: "c"}`
D. `[[1, "a"], [2, "b"], [3, "c"]]`

---

**75.** What does `sorted(["bb", "a", "ccc"], key=len)` return?

A. `["a", "bb", "ccc"]`
B. `["ccc", "bb", "a"]`
C. `["bb", "a", "ccc"]`
D. `["a", "ccc", "bb"]`

---

**76.** What does `(lambda x, y: x * y)(3, 4)` return?

A. `7`
B. `12`
C. `(3, 4)`
D. `Error`

---

**77.** What does this print?

```python
count = 0
def increment():
    global count
    count += 1

increment()
increment()
print(count)
```

A. `0`
B. `1`
C. `2`
D. `NameError`

---

**78.** What does this print?

```python
def f():
    return

result = f()
print(result)
```

A. `None`
B. `0`
C. (empty output)
D. `Error`

---

**79.** Why would you write `pass` inside a function body?

A. As a placeholder so the function is syntactically valid but does nothing
B. To pause execution
C. To skip to the next loop iteration
D. To raise a default exception

---

**80.** What is the length of the raw string `r"\n"`?

A. `1`
B. `2`
C. `0`
D. depends on the platform

---

**81.** The regex `[a-z]+` matches:

A. Exactly one lowercase letter
B. One or more lowercase letters
C. Any letter (upper or lowercase)
D. The literal text `[a-z]+`

---

**82.** What does the regex `^abc` match?

A. The literal text `^abc`
B. Any string ending with `abc`
C. A string that **starts** with `abc`
D. Any string containing `abc`

---

**83.** What does the regex `colou?r` match?

A. Only `colour`
B. Only `color`
C. Either `color` or `colour`
D. Any word starting with `colo`

---

**84.** In regex, what is the difference between `+` and `*`?

A. They behave identically
B. `+` matches one or more; `*` matches zero or more
C. `+` matches zero or more; `*` matches one or more
D. `+` works on digits only; `*` works on letters only

---

**85.** After `m = re.search(r"\d+", "abc123def")`, what does `m.start()` return?

A. `0`
B. `3`
C. `6`
D. `None`

---

**86.** What does `re.search(r"xyz", "abc")` return when there is no match?

A. An empty string `""`
B. An empty list `[]`
C. `None`
D. Raises `ValueError`

---

**87.** What does the `re.IGNORECASE` flag do?

A. Disables anchor matching (`^`, `$`)
B. Makes the pattern match without distinguishing letter case
C. Treats special characters as literal
D. Returns the match in lowercase

---

**88.** What does `file.read()` return when called on an open text file (no argument)?

A. The first line as a string
B. A list of lines
C. The entire file contents as a single string
D. A `bytes` object

---

**89.** What does this code do?

```python
with open("data.txt") as f:
    for line in f:
        print(line.rstrip())
```

A. Reads the whole file into memory before printing anything
B. Iterates the file line by line, printing each without the trailing newline
C. Prints only the first line
D. Raises an error because `with`-blocked files cannot be iterated

---

**90.** What does `f.tell()` return?

A. The size of the file in bytes
B. The current read/write position (byte offset)
C. The line number being read
D. The file's mode string

---

**91.** What is the **portable** way to build the path `dir/file.txt`?

A. `"dir" + "/" + "file.txt"`
B. `os.path.join("dir", "file.txt")`
C. `f"dir\\file.txt"`
D. `"dir,file.txt"`

---

**92.** Which function returns `True` only if a path exists **and is a regular file**?

A. `os.path.exists`
B. `os.path.isfile`
C. `os.path.isdir`
D. `os.listdir`

---

**93.** When iterating `csv.reader(f)`, each iteration yields:

A. A string containing the whole row
B. A list of column values (strings)
C. A dictionary mapping column names to values
D. A tuple of `bytes`

---

**94.** What is the difference between `json.load()` and `json.loads()`?

A. `json.load()` reads from a **file object**; `json.loads()` parses a **string**
B. `json.load()` parses a string; `json.loads()` reads from a file
C. They are identical
D. `json.load()` is for writing; `json.loads()` is for reading

---

**95.** Which mode opens a file for **reading binary data**?

A. `"r"`
B. `"rb"`
C. `"wb"`
D. `"rt"`

---

**96.** In `struct.pack("i", 7)`, the format code `i` represents:

A. A 4-byte signed integer
B. An arbitrary-precision integer
C. A single character
D. A floating-point number

---

**97.** What does `os.getpid()` return?

A. The current user's UID
B. The PID of the current process
C. The PID of the parent process
D. A random integer

---

**98.** `os.pipe()` returns:

A. A single file descriptor for a bidirectional pipe
B. A tuple `(read_fd, write_fd)` for one-way communication
C. A FIFO pathname string
D. A pair of sockets

---

**99.** To register a custom signal handler in Python, you use:

A. `signal.handler(SIGTERM, fn)`
B. `signal.signal(SIGTERM, fn)`
C. `os.signal(SIGTERM, fn)`
D. `kill.register(SIGTERM, fn)`

---

**100.** A typical TCP **server** uses which sequence of socket calls?

A. `socket → connect → send → recv → close`
B. `socket → bind → listen → accept → recv/send → close`
C. `socket → sendto → recvfrom → close`
D. `socket → mkfifo → write → read → close`

---

**101.** What does this print?

```python
print("a", "b", "c", sep="-")
```

A. `a b c`
B. `a-b-c`
C. `abc`
D. `a, b, c`

---

**102.** What does this assign to `status`?

```python
n = 5
status = "even" if n % 2 == 0 else "odd"
```

A. `"even"`
B. `"odd"`
C. `None`
D. `SyntaxError`

---

**103.** What does `chr(65)` return?

A. `65`
B. `"A"`
C. `"65"`
D. `"a"`

---

**104.** What does `sum([1, 2, 3])` return?

A. `123`
B. `6`
C. `[1, 2, 3]`
D. `Error`

---

**105.** What does `round(3.7)` return?

A. `3`
B. `4`
C. `3.7`
D. `Error`

---

**106.** What does `divmod(17, 5)` return?

A. `(3, 2)`
B. `(5, 17)`
C. `3.4`
D. `[3, 2]`

---

**107.** What does `"-".join(["a", "b", "c"])` return?

A. `["a-b-c"]`
B. `"abc"`
C. `"a-b-c"`
D. `"a, b, c"`

---

**108.** What does `"{} and {}".format("nginx", "redis")` produce?

A. `"{} and {}"`
B. `"nginx and redis"`
C. `"{nginx} and {redis}"`
D. `Error`

---

**109.** What does `"User: %s, UID: %d" % ("alice", 1001)` produce?

A. `"User: alice, UID: 1001"`
B. `"User: %s, UID: %d"`
C. `"User: alice 1001"`
D. `Error`

---

**110.** What is the value of `not (3 > 5)`?

A. `True`
B. `False`
C. `None`
D. `Error`

---

**111.** What does this print?

```python
for n in range(3):
    if n == 5:
        break
else:
    print("completed")
```

A. (no output)
B. `completed`
C. `Error`
D. `0 1 2`

---

**112.** What does this print?

```python
for i in range(2):
    for j in range(3):
        print(i, j, end=" ")
```

A. `0 0 0 1 0 2 1 0 1 1 1 2 ` (with a trailing space)
B. `0 0 1 1 2 2`
C. `0 1 0 1 0 1`
D. `Error`

---

**113.** Using pattern `r"(\d+)-(\d+)"`, what does `re.findall(pattern, "1-2 and 3-4")` return?

A. `["1-2", "3-4"]`
B. `[("1", "2"), ("3", "4")]`
C. `[("1-2",), ("3-4",)]`
D. `["1", "2", "3", "4"]`

---

**114.** What does the `re.MULTILINE` (`re.M`) flag do?

A. Allows `.` to match newline characters
B. Makes `^` and `$` match at the start/end of **each line**, not only the whole string
C. Allows multi-character patterns
D. Performs case-insensitive matching

---

**115.** The regex `(\w+) \1` matches:

A. Two arbitrary words separated by a space
B. The **same** word repeated, separated by a space
C. A word followed by the literal text `\1`
D. Backreferences are not supported in Python regex

---

**116.** What is the purpose of `(?:...)` in a regex?

A. To define a named group
B. To create a **non-capturing** group (groups for structure but does not record the match)
C. To make matching case-insensitive
D. To make the group optional

---

**117.** The regex `cat|dog` matches:

A. The literal text `cat|dog`
B. Either `cat` **or** `dog`
C. `cat` immediately followed by `dog`
D. Only `cat`

---

**118.** To match a **literal dot** (period) in a regex, you should write:

A. `.`
B. `\.`
C. `*`
D. `\d`

---

**119.** After this code runs, what is the value of `a`?

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
```

A. `[1, 2, 3]`
B. `[1, 2, 3, 4]`
C. `[1, 2, 3, [4]]`
D. `Error`

---

**120.** What does `del nums[1]` do when `nums = [10, 20, 30]`?

A. Removes the value `1`
B. Removes the element at **index 1**, leaving `[10, 30]`
C. Sets `nums[1]` to `None`
D. Raises an error

---

**121.** What does `max([3, 1, 4, 1, 5, 9])` return?

A. `9`
B. `23`
C. `5`
D. `[9]`

---

**122.** What does `any([0, "", None, "hello"])` return?

A. `True`
B. `False`
C. `"hello"`
D. `Error`

---

**123.** Given `d = {"a": 1, "b": 2}`, what does `list(d.values())` return?

A. `["a", "b"]`
B. `[1, 2]`
C. `[("a", 1), ("b", 2)]`
D. `{1, 2}`

---

**124.** Given `d = {"a": 1}`, what does `d.pop("x", None)` do?

A. Removes the key `"x"` and returns its value
B. Raises `KeyError`
C. Returns `None` without modifying `d`
D. Returns the string `"x"`

---

**125.** What is the difference between `set.remove(x)` and `set.discard(x)` when `x` is **not** in the set?

A. They behave identically
B. `remove` raises `KeyError`; `discard` does nothing
C. `discard` raises `KeyError`; `remove` does nothing
D. Both raise `KeyError`

---

**126.** What does `{1, 2}.issubset({1, 2, 3})` return?

A. `True`
B. `False`
C. `{1, 2}`
D. `Error`

---

**127.** Which expression is equivalent to `{1, 2} | {3, 4}`?

A. `{1, 2}.intersection({3, 4})`
B. `{1, 2}.union({3, 4})`
C. `{1, 2}.difference({3, 4})`
D. `{1, 2}.symmetric_difference({3, 4})`

---

**128.** What does this assign?

```python
a, *b = [1, 2, 3, 4]
```

A. `a = 1`, `b = [2, 3, 4]`
B. `a = [1, 2, 3]`, `b = 4`
C. `a = 1`, `b = 2`
D. `Error`

---

**129.** What is the **subtle bug** in this function?

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

A. `items` cannot be modified
B. The default `[]` is **shared** across calls, so the list keeps growing between calls
C. `items` should be a tuple
D. There is no bug

---

**130.** What does this recursive function return when called as `f(4)`?

```python
def f(n):
    if n <= 1:
        return 1
    return n * f(n - 1)
```

A. `4`
B. `10`
C. `24`
D. Infinite recursion

---

**131.** What does this print?

```python
def outer():
    def inner():
        return "hi"
    return inner()

print(outer())
```

A. `inner`
B. `hi`
C. `<function inner>`
D. `Error`

---

**132.** What are `x` and `y` after this code?

```python
x, y = 10, 20
x, y = y, x
```

A. `x = 10, y = 20`
B. `x = 20, y = 10`
C. `x = 20, y = 20`
D. `Error`

---

**133.** What does this print?

```python
def apply(fn, x):
    return fn(x)

print(apply(str.upper, "unix"))
```

A. `unix`
B. `UNIX`
C. `<function>`
D. `Error`

---

**134.** What does `file.write("hello")` return when called on a writable text file?

A. `None`
B. The number of characters written (`5`)
C. The file object
D. The string `"hello"`

---

**135.** To delete a regular file from disk, you use:

A. `os.delete(path)`
B. `os.remove(path)`
C. `del path`
D. `os.rmdir(path)`

---

**136.** To get the **size in bytes** of a file at a given path, the simplest call is:

A. `len(open(path).read())`
B. `os.path.getsize(path)`
C. `os.size(path)`
D. `file.size()`

---

**137.** What does `os.path.basename("/home/user/data.txt")` return?

A. `"/home/user"`
B. `"data.txt"`
C. `"data"`
D. `".txt"`

---

**138.** What does `os.path.splitext("report.csv")` return?

A. `["report", "csv"]`
B. `("report", ".csv")`
C. `("report.csv", "")`
D. `"report"`

---

**139.** To create the directory `a/b/c` even when `a` and `a/b` don't exist yet, you call:

A. `os.mkdir("a/b/c")`
B. `os.makedirs("a/b/c")`
C. `os.mkdir("a/b/c", recursive=True)`
D. `os.path.create("a/b/c")`

---

**140.** In `struct.pack`/`unpack`, the format code `d` represents:

A. A single decimal digit
B. An 8-byte (double-precision) floating-point number
C. A 4-byte integer
D. A datetime value

---

**141.** To compute a SHA-256 hex digest of a `bytes` value `data`, you write:

A. `hashlib.sha256(data).hexdigest()`
B. `hash.sha256(data)`
C. `crypto.sha256(data)`
D. `os.sha256(data)`

---

**142.** The key difference between `bytes` and `bytearray` is:

A. `bytes` is mutable; `bytearray` is immutable
B. `bytes` is **immutable**; `bytearray` is **mutable**
C. They are aliases for the same type
D. `bytearray` only supports ASCII

---

**143.** A Caesar cipher shifts an uppercase letter by `n` positions with wrap-around. Which expression encodes the single-character string `c` by shift `n`?

A. `chr(ord(c) + n)`
B. `chr((ord(c) - ord('A') + n) % 26 + ord('A'))`
C. `c + n`
D. `c.shift(n)`

---

**144.** `os.getppid()` returns:

A. The current process's PID
B. The **parent** process's PID
C. The user's UID
D. The current group ID

---

**145.** After `pid = os.fork()` in the parent, what does `os.waitpid(pid, 0)` do?

A. Sends a kill signal to `pid`
B. Blocks until the child with that PID terminates and returns its exit info
C. Suspends both parent and child indefinitely
D. Returns immediately whether the child has finished or not

---

**146.** To send signal `SIGTERM` to process `pid` from Python, you call:

A. `os.kill(pid, signal.SIGTERM)`
B. `signal.send(pid, SIGTERM)`
C. `os.terminate(pid)`
D. `kill(pid, "TERM")`

---

**147.** To run an external command and **capture its stdout** as a string, the simplest modern API is:

A. `os.system("ls").stdout`
B. `subprocess.run(["ls"], capture_output=True, text=True).stdout`
C. `os.popen("ls")`
D. `subprocess.exec("ls")`

---

**148.** Given a Linux Python script with this code, what happens?

```python
from multiprocessing import Process

def task(n):
    print(n * 2)

if __name__ == "__main__":
    p = Process(target=task, args=(5,))
    p.start()
    p.join()
```

A. A new child process runs `task(5)`, printing `10`
B. The current process runs `task(5)` synchronously
C. Raises `NameError`
D. Nothing prints

---

**149.** In TCP socket programming, what does `data = sock.recv(1024)` do?

A. Reads exactly 1024 bytes, blocking until all 1024 arrive
B. Reads **up to** 1024 bytes that are currently available; may return fewer
C. Reads until a newline is found
D. Reads until the connection is closed

---

**150.** For a UDP socket, the typical send/receive call pair is:

A. `send` / `recv`
B. `sendto` / `recvfrom`
C. `connect` / `accept`
D. `write` / `read`

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | **C** | `#!/usr/bin/env python3` searches `PATH` for the interpreter, making it the most portable across systems. |
| 2 | **B** | `sys.argv` elements are strings, so `"10" + "20"` performs string concatenation → `"1020"`. |
| 3 | **C** | `list`, `set`, `dict` are mutable; `tuple` and `str` are immutable. |
| 4 | **B** | `re.findall(r"\d+", ...)` returns all non-overlapping digit groups as a list of strings → `['42', '7']`. |
| 5 | **B** | `re.match()` only anchors at the start of the string; `re.search()` scans the whole string. |
| 6 | **C** | A `set` enforces uniqueness and ignores order. |
| 7 | **B** | Lists are mutable and passed by reference, so `append` modifies the original list. Output: `[1, 2, 3, 99]`. |
| 8 | **C** | `"a"` opens for appending — creates the file if missing, preserves existing content. (`"w"` overwrites; `"x"` fails if file exists; `"r+"` fails if file doesn't exist.) |
| 9 | **B** | `json.dump(obj, f)` serializes the Python object to JSON and writes it to the file. |
| 10 | **B** | After `fork()`, both processes continue from the same line; the return value distinguishes them — `0` in child, child PID in parent. |
| 11 | **A** | `s[5:12]` takes indices 5–11 → `"Program"`. |
| 12 | **C** | `is` compares identity (same object); `==` compares values. |
| 13 | **C** | `10 == "10"` is `False` (different types); `is` is also `False`. |
| 14 | **A** | `:.2f` rounds to 2 decimal places → `3.14`. |
| 15 | **B** | `1+2+3+4 = 10`. `range(1,5)` excludes 5. |
| 16 | **B** | `^\w+@\w+\.\w+$` = word, `@`, word, literal `.`, word — basic email shape. |
| 17 | **A** | `\s+` matches one or more whitespace; replaced with single `_`. |
| 18 | **C** | `\b` is the word boundary. `\w`/`\W` match word/non-word chars; `\s` is whitespace. |
| 19 | **B** | Greedy `.*` consumes as much as possible; `.*?` stops at first match. |
| 20 | **A** | `[::-1]` reverses a list. |
| 21 | **C** | `A - B` = difference. `|` union, `&` intersection, `^` symmetric difference. |
| 22 | **B** | Tuple unpacking assigns `uid = 1001`. |
| 23 | **C** | `dict.get(key, default)` returns the default if key missing → `0`. |
| 24 | **A** | `a=1, b=2, args=(3,4)` → `1+2+3+4 = 10`. (Note: positional `2` overrides default `b=10`.) |
| 25 | **A** | `**kwargs` collects keyword args; `kwargs["name"]` → `"bob"`. |
| 26 | **C** | `"x"` is exclusive create — fails if file exists. |
| 27 | **B** | `struct.pack` returns a `bytes` object with binary-encoded values. |
| 28 | **C** | `seek(0)` moves the file pointer to the start. |
| 29 | **B** | Targeted `try/except FileNotFoundError` is the idiomatic pattern; bare `except` is too broad. |
| 30 | **B** | `os.walk()` recursively yields `(dirpath, dirnames, filenames)` for every subdirectory. |
| 31 | **B** | `//` is integer division (3), `%` is modulo (1), `**` is exponentiation (8). |
| 32 | **B** | `input()` always returns a `str`; convert with `int()` or `float()` if needed. |
| 33 | **A** | `.strip()` removes leading and trailing whitespace. |
| 34 | **A** | `in` checks substring membership; `"x"` is in `"unix"`, `"z"` is not. |
| 35 | **A** | `str.split(sep)` returns a list of substrings. |
| 36 | **A** | `and` has higher precedence than `or`: `(True and False) or True` → `False or True` → `True`. |
| 37 | **A** | `match`/`case` matches the first equal pattern; `_` is the default. |
| 38 | **A** | The loop breaks before incrementing when `i == 3`, so `i` stays at `3`. |
| 39 | **B** | `continue` skips even numbers; `1+3+5 = 9`. |
| 40 | **A** | `\s+` splits on one or more whitespace characters → 3 clean tokens. |
| 41 | **A** | `group(1)` and `group(2)` return the captured groups (`user`, `host`). |
| 42 | **B** | `{n,m}` means between *n* and *m* repetitions, inclusive. |
| 43 | **C** | `list.sort()` sorts **in place** and returns `None`. Use `sorted(nums)` to get a new sorted list. |
| 44 | **B** | `dict.items()` yields `(key, value)` pairs; each `print` writes one line. |
| 45 | **B** | Multiple return values are returned as a tuple and unpacked into `first, last`. |
| 46 | **A** | The default value `"Hello"` is used when `greeting` is not supplied. |
| 47 | **C** | `readlines()` reads everything and returns a list of lines (each typically ending with `\n`). |
| 48 | **B** | `.encode()` converts `str` to `bytes`; the literal prefix `b""` denotes a bytes object. |
| 49 | **C** | `struct.unpack` always returns a tuple, even with a single value (`(x,)`). |
| 50 | **B** | `SOCK_STREAM` = TCP (connection-oriented). `SOCK_DGRAM` = UDP. |
| 51 | **B** | `type(x)` returns the class object; `print()` shows it as `<class 'int'>`. |
| 52 | **B** | `len()` counts characters in a string → 4 (`U`, `n`, `i`, `x`). |
| 53 | **B** | `*` repeats the string the given number of times. |
| 54 | **D** | Empty containers, `0`, `""`, and `None` are falsy. Any **non-empty** string (even `"0"`) is truthy. |
| 55 | **A** | Python supports chained comparisons: `1 < 5` and `5 < 10` are both true. |
| 56 | **B** | `int("42")` converts the string to integer 42; `42 + 8 = 50`. |
| 57 | **A** | `.upper()` returns a new uppercase copy (strings are immutable). |
| 58 | **A** | `.replace(old, new)` replaces all occurrences → `"heLLo"`. |
| 59 | **A** | `.startswith(prefix)` returns a boolean. |
| 60 | **B** | `.find()` returns the index, or `-1` if not found (unlike `.index()` which raises). |
| 61 | **C** | `x += 3` is equivalent to `x = x + 3` → `8`. |
| 62 | **A** | `enumerate()` yields `(index, value)` pairs starting at 0. |
| 63 | **B** | `range(start, stop, step)` is `start ≤ n < stop`; with step 2 → `[0, 2, 4, 6, 8]`. |
| 64 | **C** | `m[1]` is `[3, 4]`; `m[1][0]` is `3`. |
| 65 | **C** | `list.append()` modifies the list in place and returns `None`. |
| 66 | **B** | `extend(iterable)` adds each element of the iterable individually. (`append` would nest the list.) |
| 67 | **B** | `pop()` with no argument removes and returns the **last** element. |
| 68 | **C** | `dict.keys()` returns a *view* — a live, dynamic object that reflects subsequent changes to the dict. |
| 69 | **A** | `in` on a dict tests for **key** membership, not value. |
| 70 | **B** | `update()` overwrites existing keys (`a` → 99) and adds new ones (`b` → 2). |
| 71 | **B** | Sets ignore duplicates, so adding `2` again has no effect. |
| 72 | **B** | `&` is set intersection — elements in both. |
| 73 | **B** | A **trailing comma** is required to make a single-element tuple. `(1)` is just the integer 1 in parentheses. |
| 74 | **B** | `zip()` pairs elements positionally; `list()` materializes the result. |
| 75 | **A** | `key=len` sorts by string length ascending. |
| 76 | **B** | A `lambda` is an anonymous function; calling it with `(3, 4)` returns `12`. |
| 77 | **C** | `global count` allows the function to modify the module-level variable; two calls increment it to `2`. |
| 78 | **A** | A bare `return` (or no return) yields `None`. |
| 79 | **A** | `pass` is a no-op statement used where syntax requires a body. |
| 80 | **B** | A raw string keeps the backslash literal; `r"\n"` contains `\` and `n` → length 2. (Without `r`, `"\n"` would be a single newline character.) |
| 81 | **B** | `[a-z]` is a character class for one lowercase letter; `+` makes it "one or more". |
| 82 | **C** | `^` anchors the match to the start of the string (or line, with `re.MULTILINE`). |
| 83 | **C** | `?` makes the previous character optional → `u` may or may not appear. |
| 84 | **B** | `+` requires at least one match; `*` allows zero matches. |
| 85 | **B** | The first digit (`1` of `123`) is at index 3 in `"abc123def"`. |
| 86 | **C** | When no match is found, `re.search` returns `None`. |
| 87 | **B** | `re.IGNORECASE` (or `re.I`) makes the pattern case-insensitive. |
| 88 | **C** | `.read()` with no argument reads everything as one string. |
| 89 | **B** | A file is iterable line-by-line; `rstrip()` strips the trailing newline before printing. |
| 90 | **B** | `tell()` returns the current byte offset of the file pointer. |
| 91 | **B** | `os.path.join` uses the OS-appropriate separator and avoids manual string concatenation bugs. |
| 92 | **B** | `os.path.isfile` is `True` only if the path exists *and* is a regular file. `os.path.exists` is also true for directories. |
| 93 | **B** | `csv.reader` yields each row as a list of strings (use `csv.DictReader` for dictionaries). |
| 94 | **A** | `json.load(f)` reads from an open file object; `json.loads(s)` parses a JSON string. (The trailing `s` = "string".) |
| 95 | **B** | `"rb"` = read + binary. |
| 96 | **A** | Format `i` in `struct` is a 4-byte signed integer. |
| 97 | **B** | `os.getpid()` returns the current process's PID; `os.getppid()` returns the parent's. |
| 98 | **B** | `os.pipe()` creates a one-way pipe; the read-end and write-end file descriptors are returned as a tuple. |
| 99 | **B** | `signal.signal(signum, handler)` registers a handler function for a given signal. |
| 100 | **B** | TCP servers `bind` to an address, `listen` for connections, then `accept` each client to get a per-connection socket. |
| 101 | **B** | The `sep` parameter overrides the default space separator between `print()` arguments. |
| 102 | **B** | Conditional expression `x if cond else y` evaluates to `y` when `cond` is false; `5 % 2 == 0` is false. |
| 103 | **B** | `chr(n)` returns the character whose Unicode code point is `n`; `65` is `'A'`. (Inverse of `ord()`.) |
| 104 | **B** | `sum()` returns the arithmetic sum of an iterable of numbers. |
| 105 | **B** | `round(3.7)` rounds to nearest int → `4`. |
| 106 | **A** | `divmod(a, b)` returns `(a // b, a % b)` → `(3, 2)`. |
| 107 | **C** | `str.join(iterable)` concatenates the iterable's strings with the separator string between them. |
| 108 | **B** | `str.format()` substitutes positional `{}` placeholders in order. |
| 109 | **A** | Printf-style formatting: `%s` for strings, `%d` for integers. |
| 110 | **A** | `3 > 5` is `False`; `not False` is `True`. |
| 111 | **B** | A `for-else` runs the `else` block only if the loop **completes without `break`**. The loop here never breaks, so `else` runs. |
| 112 | **A** | Outer loop iterates `i` over `0,1`; inner loop iterates `j` over `0,1,2` for each `i`; `end=" "` keeps everything on one line. |
| 113 | **B** | When the pattern has groups, `re.findall` returns a list of **tuples** (one per match) of the captured groups. |
| 114 | **B** | `re.MULTILINE` makes `^`/`$` match line boundaries. (`re.DOTALL` is the one that lets `.` match newline.) |
| 115 | **B** | `\1` is a **backreference** that matches the same text captured by group 1. |
| 116 | **B** | `(?:...)` groups for structure (alternation, quantifier scope) without consuming a capture-group number. |
| 117 | **B** | `|` is alternation: matches the expression on either side. |
| 118 | **B** | The `.` is a metacharacter; escape it with `\.` to match a literal period. |
| 119 | **A** | `b = a.copy()` creates a separate (shallow) copy; appending to `b` does not affect `a`. |
| 120 | **B** | `del seq[i]` removes the element at that index. |
| 121 | **A** | `max()` returns the largest element. |
| 122 | **A** | `any()` returns `True` if **at least one** element is truthy; `"hello"` is truthy. |
| 123 | **B** | `dict.values()` yields the values; wrapping in `list()` materializes them. |
| 124 | **C** | `dict.pop(key, default)` returns `default` (here `None`) when the key is absent, instead of raising. |
| 125 | **B** | `remove` raises `KeyError` if the element is missing; `discard` silently does nothing. |
| 126 | **A** | `{1, 2}` is a subset of `{1, 2, 3}`. |
| 127 | **B** | `|` is set union, equivalent to the `.union()` method. |
| 128 | **A** | The starred target captures the remaining elements as a list. |
| 129 | **B** | The default value is evaluated **once** at function definition time. The same list is reused across calls — a classic Python pitfall. Use `items=None` and create a new list inside instead. |
| 130 | **C** | Factorial: `4 * 3 * 2 * 1 = 24`. |
| 131 | **B** | `inner` is defined inside `outer`; calling `inner()` returns `"hi"`, which `outer` returns. |
| 132 | **B** | Tuple packing/unpacking swaps values without a temporary variable. |
| 133 | **B** | Functions are first-class objects; `str.upper` is passed as `fn` and called on `"unix"`. |
| 134 | **B** | `file.write(s)` returns the number of characters written. |
| 135 | **B** | `os.remove(path)` deletes a file. (`os.rmdir` only removes empty directories.) |
| 136 | **B** | `os.path.getsize(path)` returns the file's size in bytes without opening it. |
| 137 | **B** | `basename` returns the final component of the path. (`dirname` returns the leading directory.) |
| 138 | **B** | `splitext` separates the path into root and extension; the extension **includes the dot**. |
| 139 | **B** | `os.makedirs` creates all missing intermediate directories. (`os.mkdir` only creates the leaf.) |
| 140 | **B** | `d` is double (8-byte float). `f` is single-precision float (4 bytes). |
| 141 | **A** | `hashlib.sha256(bytes).hexdigest()` returns the hex string of the digest. |
| 142 | **B** | `bytes` is immutable like `str`; `bytearray` supports in-place mutation. |
| 143 | **B** | Subtract `'A'`, shift, take `% 26`, add `'A'` back — this wraps `Z + 1` to `A`. Just adding `n` would push letters past `Z`. |
| 144 | **B** | `os.getppid()` returns the **parent** process's PID; `os.getpid()` returns the current PID. |
| 145 | **B** | `os.waitpid(pid, 0)` blocks until the specified child terminates and returns `(pid, status)`. |
| 146 | **A** | `os.kill(pid, sig)` sends a signal to a process by PID. |
| 147 | **B** | `subprocess.run(..., capture_output=True, text=True)` returns a `CompletedProcess` with `.stdout` as a string. |
| 148 | **A** | The `multiprocessing.Process` spawns a child process running `task(5)`, which prints `10`; `join()` waits for it. |
| 149 | **B** | `recv(bufsize)` returns up to `bufsize` bytes that are currently available — TCP is a stream, so a single `recv` may return fewer bytes than requested. |
| 150 | **B** | UDP is connectionless: `sendto(data, addr)` sends a datagram to an address; `recvfrom(bufsize)` returns `(data, addr)`. |
