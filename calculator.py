'''
Docstring for calculator
this is a real calculator!

'''
import math

def add(numbers):
    res = sum(numbers)
    return f"the sum is {res}"

def tafrigh(numbers):
    res = numbers[0]
    for num in numbers[1:]:
        res -= num
    return f"the substract of the numbers is {res}"

def zarb(numbers):
    res = 1
    for num in numbers:
        res *= num
    return f"zarb adad hast {res} "

def taqsim(numbers):
    res = numbers[0]
    for num in numbers[1:]:
        if num == 0:
            raise ValueError("can not divide by zero!")
        res /= num
    return f"taqsim adad = {res}"

def logarithms(x, base=math.e):
    return f"the logarithm is = {math.log(x, base)}"


adad = [4, 5, 6]
print(zarb(adad))
print(add(adad))
print(taqsim(adad))
print(tafrigh(adad))
print(logarithms(10))