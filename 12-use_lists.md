# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Twelve - Use Lists in Python

Create a list in Python:

```python
a = [1, 2, 3, 4]
b = [1, 'cat', 7, {'car': 'chevy'}]
```

Access an individual item by index number in Python:

```python
b[0] # prints the first item in the list
b[1] # prints the second item in the list
```

Append items to a list:

```python
pets = []
pets.append('cat')
pets.append('dog')
pets.append('bear')
pets.append('shark')
```

Remove an item from a list:

```python
pets.remove('dog')
```

Use the `pop` method to remove the last item from a list:

```python
pets.pop()
```

Use the `pop` method to specify an item to remove by index number:

```python
pets.pop(0) # removes cat from the list
```

Use the `sort` method to sort items in a list:

```python
pets = ['cat', 'dog', 'bear', 'shark']
pets.sort()
pets # returns ['bear', 'cat', 'dog', 'shark']
```


Use the `reverse` method to reverse the list:

```python
pets.reverse() # returns ['shark', 'dog', 'cat', 'bear']
```

Get the number of items in a list:

```python
len(pets) # returns 4
```

Get the number of occurrences of an item in a list:

```python
pets.count('bear') # returns 1
```