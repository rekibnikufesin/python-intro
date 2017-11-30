# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Thirteen - Slice Lists in Python

Slice a list in Python:

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[2:5] # returns [3, 4, 5]
a[2:]  # returns [3, 4, 5, 6, 7, 8, 9]
a[:5]  # returns [1, 2, 3, 4, 5]
a[-4:] # returns [6, 7, 8, 9]
```

Use slice to replace part of a list in Python:

```python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[2:5] = ['foo', 'bar', 'baz']
a # returns [1, 2, 'foo', 'bar', 'baz', 6, 7, 8, 9]
```