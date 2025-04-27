import sys
import re

target = sys.argv[1]

f = open(target, "r").read()

while True:
    m = re.search("\\\\input{([^}]+)}", f)
    if m is None:
        break
    
    filename = m[1]
    file = open("build/"+filename, "r").read()
    f = f.replace("\\input{"+filename+"}", file)

with open(target, "w") as out:
    out.write(f)
