Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers
<function create_servers at 0x00000172AEB8B158>
>>> create_servers("1")
>>> create_client("test1")
>>> serv_dict["1"]
<__main__.Server object at 0x00000172AEB87A90>
>>> serv_dict["1"].add_services()
Enter Service Name :Splitter
Enter Passkey to generate Random Key :test123
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    serv_dict["1"].add_services()
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 82, in add_services
    b=int(input("Enter Passkey to generate Random Key :"))
ValueError: invalid literal for int() with base 10: 'test123'
>>> serv_dict["1"].add_services()
Enter Service Name :Splitter
Enter Passkey to generate Random Key :123
>>>  serv_dict['1'].temp_print()
 
SyntaxError: unexpected indent
>>> serv_dict['1'].temp_print()
ID : 410777
Client ID : 1756861
Client Key : 8598bba2

Service Name : Splitter
Service Key : 9cc6a584

Printing Service side Info

Name : Splitter
Service ID : 123
Service Key : 9cc6a584
>>> cli_dict['test1'].connect_to('1','Splitter')
First level Authentication 
(['8598bba2', '976c889d'], ['e666545c', ['976c889d', 1756861]])
Second level Authentication
Second level Authorized
(['976c889d', 'd5fbfe8c'], ['9cc6a584', ['d5fbfe8c', 1756861]])
Third Level Authentication
Splitter ['9cc6a584', ['d5fbfe8c', 1756861]] ['d5fbfe8c', 1756861]
Third Level Authorized!
Connection Successful!
>>> cli_dict['test1'].connect_to('1','Splitter')
First level Authentication 
(['8598bba2', 'cfb958a8'], ['e666545c', ['cfb958a8', 1756861]])
Second level Authentication
Second level Authorized
(['cfb958a8', '7753b83f'], ['9cc6a584', ['7753b83f', 1756861]])
Third Level Authentication
Splitter ['9cc6a584', ['7753b83f', 1756861]] ['7753b83f', 1756861]
Third Level Authorized!
Connection Successful!
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers("1")
>>> create_client("test1")
>>> serv_dict["1"].add_services()
Enter Service Name :Splitter
Enter Passkey to generate Random Key :1134
>>> serv_dict['1'].temp_print()
ID : 253142
Client ID : 8333662
Client Key : c2c573bf

Service Name : Splitter
Service Key : 751ae814

Printing Service side Info

Name : Splitter
Service ID : 1134
Service Key : 751ae814
>>> cli_dict['test1'].connect_to('1','Splitter')
First level Authentication 
(['c2c573bf', '53ee3022'], ['12e86828', ['53ee3022', 8333662]])
Second level Authentication
Second level Authorized
(['53ee3022', 'fa7fd3e8'], ['751ae814', ['fa7fd3e8', 8333662]])
Third Level Authentication
Splitter ['751ae814', ['fa7fd3e8', 8333662]] ['fa7fd3e8', 8333662]
Third Level Authorized!
Connection Successful!
Enter data to be sent :test
Enter data to be sent :test
Enter data to be sent :
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    cli_dict['test1'].connect_to('1','Splitter')
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 56, in connect_to
    a=input("Enter data to be sent :")
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\lib\idlelib\PyShell.py", line 1386, in readline
    line = self._line_buffer or self.shell.readline()
KeyboardInterrupt
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
>>> create_servers("1")
>>> create_client("test1")
>>> serv_dict["1"].add_services()
Enter Service Name :Splitter
Enter Passkey to generate Random Key :12345
>>> serv_dict['1'].temp_print()
ID : 111084
Client ID : 6786245
Client Key : 0e130570

Service Name : Splitter
Service Key : 82bb832d

Printing Service side Info

Name : Splitter
Service ID : 12345
Service Key : 82bb832d
>>> cli_dict['test1'].connect_to('1','Splitter')
First level Authentication 
(['0e130570', 'b58585d5'], ['fc6b6cdc', ['b58585d5', 6786245]])
Second level Authentication
Second level Authorized
(['b58585d5', '90d64336'], ['82bb832d', ['90d64336', 6786245]])
Third Level Authentication
Splitter ['82bb832d', ['90d64336', 6786245]] ['90d64336', 6786245]
Third Level Authorized!
Connection Successful!
Do you want to send data (Y/n)? n
>>> cli_dict['test1'].connect_to('1','Splitter')
First level Authentication 
(['0e130570', '5f4fcc46'], ['fc6b6cdc', ['5f4fcc46', 6786245]])
Second level Authentication
Second level Authorized
(['5f4fcc46', '16690179'], ['82bb832d', ['16690179', 6786245]])
Third Level Authentication
Splitter ['82bb832d', ['16690179', 6786245]] ['16690179', 6786245]
Third Level Authorized!
Connection Successful!
Do you want to send data (Y/n)? y
Enter Data (0 to quit) :0
Connection Terminated
>>> cli_dict['test1'].connect_to('1','Splitter')
First level Authentication 
(['0e130570', '9e523e2c'], ['fc6b6cdc', ['9e523e2c', 6786245]])
Second level Authentication
Second level Authorized
(['9e523e2c', 'debdb989'], ['82bb832d', ['debdb989', 6786245]])
Third Level Authentication
Splitter ['82bb832d', ['debdb989', 6786245]] ['debdb989', 6786245]
Third Level Authorized!
Connection Successful!
Do you want to send data (Y/n)? y
Enter Data (0 to quit) :abcdefgaa
Third Level Authentication
Splitter ['82bb832d', ['debdb989', 6786245]] ['debdb989', 6786245]
Third Level Authorized!
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    cli_dict['test1'].connect_to('1','Splitter')
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 61, in connect_to
    a=serv_dict[server].serc_connect(service,d2,[self.__temp_key_2,self.cl_id],dat)
  File "C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py", line 174, in serc_connect
    if i not in token:
NameError: name 'token' is not defined
>>> 
 RESTART: C:\Users\admin\AppData\Local\Programs\Python\Python35\Kichu_FYP\Kerb_Base.py 
Enter Service Name :Splitter
Enter Passkey to generate Random Key :123
ID : 268165
Client ID : 3942845
Client Key : 81ae24e6

Service Name : Splitter
Service Key : 9cc6a584

Printing Service side Info

Name : Splitter
Service ID : 123
Service Key : 9cc6a584
>>> cli_dict['test1'].connect_to('1','Splitter')
First level Authentication 
(['81ae24e6', '4cf772f0'], ['74a77115', ['4cf772f0', 3942845]])
Second level Authentication
Second level Authorized
(['4cf772f0', 'e3ce8a99'], ['9cc6a584', ['e3ce8a99', 3942845]])
Third Level Authentication
Splitter ['9cc6a584', ['e3ce8a99', 3942845]] ['e3ce8a99', 3942845]
Third Level Authorized!
Connection Successful!
Do you want to send data (Y/n)? y
Enter Data (0 to quit) :abcdefaa
Third Level Authentication
Splitter ['9cc6a584', ['e3ce8a99', 3942845]] ['e3ce8a99', 3942845]
Third Level Authorized!
{'e': 1, 'd': 1, 'c': 1, 'b': 1, 'a': 3, 'f': 1}

Enter Data (0 to quit) :abcdefff
Third Level Authentication
Splitter ['9cc6a584', ['e3ce8a99', 3942845]] ['e3ce8a99', 3942845]
Third Level Authorized!
{'e': 1, 'd': 1, 'c': 1, 'b': 1, 'a': 1, 'f': 3}

Enter Data (0 to quit) :0
Connection Terminated
>>> 
