(venv) PS D:\Wary\MEMS> python app.py                                                                                                  
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [11/Jun/2026 11:12:54] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:12:54] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [11/Jun/2026 11:12:54] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [11/Jun/2026 11:12:54] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:12:56] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:12:56] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:12:57] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:12:58] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:12:58] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:12:58] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:12:58] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:12:59] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:00] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:01] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:01] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:01] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [11/Jun/2026 11:13:01] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [11/Jun/2026 11:13:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:01] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:02] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:02] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:03] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:03] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:04] "GET /status HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [11/Jun/2026 11:13:04] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:04] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:04] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:05] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:05] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:06] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:07] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:07] "GET /data HTTP/1.1" 200 -
HEX = 475720494e5354454b2c4750442d32333033532c534e3a454c3836333637322c56322e30340d0a
RAW BYTES = b'GW INSTEK,GPD-2303S,SN:EL863672,V2.04\r\n'
SCPI QUERY [*IDN?] -> GW INSTEK,GPD-2303S,SN:EL863672,V2.04
127.0.0.1 - - [11/Jun/2026 11:13:08] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:08] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:08] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:09] "GET /data HTTP/1.1" 200 -
HEX = 322e303130560d0a
RAW BYTES = b'2.010V\r\n'
SCPI QUERY [VSET1?] -> 2.010V
127.0.0.1 - - [11/Jun/2026 11:13:09] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:10] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:10] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:11] "GET /status HTTP/1.1" 200 -
HEX = 302e323130410d0a
RAW BYTES = b'0.210A\r\n'
SCPI QUERY [ISET1?] -> 0.210A
IDN  = GW INSTEK,GPD-2303S,SN:EL863672,V2.04
VSET = 2.010V
ISET = 0.210A
127.0.0.1 - - [11/Jun/2026 11:13:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:12] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:13] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:14] "GET /status HTTP/1.1" 200 -
HEX = 322e303030560d0a
RAW BYTES = b'2.000V\r\n'
SCPI QUERY [VSET1?] -> 2.000V
127.0.0.1 - - [11/Jun/2026 11:13:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:15] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:16] "GET /status HTTP/1.1" 200 -
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

127.0.0.1 - - [11/Jun/2026 11:13:17] "POST /connect_psu HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:18] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:18] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:19] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:19] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:20] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:21] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:22] "POST /psu/set HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:23] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:24] "GET /status HTTP/1.1" 200 -

Trying baudrate: 9600
FAILED at 9600: could not open port 'COM5': PermissionError(13, 'Access is denied.', None, 5)

Trying baudrate: 19200
FAILED at 19200: could not open port 'COM5': PermissionError(13, 'Access is denied.', None, 5)

Trying baudrate: 38400
FAILED at 38400: could not open port 'COM5': PermissionError(13, 'Access is denied.', None, 5)

Trying baudrate: 57600
FAILED at 57600: could not open port 'COM5': PermissionError(13, 'Access is denied.', None, 5)

Trying baudrate: 115200
FAILED at 115200: could not open port 'COM5': PermissionError(13, 'Access is denied.', None, 5)
127.0.0.1 - - [11/Jun/2026 11:13:25] "POST /connect_dmm HTTP/1.1" 500 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:26] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:26] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:27] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:28] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:28] "GET /data HTTP/1.1" 200 -

Trying baudrate: 9600
127.0.0.1 - - [11/Jun/2026 11:13:29] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:30] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:30] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:31] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:32] "GET /status HTTP/1.1" 200 -
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

127.0.0.1 - - [11/Jun/2026 11:13:33] "POST /connect_dmm HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:34] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:34] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:34] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:34] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:35] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:36] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:37] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:37] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:38] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:39] "GET /status HTTP/1.1" 200 -
HEX = 312e393938560d0a
RAW BYTES = b'1.998V\r\n'
SCPI QUERY [VOUT1?] -> 1.998V
127.0.0.1 - - [11/Jun/2026 11:13:40] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:41] "GET /status HTTP/1.1" 200 -
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU V = 1.998V
PSU I = 0.000A
127.0.0.1 - - [11/Jun/2026 11:13:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:42] "POST /psu/stop HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:42] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:43] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:43] "POST /auto/start HTTP/1.1" 404 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:43] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:43] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:44] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:44] "POST /auto/start HTTP/1.1" 404 -
127.0.0.1 - - [11/Jun/2026 11:13:44] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:45] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:45] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:45] "POST /auto/start HTTP/1.1" 404 -
127.0.0.1 - - [11/Jun/2026 11:13:45] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:46] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:47] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:48] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:48] "GET /status HTTP/1.1" 200 -
PSU V = 0
127.0.0.1 - - [11/Jun/2026 11:13:49] "GET /status HTTP/1.1" 200 -
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:49] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:50] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:50] "POST /auto/start HTTP/1.1" 404 -
127.0.0.1 - - [11/Jun/2026 11:13:50] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:51] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:51] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:52] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:52] "POST /auto/start HTTP/1.1" 404 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:52] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:52] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:53] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:53] "POST /auto/start HTTP/1.1" 404 -
127.0.0.1 - - [11/Jun/2026 11:13:53] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:54] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:54] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:54] "POST /auto/start HTTP/1.1" 404 -
127.0.0.1 - - [11/Jun/2026 11:13:54] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:55] "POST /config HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:55] "POST /auto/start HTTP/1.1" 404 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:55] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:55] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:56] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:57] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:13:58] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:58] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:13:59] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:14:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:00] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:14:01] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:02] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:14:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:03] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:14:04] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:04] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:05] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:14:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:06] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:14:07] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:07] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:09] "GET /status HTTP/1.1" 200 -
PSU V = 0
PSU I = 0
127.0.0.1 - - [11/Jun/2026 11:14:10] "GET /status HTTP/1.1" 200 -
127.0.0.1 - - [11/Jun/2026 11:14:10] "GET /data HTTP/1.1" 200 -
