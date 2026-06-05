(venv) PS D:\Wary\MEMS> python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [05/Jun/2026 16:43:11] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:11] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 16:43:11] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 16:43:11] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:15] "GET /data HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [05/Jun/2026 16:43:17] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
127.0.0.1 - - [05/Jun/2026 16:43:18] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 

Trying PSU baudrate: 19200
127.0.0.1 - - [05/Jun/2026 16:43:20] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
127.0.0.1 - - [05/Jun/2026 16:43:21] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 

Trying PSU baudrate: 38400
127.0.0.1 - - [05/Jun/2026 16:43:23] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
127.0.0.1 - - [05/Jun/2026 16:43:24] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 

Trying PSU baudrate: 57600
127.0.0.1 - - [05/Jun/2026 16:43:26] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
127.0.0.1 - - [05/Jun/2026 16:43:27] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 

Trying baudrate: 9600
127.0.0.1 - - [05/Jun/2026 16:43:28] "POST /connect_psu HTTP/1.1" 500 -
RAW BYTES = b'GWInstek,GDM8261A,GEO882227,1.02\r'
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
RAW ID RESPONSE: GWInstek,GDM8261A,GEO882227,1.02

================================
DMM CONNECTED SUCCESSFULLY
PORT: COM3
BAUDRATE: 9600
DMM ID: GWInstek,GDM8261A,GEO882227,1.02
================================

127.0.0.1 - - [05/Jun/2026 16:43:31] "POST /connect_dmm HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:33] "GET /data HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [05/Jun/2026 16:43:35] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
127.0.0.1 - - [05/Jun/2026 16:43:36] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 

Trying PSU baudrate: 19200
127.0.0.1 - - [05/Jun/2026 16:43:38] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
127.0.0.1 - - [05/Jun/2026 16:43:39] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 

Trying PSU baudrate: 38400
127.0.0.1 - - [05/Jun/2026 16:43:41] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
127.0.0.1 - - [05/Jun/2026 16:43:42] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 

Trying PSU baudrate: 57600
127.0.0.1 - - [05/Jun/2026 16:43:44] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
127.0.0.1 - - [05/Jun/2026 16:43:45] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
127.0.0.1 - - [05/Jun/2026 16:43:46] "GET /data HTTP/1.1" 200 -
VSET = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
127.0.0.1 - - [05/Jun/2026 16:43:47] "POST /connect_psu HTTP/1.1" 500 -
127.0.0.1 - - [05/Jun/2026 16:43:49] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:51] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 16:43:53] "GET /data HTTP/1.1" 200 -
