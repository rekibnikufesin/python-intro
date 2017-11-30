# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Fifteen - Manipulate Data with Dictionaries in Python

Create a dictionary and add values to it in Python:

```python
age = {}
age['will'] = 40
age['bob'] = 30
age['john'] = 20
age # returns {'will': 40, 'bob': 30, 'john': 20}
```

Access the value for a specific key in the dictionary:

```python
print(age['will']) # returns 40
```

Check to see if a key is present in the dictionary:

```python
'will' in age # returns True
'austin' in age # returns False
```

Delete a key/value pair from a dictionary:

```python
del age['bob']
```

Use the `get` method to retrieve a value or a default value if not found:

```python
print(age.get('will', 'Key not found')) # returns 40
print(age.get('austin', 'Key not found')) # returns Key not found
```

Iterate the key value pairs in a dictionary:

```python
for key, value in age.items():
    print(key, value)
```
