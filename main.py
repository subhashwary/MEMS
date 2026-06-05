self.ser = serial.Serial(
    port=port,
    baudrate=baudrate,
    timeout=timeout
)

# IMPORTANT FOR GPD-2303S
self.ser.dtr = False
self.ser.rts = False
