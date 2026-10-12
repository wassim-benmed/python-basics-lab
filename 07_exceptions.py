try:
    num1 = input('Please enter the first digit: ')
    num2 = input('Please enter the second digit: ')
    print('The first number divided by the second number is %f' % (int(num1) / int(num2)))
except ZeroDivisionError:
    print('The second digit cannot be 0.')
except Exception as result:
    print('Captured exception: %s' % result)
else:
    print('No exception occurred.')
finally:
    print('This always runs.')