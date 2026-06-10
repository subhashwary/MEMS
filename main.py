  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:45] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:45] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:01:46,571] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:46] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:47] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:01:48] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:01:48,074] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:48] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:48] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:01:49,576] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:49] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:50] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:01:51] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:01:51,078] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:51] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:51] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:01:52,575] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:52] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:53] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:01:54] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:01:54,077] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:54] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:54] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:01:55,570] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:55] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:56] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:01:57] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:01:57,078] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:57] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:57] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:01:58,573] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:01:58] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:01:59] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:00] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:00,076] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:00] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:00] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:02:01,576] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:01] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:02] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:03] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:03,071] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:03] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:03] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:02:04,578] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:04] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:04] "POST /mode HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:06] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:06,073] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:06] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:06] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:02:07,571] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:07] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:07] "POST /mode HTTP/1.1" 200 -
[2026-06-10 15:02:09,077] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:09] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:09] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:10,569] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:10] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:11] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:12,075] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:12] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 15:02:12] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:12] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:13,575] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:13] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:14] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:15,080] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:15] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:15] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:16,571] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:16] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:17] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:18,085] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:18] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 15:02:18] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:18] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:19,578] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:19] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:20] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:21,073] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:21] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:21] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:22,576] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:22] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:23] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:24,074] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 354, in data
    if elapsed < initial_delay:
       ^^^^^^^
UnboundLocalError: cannot access local variable 'elapsed' where it is not associated with a value
127.0.0.1 - - [10/Jun/2026 15:02:24] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:24] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 15:02:25] "POST /auto/start HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 15:02:26] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:26] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:26,540] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:26] "GET /data HTTP/1.1" 500 -
[2026-06-10 15:02:27,080] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:27] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 15:02:27] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:27] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:02:28,578] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:28] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:29] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:30] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:30,074] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:30] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:30] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:02:31,579] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:31] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:32] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:33] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:33,073] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:33] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:33] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:02:34,571] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:34] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:35] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:02:36,076] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:36] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 15:02:36] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:36] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:02:37,577] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:37] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:38] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:39] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:39,078] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:39] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:39] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
[2026-06-10 15:02:40,570] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:40] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:41] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:42] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:42,076] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:42] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:42] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:44] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:44,179] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:44] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:44] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:45,179] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:45] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:45] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:47] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:47,168] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:47] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:47] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:48] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:48,171] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:48] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:48] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 15:02:50] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:50,172] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:50] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:50] "GET /status HTTP/1.1" 200 -
[2026-06-10 15:02:51,165] ERROR in app: Exception on /data [GET]
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
  File "D:\Wary\MEMS\app.py", line 529, in data
    log_data(
TypeError: log_data() takes 5 positional arguments but 8 were given
127.0.0.1 - - [10/Jun/2026 15:02:51] "GET /data HTTP/1.1" 500 -
127.0.0.1 - - [10/Jun/2026 15:02:51] "GET /status HTTP/1.1" 200 -
