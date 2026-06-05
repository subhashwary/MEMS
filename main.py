self.ser.write(cmd.encode())

time.sleep(0.5)

raw = self.ser.read_all()

print("RAW BYTES =", raw)

response = raw.decode(errors="ignore").strip()

print(f"SCPI QUERY [{cmd.strip()}] -> {response}")

return response
