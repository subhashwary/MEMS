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
(venv) PS D:\Wary\MEMS> python test_voltage.py                                                                  
Connected:             
SCPI QUERY [*IDN?] -> GWInstek,GDM8261A,GEO882227,1.02
GWInstek,GDM8261A,GEO882227,1.02

Reading voltage...

RAW RESPONSE: -1.46200E-2
Voltage = -0.0146
RAW RESPONSE: -1.46222E-2
Voltage = -0.0146
RAW RESPONSE: -1.46225E-2
Voltage = -0.0146
RAW RESPONSE: -1.46226E-2
Voltage = -0.0146
RAW RESPONSE: -1.46230E-2
Voltage = -0.0146
RAW RESPONSE: -1.46231E-2
Voltage = -0.0146
RAW RESPONSE: -1.46233E-2
Voltage = -0.0146
RAW RESPONSE: -1.46237E-2
Voltage = -0.0146
RAW RESPONSE: -1.46240E-2
Voltage = -0.0146
Traceback (most recent call last):
  File "D:\Wary\MEMS\test_voltage.py", line 13, in <module>
    voltage = dmm.measure_voltage()
              ^^^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\instrument.py", line 131, in measure_voltage
    response = self.ser.readline().decode(errors='ignore').strip()
               ^^^^^^^^^^^^^^^^^^^
  File "D:\Wary\MEMS\venv\Lib\site-packages\serial\serialwin32.py", line 288, in read
    result_ok = win32.GetOverlappedResult(
                ^^^^^^^^^^^^^^^^^^^^^^^^^^
KeyboardInterrupt
