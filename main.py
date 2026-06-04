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
