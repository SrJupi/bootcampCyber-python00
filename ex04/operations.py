import sys

try:
    assert len(sys.argv) <= 3, "Too many arguments"
    assert len(sys.argv) > 2, "Usage: python operations.py INTEGER1 INTEGER2"
    try:
        first_num = int(sys.argv[1])
        second_num = int(sys.argv[2])
    except:
        raise AssertionError("Argument is not an integer")
except AssertionError as msg:
    print("AssertionError:", msg)
else:
    my_sum = first_num + second_num
    my_subtraction = first_num - second_num
    my_product = first_num * second_num
    try:
        my_division = first_num / second_num
    except:
        my_division = "Error"
    try:
        my_remainder = first_num % second_num
    except:
        my_remainder = "Error"
    print(f"Sum: {my_sum}\nDifference: {my_subtraction}\nProduct: {my_product}\nQuotient: {my_division}\nRemainder: {my_remainder}")
