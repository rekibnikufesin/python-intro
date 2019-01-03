# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Eleven - Comparison Operators in Python

Test for equality in Python:

`5 == 5` returns True

`5 == 4` returns False

Test for inequality in Python:

`5 != 4` returns True

Test for greater than in Python:

`5 > 3` returns True

Test for less than in Python:

`3 < 5` returns True

Test for greater than or equal to in Python:

`5 >= 3` returns True

`5 >= 5` returns True

Use chaining to test multiple conditions in Python:

`3 < x < 5` returns True

Test to see if an object is a given type:

`isinstance("will", str)` returns True

`isinstance("will", int)` returns False

Test to see if an object is the exact same with the `is` operator:

```python
a = True
b = True
a is b # returns True
x = [1, 2, 3]
y = [1, 2, 3]
x is y # returns False
```

Use the `in` operator to check if a value is present:

```python
x = [1, 2, 3]
3 in x # returns True
5 in x # returns False
```

Iterate over a list and test for conditional values:

```python
x = [1, 2, 3]
for value in x:
    if value == 2:
        print('Value is 2!')

car = {'model': 'Chevy', 'year': 1970, 'color': 'red'}
if 'model' in car:
    print('This is a {0}'.format(car['model']))
```
