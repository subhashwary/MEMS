(venv) PS D:\Wary\MEMS> python app.py                                                                                                  
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [08/Jun/2026 10:32:48] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:32:49] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 10:32:49] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 10:32:51] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:32:52] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:32:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:32:55] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:32:56] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:32:58] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:02] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:05] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:05] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:07] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:08] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:10] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:12] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:17] "GET /static/images/cense.png HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:17] "GET /static/images/IISc.png HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:22] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:22] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:25] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:26] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [08/Jun/2026 10:33:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:28] "GET /data HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [08/Jun/2026 10:33:30] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:33] "GET /data HTTP/1.1" 200 -
HEX = 475720494e5354454b2c4750442d32333033532c534e3a454c3836333637322c56322e30340d0a
RAW BYTES = b'GW INSTEK,GPD-2303S,SN:EL863672,V2.04\r\n'
SCPI QUERY [*IDN?] -> GW INSTEK,GPD-2303S,SN:EL863672,V2.04
IDN  = GW INSTEK,GPD-2303S,SN:EL863672,V2.04
127.0.0.1 - - [08/Jun/2026 10:33:34] "GET /data HTTP/1.1" 200 -
HEX = 372e363131560d0a
RAW BYTES = b'7.611V\r\n'
SCPI QUERY [VSET1?] -> 7.611V
VSET = 7.611V
127.0.0.1 - - [08/Jun/2026 10:33:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:37] "GET /data HTTP/1.1" 200 -
HEX = 332e323030410d0a
RAW BYTES = b'3.200A\r\n'
SCPI QUERY [ISET1?] -> 3.200A
ISET = 3.200A
127.0.0.1 - - [08/Jun/2026 10:33:39] "GET /data HTTP/1.1" 200 -
PORT = COM5
BAUD = 9600
OPEN = True

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
================================

127.0.0.1 - - [08/Jun/2026 10:33:39] "POST /connect_psu HTTP/1.1" 200 -
HEX = 302e303030560d0a
RAW BYTES = b'0.000V\r\n'
SCPI QUERY [VOUT1?] -> 0.000V

Trying baudrate: 9600
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:33:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:48] "GET /data HTTP/1.1" 200 -
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

127.0.0.1 - - [08/Jun/2026 10:33:49] "POST /connect_dmm HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:51] "GET /data HTTP/1.1" 200 -
HEX = 302e303030560d0a
RAW BYTES = b'0.000V\r\n'
SCPI QUERY [VOUT1?] -> 0.000V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:33:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:33:58] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:01] "POST /psu/set HTTP/1.1" 200 -
HEX = 302e393938560d0a
RAW BYTES = b'0.998V\r\n'
SCPI QUERY [VOUT1?] -> 0.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:34:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:11] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:15] "GET /data HTTP/1.1" 200 -
HEX = 312e393938560d0a
RAW BYTES = b'1.998V\r\n'
SCPI QUERY [VOUT1?] -> 1.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:34:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:21] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:25] "GET /data HTTP/1.1" 200 -
HEX = 322e393938560d0a
RAW BYTES = b'2.998V\r\n'
SCPI QUERY [VOUT1?] -> 2.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:34:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:32] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:32] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:35] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:36] "GET /data HTTP/1.1" 200 -
HEX = 332e393938560d0a
RAW BYTES = b'3.998V\r\n'
SCPI QUERY [VOUT1?] -> 3.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:34:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:42] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:45] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:46] "GET /data HTTP/1.1" 200 -
HEX = 332e393938560d0a
RAW BYTES = b'3.998V\r\n'
SCPI QUERY [VOUT1?] -> 3.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:34:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:53] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:53] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:34:57] "GET /data HTTP/1.1" 200 -
HEX = 302e393938560d0a
RAW BYTES = b'0.998V\r\n'
SCPI QUERY [VOUT1?] -> 0.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:35:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:04] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:07] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:08] "POST /psu/set HTTP/1.1" 200 -
HEX = 302e393938560d0a
RAW BYTES = b'0.998V\r\n'
SCPI QUERY [VOUT1?] -> 0.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:35:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:15] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:15] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:15] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:15] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:17] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:19] "GET /data HTTP/1.1" 200 -
HEX = 496e76616c6964204368617261637465722e0d0a
RAW BYTES = b'Invalid Character.\r\n'
SCPI QUERY [VOUT1?] -> Invalid Character.
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:35:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:28] "POST /psu/set HTTP/1.1" 200 -
HEX = 322e393938560d0a
RAW BYTES = b'2.998V\r\n'
SCPI QUERY [VOUT1?] -> 2.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
127.0.0.1 - - [08/Jun/2026 10:35:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:37] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:39] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:40] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:35:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:47] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:49] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:49] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:51] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:35:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:57] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:35:59] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:01] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:36:08] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:08] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:08] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:08] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:08] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:12] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:36:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:18] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:18] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:22] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:36:29] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:29] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:29] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:29] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:29] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:33] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:36:39] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:39] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:39] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:39] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:39] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:41] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:43] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:36:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:50] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:51] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:52] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:36:54] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:37:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:04] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:37:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:11] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:15] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:37:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:21] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:25] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:37:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:33] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:34] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:35] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:36] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:37:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:43] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:45] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:45] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:46] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:37:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:53] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:54] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:55] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:37:57] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:38:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:03] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:03] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:05] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:07] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:38:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:14] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:18] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:38:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:25] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:28] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:28] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:29] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:38:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:37] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:38] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:40] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:38:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:47] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:48] "GET /data HTTP/1.1" 200 -
PSU CMD -> OUT1
127.0.0.1 - - [08/Jun/2026 10:38:49] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 10:38:51] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
VERIFY VOUT = 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
VERIFY IOUT = 
PSU OUTPUT ON
127.0.0.1 - - [08/Jun/2026 10:38:56] "POST /psu/start HTTP/1.1" 200 -
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
127.0.0.1 - - [08/Jun/2026 10:39:02] "POST /psu/start HTTP/1.1" 200 -
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
127.0.0.1 - - [08/Jun/2026 10:39:09] "POST /psu/start HTTP/1.1" 200 -
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
127.0.0.1 - - [08/Jun/2026 10:39:15] "POST /psu/start HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [08/Jun/2026 10:39:20] "GET /data HTTP/1.1" 200 -
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
127.0.0.1 - - [08/Jun/2026 10:39:27] "POST /psu/start HTTP/1.1" 200 -
PSU CMD -> OUT1
