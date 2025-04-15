import string
from specialcharnames import *

# TODO: make newline depend on \the\endlinechar

of = open("active_chars.tex", "w")

of.write("\\def\\@pytexTMP@prevTildaCatcode{\\the\\catcode"+str(ord("~"))+"}\n")
of.write("\\def\\@pytexTMP@prevCaretCatcode{\\the\\catcode"+str(ord("^"))+"}\n")
of.write("\\def\\@pytexTMP@prevStarCatcode{\\the\\catcode"+str(ord("*"))+"}\n")

of.write("\\catcode`~=13\n")
of.write("\\catcode`^=13\n")
of.write("\\catcode`*=13\n")
of.write("\\let~\\let\n")
of.write("\\let^\\catcode\n\n")

# letters
for char in string.ascii_lowercase + string.ascii_uppercase:
    of.write("\\def*{\\@pytexChar@" + char + "}\n")
    of.write("^" + str(ord(char)) + "=13\n")
    of.write("~"+char+"*\n")
    of.write("^" + str(ord(char)) + "=11\n\n")

# numbers + special chars
for char in specialcharnames:
    if char == "\\" or char == "@" or char == "\n" or char == "\r" or char == "{" or char == "}":
        continue
    of.write("\\edef\\@pytexTMP@prevcatcode{\\the\\catcode" + str(ord(char)) +"}\n")
    of.write("\\def\\@pytexTMP@resetcatcode{\\catcode" + str(ord(char)) + "=\\@pytexTMP@prevcatcode}\n")
    of.write("\\catcode" + str(ord(char)) + "=13\n")
    of.write("\\def"+char+"{\\@pytexChar@" + specialcharnames[char] + "}\n")
    of.write("\\@pytexTMP@resetcatcode\n\n")

# { and }
of.write("\\def\\@pytexTMP@macro{\\@pytexChar@"+specialcharnames['{']+"}")
of.write("\\edef\\@pytexTMP@prevcatcode{\\the\\catcode" + str(ord('{')) +"}\n")
of.write("\\def\\@pytexTMP@resetcatcode{\\catcode" + str(ord('{')) + "=\\@pytexTMP@prevcatcode}\n")
of.write("\\catcode" + str(ord('{')) + "=13\n")
of.write("\\let{\\@pytexTMP@macro\n")
of.write("\\@pytexTMP@resetcatcode\n\n")

of.write("\\def\\@pytexTMP@macro{\\@pytexChar@"+specialcharnames['}']+"}")
of.write("\\edef\\@pytexTMP@prevcatcode{\\the\\catcode" + str(ord('}')) +"}\n")
of.write("\\def\\@pytexTMP@resetcatcode{\\catcode" + str(ord('}')) + "=\\@pytexTMP@prevcatcode}\n")
of.write("\\catcode" + str(ord('}')) + "=13\n")
of.write("\\let}\\@pytexTMP@macro\n")
of.write("\\@pytexTMP@resetcatcode\n\n")

# backslash
of.write("\\def\\@pytexTMP@macro{\\@pytexChar@Backslash}\n")
of.write("\\edef\\@pytexTMP@prevcatcode{\\the\\catcode" + str(ord('~')) +"}\n")
of.write("\\def\\@pytexTMP@resetcatcode{\\catcode" + str(ord('~')) + "=\\@pytexTMP@prevcatcode\\catcode"+ str(ord('\\')) + "=0}\n")
of.write("\\catcode" + str(ord('~')) + "=0\n")
of.write("\\catcode" + str(ord('\\')) + "=13\n")
of.write("~let\\~@pytexTMP@macro\n")
of.write("~@pytexTMP@resetcatcode\n\n")

# newline chars
of.write("\\def\\@pytexTMP@macro{\\@pytexChar@" + specialcharnames['\r'] + "}\n")
of.write("\\edef\\@pytexTMP@prevcatcode{\\the\\catcode" + str(ord('\r')) +"}\n")
of.write("\\def\\@pytexTMP@resetcatcode{\\catcode" + str(ord('\r')) + "=\\@pytexTMP@prevcatcode}%\n")
of.write("\\catcode" + str(ord('\r')) + "=13%\n")
of.write("\\let\n\\@pytexTMP@macro%\n")
of.write("\\catcode" + str(ord('\r')) + "=5 %\n\n") # note: the space before the % IS required


# reset catcodes
of.write("\\catcode`~=\\@pytexTMP@prevTildaCatcode\n")
of.write("\\catcode`^=\\@pytexTMP@prevCaretCatcode\n")
of.write("\\catcode`*=\\@pytexTMP@prevStarCatcode\n\n")

# be nice and undefine temporary macros
of.write("\\let\\@pytexTMP@macro\\undefined\n")
of.write("\\let\\@pytexTMP@prevcatcode\\undefined\n")
of.write("\\let\\@pytexTMP@prevTildaCatcode\\undefined\n")
of.write("\\let\\@pytexTMP@prevCaretCatcode\\undefined\n")
of.write("\\let\\@pytexTMP@prevStarCatcode\\undefined\n")
of.write("\\let\\@pytexTMP@resetcatcode\\undefined\n\n\n")

# macro to set all characters as active
of.write("\\def\\@pytexCatcodes@setallactive{\n")
for char in string.printable:
    of.write("\t\\catcode"+str(ord(char))+"=13\n")
#of.write("\t\\endlinechar=10\n")
of.write("}\n")
