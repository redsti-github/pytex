import glob, os
import re
from specialcharnames import *
from symbolnames import *
import string
import keyword

of = open("clean_macros.tex", "w")


macros = set()
for file in glob.glob("*.tex"):
    if file == "clean_macros.tex":
        continue
    text = open(file, "r").read()
    x = re.findall("\\\\[a-zA-Z@]+", text)
    for m in x:
        macros.add(m)

builtin = ["ifx", "def", "let", "edef", "gdef", "xdef", "fi", "else", "ifnum", "the", "catcode", "par", "input", "expandafter", "newcount", "bye", "undefined", "show", "csname", "endcsname", "numexpr", "relax"]
for b in builtin:
    if "\\"+b in macros:
        macros.remove("\\"+b)

for m in macros:
    if not m.startswith("\\@pytex"):
        print("MACRO " + m + " doesn't start with @pytex ")
        of.write("BAD MACRO: "+m[1:]+"\n\n")
        continue
        
    if m.startswith("\\@pytexChar@"):
        if m.removeprefix("\\@pytexChar@") in string.ascii_lowercase + string.ascii_uppercase:
            continue
        if m.removeprefix("\\@pytexChar@") in specialcharnames.values():
            continue
        print("MACRO " + m + " is not a character ")
        of.write("BAD MACRO: "+m[1:]+"\n\n")
        continue
        
    if m.startswith("\\@pytexToken@"):
        if m.removeprefix("\\@pytexToken@") in keyword.kwlist:
            continue
        if m.removeprefix("\\@pytexToken@") in symbolnames.values():
            continue
        if m in ["\\@pytexToken@Identifier", "\\@pytexToken@Number", "\\@pytexToken@Newline"]:
            continue
        print("MACRO " + m + " is not a keyword ")
        of.write("BAD MACRO: "+m[1:]+"\n\n")
        continue  

    if m.startswith("\\@pytexTMP@"):
        of.write("\\ifx"+m+"\\undefined\\else TMP MACRO: "+m[1:]+" was not undefined\n\\fi\n\n")
        continue

    if m.startswith("\\@pytexTokeniser@"):
        continue
    if m.startswith("\\@pytexCatcodes@"):
        continue
    if m.startswith("\\@pytexQueue@"):
        continue
    if m.startswith("\\@pytexStack@"):
        continue
    
    of.write("\\ifx"+m+"\\undefined\\else DEFINED MACRO: "+m[1:]+"\n\\fi\n\n")
    print("I DONT KNOW WHAT TO DO WITH", m)



