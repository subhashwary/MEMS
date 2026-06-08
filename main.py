(venv) PS D:\Wary\MEMS> python app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [08/Jun/2026 13:00:12] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:12] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 13:00:12] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 13:00:14] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:15] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:17] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:18] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:19] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:21] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:24] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:27] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:28] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 13:00:28] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [08/Jun/2026 13:00:29] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:29] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:30] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:30] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:33] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:34] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:36] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:37] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:39] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:42] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:43] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:44] "GET /data HTTP/1.1" 200 -

Trying PSU baudrate: 9600
127.0.0.1 - - [08/Jun/2026 13:00:45] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:47] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
127.0.0.1 - - [08/Jun/2026 13:00:48] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:00:50] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
127.0.0.1 - - [08/Jun/2026 13:00:51] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
127.0.0.1 - - [08/Jun/2026 13:00:53] "GET /data HTTP/1.1" 200 -
PORT = COM5
BAUD = 9600
OPEN = True

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
================================

127.0.0.1 - - [08/Jun/2026 13:00:53] "POST /connect_psu HTTP/1.1" 200 -

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
127.0.0.1 - - [08/Jun/2026 13:00:57] "POST /connect_dmm HTTP/1.1" 500 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:00] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 

Trying baudrate: 9600
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:04] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:08] "GET /data HTTP/1.1" 200 -
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

127.0.0.1 - - [08/Jun/2026 13:01:10] "POST /connect_dmm HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:14] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:19] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:23] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:29] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:34] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:38] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:38] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:44] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:44] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:44] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:44] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:44] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:50] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:51] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:01:51] "POST /psu/start HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:01:57] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:01] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:02] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:07] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:12] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:16] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:20] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:28] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:32] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:38] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:42] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:46] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:47] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:47] "POST /psu/set HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:47] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:51] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:02:56] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:56] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:56] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:56] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:56] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:56] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:02:56] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:02] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:07] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:11] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:11] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:18] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:23] "GET /data HTTP/1.1" 200 -

Trying PSU baudrate: 9600
HEX = 
RAW BYTES = b''
SCPI QUERY [*IDN?] -> 
IDN  = 
HEX = 
RAW BYTES = b''
SCPI QUERY [VSET1?] -> 
VSET = 
HEX = 
RAW BYTES = b''
SCPI QUERY [ISET1?] -> 
ISET = 
PORT = COM5
BAUD = 9600
OPEN = True

================================
PSU CONNECTED SUCCESSFULLY
PORT: COM5
BAUDRATE: 9600
================================

127.0.0.1 - - [08/Jun/2026 13:03:31] "POST /connect_psu HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:35] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [08/Jun/2026 13:03:40] "POST /psu/set HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:46] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:50] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
HEX = 
RAW BYTES = b''
SCPI QUERY [IOUT1?] -> 
WARNING: PSU returned empty response
127.0.0.1 - - [08/Jun/2026 13:03:54] "GET /data HTTP/1.1" 200 -
HEX = 
RAW BYTES = b''
SCPI QUERY [VOUT1?] -> 
