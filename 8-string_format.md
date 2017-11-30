# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Eight - Format Strings in Python

Create a string in Python:

`name = 'will`

Create a string with single quotes in Python:

`my_ball = "Will's ball"`

Create a multiline string in Python:

```
multiline = """Will's ball
is red
and bouncy!"""
```

Code to escape a single quote in Python:

`print("Will's ball is red")`

or

`print('Will\'s ball is red')`

or

`print("""Will's ball is red""")`

Code to print tab characters in Python:

`print("Will's\tball\tis\tred")`

Code to use variable substitution in a string:

```
item = 'ball'
color = 'red'
print("Will's %s is %s." % (item, color))
```

Code to use variable substitution with the string format method:

```
item = 'ball'
color = 'red'
print("Will's {0} is {1}".format(item, color))
```