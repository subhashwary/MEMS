candidate.write("VSET1:2.00")
time.sleep(0.5)

candidate.write("ISET1:0.10")
time.sleep(0.5)

check_v = candidate.query("VSET1?")
check_i = candidate.query("ISET1?")

print("VERIFY V =", check_v)
print("VERIFY I =", check_i)
