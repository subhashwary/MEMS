(venv) PS D:\Wary\MEMS> mode COM5

Status for device COM5:
-----------------------
    Baud:            9600
    Parity:          None
    Data Bits:       8
    Stop Bits:       1
    Timeout:         ON
    XON/XOFF:        OFF
    CTS handshaking: OFF
    DSR handshaking: OFF
    DSR sensitivity: OFF
    DTR circuit:     ON
    RTS circuit:     ON

(venv) PS D:\Wary\MEMS> python test_baud.py 

Testing 9600
Waiting: 0
Received: b''

Testing 19200
Waiting: 0
Received: b''

Testing 38400
Waiting: 0
Received: b''

Testing 57600
Waiting: 0
Received: b''

Testing 115200
Waiting: 0
Received: b''


