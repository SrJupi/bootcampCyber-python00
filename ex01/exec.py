import sys

if len(sys.argv) == 1:
    print("Usage: python exec.py STRING1 [STRING2 ...]")
else:
    print(" ".join(sys.argv[1:])[::-1].swapcase())
