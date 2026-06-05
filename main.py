class SCPIInstrument:

    def __init__(self, port, baudrate=115200, timeout=2):

        self.port = port

        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=2,
            xonxoff=True,
            rtscts=False,
            dsrdtr=False
        )

        self.ser.dtr = False
        self.ser.rts = False

        time.sleep(1)
