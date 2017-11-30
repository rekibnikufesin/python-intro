# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Fourteen - List Comprehension in Python

Use list comprehension to create a new list with items not found in the second list:

```python
zoo_animals = ['giraffe', 'monkey', 'elephant', 'lion', 'bear', 'pig', 'horse', 'aardvark']
my_animals = ['monkey', 'bear', 'pig']

other_animals = [animal for animal in zoo_animals if animal not in my_animals]
```

Use list comprehension to create a new list after each list item is modified:

```python
sales = [3.14, 7.99, 10.99, 0.99, 1.24]

sales = [sale * 1.07 for sale in sales]
```

