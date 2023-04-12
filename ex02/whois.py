import sys

try:
    assert len(sys.argv) <= 2, "More than one argument provided"
    assert len(sys.argv) > 1, "Usage: python whois.py INTEGER"
    try:
        num = int(sys.argv[1])
    except:
        raise AssertionError("Argument is not an integer")
except AssertionError as msg:
    print("AssertionError:", msg)
else:
    if num == 0:
        print("I am Zero!");
    elif num % 2 == 0:
        print("I am Even!");
    else:
        print("I am Odd!");
