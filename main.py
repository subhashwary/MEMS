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
127.0.0.1 - - [05/Jun/2026 14:48:28] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 14:48:28] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 14:48:28] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 14:48:29] "GET /ports HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:32] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:34] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 14:48:37] "GET / HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:38] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 14:48:38] "GET /static/images/cense.png HTTP/1.1" 304 -
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 14:48:38] "GET /ports HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:40] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:42] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:44] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:46] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 

========================
PSU CONNECTED
PORT: COM5
ID: 
========================

127.0.0.1 - - [05/Jun/2026 14:48:48] "POST /connect_psu HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 

========================
PSU CONNECTED
PORT: COM5
ID: 
========================

127.0.0.1 - - [05/Jun/2026 14:48:50] "POST /connect_psu HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:52] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 

Trying baudrate: 9600
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:54] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:56] "GET /data HTTP/1.1" 200 -
RAW BYTES = b'GWInstek,GDM8261A,GEO882227,1.02\r'
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
RAW ID RESPONSE: GWInstek,GDM8261A,GEO882227,1.02

================================
DMM CONNECTED SUCCESSFULLY
PORT: COM3
BAUDRATE: 9600
DMM ID: GWInstek,GDM8261A,GEO882227,1.02
================================

127.0.0.1 - - [05/Jun/2026 14:48:57] "POST /connect_dmm HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:48:59] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:01] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:03] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:05] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:07] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:09] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:11] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:13] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:15] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:17] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:19] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:21] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:23] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
PSU CMD -> VSET1:2.0
PSU CMD -> ISET1:0.2
127.0.0.1 - - [05/Jun/2026 14:49:25] "GET /data HTTP/1.1" 200 -
PSU CMD -> OUT1
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 14:49:25] "POST /psu/start HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 2.0
Current = 0.2
====================
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:27] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:29] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
PSU CMD -> VSET1:2.0
PSU CMD -> ISET1:0.2
127.0.0.1 - - [05/Jun/2026 14:49:31] "GET /data HTTP/1.1" 200 -
PSU CMD -> OUT1
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 14:49:31] "POST /psu/start HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 2.0
Current = 0.2
====================
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:33] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:36] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:38] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:40] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:42] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 14:49:44] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
PSU CMD -> VSET1:2.0
PSU CMD -> ISET1:0.2
127.0.0.1 - - [05/Jun/2026 14:49:46] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET1? = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
