import serial
import time

from threading import Lock

serial_lock = Lock()

class SCPIInstrument:

    def __init__(self, port, baudrate=115200, timeout=2):

        self.port = port

        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=timeout
        )

        # IMPORTANT FOR GPD-2303S
        self.ser.dtr = False
        self.ser.rts = False


        time.sleep(1)

    # -------------------------------------------------
    # WRITE COMMAND
    # -------------------------------------------------
    def write(self, cmd):

        if not cmd.endswith("\n"):
            cmd += "\n"

        self.ser.write(cmd.encode())

    # -------------------------------------------------
    # QUERY COMMAND
    # -------------------------------------------------
                self.ser.write(cmd.encode())

                time.sleep(0.5)

                raw = self.ser.read_all()

                print("RAW BYTES =", raw)

                response = raw.decode(errors="ignore").strip()

                print(f"SCPI QUERY [{cmd.strip()}] -> {response}")

                return response

            
            except Exception as e:

                print("SCPI Query Error:", e)

                return "ERROR"

    # -------------------------------------------------
    # CLOSE PORT
    # -------------------------------------------------
    def close(self):

        if self.ser.is_open:
            self.ser.close()


# =====================================================
# POWER SUPPLY CLASS
# =====================================================

class PowerSupply(SCPIInstrument):

    def idn(self):
        return self.query("*IDN?")

    def set_voltage(self, voltage):
        print(f"PSU CMD -> VSET1:{voltage}")
        self.write(f"VSET1:{voltage}")

    def set_current(self, current):
        print(f"PSU CMD -> ISET1:{current}")
        self.write(f"ISET1:{current}")

    def get_voltage(self):
        return self.query("VOUT1?")

    def get_current(self):
        return self.query("IOUT1?")

    def output_on(self):
        print("PSU CMD -> OUT1")
        self.write("OUT1")

    def output_off(self):
        print("PSU CMD -> OUT0")
        self.write("OUT0")

# =====================================================
# MULTIMETER CLASS
# =====================================================

class Multimeter(SCPIInstrument):

    def idn(self):

        return self.query("*IDN?")

    def measure_voltage(self):

        try:
            with serial_lock:

                # Clear old garbage data
                self.ser.reset_input_buffer()

                # Send command
                self.ser.write(b"MEAS:VOLT:DC?\n")

                # Small wait for full response
                time.sleep(0.2)

                # Read full line
                response = self.ser.readline().decode(errors='ignore').strip()

                print("RAW RESPONSE:", response)

                # Clean unwanted characters
                response = response.replace('\r', '').replace('\n', '')

                # Reject incomplete scientific notation
                if response.endswith('E') or response.endswith('+') or response.endswith('-'):
                    raise ValueError(f"Incomplete reading: {response}")

                value = float(response)

                return round(value, 4)

        except Exception as e:

            print("Measurement Error:", e)

            return None
