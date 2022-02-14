import sys
def sum(x, y):
    '''Sum func'''
    assert x>0, "x must be greater then 0"
    assert y>0, "y must be greater then 0"

    return x+y

print("Insert x: ")
x = float(input())
print("Insert y: ")
y = float(input())
print("\nSum: ")
try:
    print(sum(x, y))
except AssertionError as e:
    print("Error: ",e, file=sys.stderr)