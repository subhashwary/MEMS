# Wait for instrument response
time.sleep(1)

# Read everything available
raw = self.ser.read_all()

print("RAW BYTES =", raw)

response = raw.decode(
    errors="ignore"
).strip()

print(f"SCPI QUERY [{cmd.strip()}] -> {response}")

return response
