x = int(input("enter an integer:  "))
if x < 0:
    x = 0
    print('Negative number changed to zero.')
elif x == 0:
    print('zero')
elif x == 1:
    print('one')
else:
    print('Some other number')