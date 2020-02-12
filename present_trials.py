Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("{0:04b}".format(int("A",16)))
1010
>>> type("{0:04b}".format(int("A",16)))
<class 'str'>
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Kichu_FYP/Present_Py3.py 
>>> print(to_bin("F"))
1111
>>> print(to_bin("3"))
0011
>>> int("0011",2)
3
>>> int("1111",2)
15
>>> int("0011",16)
17
>>> hex(int("1111",2))
'0xf'
>>> hex(int("1111",2))[:-1]
'0x'
>>> hex(int("1111",2))[-1]
'f'
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Kichu_FYP/Present_Py3.py 
>>> print(to_bin("F"))
1111
>>> to_hex(to_bin("F"))
'F'
>>> to_hex(to_bin("A"))
'A'
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Kichu_FYP/Present_Py3.py 
B   8
0   C
A   F
6   A
D   7
5   0
C   4
E   1
1   5
4   9
F   2
9   E
2   6
7   D
3   B
8   3
>>> int("0011",2)
3
>>> bin(int("0011",2))
'0b11'
>>> a="11111111111"
>>> len(a[:8])
8
>>> b=a
>>> a="11"
>>> b
'11111111111'
>>> a
'11'
>>> b=str(a)
>>> b
'11'
>>> a="12"
>>> a
'12'
>>> b
'11'
>>> a="123456"
>>> a[-3:]+a[:-3]
'456123'
>>> len(a[:4])
4
>>> a[:4]
'1234'
>>> 
 RESTART: C:/Users/admin/AppData/Local/Programs/Python/Python35/Kichu_FYP/Present_Py3.py 
>>> S_box("1111")
'0010'
>>> a="123456789"
>>> len(a)
9
>>> a[:-5]
'1234'
>>> len(a[:-5])
4
>>> 15^1
14
>>> a="543210"
>>> a[:-2]
'5432'
>>> "{0:05b}".format(19,2)
'10011'
>>> int('10011',2)
19
>>> int('10011',10)
10011
>>> int('10011',2)
19
>>> 19^1
18
>>> "{0:05b}".format(18,2)
'10010'
>>> 
