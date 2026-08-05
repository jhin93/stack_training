# Python Quiz — 32547 Unix Systems Programming

Replica of the **Multiple Choice — Python (Spring 2025)** past exam:
- 15 questions · 15 points · 75 minutes
- **Multi-select** format: each question may have *more than one* correct answer
- Answers and explanations are placed immediately below each question

---

**Question 1.** In Python, which of the following statements are true? (select all that apply)

- [ ] A. expression `'abc' - 'bc'` evaluates to string `'a'`
- [x] B. if variable `lis` is a list with a sufficient number of elements, `lis[0:3]` is the list of its first three elements
- [ ] C. expression `'c' + 'ab'` evaluates to string `'abc'`
- [x] D. expression `"Sydney"[1:3]` will evaluate to string `"yd"`
- [x] E. expression `re.split(":\s", "here: 235")` calls method `split` of module `re` with string `":\s"` as the first argument and string `"here: 235"` as the second

**Answer: B, D, E**

- A: strings do not support the `-` operator → `TypeError`
- B: slicing `lis[0:3]` returns the first three elements
- C: `'c' + 'ab'` is `'cab'`, not `'abc'`
- D: `"Sydney"[1:3]` picks indices 1 and 2 → `"yd"`
- E: the statement just describes the call's arguments correctly

---

**Question 2.** After the following Python code is executed:

```python
a = 123
b = a
a = 'I was a number'
d = str(123)
```

Which of the following expressions will evaluate to `True`? (select all)

- [x] A. `d == '123'`
- [x] B. `a == "I was a number"`
- [ ] C. `b == "123"`
- [ ] D. `a is b`

**Answer: A, B**

- A: `str(123)` produces `'123'`, so `d == '123'` is `True`
- B: `a` has been rebound to the string `"I was a number"`
- C: `b` is still the integer `123`, not the string `"123"` (different types → `==` is False)
- D: after `a = 'I was a number'`, `a` and `b` point to different objects

---

**Question 3.** Python has a module for regular expressions, **`re`**, which contains a method called **`split`**. Assuming you have imported `re`, consider each of the following statements about `re.split` and select all that are true:

- [ ] A. calling `re.split('-', '14/05/2024')` returns list `['14', '05', '2024']`
- [x] B. calling `re.split('\d', 'alpha1beta2gamma')` returns list `['alpha', 'beta', 'gamma']`
- [ ] C. calling `re.split(':', 'a:b:c')` returns string `'abc'`
- [x] D. calling `print(re.split('\s+', 'Gen AI'))` prints `['Gen', 'AI']` to the standard output

**Answer: B, D**

- A: the input has no `-`; `re.split` returns the original string in a single-element list `['14/05/2024']`
- B: digits act as separators, producing the three words
- C: `re.split` always returns a *list*, not a concatenated string → `['a', 'b', 'c']`
- D: `\s+` splits on whitespace, yielding `['Gen', 'AI']`

---

**Question 4.** In Python, which of the following are true about `sys.argv`? (select all)

- [ ] A. `len(sys.argv[0])` is the number of command-line arguments
- [x] B. `sys.argv` is the list of the command-line arguments passed to the script (`sys.argv[0]` is the script name)
- [x] C. `sys.argv[1:3]` is a list with the first and second arguments passed to the script from the command line, if provided
- [ ] D. `sys.argv[1+2]` are the first and second arguments passed to the script

**Answer: B, C**

- A: `len(sys.argv)` (without the `[0]`) would give the count; `len(sys.argv[0])` is the length of the script-name string
- B: correct definition
- C: slice `[1:3]` returns `[argv[1], argv[2]]` — the first and second user args
- D: `1 + 2 = 3`, so this is `sys.argv[3]` — the **third** argument, not first-and-second

---

**Question 5.** Which of the following code sequences will create a list named **`lis`** with content **`['mars', 'earth', 'venus']`**? (select all)

- [ ] A. `lis[0:3] = ['mars', 'earth', 'venus']`
- [x] B. `lis = ['mars']` then `lis.append('earth')` then `lis.append('venus')`
- [ ] C. `lis = ['mercury', 'mars', 'earth', 'venus'] - ['mercury']`
- [x] D. `lis = ['earth', 'venus']` then `lis.insert(0, 'mars')`
- [ ] E. `lis = ['mars', 'earth']` then `lis[2] = 'venus'`

**Answer: B, D**

