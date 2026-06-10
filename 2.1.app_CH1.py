(venv) PS D:\Wary\MEMS> python app.py                                                                                                  
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [10/Jun/2026 10:18:14] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:18:15] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [10/Jun/2026 10:18:15] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [10/Jun/2026 10:18:17] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:18:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:18:30] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:18:31] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [10/Jun/2026 10:18:31] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [10/Jun/2026 10:18:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:18:32] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [10/Jun/2026 10:18:32] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:18:33] "GET /data HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [10/Jun/2026 10:18:38] "GET /data HTTP/1.1" 200 -
HEX = 475720494e5354454b2c4750442d32333033532c534e3a454c3836333637322c56322e30340d0a
RAW BYTES = b'GW INSTEK,GPD-2303S,SN:EL863672,V2.04\r\n'
SCPI QUERY [*IDN?] -> GW INSTEK,GPD-2303S,SN:EL863672,V2.04
127.0.0.1 - - [10/Jun/2026 10:18:41] "GET /data HTTP/1.1" 200 -
HEX = 332e303030560d0a
RAW BYTES = b'3.000V\r\n'
SCPI QUERY [VSET1?] -> 3.000V
127.0.0.1 - - [10/Jun/2026 10:18:44] "GET /data HTTP/1.1" 200 -
HEX = 302e353030410d0a
RAW BYTES = b'0.500A\r\n'
SCPI QUERY [ISET1?] -> 0.500A
IDN  = GW INSTEK,GPD-2303S,SN:EL863672,V2.04
VSET = 3.000V
ISET = 0.500A
127.0.0.1 - - [10/Jun/2026 10:18:45] "GET /data HTTP/1.1" 200 -
HEX = 322e303030560d0a
RAW BYTES = b'2.000V\r\n'
SCPI QUERY [VSET1?] -> 2.000V
127.0.0.1 - - [10/Jun/2026 10:18:48] "GET /data HTTP/1.1" 200 -
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
VERIFY V = 2.000V
VERIFY I = 0.100A
PORT = COM5
BAUD = 9600
OPEN = True

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
================================

127.0.0.1 - - [10/Jun/2026 10:18:50] "POST /connect_psu HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:18:51] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:18:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:18:54] "POST /psu/set HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:18:55] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:18:57] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:18:59] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:00] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:02] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:03] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:05] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:19:06] "POST /psu/set HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:08] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:19:09] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:11] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:19:13] "POST /psu/set HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:15] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:16] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:18] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:19:21] "POST /psu/set HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:22] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:24] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:19:26] "POST /psu/set HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:19:28] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:19:30] "POST /psu/start HTTP/1.1" 200 -
HEX = 362e303038560d0a
RAW BYTES = b'6.008V\r\n'
SCPI QUERY [VOUT1?] -> 6.008V

Trying baudrate: 9600

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
127.0.0.1 - - [10/Jun/2026 10:19:35] "POST /connect_dmm HTTP/1.1" 500 -
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU V = 6.008V
PSU I = 0.000A
127.0.0.1 - - [10/Jun/2026 10:19:36] "GET /data HTTP/1.1" 200 -
HEX = 4757496e7374656b2c47444d38323631412c47454f3838323232372c312e30320d
RAW BYTES = b'GWInstek,GDM8261A,GEO882227,1.02\r'
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
RAW ID RESPONSE: GWInstek,GDM8261A,GEO882227,1.02

================================
DMM CONNECTED SUCCESSFULLY
PORT: COM3
BAUDRATE: 9600
DMM ID: GWInstek,GDM8261A,GEO882227,1.02
================================

127.0.0.1 - - [10/Jun/2026 10:19:40] "POST /connect_dmm HTTP/1.1" 200 -
HEX = 362e303038560d0a
RAW BYTES = b'6.008V\r\n'
SCPI QUERY [VOUT1?] -> 6.008V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU V = 6.008V
PSU I = 0.000A
127.0.0.1 - - [10/Jun/2026 10:19:44] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:19:45] "POST /dmm/start HTTP/1.1" 200 -
RAW RESPONSE: +0.600964E+1
HEX = 362e303038560d0a
RAW BYTES = b'6.008V\r\n'
SCPI QUERY [VOUT1?] -> 6.008V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU V = 6.008V
PSU I = 0.000A
127.0.0.1 - - [10/Jun/2026 10:19:52] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.600958E+1
HEX = 362e303038560d0a
RAW BYTES = b'6.008V\r\n'
SCPI QUERY [VOUT1?] -> 6.008V
127.0.0.1 - - [10/Jun/2026 10:19:57] "POST /dmm/stop HTTP/1.1" 200 -
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU V = 6.008V
PSU I = 0.000A
127.0.0.1 - - [10/Jun/2026 10:19:59] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:20:00] "GET /data HTTP/1.1" 200 -
HEX = 362e303038560d0a
RAW BYTES = b'6.008V\r\n'
SCPI QUERY [VOUT1?] -> 6.008V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU V = 6.008V
PSU I = 0.000A
127.0.0.1 - - [10/Jun/2026 10:20:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:20:06] "POST /psu/stop HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:08] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:09] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:11] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:12] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:14] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [10/Jun/2026 10:20:17] "POST /psu/set HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:18] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:20] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:21] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:23] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:24] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:26] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:27] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:29] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:30] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:32] "GET /data HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [10/Jun/2026 10:20:34] "GET /data HTTP/1.1" 200 -
