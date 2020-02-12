Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a="1234567"
>>> len(a)
7
>>> a[7]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a[7]
IndexError: string index out of range
>>> a[:7]
'1234567'
>>> for i in range(5)
SyntaxError: invalid syntax
>>> for i in range(5):
	print(i)

	
0
1
2
3
4
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Present_Py3.py 
>>> S_box("1111")
'0010'
>>> type(S_box("1111"))
<class 'str'>
>>> a="1"*4
>>> a
'1111'
>>> '1111'^1
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    '1111'^1
TypeError: unsupported operand type(s) for ^: 'str' and 'int'
>>> '1111'^'0001'
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    '1111'^'0001'
TypeError: unsupported operand type(s) for ^: 'str' and 'str'
>>> int('1111',2)
15
>>> to_hex(int('1111',2))
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    to_hex(int('1111',2))
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Present_Py3.py", line 9, in to_hex
    return hex(int(a,2))[-1].upper()
TypeError: int() can't convert non-string with explicit base
>>> int('1111',2)
15
>>> "1000"*16
'1000100010001000100010001000100010001000100010001000100010001000'
>>> 4919131752989213764*2
9838263505978427528
>>> int('1000100010001000100010001000100010001000100010001000100010001000',2)^1
9838263505978427529
>>> "{0:64b}".format(9838263505978427529,2)
'1000100010001000100010001000100010001000100010001000100010001001'
>>> '1000100010001000100010001000100010001000100010001000100010001001'=='1000100010001000100010001000100010001000100010001000100010001001'
True
>>> "{0:064b}".format(9838263505978427529,2)
'1000100010001000100010001000100010001000100010001000100010001001'
>>> 307445734561825860*2
614891469123651720
>>> 307445734561825860*2
614891469123651720
>>> 614891469123651720^1
614891469123651721
>>> "{0:064b}".format(614891469123651721,2)
'0000100010001000100010001000100010001000100010001000100010001001'
>>> len('0000100010001000100010001000100010001000100010001000100010001001')
64
>>> 
