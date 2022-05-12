''' 
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

name equal owner return "Hello boss"
otherwise return "Hello guest"
'''

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

#Ternary operator in python