- A: `lis` doesn't exist yet, so slice-assigning to it raises `NameError`
- B: build incrementally with `append`
- C: lists do not support the `-` operator → `TypeError`
- D: `insert(0, x)` prepends `x`
- E: assigning to an out-of-range index raises `IndexError` (you cannot extend a list by index assignment)

---

**Question 6.** If `my_list = [1, -1, 1, -1, 1]`, which of the following statements has the effect (possibly amongst others) of setting the value of the list's **last element** to `0`? (select all)

- [x] A. `my_list[-1] = 0`
- [ ] B. `my_list[4] += 1`
- [x] C. `my_list[3:5] = [0, 0]`
- [x] D. `my_list[my_list[1]] = 0`   *# tricky! pay attention!*
- [x] E. `my_list[4] = my_list[0] + my_list[1]`

**Answer: A, C, D, E**

- A: direct assignment via negative index
- B: `1 + 1 = 2`, not `0`
- C: replaces the last two elements with `[0, 0]` — last element becomes `0`
- D: `my_list[1]` is `-1`, so this becomes `my_list[-1] = 0`
- E: `1 + (-1) = 0`

---

**Question 7.** If `y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, which of the following expressions evaluate to `10`? (select all)

- [x] A. `y[-1]`
- [x] B. `len(y[2:]) + len(y[0:2])`
- [ ] C. `2 * y[5]`
- [x] D. `len(y)`
- [ ] E. `y[2] + y[8]`

**Answer: A, B, D**

- A: last element is `10`
- B: `len(y[2:])` is `8`, `len(y[0:2])` is `2`, total `10`
- C: `y[5]` is `6`, so `2 * 6 = 12`
- D: list has 10 elements
- E: `y[2] + y[8] = 3 + 9 = 12`

---

**Question 8.** If `my_dict = {"AAA": 10, "AAB": 7, "ABB": 4, "BBB": 1}`, which of the following evaluate to `True`? (select all)

- [ ] A. `my_dict[10] == "AAA"`
- [x] B. `my_dict["ABB"] == 4 * my_dict["BBB"]`
- [x] C. `"ABB" in my_dict`
- [ ] D. `len(my_dict) == 8`
- [x] E. `my_dict["BBB"] == 1`

**Answer: B, C, E**

- A: there is no key `10` in the dict → `KeyError`
- B: `4 == 4 * 1` → `True`
- C: key membership test → `True`
- D: there are 4 keys, not 8
- E: direct lookup matches

---

**Question 9.** After executing the following statements:

```python
scores_dict = {"mark": 150, "anika": 250}
scores_list = [150, 250]
scores_dict["dacheng"] = 200
scores_list.append(200)
```

Which of the following are true? (select all)

- [ ] A. Expression `scores_dict[0]` returns an integer
- [ ] B. The value of `scores_list[1]` is `200`
- [x] C. Expression `scores_dict["dacheng"] == scores_list[2]` evaluates to `True`
- [x] D. The value of `scores_dict["mark"]` is `150`
- [ ] E. String `'150'` is a key in dictionary `scores_dict`

**Answer: C, D**

- A: no key `0` exists → `KeyError`
- B: `scores_list` is `[150, 250, 200]`, so `[1]` is `250`
- C: both are `200`
- D: the original value is still there
- E: keys of `scores_dict` are `"mark"`, `"anika"`, `"dacheng"` — not `'150'`

---

**Question 10.** Using `re.search()` with the regular expression `\D{2}` in Python, in which of the following **strings** a match will be found? (NB: pay attention to the meaning of `\D` — a *non-digit* character.)

- [x] A. `(0410) 676767`
- [x] B. `******`
- [x] C. `my number is not 0410 676767`
- [ ] D. `0410 676767`
- [ ] E. `8s20s20s`

**Answer: A, B, C**

`\D{2}` requires **two consecutive non-digit characters**.

- A: `) ` (close-paren and space) are two consecutive non-digits → match
- B: every `*` is a non-digit; plenty of consecutive non-digits
- C: `"my"`, `" n"`, etc. — many runs of 2+ non-digits
- D: digits are separated by *only one* space at a time — no two consecutive non-digits
- E: every `s` is sandwiched between digits — no two consecutive non-digits

---

**Question 11.** Consider this function:

```python
def fun(w = 10, x = 10, b = 0):
    print(w * x + b)
