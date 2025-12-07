'''
Docstring for fibonacci
fibonacci by using yield

'''

def fibo(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


for num in fibo(7):
    print(num)