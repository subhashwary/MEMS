127.0.0.1 - - [10/Jun/2026 17:17:20] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:21] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:22,351] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:22] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:22] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:23] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:23] "POST /auto/start HTTP/1.1" 200 -
[2026-06-10 17:17:23,843] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:23] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:23] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:24] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:25,351] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:25] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:25] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:26,853] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:26] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:26] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:27] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:28] "POST /auto/stop HTTP/1.1" 200 -
[2026-06-10 17:17:28,352] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:28] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:28] "GET /status HTTP/1.1" 200 -

Trying PSU baudrate: 9600
[2026-06-10 17:17:29,847] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:29] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:29] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:30] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:31,348] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:31] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:31] "GET /status HTTP/1.1" 200 -
HEX = 475720494e5354454b2c4750442d32333033532c534e3a454c3836333637322c56322e30340d0a
RAW BYTES = b'GW INSTEK,GPD-2303S,SN:EL863672,V2.04\r\n'
SCPI QUERY [*IDN?] -> GW INSTEK,GPD-2303S,SN:EL863672,V2.04
[2026-06-10 17:17:32,851] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:32] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:32] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:33] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:34,352] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:34] "GET /data HTTP/1.1" 500 -
HEX = 322e303030560d0a
RAW BYTES = b'2.000V\r\n'
SCPI QUERY [VSET1?] -> 2.000V
127.0.0.1 - - [10/Jun/2026 17:17:34] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:35,852] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:35] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:35] "GET /status HTTP/1.1" 200 -
HEX = 302e323030410d0a
RAW BYTES = b'0.200A\r\n'
SCPI QUERY [ISET1?] -> 0.200A
IDN  = GW INSTEK,GPD-2303S,SN:EL863672,V2.04
VSET = 2.000V
ISET = 0.200A
127.0.0.1 - - [10/Jun/2026 17:17:36] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:37,353] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:37] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:37] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:38,859] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:38] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:38] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:39] "GET /status HTTP/1.1" 200 -
HEX = 322e303030560d0a
RAW BYTES = b'2.000V\r\n'
SCPI QUERY [VSET1?] -> 2.000V
[2026-06-10 17:17:40,350] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:40] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:40] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:41,861] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:41] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:41] "GET /data HTTP/1.1" 500 -
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
VERIFY V = 2.000V
VERIFY I = 0.100A
PORT = COM5
BAUD = 9600
OPEN = True

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
================================

127.0.0.1 - - [10/Jun/2026 17:17:42] "POST /connect_psu HTTP/1.1" 200 -
[2026-06-10 17:17:43,513] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:43] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:43] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:43] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:44,846] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:44] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:44] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:45] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:46,345] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:46] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:46] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:47,851] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:47] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:47] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:48] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:49,352] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:49] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:49] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:50,845] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:50] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:50] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:50] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:51] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:52,356] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:52] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:52] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:53,848] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:53] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:53] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:54] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:55] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:55] "POST /auto/start HTTP/1.1" 200 -
[2026-06-10 17:17:55,346] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:55] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:55] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:56,848] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:56] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:17:56] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:57] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:58,343] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:58] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:58] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:17:59,848] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:17:59] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:17:59] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:00] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:01,344] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:01] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:01] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:02,858] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:02] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:02] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:03] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:04,351] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:04] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:04] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:05,846] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:05] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:05] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:06] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:07,348] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:07] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:07] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:08,850] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:08] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:08] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:09] "POST /auto/stop HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:09] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:10,348] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:10] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:10] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:11,846] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:11] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:11] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:12] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:13,342] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:13] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:13] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:14] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:14] "POST /auto/start HTTP/1.1" 200 -
[2026-06-10 17:18:14,847] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:14] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:14] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:15] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:16,343] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:16] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:16] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:17,852] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:17] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:17] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:18] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:19,346] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:19] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:19] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:20,847] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:20] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:20] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:21] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:22,351] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:22] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:22] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:23,848] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:23] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:23] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:24] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:25,345] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:25] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:25] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:26,846] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:26] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:26] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:28] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:29,170] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:29] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:29] "GET /data HTTP/1.1" 500 -
[2026-06-10 17:18:30,178] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:30] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:30] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 17:18:31] "GET /status HTTP/1.1" 200 -
[2026-06-10 17:18:32,172] ERROR in app: Exception on /data [GET]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 376, in data
    completed_cycles = int(adjusted // cycle_period)
                           ^^^^^^^^
UnboundLocalError: cannot access local variable 'adjusted' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 17:18:32] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 17:18:32] "GET /data HTTP/1.1" 500 -
