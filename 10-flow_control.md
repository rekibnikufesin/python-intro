# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Ten - Add Flow Control to your Python Application

Use an `if` statement in Python:

```
x = int(input("enter an integer: "))
if x < 0:
    x = 0
    print("Negative number changed to zero")
```


Use an `elif` statement in Python:
```
x = int(input("enter an integer: "))
if x < 0:
    x = 0
    print("Negative number changed to zero")
elif x == 0:
    print("zero")
elif x == 1:
    print("one")
else:
    print("Some other number")
```

Use a `for` statement in Python:

```
pets = ['cat', 'dog', 'elephant']
for pet in pets:
    print('I have a pet {0}.format(pet))
```

Use `for` with a range of numbers in Python:

```
for i in range(5):
    print(i)
```

Use a `while` statement in Python:

```
x = 1
while x < 10:
    print(x)
    x = x + 1
```

Terminate a loop with a `break` statement in Python:

```
pets = ['cat', 'dog', 'elephant']
for pet in pets:
    if pet == 'dog':
        print("No dogs allowed")
        break
    else:
        print("We love {0}.format(pet))
```