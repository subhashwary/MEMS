(venv) PS D:\Wary\MEMS> python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [05/Jun/2026 16:31:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:31:58] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:31:59] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:02] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:04] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:05] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:05] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:06] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 16:32:06] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:06] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 16:32:07] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:09] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:10] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:12] "GET /data HTTP/1.1" 200 -

Testing PSU...
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN = 
127.0.0.1 - - [05/Jun/2026 16:32:13] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
127.0.0.1 - - [05/Jun/2026 16:32:15] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 

========================
PSU CONNECTED
PORT: COM5
ID: 
========================

127.0.0.1 - - [05/Jun/2026 16:32:15] "POST /connect_psu HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:17] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:19] "GET /data HTTP/1.1" 200 -

Trying baudrate: 9600
127.0.0.1 - - [05/Jun/2026 16:32:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:22] "GET /data HTTP/1.1" 200 -
RAW BYTES = b'GWInstek,GDM8261A,GEO882227,1.02\r'
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
RAW ID RESPONSE: GWInstek,GDM8261A,GEO882227,1.02

================================
DMM CONNECTED SUCCESSFULLY
PORT: COM3
BAUDRATE: 9600
DMM ID: GWInstek,GDM8261A,GEO882227,1.02
================================

127.0.0.1 - - [05/Jun/2026 16:32:22] "POST /connect_dmm HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:25] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:28] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:30] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:33] "GET /data HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
127.0.0.1 - - [05/Jun/2026 16:32:34] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET1? = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 16:32:35] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:42] "GET /data HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET1? = 
127.0.0.1 - - [05/Jun/2026 16:32:43] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 16:32:43] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:45] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
127.0.0.1 - - [05/Jun/2026 16:32:46] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 16:32:47] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:48] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:49] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:51] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:52] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:54] "GET /data HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
127.0.0.1 - - [05/Jun/2026 16:32:55] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 16:32:56] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:32:57] "GET /data HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
127.0.0.1 - - [05/Jun/2026 16:32:58] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 16:32:59] "POST /psu/start HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
127.0.0.1 - - [05/Jun/2026 16:33:00] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 16:33:00] "POST /psu/start HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
127.0.0.1 - - [05/Jun/2026 16:33:01] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 16:33:02] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:04] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:07] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:09] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:10] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:19] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:22] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:33:25] "GET /data HTTP/1.1" 200 -
