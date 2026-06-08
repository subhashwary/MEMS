except Exception as e:

    global psu

    print("PSU read error:", e)

    try:
        psu.close()
    except:
        pass

    psu = None
