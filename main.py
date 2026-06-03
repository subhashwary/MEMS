import serial.tools.list_ports

print("\nAvailable COM Ports:\n")

ports = serial.tools.list_ports.comports()

if len(ports) == 0:
    print("No COM ports detected.")

else:
    for port in ports:
        print(f"Port: {port.device}")
        print(f"Description: {port.description}")
        print(f"HWID: {port.hwid}")
        print("-" * 40)
