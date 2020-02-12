Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=Client()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=Client()
NameError: name 'Client' is not defined
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> a=Client()
>>> b=Server()
>>> b.add_service()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b.add_service()
AttributeError: 'Server' object has no attribute 'add_service'
>>> b.add_services()
Enter Service Name :ftp
Enter Passkey to generate Random Keytest111
>>> b.service_list
{}
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> a=Client()
>>> b=Server()
>>> b.add_services()
Enter Service Name :ftp
Enter Passkey to generate Random Keytest
>>> b.service_list
{'ftp': 'test'}
>>> from random import randint
>>> randint(10,130)
52
>>> a='test'
>>> d={}
>>> d[a]=Server(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[a]=Server(a)
TypeError: __init__() takes 1 positional argument but 2 were given
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> a='test'
>>> d=
SyntaxError: invalid syntax
>>> d={}
>>> d[a]=Server(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    d[a]=Server(a)
TypeError: __init__() takes 1 positional argument but 2 were given
>>> d[a]=Server()
>>> d['test'].add_services()
Enter Service Name :testtt
Enter Passkey to generate Random Key123
>>> print(d)
{'test': <__main__.Server object at 0x00000166AB109668>}
>>> import xxhash
>>> a=xxhash.xxh32()
>>> a.hexdigest
<built-in method hexdigest of xxhash.xxh32 object at 0x00000166AB10E110>
>>> a.hexdigest("test")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.hexdigest("test")
TypeError: hexdigest() takes no arguments (1 given)
>>> a=xxhash.xxh32("test").hexdigest()
>>> a
'3e2023cf'
>>> a=xxhash.xxh32("test").hexdigest()
>>> a
'3e2023cf'
>>> a=xxhash.xxh32("test",seed=1).hexdigest()
>>> a
'f782311e'
>>> a=xxhash.xxh32("test",seed=1).hexdigest()
>>> a
'f782311e'
>>> a=xxhash.xxh32("test",seed=2).hexdigest()
>>> a
'e392746c'
>>> type(a)
<class 'str'>
>>> d={1:2,2:3}
>>> for i in d:
	print(i)

	
1
2
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_servers('2')
>>> create_
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    create_
NameError: name 'create_' is not defined
>>> serv_dict
{'1': <__main__.Server object at 0x0000017976FCA668>, '2': <__main__.Server object at 0x0000017976F80588>}
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_servers('2')
>>> create_client('test1')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    create_client('test1')
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 78, in create_client
    serv_dict[i].add_client(cli_dict[client_name].cl_id)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 45, in add_client
    self.__client_key_list[cl_id]=xxhash.xxh32(str(self.cl_id),seed=self.cl_id).hexdigest()
AttributeError: 'Server' object has no attribute 'cl_id'
>>> serv_dict
{'2': <__main__.Server object at 0x000001F369250588>, '1': <__main__.Server object at 0x000001F369250780>}
>>> cli_dict
{'test1': <__main__.Client object at 0x000001F36929A940>}
>>> cli_dict['test1'].cl_id
3921552
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_servers('2')
>>> create_client('test1')
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_servers('2')
>>> create_client('test1')
>>> create_client('test2')
>>> cli_dict['1'].temp_print()
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    cli_dict['1'].temp_print()
KeyError: '1'
>>> cli_dict['test1'].temp_print()
ID : 5629611
Key : b6834869
>>> cli_dict['test2'].temp_print()
ID : 1665635
Key : 4efd43a5
>>> serv_dict['1'].temp_print()
ID : 594598
Client ID : 1665635
Client Key : 4efd43a5

Client ID : 5629611
Client Key : b6834869

>>> serv_dict['2'].temp_print()
ID : 821208
Client ID : 1665635
Client Key : 4efd43a5

Client ID : 5629611
Client Key : b6834869

>>> serv_dict['2'].temp_print()
ID : 821208
Client ID : 1665635
Client Key : 4efd43a5

Client ID : 5629611
Client Key : b6834869

>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_servers('2')
>>> create_client('test1')
>>> serv_dict['1'].add_services
<bound method Server.add_services of <__main__.Server object at 0x000001A8B0E90780>>
>>> serv_dict['1'].add_services()
Enter Service Name :hello
Enter Passkey to generate Random Key123
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_servers('2')
>>> create_client('test1')
>>> serv_dict['1'].add_services
<bound method Server.add_services of <__main__.Server object at 0x0000023DFC8C07B8>>
>>> serv_dict['1'].add_services()
Enter Service Name :hello
Enter Passkey to generate Random Key :123
>>> serv_dict['2'].temp_print()
ID : 719277
Client ID : 5945081
Client Key : 78d255fe

Printing Service side Info

>>> serv_dict['1'].temp_print()
ID : 462613
Client ID : 5945081
Client Key : 78d255fe

Service Name : hello
Service Key : 7ff9b02e

Printing Service side Info

Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    serv_dict['1'].temp_print()
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 68, in temp_print
    self.__service_key_list[i].temp_print()
AttributeError: 'str' object has no attribute 'temp_print'
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_servers('2')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :hello
Enter Passkey to generate Random Key :123
>>> serv_dict['1'].temp_print()
ID : 457498
Client ID : 9430910
Client Key : 89e219bc

Service Name : hello
Service Key : 7ff9b02e

Printing Service side Info

Name : hello
Service ID : 123
Service Key : 7ff9b02e
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :qwert
Enter Passkey to generate Random Key :12
>>> serv_dict['1'].add_services()
Enter Service Name :asd
Enter Passkey to generate Random Key :12
>>> serv_dict['1'].temp_print()
ID : 33506
Client ID : 3664010
Client Key : 49ae8758

Service Name : qwert
Service Key : 335ee167

Service Name : asd
Service Key : 0717adff

Printing Service side Info

Name : qwert
Service ID : 12
Service Key : 335ee167
Name : asd
Service ID : 12
Service Key : 0717adff
>>> cli_dict['test1'].connect_to('1','qwert')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    cli_dict['test1'].connect_to('1','qwert')
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 23, in connect_to
    a=server.base_auth(self.cl_id)    #First step - Client ID transmitted to Server(AS) without encryption
AttributeError: 'str' object has no attribute 'base_auth'
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :qwert
Enter Passkey to generate Random Key :13
>>> serv_dict['1'].add_services()
Enter Service Name :asdf
Enter Passkey to generate Random Key :12
>>> serv_dict['1'].temp_print()
ID : 791685
Client ID : 3782560
Client Key : b9db2cf7

Service Name : qwert
Service Key : af57444f

Service Name : asdf
Service Key : 88de0368

Printing Service side Info

Name : qwert
Service ID : 13
Service Key : af57444f
Name : asdf
Service ID : 12
Service Key : 88de0368
>>> cli_dict['test1'].connect_to('1','qwert')
First level Authentication 
(['b9db2cf7', 'a7bbf844'], ['537df492', ['a7bbf844', 3782560]])
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :qwert
Enter Passkey to generate Random Key :123
>>> serv_dict['1'].add_services()
Enter Service Name :asdf
Enter Passkey to generate Random Key :12
>>> serv_dict['1'].temp_print()
ID : 938031
Client ID : 9071621
Client Key : 04d19ddf

Service Name : asdf
Service Key : 88de0368

Service Name : qwert
Service Key : d5458980

Printing Service side Info

Name : asdf
Service ID : 12
Service Key : 88de0368
Name : qwert
Service ID : 123
Service Key : d5458980
>>> cli_dict['test1'].connect_to('1','qwert')
First level Authentication 
(['04d19ddf', '1d799678'], ['46ab0e61', ['1d799678', 9071621]])
Second level Authentication
Second level Authorized
(['1d799678', '96948022'], ['d5458980', ['96948022', 9071621]])
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :qwert
Enter Passkey to generate Random Key :123
>>> serv_dict['1'].add_services()
Enter Service Name :asdf
Enter Passkey to generate Random Key :12
>>> serv_dict['1'].temp_print()
ID : 576250
Client ID : 5579925
Client Key : 90e7994a

Service Name : asdf
Service Key : 88de0368

Service Name : qwert
Service Key : d5458980

Printing Service side Info

Name : asdf
Service ID : 12
Service Key : 88de0368
Name : qwert
Service ID : 123
Service Key : d5458980
>>> cli_dict['test1'].connect_to('1','qwert')
First level Authentication 
(['90e7994a', '2f56dcec'], ['1a12bb30', ['2f56dcec', 5579925]])
Second level Authentication
Second level Authorized
(['2f56dcec', '15ffed5d'], ['d5458980', ['15ffed5d', 5579925]])
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    cli_dict['test1'].connect_to('1','qwert')
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 48, in connect_to
    a=serv_dict[server].serc_connect(serc_name,d2,[self.__temp__key_2,self.cl_id])
NameError: name 'serc_name' is not defined
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :qwert
Enter Passkey to generate Random Key :123
>>> serv_dict['1'].add_services()
Enter Service Name :asdf
Enter Passkey to generate Random Key :12
>>> serv_dict['1'].temp_print()
ID : 391325
Client ID : 2843478
Client Key : cb115d88

Service Name : asdf
Service Key : 88de0368

Service Name : qwert
Service Key : d5458980

Printing Service side Info

Name : asdf
Service ID : 12
Service Key : 88de0368
Name : qwert
Service ID : 123
Service Key : d5458980
>>> cli_dict['test1'].connect_to('1','qwert')
First level Authentication 
(['cb115d88', '0b9906f0'], ['6d0cbd9f', ['0b9906f0', 2843478]])
Second level Authentication
Second level Authorized
(['0b9906f0', '84f93aa8'], ['d5458980', ['84f93aa8', 2843478]])
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    cli_dict['test1'].connect_to('1','qwert')
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 48, in connect_to
    a=serv_dict[server].serc_connect(service,d2,[self.__temp__key_2,self.cl_id])
AttributeError: 'Client' object has no attribute '_Client__temp__key_2'
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :qwert
Enter Passkey to generate Random Key :123
>>> serv_dict['1'].add_services()
Enter Service Name :asdf
Enter Passkey to generate Random Key :12
>>> serv_dict['1'].temp_print()
ID : 757495
Client ID : 8531876
Client Key : 33e40da6

Service Name : qwert
Service Key : d5458980

Service Name : asdf
Service Key : 88de0368

Printing Service side Info

Name : qwert
Service ID : 123
Service Key : d5458980
Name : asdf
Service ID : 12
Service Key : 88de0368
>>> cli_dict['test1'].connect_to('1','qwert')
First level Authentication 
(['33e40da6', 'cab102c2'], ['fac4437d', ['cab102c2', 8531876]])
Second level Authentication
Second level Authorized
(['cab102c2', '288e3885'], ['d5458980', ['288e3885', 8531876]])
Third Level Authentication
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    cli_dict['test1'].connect_to('1','qwert')
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 48, in connect_to
    a=serv_dict[server].serc_connect(service,d2,[self.__temp_key_2,self.cl_id])
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 142, in serc_connect
    if d[0]==self.__service_list_key[serc_name]:
AttributeError: 'Server' object has no attribute '_Server__service_list_key'
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :qwert
Enter Passkey to generate Random Key :123
>>> serv_dict['1'].add_services()
Enter Service Name :asdf
Enter Passkey to generate Random Key :1234
>>> serv_dict['1'].temp_print()
ID : 76517
Client ID : 2300496
Client Key : bb368dda

Service Name : qwert
Service Key : d5458980

Service Name : asdf
Service Key : c3d37d68

Printing Service side Info

Name : qwert
Service ID : 123
Service Key : d5458980
Name : asdf
Service ID : 1234
Service Key : c3d37d68
>>> cli_dict['test1'].connect_to('1','qwert')
First level Authentication 
(['bb368dda', '742774f7'], ['11e0871f', ['742774f7', 2300496]])
Second level Authentication
Second level Authorized
(['742774f7', 'e0904b6f'], ['d5458980', ['e0904b6f', 2300496]])
Third Level Authentication
Third Level Authorized!
Invalid Creds!
Connection Successful!
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :qwert
Enter Passkey to generate Random Key :123
>>> serv_dict['1'].add_services()
Enter Service Name :asdf
Enter Passkey to generate Random Key :12
>>> serv_dict['1'].temp_print()
ID : 571174
Client ID : 5121447
Client Key : 0c477937

Service Name : qwert
Service Key : d5458980

Service Name : asdf
Service Key : 88de0368

Printing Service side Info

Name : qwert
Service ID : 123
Service Key : d5458980
Name : asdf
Service ID : 12
Service Key : 88de0368
>>> cli_dict['test1'].connect_to('1','qwert')
First level Authentication 
(['0c477937', '8872ecec'], ['a325e1bc', ['8872ecec', 5121447]])
Second level Authentication
Second level Authorized
(['8872ecec', '8d6d90c8'], ['d5458980', ['8d6d90c8', 5121447]])
Third Level Authentication
qwert ['d5458980', ['8d6d90c8', 5121447]] ['8d6d90c8', 5121447]
Third Level Authorized!
Invalid Creds!
Connection Successful!
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers('1')
>>> create_client('test1')
>>> serv_dict['1'].add_services()
Enter Service Name :qwert
Enter Passkey to generate Random Key :123
>>> serv_dict['1'].add_services()
Enter Service Name :asdf
Enter Passkey to generate Random Key :12
>>> serv_dict['1'].temp_print()
ID : 91399
Client ID : 432910
Client Key : bc9c5350

Service Name : qwert
Service Key : d5458980

Service Name : asdf
Service Key : 88de0368

Printing Service side Info

Name : qwert
Service ID : 123
Service Key : d5458980
Name : asdf
Service ID : 12
Service Key : 88de0368
>>> cli_dict['test1'].connect_to('1','qwert')
First level Authentication 
(['bc9c5350', 'c35e5c27'], ['45f807a3', ['c35e5c27', 432910]])
Second level Authentication
Second level Authorized
(['c35e5c27', 'dddfa4f7'], ['d5458980', ['dddfa4f7', 432910]])
Third Level Authentication
qwert ['d5458980', ['dddfa4f7', 432910]] ['dddfa4f7', 432910]
Third Level Authorized!
Using service qwert
Connection Successful!
>>> 
