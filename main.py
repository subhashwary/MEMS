(venv) PS D:\Wary\MEMS> python app.py                                                                                                  
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [06/Jun/2026 11:30:21] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 11:30:22] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 11:31:57] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [06/Jun/2026 11:31:58] "GET /ports HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [06/Jun/2026 11:32:02] "GET /data HTTP/1.1" 200 -
HEX = 475720494e5354454b2c4750442d32333033532c534e3a454c3836333637322c56322e30340d0a
RAW BYTES = b'GW INSTEK,GPD-2303S,SN:EL863672,V2.04\r\n'
SCPI QUERY [*IDN?] -> GW INSTEK,GPD-2303S,SN:EL863672,V2.04
IDN  = GW INSTEK,GPD-2303S,SN:EL863672,V2.04
127.0.0.1 - - [06/Jun/2026 11:32:06] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 11:32:07] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [06/Jun/2026 11:32:08] "GET /data HTTP/1.1" 200 -
HEX = 352e303239560d0a
RAW BYTES = b'5.029V\r\n'
SCPI QUERY [VSET1?] -> 5.029V
VSET = 5.029V
127.0.0.1 - - [06/Jun/2026 11:32:08] "GET /data HTTP/1.1" 200 -
HEX = 302e373030410d0a
RAW BYTES = b'0.700A\r\n'
SCPI QUERY [ISET1?] -> 0.700A
ISET = 0.700A
127.0.0.1 - - [06/Jun/2026 11:32:11] "GET /data HTTP/1.1" 200 -
HEX = 496e76616c6964204368617261637465722e0d0a
RAW BYTES = b'Invalid Character.\r\n'
SCPI QUERY [*VSET1?] -> Invalid Character.
VSET RESPONSE =

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
ID: Invalid Character.
================================

127.0.0.1 - - [06/Jun/2026 11:32:13] "POST /connect_psu HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [06/Jun/2026 11:32:14] "GET /data HTTP/1.1" 200 -
HEX = 475720494e5354454b2c4750442d32333033532c534e3a454c3836333637322c56322e30340d0a
RAW BYTES = b'GW INSTEK,GPD-2303S,SN:EL863672,V2.04\r\n'
SCPI QUERY [*IDN?] -> GW INSTEK,GPD-2303S,SN:EL863672,V2.04
IDN  = GW INSTEK,GPD-2303S,SN:EL863672,V2.04
127.0.0.1 - - [06/Jun/2026 11:32:17] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 11:32:18] "POST /psu/set HTTP/1.1" 500 -
127.0.0.1 - - [06/Jun/2026 11:32:19] "GET /data HTTP/1.1" 200 -
HEX = 352e303239560d0a
RAW BYTES = b'5.029V\r\n'
SCPI QUERY [VSET1?] -> 5.029V
VSET = 5.029V
127.0.0.1 - - [06/Jun/2026 11:32:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [06/Jun/2026 11:32:21] "POST /psu/set HTTP/1.1" 500 -
127.0.0.1 - - [06/Jun/2026 11:32:22] "GET /data HTTP/1.1" 200 -
HEX = 302e373030410d0a
RAW BYTES = b'0.700A\r\n'
SCPI QUERY [ISET1?] -> 0.700A
ISET = 0.700A
127.0.0.1 - - [06/Jun/2026 11:32:23] "GET /data HTTP/1.1" 200 -
HEX = 496e76616c6964204368617261637465722e0d0a
RAW BYTES = b'Invalid Character.\r\n'
SCPI QUERY [*VSET1?] -> Invalid Character.
VSET RESPONSE =

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
ID: Invalid Character.
================================

127.0.0.1 - - [06/Jun/2026 11:32:24] "POST /connect_psu HTTP/1.1" 200 -
HEX = 302e303030560d0a
RAW BYTES = b'0.000V\r\n'
SCPI QUERY [VOUT1?] -> 0.000V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [06/Jun/2026 11:32:30] "GET /data HTTP/1.1" 200 -
HEX = 302e303030560d0a
RAW BYTES = b'0.000V\r\n'
SCPI QUERY [VOUT1?] -> 0.000V

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
127.0.0.1 - - [06/Jun/2026 11:32:33] "POST /connect_dmm HTTP/1.1" 500 -
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU read error: could not convert string to float: '0.000V'
PSU CMD -> VSET1:2.0
PSU CMD -> ISET1:0.2
127.0.0.1 - - [06/Jun/2026 11:32:35] "GET /data HTTP/1.1" 200 -
PSU CMD -> OUT1

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
127.0.0.1 - - [06/Jun/2026 11:32:37] "POST /connect_dmm HTTP/1.1" 500 -
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

127.0.0.1 - - [06/Jun/2026 11:32:37] "POST /connect_dmm HTTP/1.1" 200 -
HEX = 312e393938560d0a
RAW BYTES = b'1.998V\r\n'
SCPI QUERY [VOUT1?] -> 1.998V
VERIFY VOUT = 1.998V
127.0.0.1 - - [06/Jun/2026 11:32:42] "POST /dmm/start HTTP/1.1" 200 -
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
VERIFY IOUT = 0.000A
PSU OUTPUT ON
127.0.0.1 - - [06/Jun/2026 11:32:42] "POST /psu/start HTTP/1.1" 200 -
HEX = 312e393938560d0a
RAW BYTES = b'1.998V\r\n'
SCPI QUERY [VOUT1?] -> 1.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [06/Jun/2026 11:32:47] "GET /data HTTP/1.1" 200 -
HEX = 312e393938560d0a
RAW BYTES = b'1.998V\r\n'
SCPI QUERY [VOUT1?] -> 1.998V
HEX = 302e303030410d0a
RAW BYTES = b'0.000A\r\n'
SCPI QUERY [IOUT1?] -> 0.000A
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [06/Jun/2026 11:32:52] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.282889E+1
RAW RESPONSE: +0.282883E+1
RAW RESPONSE: +0.282877E+1
RAW RESPONSE: +0.282871E+1
RAW RESPONSE: +0.282866E+1
RAW RESPONSE: +0.282862E+1
RAW RESPONSE: +0.282862E+1
RAW RESPONSE: +0.282858E+1
RAW RESPONSE: +0.282853E+1
RAW RESPONSE: +0.282848E+1
HEX = 312e393938560d0a
RAW BYTES = b'1.998V\r\n'
SCPI QUERY [VOUT1?] -> 1.998V
RAW RESPONSE: +0.282844E+1
RAW RESPONSE: +0.282838E+1
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [06/Jun/2026 11:33:32] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:33:37] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.40667E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.44204E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:33:46] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.45592E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:33:54] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.46186E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:34:01] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:34:06] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46569E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.46669E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:34:16] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.46774E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:34:24] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.46834E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:34:31] "GET /data HTTP/1.1" 200 -

====================
USER UPDATED PSU
Voltage = 1.0
Current = 0.1
====================
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:34:36] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.46929E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:34:44] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:34:49] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46965E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:34:56] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:35:01] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46973E-2
RAW RESPONSE: -1.46974E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:35:10] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46983E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
RAW RESPONSE: -1.46999E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:35:20] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:35:25] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46991E-2
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
127.0.0.1 - - [06/Jun/2026 11:35:32] "GET /data HTTP/1.1" 200 -
