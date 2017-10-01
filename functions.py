# def say_name(name):
#     """
#     Returns name passed in as a parameter
#     """
#     return name

# foo = say_name("will")
# print(foo)

# def add(num1=1, num2=2):
#     return num1 + num2

# num1 = add()
# print(num1)

def madlibs(name, noun="shoes", adjective="red"):
    return "{0} has {1} {2}".format(name, adjective, noun)

madlib = madlibs(name="Will", noun="boots", adjective="black")
print(madlib)