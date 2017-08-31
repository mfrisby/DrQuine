import os, sys
os.path.basename(__file__)
i = 5
if i == 0 : sys.exit(0)
if 'Sully_' in __file__ :
    i -= 1
OPEN = 'name = "Sully_" + str(i) + ".py";f = open(name, "w")'
REALLY = 'start = "import os, sys%cos.path.basename(__file__)%ci = %d%cif i == 0 : sys.exit(0)%cif %cSully_%c in __file__ :%c    i -= 1%cOPEN = %c%s%c%cREALLY = %c%s%c%c"'
BIG = 'bn = chr(10);bc = chr(39);bs = chr(34);sys.stdout = f;s = "BIG = %c%s%c%cBAD = %c%s%c%cWOLF = %c%s%c%c";'
BAD = 'exec(WOLF)'
WOLF = 'exec(OPEN);exec(BIG);exec(REALLY);print(start % (bn, bn, i, bn, bn, bc, bc, bn, bn, bc, OPEN, bc, bn, bc, REALLY, bc, bn) + s % (bc, BIG, bc, bn, bc, BAD, bc, bn, bc, WOLF, bc, bn) + BAD);f.close();os.system("python " + name)'
exec(WOLF)
