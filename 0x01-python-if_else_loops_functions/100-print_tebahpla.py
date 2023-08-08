#!/usr/bin/python3
indie = 0
for varchar in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(varchar - indie)), end="")
    indie = 32 if indie == 0 else 0
