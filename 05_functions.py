def Print_Hello():
    print("Hello, Python.")
Print_Hello()

def hello(greeting='hello', name='world'):
    print('%s, %s!' % (greeting, name))
hello()
hello('Greetings')
hello(name='Huawei')
hello('Greetings', 'universe')

def test(a, b, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)
test(1, 2, 3, 4, 5, 6, x=10, y=11)

def plus_one(number):
    return int(number) + 1
print(plus_one(10))