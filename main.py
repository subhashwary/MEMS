import re

def parse_value(x):
    try:
        if x is None:
            return 0.0
        x = str(x)

        # extract number from: "1.998V", "0.700A", "+0.282E+1"
        match = re.search(r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?", x)
        return float(match.group()) if match else 0.0

    except:
        return 0.0
