Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=89
>>> b=208
>>> a=b
>>> b=a
>>> 
================================ RESTART: Shell ================================
>>> a=4
>>> b=8
>>> a = a+b
>>> b=a-b
>>> a=a-b
>>> print(a,b)
8 4
>>> 
================================ RESTART: Shell ================================
>>> a=4
>>> b=10
>>> a=a*b
>>> b=a-b
>>> a=a/b
>>> print(a,b)
1.3333333333333333 30
>>> 
================================ RESTART: Shell ================================
>>> a=4
>>> B=8
>>> a=a+b
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a=a+b
NameError: name 'b' is not defined
>>> 
================================ RESTART: Shell ================================
>>>  ================================
>>> a=4
>>> b=8
>>> a = a+b
>>> b=a-b
>>> a=a-b
SyntaxError: unexpected indent
>>> 
================================ RESTART: Shell ================================
>>> a=4
>>> b=8
>>> a=a+b
>>> b=a-b
>>> a=a-b
>>> print(a,b)
8 4
>>> 