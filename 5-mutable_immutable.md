# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Five - Mutable vs. Immutable Objects in Python

Code to see the id of a mutable object in Python:

```
b = []
id(b)

b.append(3)
id(b)
```


Code to see the id of an immutable object in Python:

```
a = 4
id(a)

a = a + 1
id(a)
```
