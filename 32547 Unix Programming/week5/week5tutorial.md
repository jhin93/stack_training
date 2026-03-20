## grep meta characters

- ^, $ - carat and the dollar sign match the beginning and end of a line, respectively;
- \<, \> - the beginning and end of a word;
- . - full-stop matches any character.
- string1\|string2 - matches either the text string1 or the text string2
- [abc] - matches any character that is one of "a" or "b" or "c"
- [^abc] - matches any character that is NOT one of "a" or "b" or "c"
- [a-z], [A-Z], [0-9] - matches a lowercase character, an uppercase character, a digit, respectively
- *, \+ - * matches zero or more of the previous thing. \+ matches 1 or more of the previous thing.

## egrep and or (grep -E) meta characters
- ^,$ - carat and the dollar sign match the beginning and end of a line, respectively;
- \b the beginning and end of a word
- . - full-stop matches any character.
- \. a literal full-stop ,note the \
- string1|string2 - matches either the text string1 or the text string2
- [abc] - matches any character that is one of "a" or "b" or "c"
- [^abc] - matches any character that is NOT one of "a" or "b" or "c"
- [a-z], [A-Z], [0-9] - matches a lowercase character, an uppercase character, a digit, respectively
- *, + - * matches zero or more of the previous thing. + matches 1 or more of the previous thing.

When using these expressions in grep, you need to enclose your pattern in quotes to prevent bash from interpreting those symbols.

Its also helpful to use the --color option to see what is matched.

아래 명령어들 뭔지 공부하기

[user@sahara ~]$ ls /bin | grep '[xz]$'
[user@sahara ~]$ ls /bin | grep '^[aeiou]'
[user@sahara ~]$ ls /bin | grep '^q'
[user@sahara ~]$ ls /bin | grep '^[0123456789]'
411toppm
[user@sahara ~]$ ls /bin | grep '^[0-9]'
411toppm
[user@sahara ~]$ ls /bin | grep '^[^0-9].*[0-9].*[^0-9]$' | wc -l
560
[user@sahara ~]$ vim email.txt
[user@sahara ~]$ cat email.txt 


ryan@ryanheise.com
bob@jones
bob@jones.
bob@jones.9
bob@jim . smith
massimo@uts.edu.au
[user@sahara ~]$ cat email.txt | grep -E '^[a-z@0-9.\-]+@[a-z.]+'
[user@sahara ~]$ grep '^#!' *


hello           "hello"
hel*o           zero or more l's 
hel+o           at least one l  <-- Extended
hel?o           zero or one l's
hel{2}o         exactly 2 l's   <-- Extended
hel{2,4}o       between 2 - 4 l's   <-- Extended
hel{2,}o        at least 2 l's  <-- Extended
hel{,4}o        at most 4 l's   <-- Extended
[abc]           a or b or c 
[^abc]          any character EXCEPT for (a or b or c)
hello$          hello at the end of the line
^hello          hello at the beginning of the line
^[^z]           any line that begins with some character except z
[a-z]           a lowercase character
[A-Z]           a uppercase character
[a-zA-Z]        any letter
[aeiou]         a vowel
a|e|i|o|u       a vowel     <-- Extended
dog|cat         dog or cat      <-- Extended
dog*            dogggggggggggg
(dog)*          dogdogdogdogdogdogdogdogdog
(dog|cat)*      dogdogcatdogcatcatdogcat
.               any character
\.              an actual dot
\$              an actual dollar sign

ls *.txt === ls | grep '.*\.txt$'


















