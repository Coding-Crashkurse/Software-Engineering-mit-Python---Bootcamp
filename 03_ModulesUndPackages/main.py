from package_a.module_a1 import greet
from package_a.module_a2 import add_numbers
from package_b.module_b1 import multiply_numbers
from package_b.module_b2 import divide_numbers

if __name__ == "__main__":
    print(greet("Max Müller"))

    a, b = 4, 2
    print(f"{a} + {b} = {add_numbers(a, b)}")
    print(f"{a} * {b} = {multiply_numbers(a, b)}")
    print(f"{a} / {b} = {divide_numbers(a, b)}")
