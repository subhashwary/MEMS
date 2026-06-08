(venv) PS D:\Wary\MEMS> python app.py                          
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [08/Jun/2026 17:54:16] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:54:16] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 17:54:16] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 17:54:17] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:54:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:54:30] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:54:30] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 17:54:30] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 17:54:31] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:54:31] "GET /data HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [08/Jun/2026 17:54:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:54:38] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [08/Jun/2026 17:54:40] "GET /data HTTP/1.1" 200 -
HEX = 475720494e5354454b2c4750442d32333033532c534e3a454c3836333637322c56322e30340d0a
RAW BYTES = b'GW INSTEK,GPD-2303S,SN:EL863672,V2.04\r\n'
SCPI QUERY [*IDN?] -> GW INSTEK,GPD-2303S,SN:EL863672,V2.04
127.0.0.1 - - [08/Jun/2026 17:54:41] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:54:43] "GET /data HTTP/1.1" 200 -
HEX = 322e303030560d0a
RAW BYTES = b'2.000V\r\n'
SCPI QUERY [VSET1?] -> 2.000V
127.0.0.1 - - [08/Jun/2026 17:54:44] "GET /data HTTP/1.1" 200 -
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
IDN  = GW INSTEK,GPD-2303S,SN:EL863672,V2.04
VSET = 2.000V
ISET = 0.100A
127.0.0.1 - - [08/Jun/2026 17:54:46] "GET /data HTTP/1.1" 200 -
PORT = COM5
BAUD = 9600
OPEN = True

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
================================

127.0.0.1 - - [08/Jun/2026 17:54:46] "POST /connect_psu HTTP/1.1" 200 -
HEX = 322e303030560d0a
RAW BYTES = b'2.000V\r\n'
SCPI QUERY [VSET1?] -> 2.000V
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
127.0.0.1 - - [08/Jun/2026 17:54:54] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:54:55] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:00] "GET /data HTTP/1.1" 200 -
HEX = 342e303030560d0a
RAW BYTES = b'4.000V\r\n'
SCPI QUERY [VSET1?] -> 4.000V
HEX = 302e323030410d0a
RAW BYTES = b'0.200A\r\n'
SCPI QUERY [ISET1?] -> 0.200A
127.0.0.1 - - [08/Jun/2026 17:55:09] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:10] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:16] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:17] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:18] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:19] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:19] "POST /psu/start HTTP/1.1" 200 -
HEX = 342e303030560d0a
RAW BYTES = b'4.000V\r\n'
SCPI QUERY [VSET1?] -> 4.000V
HEX = 302e343030410d0a
RAW BYTES = b'0.400A\r\n'
SCPI QUERY [ISET1?] -> 0.400A
127.0.0.1 - - [08/Jun/2026 17:55:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:26] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:27] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:28] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:28] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:29] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:33] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:34] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:34] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:35] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:36] "POST /psu/start HTTP/1.1" 200 -
HEX = 382e303030560d0a
RAW BYTES = b'8.000V\r\n'
SCPI QUERY [VSET1?] -> 8.000V
HEX = 302e343030410d0a
RAW BYTES = b'0.400A\r\n'
SCPI QUERY [ISET1?] -> 0.400A
127.0.0.1 - - [08/Jun/2026 17:55:41] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:42] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:43] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:43] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:44] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:45] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:47] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:49] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:52] "POST /psu/start HTTP/1.1" 200 -
HEX = 382e303030560d0a
RAW BYTES = b'8.000V\r\n'
SCPI QUERY [VSET1?] -> 8.000V
HEX = 302e343030410d0a
RAW BYTES = b'0.400A\r\n'
SCPI QUERY [ISET1?] -> 0.400A
127.0.0.1 - - [08/Jun/2026 17:55:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:59] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:55:59] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:01] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:02] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:07] "POST /psu/start HTTP/1.1" 200 -
HEX = 31352e303030560d0a
RAW BYTES = b'15.000V\r\n'
SCPI QUERY [VSET1?] -> 15.000V
HEX = 302e383030410d0a
RAW BYTES = b'0.800A\r\n'
SCPI QUERY [ISET1?] -> 0.800A
127.0.0.1 - - [08/Jun/2026 17:56:12] "GET /data HTTP/1.1" 200 -
HEX = 31352e303030560d0a
RAW BYTES = b'15.000V\r\n'
SCPI QUERY [VSET1?] -> 15.000V
HEX = 302e383030410d0a
RAW BYTES = b'0.800A\r\n'
SCPI QUERY [ISET1?] -> 0.800A
127.0.0.1 - - [08/Jun/2026 17:56:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:29] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:29] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:35] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:35] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:37] "GET /data HTTP/1.1" 200 -
HEX = 312e303030560d0a
RAW BYTES = b'1.000V\r\n'
SCPI QUERY [VSET1?] -> 1.000V
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
127.0.0.1 - - [08/Jun/2026 17:56:45] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:47] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:56:49] "GET /data HTTP/1.1" 200 -
HEX = 322e303030560d0a
RAW BYTES = b'2.000V\r\n'
SCPI QUERY [VSET1?] -> 2.000V
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
127.0.0.1 - - [08/Jun/2026 17:57:00] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:57:06] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:57:07] "GET /data HTTP/1.1" 200 -
HEX = 322e313030560d0a
RAW BYTES = b'2.100V\r\n'
SCPI QUERY [VSET1?] -> 2.100V
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
127.0.0.1 - - [08/Jun/2026 17:57:15] "GET /data HTTP/1.1" 200 -
HEX = 322e313030560d0a
RAW BYTES = b'2.100V\r\n'
SCPI QUERY [VSET1?] -> 2.100V
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
127.0.0.1 - - [08/Jun/2026 17:57:30] "GET /data HTTP/1.1" 200 -
HEX = 322e313030560d0a
RAW BYTES = b'2.100V\r\n'
SCPI QUERY [VSET1?] -> 2.100V
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
127.0.0.1 - - [08/Jun/2026 17:57:45] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:57:57] "POST /psu/start HTTP/1.1" 200 -
HEX = 332e313030560d0a
RAW BYTES = b'3.100V\r\n'
SCPI QUERY [VSET1?] -> 3.100V
HEX = 302e313030410d0a
RAW BYTES = b'0.100A\r\n'
SCPI QUERY [ISET1?] -> 0.100A
127.0.0.1 - - [08/Jun/2026 17:58:02] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 17:58:17] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 17:58:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:58:22] "POST /psu/start HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 17:58:28] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:58:29] "POST /psu/start HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 17:58:35] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:58:36] "POST /psu/start HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 17:58:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:58:43] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:58:46] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 17:58:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:58:51] "POST /psu/start HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 17:58:57] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:58:58] "POST /psu/start HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 17:59:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:59:17] "POST /psu/start HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:59:18] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:59:21] "POST /psu/start HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 17:59:25] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 17:59:27] "POST /psu/start HTTP/1.1" 200 -
