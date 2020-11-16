import pglet

p = pglet.page()

p.send("add textbox id=name")

# row
#   col
#     button id=ok
#     button id=cancel

r1 = p.send("add row")
c1 = p.send(f"add col to={r1}")
c2 = p.send(f"add col to={r1}")

p.send(f"add button id=ok text='OK' to={c1}")
p.send(f"add button id=cancel text='Cancel' to={c2}")

# wait for event
e = p.wait_events()

name = p.send("get name value")
p.send("clean page")

if e.target == "ok":
    p.send(f"add text value='Good luck, {name}!'")
else:
    p.send(f"add text value='OK, maybe next time...'")

