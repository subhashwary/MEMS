
Copyright (C) Microsoft Corporation. All rights reserved.

Try the new cross-platform PowerShell https://aka.ms/pscore6

PS C:\Users\mahim> mode

Status for device LPT1:
-----------------------
    Printer output is not being rerouted.


Status for device COM1:
-----------------------
    Baud:            1200
    Parity:          None
    Data Bits:       7
    Stop Bits:       1
    Timeout:         OFF
    XON/XOFF:        OFF
    CTS handshaking: OFF
    DSR handshaking: OFF
    DSR sensitivity: OFF
    DTR circuit:     ON
    RTS circuit:     ON


Status for device COM3:
-----------------------
    Baud:            9600
    Parity:          None
    Data Bits:       8
    Stop Bits:       1
    Timeout:         ON
    XON/XOFF:        ON
    CTS handshaking: OFF
    DSR handshaking: OFF
    DSR sensitivity: OFF
    DTR circuit:     ON
    RTS circuit:     ON


Status for device COM5:
-----------------------
    Baud:            115200
    Parity:          None
    Data Bits:       8
    Stop Bits:       1
    Timeout:         ON
    XON/XOFF:        ON
    CTS handshaking: OFF
    DSR handshaking: OFF
    DSR sensitivity: OFF
    DTR circuit:     ON
    RTS circuit:     ON


Status for device CON:
----------------------
    Lines:          3000
    Columns:        120
    Keyboard rate:  31
    Keyboard delay: 1
    Code page:      437

PS C:\Users\mahim> python -m serial.tools.list_ports
COM1
COM3
COM5
3 ports found
PS C:\Users\mahim>
