Connecting to COM3...
DMM ID:
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
GWInstek,GDM8261A,GEO882227,1.02
PS D:\Wary\MEMS> & d:/Wary/MEMS/venv/Scripts/python.exe d:/Wary/MEMS/test_dmm.py
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
GWInstek,GDM8261A,GEO882227,1.02
PS D:\Wary\MEMS> (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& d:\Wary\MEMS\venv\Scripts\Activate.ps1)
(venv) PS D:\Wary\MEMS> & d:/Wary/MEMS/venv/Scripts/python.exe d:/Wary/MEMS/test_voltage.py
Connected:
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
GWInstek,GDM8261A,GEO882227,1.02

Reading voltage...

RAW RESPONSE: -1.46398E-2
Voltage = -0.0146
RAW RESPONSE: -1.46403E-2
Voltage = -0.0146
RAW RESPONSE: -1.46397E-2
Voltage = -0.0146
RAW RESPONSE: -1.46398E-2
Voltage = -0.0146
RAW RESPONSE: -1.46402E-2
Voltage = -0.0146
RAW RESPONSE: -1.46402E-2
Voltage = -0.0146
RAW RESPONSE: -1.46401E-2
Voltage = -0.0146
RAW RESPONSE: -1.46403E-2
Voltage = -0.0146
RAW RESPONSE: -1.46395E-2
Voltage = -0.0146
RAW RESPONSE: -1.46388E-2
Voltage = -0.0146
RAW RESPONSE: -1.46391E-2
Voltage = -0.0146
RAW RESPONSE: -1.46386E-2
Voltage = -0.0146
RAW RESPONSE: -1.46396E-2
Voltage = -0.0146
RAW RESPONSE: -1.46393E-2
Voltage = -0.0146
RAW RESPONSE: -1.46384E-2
Voltage = -0.0146
RAW RESPONSE: -1.46385E-2
Voltage = -0.0146
RAW RESPONSE: -1.46379E-2
Voltage = -0.0146
RAW RESPONSE: -1.46322E-2
Voltage = -0.0146
RAW RESPONSE: -1.46385E-2
Voltage = -0.0146
RAW RESPONSE: -1.46378E-2
Voltage = -0.0146
RAW RESPONSE: -1.46357E-2
Voltage = -0.0146
RAW RESPONSE: -1.46354E-2
Voltage = -0.0146
RAW RESPONSE: -1.46354E-2
Voltage = -0.0146
RAW RESPONSE: -1.46546E-2
Voltage = -0.0147
RAW RESPONSE: -1.46352E-2
Voltage = -0.0146
RAW RESPONSE: -1.46351E-2
Voltage = -0.0146
Traceback (most recent call last):
  File "d:\Wary\MEMS\test_voltage.py", line 17, in <module>
    time.sleep(1)
KeyboardInterrupt
