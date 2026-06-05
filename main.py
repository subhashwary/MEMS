(venv) PS D:\Wary\MEMS> python app.py       
================================
PSU CONNECTED
PORT = COM5
================================
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [05/Jun/2026 14:29:47] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 14:29:47] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 14:29:47] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 14:29:47] "GET /ports HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:29:50] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:29:55] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:00] "GET / HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 14:30:00] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 14:30:00] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 14:30:00] "GET /ports HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:04] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 

Trying baudrate: 9600
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:09] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
RAW ID RESPONSE: GWInstek,GDM8261A,GEO882227,1.02

================================
DMM CONNECTED SUCCESSFULLY
PORT: COM3
BAUDRATE: 9600
DMM ID: GWInstek,GDM8261A,GEO882227,1.02
================================

127.0.0.1 - - [05/Jun/2026 14:30:13] "POST /connect_dmm HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:16] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:20] "GET /data HTTP/1.1" 200 -
SCPI QUERY [*IDN?] -> 
[2026-06-05 14:30:24,325] ERROR in app: Exception on /connect_psu [POST]
Traceback (most recent call last):
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 920, in full_dispatch_request
    return self.finalize_request(rv)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 939, in finalize_request
    response = self.make_response(rv)
               ^^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\flask\app.py", line 1212, in make_response
    raise TypeError(
TypeError: The view function for 'connect_psu' did not return a valid response. The function either returned None or ended without a return statement.
127.0.0.1 - - [05/Jun/2026 14:30:24] "POST /connect_psu HTTP/1.1" 500 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:28] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:33] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:38] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:42] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:47] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:52] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:30:56] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:01] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:05] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:10] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:15] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:19] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:24] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:28] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:33] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:38] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:42] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:47] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:52] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:31:56] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:01] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:05] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:10] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:15] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:19] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:24] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:28] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:33] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:38] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:42] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:47] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:52] "GET /data HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:32:56] "GET /data HTTP/1.1" 200 -
