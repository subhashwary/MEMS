def parse_value(x):
    try:
        return float(str(x).replace("V", "").replace("A", "").strip())
    except:
        return 0.0
