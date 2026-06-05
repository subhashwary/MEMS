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
127.0.0.1 - - [05/Jun/2026 11:56:48] "GET / HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:56:48] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 11:56:48] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 11:56:48] "GET /ports HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:56:53] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:56:55] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:56:57] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:56:57] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 11:56:57] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 11:56:57] "GET /ports HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:57:00] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 

Trying baudrate: 9600
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:57:06] "GET /data HTTP/1.1" 200 -
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:57:09] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
RAW ID RESPONSE: GWInstek,GDM8261A,GEO882227,1.02

================================
DMM CONNECTED SUCCESSFULLY
PORT: COM3
BAUDRATE: 9600
DMM ID: GWInstek,GDM8261A,GEO882227,1.02
================================

127.0.0.1 - - [05/Jun/2026 11:57:13] "POST /connect_dmm HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI Query Error: 'NoneType' object has no attribute 'hEvent'
PSU read error: could not convert string to float: 'ERROR'
SCPI Query Error: WriteFile failed (OSError(9, 'The handle is invalid.', None, 6))
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: exception: access violation reading 0x0000000000000000
PSU read error: could not convert string to float: 'ERROR'
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
PSU read error: could not convert string to float: 'ERROR'
SCPI Query Error: Attempting to use a port that is not open
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
SCPI Query Error: Attempting to use a port that is not open
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:16] "GET /data HTTP/1.1" 200 -
SCPI Query Error: Attempting to use a port that is not open
SCPI Query Error: Attempting to use a port that is not open
PSU read error: could not convert string to float: 'ERROR'
127.0.0.1 - - [05/Jun/2026 11:57:17] "GET /data HTTP/1.1" 200 -
SCPI QUERY [*IDN?] -> 

========================
PSU CONNECTED
PORT: COM5
ID: 
========================

127.0.0.1 - - [05/Jun/2026 11:57:19] "POST /connect_psu HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:57:24] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:57:29] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:57:33] "GET /data HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [VSET1?] -> 
VSET1? = 

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:57:42] "GET /data HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:57:45] "GET /data HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [VSET1?] -> 
VSET1? = 
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 11:57:49] "POST /psu/set HTTP/1.1" 200 -
SCPI QUERY [VSET1?] -> 
VSET1? = 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:57:59] "GET /data HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [VSET1?] -> 
VSET1? = 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [VSET1?] -> 
VSET1? = 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:58:10] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:58:15] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 11:58:19] "POST /psu/set HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:58:22] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:58:26] "GET /data HTTP/1.1" 200 -
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 11:58:29] "POST /psu/set HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:58:31] "GET /data HTTP/1.1" 200 -
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 11:58:33] "POST /psu/set HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
PSU CMD -> VSET1:1.0
PSU CMD -> ISET1:0.1
SCPI QUERY [ISET1?] -> 
ISET1? = 
127.0.0.1 - - [05/Jun/2026 11:58:36] "POST /psu/set HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:58:40] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:58:45] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VSET1?] -> 
VSET1? = 
SCPI QUERY [VOUT1?] -> 
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [05/Jun/2026 11:58:52] "GET /data HTTP/1.1" 200 -
(venv) PS D:\Wary\MEMS> 