```

If we call `fun(9, 10, 10)`, this function will print `100`. Which of the following calls will also print `100`? (select all)

- [x] A. `fun()`
- [x] B. `fun(0, -1, 100)`
- [x] C. `fun(b=20, x=8, w=10)`
- [ ] D. `fun(100)`
- [x] E. `fun(6, 6, 64)`

**Answer: A, B, C, E**

- A: defaults `10*10 + 0 = 100`
- B: `0*(-1) + 100 = 100`
- C: `10*8 + 20 = 100` (keyword args, order doesn't matter)
- D: `100*10 + 0 = 1000`
- E: `6*6 + 64 = 36 + 64 = 100`

---

**Question 12.** Given this Python function:

```python
def maximum(*args):
    m = args[0]
    for item in args:
        if item > m:
            m = item
    print(m)
```

Which of the following calls will print `4` as its output? (select all)

- [x] A. `maximum(1, 2, 3, 4)`
- [x] B. `maximum(*[1, 2, 3, 4])`
- [ ] C. `maximum([1, 2, 3, 4])`
- [x] D. `maximum(2 * 2)`

**Answer: A, B, D**

- A: max of `1, 2, 3, 4` is `4`
- B: `*[1,2,3,4]` unpacks into four positional args — same as A
- C: passes the whole list as a single argument; `args = ([1,2,3,4],)`; prints the list, not `4`
- D: `2 * 2 = 4`; one arg, the loop runs once with `item == m == 4`, prints `4`

---

**Question 13.** After this Python code is executed:

```python
def rotate(lis):
    lis.append(lis[0])
    del lis[0]

my_list = ['a','b','c','d']
rotate(my_list)
```

Which of the following statements are true? (select all)

- [x] A. The length of list `my_list` is `4`
- [x] B. `my_list[-3]` is equal to `'c'`
- [x] C. `my_list` is equal to `['b', 'c', 'd', 'a']`
- [ ] D. Function call `rotate(my_list)` cannot modify list `my_list`
- [ ] E. `my_list` is equal to `['b', 'c', 'd']`

**Answer: A, B, C**

After `rotate`: append `'a'` → `['a','b','c','d','a']`, then delete index 0 → `['b','c','d','a']`.

- A: length is still 4
- B: `my_list[-3]` = `'c'`
- C: matches the final list
- D: lists are mutable; `rotate` *did* modify it via shared reference
- E: length is 4, not 3

---

**Question 14.** In Python, which of the following statements are true? (select all)

- [ ] A. A call to function `bytes()` returns an object of type string
- [x] B. Function `struct.pack` returns a value that can be written to a binary file
- [x] C. The first argument of function `struct.pack` is a format string
- [x] D. The `bytes` and `bytearray` types can be used to store binary data
- [ ] E. You can write strings or lists to a file opened for writing in binary mode without any conversion

**Answer: B, C, D**

- A: `bytes()` returns a `bytes` object, not a string
- B: `struct.pack` produces a `bytes` object suitable for binary file output
- C: format string is the first argument (e.g., `"if"`)
- D: both types hold binary data; `bytearray` is mutable
- E: writing to binary mode requires bytes-like objects, not arbitrary strings/lists

---

**Question 15.** In Python, which of the following statements about files are true? (select all)

- [x] A. Instruction `open('marks.csv')` opens file `marks.csv` for reading in text mode, assuming that the file exists in the current directory and the program's user has permission to read it.
- [ ] B. If `fin` is a file object opened for reading in text mode, a call to method `fin.read()` will return exactly one line of text from the file, even if more are available.
- [x] C. The following code:

  ```python
  try:
      fin = open("marks.csv")
  except:
      print(sys.exc_info()[0])
  ```

  tries to open file `marks.csv` in the current directory and assigns the returned file object to variable `fin`. If this fails, it prints an error message from the system.
- [x] D. Instruction `open('marks.csv', 'ab')` opens file `marks.csv` for appending in binary mode, assuming that the program's user has the required permissions.

**Answer: A, C, D**

- A: default mode for `open` is `"r"` (text read)
- B: `read()` returns the **whole** remaining content as one string; `readline()` is the method that returns one line
- C: the `try/except` is a standard guard that prints the exception class on failure
- D: `'a'` = append, `'b'` = binary, combined → `'ab'`

---

## Study tips

- Read every option carefully — many distractors look correct at first glance (e.g. `len(sys.argv[0])` vs `len(sys.argv)` in Q4, `read()` vs `readline()` in Q15).
- For multi-select questions, you typically lose partial credit for each wrong tick **and** each missing tick — don't guess.
- Walk through code snippets line by line on paper. Especially watch for:
  - mutable-vs-immutable side effects (Q13: lists *can* be modified through references)
  - keyword vs positional arguments (Q11)
  - `is` vs `==` for non-cached values (Q2)
  - slicing semantics (`[a:b]` is half-open)
