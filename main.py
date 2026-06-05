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
127.0.0.1 - - [05/Jun/2026 16:16:41] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:42] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 16:16:42] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 16:16:42] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:44] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:48] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:50] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:51] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 16:16:51] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 16:16:51] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:51] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:52] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:54] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:54] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
127.0.0.1 - - [05/Jun/2026 16:16:55] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:56] "GET /data HTTP/1.1" 200 -
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

127.0.0.1 - - [05/Jun/2026 16:16:56] "POST /connect_psu HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:58] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:58] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:16:59] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:00] "GET /data HTTP/1.1" 200 -

Trying baudrate: 9600
127.0.0.1 - - [05/Jun/2026 16:17:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:02] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:03] "GET /data HTTP/1.1" 200 -
RAW BYTES = b'GWInstek,GDM8261A,GEO882227,1.02\r'
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
RAW ID RESPONSE: GWInstek,GDM8261A,GEO882227,1.02

================================
DMM CONNECTED SUCCESSFULLY
PORT: COM3
BAUDRATE: 9600
DMM ID: GWInstek,GDM8261A,GEO882227,1.02
================================

127.0.0.1 - - [05/Jun/2026 16:17:03] "POST /connect_dmm HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:05] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:05] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:07] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:08] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:09] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:09] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:10] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:17] "GET /data HTTP/1.1" 200 -

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
127.0.0.1 - - [05/Jun/2026 16:17:18] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 16:17:18] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:19] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:22] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:23] "GET /data HTTP/1.1" 200 -

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
127.0.0.1 - - [05/Jun/2026 16:17:24] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 16:17:24] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:25] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:28] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:29] "GET /data HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
127.0.0.1 - - [05/Jun/2026 16:17:30] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:30] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 16:17:31] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:33] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:33] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:34] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:35] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:36] "GET /data HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
127.0.0.1 - - [05/Jun/2026 16:17:37] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:38] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 16:17:38] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:17:39] "POST /dmm/start HTTP/1.1" 200 -
RAW RESPONSE: -1.46366E-2
127.0.0.1 - - [05/Jun/2026 16:17:41] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46367E-2
127.0.0.1 - - [05/Jun/2026 16:17:43] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46368E-2
127.0.0.1 - - [05/Jun/2026 16:17:45] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46375E-2
127.0.0.1 - - [05/Jun/2026 16:17:48] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46375E-2
127.0.0.1 - - [05/Jun/2026 16:17:50] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46375E-2
127.0.0.1 - - [05/Jun/2026 16:17:52] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46379E-2
127.0.0.1 - - [05/Jun/2026 16:17:55] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46381E-2
127.0.0.1 - - [05/Jun/2026 16:17:57] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46383E-2
127.0.0.1 - - [05/Jun/2026 16:18:00] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46383E-2
127.0.0.1 - - [05/Jun/2026 16:18:02] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46381E-2
127.0.0.1 - - [05/Jun/2026 16:18:05] "GET /data HTTP/1.1" 200 -
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
PSU CMD -> OUT1
RAW RESPONSE: -1.46373E-2
127.0.0.1 - - [05/Jun/2026 16:18:07] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46374E-2
127.0.0.1 - - [05/Jun/2026 16:18:10] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46380E-2
127.0.0.1 - - [05/Jun/2026 16:18:12] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46378E-2
127.0.0.1 - - [05/Jun/2026 16:18:15] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46389E-2
127.0.0.1 - - [05/Jun/2026 16:18:17] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46391E-2
127.0.0.1 - - [05/Jun/2026 16:18:20] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46419E-2
127.0.0.1 - - [05/Jun/2026 16:18:22] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
RAW RESPONSE: -1.46424E-2
127.0.0.1 - - [05/Jun/2026 16:18:25] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46411E-2
127.0.0.1 - - [05/Jun/2026 16:18:27] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46402E-2
127.0.0.1 - - [05/Jun/2026 16:18:30] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46405E-2
127.0.0.1 - - [05/Jun/2026 16:18:32] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46402E-2
127.0.0.1 - - [05/Jun/2026 16:18:34] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46413E-2
127.0.0.1 - - [05/Jun/2026 16:18:36] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46418E-2
127.0.0.1 - - [05/Jun/2026 16:18:38] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46415E-2
127.0.0.1 - - [05/Jun/2026 16:18:41] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46418E-2
127.0.0.1 - - [05/Jun/2026 16:18:43] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46414E-2
127.0.0.1 - - [05/Jun/2026 16:18:45] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46413E-2
127.0.0.1 - - [05/Jun/2026 16:18:47] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 16:18:48] "POST /psu/start HTTP/1.1" 200 -
RAW RESPONSE: -1.46412E-2
127.0.0.1 - - [05/Jun/2026 16:18:50] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46418E-2
127.0.0.1 - - [05/Jun/2026 16:18:52] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46409E-2
127.0.0.1 - - [05/Jun/2026 16:18:55] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46406E-2
127.0.0.1 - - [05/Jun/2026 16:18:57] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46415E-2
127.0.0.1 - - [05/Jun/2026 16:19:00] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46432E-2
127.0.0.1 - - [05/Jun/2026 16:19:02] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46445E-2
127.0.0.1 - - [05/Jun/2026 16:19:04] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46458E-2
127.0.0.1 - - [05/Jun/2026 16:19:06] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46457E-2
127.0.0.1 - - [05/Jun/2026 16:19:08] "GET /data HTTP/1.1" 200 -
