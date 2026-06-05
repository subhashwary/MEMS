class SCPIInstrument:

    def __init__(self, port, baudrate=115200, timeout=2):

        self.port = port

        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            timeout=timeout
        )

        self.ser.dtr = False
        self.ser.rts = False

        time.sleep(1)

    def write(self, cmd):

        if not cmd.endswith("\r\n"):
            cmd += "\r\n"

        self.ser.write(cmd.encode())

    def query(self, cmd):

        with serial_lock:

            try:

                self.ser.reset_input_buffer()

                if not cmd.endswith("\r\n"):
                    cmd += "\r\n"

                self.ser.write(cmd.encode())

                time.sleep(0.5)

                raw = self.ser.read_all()

                print("RAW BYTES =", raw)

                response = raw.decode(
                    errors="ignore"
                ).strip()

                print(
                    f"SCPI QUERY [{cmd.strip()}] -> {response}"
                )

                return response

            except Exception as e:

                print("SCPI Query Error:", e)

                return "ERROR"

    def close(self):

        if self.ser.is_open:
            self.ser.close()
