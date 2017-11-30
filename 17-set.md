# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Seventeen - Create Uniqu Unordered Collections in Python with Set

Create a set in Python:

```python
animals = {'monkey', 'bear', 'dog', 'monkey', 'cat', 'bear', 'gorilla'}
animals # returns {'monkey', 'bear', 'gorilla', 'dog', 'cat'}
```

Check if a value is present in a set:

```python
'monkey' in animals # returns True
'shark' in animals # returns False
```

Create an empty set in Python:

```python
fish = set()
```

Add items to a set:

```python
fish.add('shark')
fish.add('guppy')
fish.add('whale')
```

Remove items from a set:

```python
fish.remove('whale')
```

Use union to combine two sets into a single, deduplicated set:

```python
fish.union(animals) # returns {'guppy', 'monkey', 'bear', 'shark', 'gorilla', 'dog', 'cat'}
```
