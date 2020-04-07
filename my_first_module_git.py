def addition(x,y):
    return (x,y)


# FizzBuzz
for x in range(100):
    if x % 5 == 0 and x % 3 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print (x)

# Fibonacci:

## Generator ---'yield'
def fib(number):
    a = 0
    b = 1
    print(a)
    while a < number:
        a,b = b, a+b
        yield (a)

for num in fib(100):
    print(num)


my_dict = {'name': 6, 'surname': 8, 'nationality': 5, 'age': 2}

for key,val in my_dict.items():
    print(f'My {key} has {val} characters')

firstlist = [1,2,3,4,5,6,7,8,9]

secondlist = [x**2 for x in firstlist]
print(secondlist)