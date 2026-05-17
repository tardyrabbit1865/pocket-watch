import time
import sys

# what time i was SUPPOSED to be there
due = "12:00"
if len(sys.argv) > 1:
    due = sys.argv[1]  # prob should check this is a real time but eh

def chk():
    now = time.strftime("%H:%M")
    # print("dbg now=" + now)
    if now > due:
        mins = (int(now[:2]) * 60 + int(now[3:])) - (int(due[:2]) * 60 + int(due[3:]))
        print("oh dear oh dear, its " + now + ". thats " + str(mins) + " min late")
    else:
        print("its " + now + ", still time (for once)")

chk()
