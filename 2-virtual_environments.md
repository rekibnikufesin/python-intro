# Commands used in the Egghead.io Series *Intro to Python*
## Lesson Two - Manage Dependencies with Python Virtual Environments

Command to install virtualenv:

`pip install virtualenv`

Steps to create a new virtual environment:

```
mkdir my_project
cd my_project
virtualenv py3 -p /usr/local/bin/python3
source py3/bin/activate
```

Command to freeze requirements into a file:

`pip freeze > requirements.txt`

Command to install dependencies from a requirements file:

`pip install -r requirements.txt`

Command to leave a virtual environment:

`deactivate`

