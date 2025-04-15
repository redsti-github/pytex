import re

log = open("py.log", "r").read()
log = re.findall("{changing ([^{}]*)}\n{into ([^{}]*)}", log)

original_defs = {}
macro_defs = {}

for before, after in log:
    name = before.split('=', 1)[0]
    assert name == after.split('=', 1)[0]
    olddef = before.split('=', 1)[1]
    newdef =  after.split('=', 1)[1]
    #print(f"changing macro '{name}' into '{newdef}'")

    if name not in macro_defs:
        original_defs[name] = olddef

    macro_defs[name] = newdef
    
for name, macro in macro_defs.items():
    if macro == "undefined":
        continue
    print(f"{name} -> {macro}")


