(venv) PS D:\Wary\MEMS> python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [06/Jun/2026 16:20:10] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:20:10] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 16:20:10] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 16:20:10] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:20:17] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:20:17] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 16:20:17] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 16:20:17] "GET /ports HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [06/Jun/2026 16:20:22] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
127.0.0.1 - - [06/Jun/2026 16:20:26] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
127.0.0.1 - - [06/Jun/2026 16:20:28] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
127.0.0.1 - - [06/Jun/2026 16:20:31] "GET /data HTTP/1.1" 200 -
PORT = COM5
BAUD = 9600
OPEN = True

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
================================

127.0.0.1 - - [06/Jun/2026 16:20:32] "POST /connect_psu HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:20:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:20:42] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:20:42] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:20:48] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:20:52] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:20:54] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:20:54] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:20:54] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:20:57] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 16:20:57] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:21:04] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 16:21:08] "GET /data HTTP/1.1" 200 -
