
# Week 2 — Filesystem and File Control in Unix

## Table of Contents
1. [Week 2 Overview](#1-week-2-overview)  
2. [Filesystem Structure and Path Semantics](#2-filesystem-structure-and-path-semantics)  
3. [File Permissions Model](#3-file-permissions-model)  
4. [Ownership and Groups](#4-ownership-and-groups)  
5. [Changing Permissions with chmod](#5-changing-permissions-with-chmod)  
6. [Core File Operations](#6-core-file-operations)  
   6.1 [`touch` — Create Files](#61-touch--create-files)  
   6.2 [`ls` — List Files](#62-ls--list-files)  
   6.3 [`cp` — Copy Files](#63-cp--copy-files)  
   6.4 [`mv` — Move/Rename Files](#64-mv--moverename-files)  
   6.5 [`find` — Search Filesystem](#65-find--search-filesystem)  
7. [`rm` — File and Directory Removal](#7-rm--file-and-directory-removal)  
8. [`tar` and `gzip` — Archiving and Compression](#8-tar-and-gzip--archiving-and-compression)  
9. [Globbing (Metacharacters)](#9-globbing-metacharacters)  

---

## 1. Week 2 Overview

By the end of Week 2, you should be able to:

- Navigate filesystem paths confidently.
- Create, list, copy, move, and locate files.
- Interpret and modify file permissions.
- Manage ownership and groups.
- Remove files safely.
- Archive and compress data.
- Use globbing to operate on multiple files.

---

## 2. Filesystem Structure and Path Semantics

### Filesystem Hierarchy

```
        /
        |
  -----------------
  |       |       |
 home    etc     var
  |
 user
  |
 project
  |
 file.txt
```

### Path Resolution Flow

```
Command → Shell → Resolve Path
                 ↓
         Absolute? ---- Yes → Start at /
             |
             No
             ↓
      Start from Current Directory
             ↓
        Apply . and ..
             ↓
        Final Path
```

Examples:

```bash
ls /usr/bin
cp ../notes.txt ./backup/
mv ~/Downloads/file.txt ./
```

---

## 3. File Permissions Model

Permissions determine access.

```
User → Group → Others
```

Symbols:

| Symbol | Meaning |
|---|---|
| r | read |
| w | write |
| x | execute |

Example:

```bash
-rwxr-xr--
```

1. First '-'  represents file type
2. 'rwx'   are user permissions
3. 'r-x' are the group permissions
4. 'r--' others perm

-rwxr-xr--  report.txt      # 일반 파일
drwxr-xr--  project/        # 폴더
lrwxr-xr--  shortcut -> ..  # 심볼릭 링크

Numeric:

| Number | Permission |
|---|---|
| 7 | rwx | (rwx = 4+2+1 = 7)
| 6 | rw- | (rw = 4+2 = 6)
| 5 | r-x | (--- = 0 + 0 + 0 = 0)
| 4 | r |
| 2 | w |
| 1 | x |


---

## 4. Ownership and Groups

Controls who owns files.

Examples:

```bash
sudo chown alice file.txt # change + owner = chown 소유자를 alice로 변경
sudo chown alice:staff file.txt # 소유자 alice, 그룹 staff로 변경
sudo chown -R alice project/ # 폴더 안의 모든 파일까지 한번에 변경
chgrp dev file.txt # 그룹만 dev로 변경
```

---

## 5. Changing Permissions with chmod

### What chmod Does

Modifies file permissions.

Common options:

| Option | Meaning |
|---|---|
| -R | recursive |

Examples:

```bash
chmod 644 file.txt      # 소유자 읽기/쓰기, 나머지 읽기만 change + mode = chmod
chmod 755 script.sh     # 소유자 전부, 나머지 읽기/실행만
chmod u+x script.sh     # 소유자(u)에게 실행(x) 권한 추가
chmod -R 755 project/   # 폴더 안의 모든 파일까지 한번에 변경
```

---

## 6. Core File Operations

### 6.1 `touch` — Create Files

Creates empty files or updates timestamps.

Common options:

| Option | Meaning |
|---|---|
| -c | don't create |
| -t | set timestamp |

Examples:

```bash
touch file.txt
touch file1 file2 file3
touch file{1..5}.txt
touch file{1..9..2}.txt
touch -c existing.txt
touch -t 202401010101 file.txt
```

---

### 6.2 `ls` — List Files

Lists directory contents.

Common options:

| Option | Meaning |
|---|---|
| -l | long listing |
| -a | include hidden |
| -h | human readable |
| -R | recursive |

Examples:

```bash
ls
ls -l
ls -la
ls -lh
ls -R
ls *.txt
```

---

### 6.3 `cp` — Copy Files

Copies files or directories.

Common options:

| Option | Meaning |
|---|---|
| -r | recursive |
| -i | interactive |
| -v | verbose |

Examples:

```bash
cp file1 file2
cp *.txt docs/
cp -r project backup/
cp -i file1 file2
cp -v file1 backup/
```

---

### 6.4 `mv` — Move/Rename Files

Moves or renames files.

Common options:

| Option | Meaning |
|---|---|
| -i | interactive |
| -v | verbose |

Examples:

```bash
mv old new
mv *.log logs/
mv report.txt ../archive/
mv -i file dest
mv -v file dest
```

---

### 6.5 `find` — Search Filesystem

Searches directory trees.

Common options:

| Option | Meaning |
|---|---|
| -name | filename match |
| -type | file type |
| -size | size filter |
| -exec | execute command |

Examples:

```bash
find . -name "*.txt"
find /var/log -type f
find . -size +1M
find . -name "*.log" -exec rm {} \;
```

---

## 7. `rm` — File and Directory Removal

Removes files or directories.

Common options:

| Option | Meaning |
|---|---|
| -r | recursive |
| -f | force |
| -i | interactive |

Examples:

```bash
rm file.txt
rm -i file.txt
rm -r project/
rm -rf build/
rm *.tmp
```

---

## 8. `tar` and `gzip` — Archiving and Compression

### tar

Archives files.

Common options:

| Option | Meaning |
|---|---|
| -c | create |
| -x | extract |
| -v | verbose |
| -f | filename |
| -z | gzip |

Examples:

```bash
tar -cvf project.tar project/
tar -xvf project.tar
tar -czvf project.tar.gz project/
```

### gzip

Compresses files.

Common options:

| Option | Meaning |
|---|---|
| -d | decompress |
| -k | keep original |

Examples:

```bash
gzip file.txt
gzip -k file.txt
gzip -d file.txt.gz
```

---

## 9. Globbing (Metacharacters)

Shell expands patterns before execution.

Metacharacters:

| Pattern | Meaning |
|---|---|
| * | any characters |
| ?(hook) | single character |
| [abc] | set |
| [a-z] | range |
| {a,b} | alternatives |
| {1..5} | sequence |

Examples:

```bash
ls *.txt
cp data* backup/
mv log2023*.txt archive/
rm *.tmp
ls file?.txt
ls report[1-5].txt
cp file{1,2,3}.txt backup/
mkdir dir{1..5}
cp *.{jpg,png} images/
mv report_202[0-3].txt archive/
rm file?.log
cp {a..d}.txt letters/
touch file{1..9..2}.txt
```

---

**End of Week 2**