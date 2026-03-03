import time

# what time i was SUPPOSED to be there
due = "12:00"

def chk():
    now = time.strftime("%H:%M")
    # print("dbg now=" + now)
    if now > due:
        print("oh dear oh dear, its " + now + " and i was due at " + due)
    else:
        print("its " + now + ", still time (for once)")

chk()
