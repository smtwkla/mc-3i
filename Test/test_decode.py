import datetime


d = datetime.datetime.now()

s1 = "LIFT1 START_UP 1/1/1 12.25.50"
s2 = "LIFT1 STOP_UP 1/1/1 12.25.50"
s3 = "LIFT1 OLR_TRIP 1/1/1 12.25.50"

s = f"{d.isoformat()} OLR_RESET"
print(s)

sp = s.split(" ")
o = f'Machine Thing ID: {sp[0]}, Time:{sp[1]}, Command: {sp[2]}'
print(o)
