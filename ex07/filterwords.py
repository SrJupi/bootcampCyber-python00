import sys
import string

try:
    assert len(sys.argv) <= 3, "Too many arguments"
    assert len(sys.argv) > 2, "Usage: python filterwords.py STRING INTEGER"
    try:
        num = int(sys.argv[2])
    except:
        raise AssertionError("Second argument is not an integer")
except AssertionError as msg:
    print("AssertionError:", msg)
else:
    no_dot_str = sys.argv[1].translate(str.maketrans('', '', string.punctuation))
    filtered_list = [word for word in no_dot_str.split() if len(word) > num]
    print(filtered_list);
