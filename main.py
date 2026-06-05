(venv) PS D:\Wary\MEMS> python app.py
PSU CONNECTION FAILED
could not open port 'COM5': PermissionError(13, 'Access is denied.', None, 5)
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [05/Jun/2026 11:36:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:36:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:36:56] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:36:56] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 11:36:56] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 11:36:57] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:36:59] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:02] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:04] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:05] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:06] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:06] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 11:37:06] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 11:37:07] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:07] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:08] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:09] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:10] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:10] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:17] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:19] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:37:19] "GET /data HTTP/1.1" 200 -
SCPI QUERY [*IDN?] -> 

========================
PSU CONNECTED
PORT: COM5
ID: 
========================

127.0.0.1 - - [05/Jun/2026 11:37:22] "POST /connect_psu HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 

Trying baudrate: 9600
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:37:27] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:37:34] "GET /data HTTP/1.1" 200 -

Trying baudrate: 9600
FAILED at 9600: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)

Trying baudrate: 19200
FAILED at 19200: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)

Trying baudrate: 38400
FAILED at 38400: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)

Trying baudrate: 57600
FAILED at 57600: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)

Trying baudrate: 115200
FAILED at 115200: could not open port 'COM3': PermissionError(13, 'Access is denied.', None, 5)
127.0.0.1 - - [05/Jun/2026 11:37:36] "POST /connect_dmm HTTP/1.1" 500 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:37:36] "GET /data HTTP/1.1" 200 -
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
RAW ID RESPONSE: GWInstek,GDM8261A,GEO882227,1.02

================================
DMM CONNECTED SUCCESSFULLY
PORT: COM3
BAUDRATE: 9600
DMM ID: GWInstek,GDM8261A,GEO882227,1.02
================================

127.0.0.1 - - [05/Jun/2026 11:37:38] "POST /connect_dmm HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:37:43] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:37:47] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:37:52] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:37:57] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:01] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:06] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:10] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VSET1?] -> 
VSET1? = 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:17] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:22] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:27] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:31] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:36] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:41] "GET /data HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:45] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:50] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:54] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:38:59] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:04] "GET /data HTTP/1.1" 200 -
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 11:39:06] "POST /psu/set HTTP/1.1" 200 -
SCPI QUERY [VSET1?] -> 
VSET1? = 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:13] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:20] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:24] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:29] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:36] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:41] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:43] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:50] "GET /data HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 11:39:50] "POST /psu/start HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:54] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:39:59] "GET /data HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 11:39:59] "POST /psu/start HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 11:39:59] "POST /psu/start HTTP/1.1" 200 -
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 11:40:01] "POST /psu/set HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:08] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:13] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:22] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:24] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:29] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:40:31] "POST /dmm/start HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:36] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:38] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:43] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:45] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:50] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:54] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:40:59] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:41:04] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.200195E+1
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:41:11] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.200185E+1
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:41:19] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:41:23] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.43691E-2
RAW RESPONSE: -1.44348E-2
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:41:32] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:41:35] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.45519E-2
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:41:41] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.45839E-2
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:41:48] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46018E-2
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.46080E-2
RAW RESPONSE: -1.46122E-2
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.46194E-2
RAW RESPONSE: -1.46216E-2
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:42:09] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46262E-2
RAW RESPONSE: -1.46283E-2
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:42:18] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:42:21] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:42:25] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:42:28] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
(venv) PS D:\Wary\MEMS> 
