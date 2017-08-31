'''
    Hello
'''
BIG = 'bn = chr(10);bc = chr(39);bs = chr(34);s = "%c%c%c%c    Hello%c%c%c%c%cBIG = %c%s%c%cBAD = %c%s%c%cWOLF = %c%s%c%c";f = open("Grace_kid.py", "w")'
BAD = 'exec(WOLF)'
WOLF = 'exec(BIG);import sys;sys.stdout = f;print(s % (bc, bc, bc, bn, bn, bc, bc, bc, bn, bc, BIG, bc, bn, bc, BAD, bc, bn, bc, WOLF, bc, bn) + BAD);f.close()'
exec(WOLF)
