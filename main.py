(venv) PS D:\Wary\MEMS> python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [06/Jun/2026 16:36:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:36:31] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:36:31] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 16:36:31] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 16:36:31] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:36:38] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:36:38] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 16:36:38] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 16:36:38] "GET /ports HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [06/Jun/2026 16:36:42] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
127.0.0.1 - - [06/Jun/2026 16:36:45] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
127.0.0.1 - - [06/Jun/2026 16:36:48] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
127.0.0.1 - - [06/Jun/2026 16:36:51] "GET /data HTTP/1.1" 200 -
PORT = COM5
BAUD = 9600
OPEN = True

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
================================

127.0.0.1 - - [06/Jun/2026 16:36:51] "POST /connect_psu HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:36:57] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:01] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:02] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:37:02] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:37:07] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:37:07] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:13] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:17] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:18] "GET /data HTTP/1.1" 200 -
PSU CMD -> OUT1
127.0.0.1 - - [06/Jun/2026 16:37:18] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
127.0.0.1 - - [06/Jun/2026 16:37:22] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [06/Jun/2026 16:37:25] "POST /psu/start HTTP/1.1" 200 -
PSU CMD -> OUT1
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [06/Jun/2026 16:37:31] "POST /psu/start HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:36] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:39] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:37:40] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:41] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:51] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:55] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:37:56] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:38:08] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:38:12] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:38:13] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:38:23] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:38:27] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:38:28] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:38:39] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:38:50] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:39:00] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:39:11] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:39:21] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:39:32] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:39:34] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:39:37] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:39:47] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:39:57] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:01] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:02] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:14] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:40:14] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 16:40:14] "GET /static/images/cense.png HTTP/1.1" 304 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:40:14] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:40:15] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:18] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:19] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET1? = 
127.0.0.1 - - [06/Jun/2026 16:40:22] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET1? = 
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:29] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VOUT1? = 
127.0.0.1 - - [06/Jun/2026 16:40:33] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:37] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
IOUT1? = 
127.0.0.1 - - [06/Jun/2026 16:40:39] "GET /psu_debug HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:40:40] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:45] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:48] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:40:50] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:41:00] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:41:03] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:41:05] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:41:15] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:41:26] "GET /data HTTP/1.1" 200 -
