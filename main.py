(venv) PS D:\Wary\MEMS> python app.py              
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [05/Jun/2026 10:12:08] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:09] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 10:12:10] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 10:12:10] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:12] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:13] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:14] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:16] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:17] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:19] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:22] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:22] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:22] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:22] "GET /static/images/cense.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 10:12:22] "GET /static/images/IISc.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Jun/2026 10:12:23] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:25] "GET /ports HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:25] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:26] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:27] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:28] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:28] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:29] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:30] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:31] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:32] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:33] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:34] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:34] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:35] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [05/Jun/2026 10:12:35] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:36] "GET /data HTTP/1.1" 200 -
SCPI QUERY [*IDN?] -> GW INSTEK,GPD-2303S,SN:EL863672,V2.04

========================
PSU CONNECTED
PORT: COM5
ID: GW INSTEK,GPD-2303S,SN:EL863672,V2.04
========================

127.0.0.1 - - [05/Jun/2026 10:12:37] "POST /connect_psu HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:38] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:39] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:39] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:40] "GET /data HTTP/1.1" 200 -

Trying baudrate: 9600
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:41] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:42] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:42] "GET /data HTTP/1.1" 200 -
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
RAW ID RESPONSE: GWInstek,GDM8261A,GEO882227,1.02

================================
DMM CONNECTED SUCCESSFULLY
PORT: COM3
BAUDRATE: 9600
DMM ID: GWInstek,GDM8261A,GEO882227,1.02
================================

127.0.0.1 - - [05/Jun/2026 10:12:45] "POST /connect_dmm HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:45] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:45] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:46] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:46] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:47] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:48] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:49] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:51] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:51] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:51] "GET /data HTTP/1.1" 200 -
127.0.0.1 - - [05/Jun/2026 10:12:52] "POST /dmm/start HTTP/1.1" 200 -
RAW RESPONSE: -1.47026E-2
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:54] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.47030E-2
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:57] "GET /data HTTP/1.1" 200 -
Setting Voltage = 2.0
Setting Current = 0.2
PSU CMD -> VSET1:2.0
PSU CMD -> ISET1:0.2
RAW RESPONSE: -1.47033E-2
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:12:59] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VSET1?] -> 2.000V
VERIFY VSET = 2.000V
RAW RESPONSE: -1.47036E-2
SCPI QUERY [VOUT1?] -> 0.000V
PSU read error: could not convert string to float: '0.000V'
127.0.0.1 - - [05/Jun/2026 10:13:02] "GET /data HTTP/1.1" 200 -
SCPI QUERY [ISET1?] -> 0.200A
VERIFY ISET = 0.200A
PSU CMD -> OUT1
PSU OUTPUT ON
127.0.0.1 - - [05/Jun/2026 10:13:03] "POST /psu/start HTTP/1.1" 200 -
RAW RESPONSE: -0.53753E-2
SCPI QUERY [VOUT1?] -> 1.998V
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [05/Jun/2026 10:13:05] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70403E+0
SCPI QUERY [VOUT1?] -> 1.998V
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [05/Jun/2026 10:13:08] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70410E+0
SCPI QUERY [VOUT1?] -> 1.998V
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [05/Jun/2026 10:13:11] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70407E+0
SCPI QUERY [VOUT1?] -> 1.998V
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [05/Jun/2026 10:13:15] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70406E+0
SCPI QUERY [VOUT1?] -> 1.998V
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [05/Jun/2026 10:13:18] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70407E+0
RAW RESPONSE: +1.70404E+0
SCPI QUERY [VOUT1?] -> 1.998V
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [05/Jun/2026 10:13:24] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 1.998V
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [05/Jun/2026 10:13:24] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70398E+0
SCPI QUERY [VOUT1?] -> 1.998V
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [05/Jun/2026 10:13:27] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70394E+0
SCPI QUERY [VOUT1?] -> 1.998V
PSU read error: could not convert string to float: '1.998V'
127.0.0.1 - - [05/Jun/2026 10:13:30] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70392E+0
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:13:36] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70381E+0
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:13:41] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70377E+0
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:13:46] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70373E+0
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:13:51] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.70361E+0
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:13:56] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +1.99673E+0
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:02] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.201085E+1
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:07] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.200287E+1
RAW RESPONSE: +0.200164E+1
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:15] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.200156E+1
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:20] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.200152E+1
RAW RESPONSE: +0.200150E+1
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:28] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.13137E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:33] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.42179E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:37] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:39] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.45102E-2
RAW RESPONSE: -1.45435E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:46] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.45858E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:51] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46119E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:14:55] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46289E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:00] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46412E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:04] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46490E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:09] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46551E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:13] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:16] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46623E-2
RAW RESPONSE: -1.46635E-2
RAW RESPONSE: -1.46660E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:25] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46692E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:29] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46711E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:34] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46728E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:38] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46746E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:43] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:45] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:47] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46787E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:52] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46796E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:57] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:15:59] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46798E-2
RAW RESPONSE: -1.46795E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:06] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46792E-2
RAW RESPONSE: -1.46797E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:13] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46801E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:17] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46798E-2
RAW RESPONSE: -1.46792E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:24] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.200150E+1
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:29] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.200165E+1
RAW RESPONSE: +0.200167E+1
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:38] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: +0.200167E+1
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:43] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -0.97558E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:47] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:50] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.44320E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:54] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:16:56] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.45723E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:01] "GET /data HTTP/1.1" 200 -
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:03] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46200E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:08] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46336E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:12] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46458E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:17] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46535E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:22] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46590E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:27] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46640E-2
RAW RESPONSE: -1.46658E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:34] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46690E-2
RAW RESPONSE: -1.46699E-2
RAW RESPONSE: -1.46698E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:43] "GET /data HTTP/1.1" 200 -
RAW RESPONSE: -1.46711E-2
RAW RESPONSE: -1.46715E-2
RAW RESPONSE: -1.46724E-2
SCPI QUERY [VOUT1?] -> 
PSU read error: could not convert string to float: ''
127.0.0.1 - - [05/Jun/2026 10:17:52] "GET /data HTTP/1.1" 200 -
